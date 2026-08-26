# Contents

<https://documentation.neutrinos.com/articles/#!alpha-platform/bpm-use_case-run-book>

This document explains how to plan and execute archival and restore operations using the Alpha Archival service, and how to work on the service as a developer.

The service manages archival of jBPM-backed process data between a primary BPM database (source) and a backup database (target), with detailed audit trails and safety controls.

## Contents

- [Overview](/articles/alpha-platform/bpm-use_case-run-book/a/overview)
- [Base URL & Docs](/articles/alpha-platform/bpm-use_case-run-book/a/base-url--docs)
- [Prerequisites & Environment](/articles/alpha-platform/bpm-use_case-run-book/a/prerequisites--environment)
- [Quick Start](/articles/alpha-platform/bpm-use_case-run-book/a/quick-start)
- [Planning an Archival](/articles/alpha-platform/bpm-use_case-run-book/a/planning-an-archival)
- [Development Methodology (End Users)](/articles/alpha-platform/bpm-use_case-run-book/a/development-methodology-end-users)
- [Backup Runbook (Async)](/articles/alpha-platform/bpm-use_case-run-book/a/backup-runbook-async)
- [Restore Runbook (Async)](/articles/alpha-platform/bpm-use_case-run-book/a/restore-runbook-async)
- [Delete Bulk Use Case](/articles/alpha-platform/bpm-use_case-run-book/a/delete-bulk-use-case)
- [Auditing, Monitoring & Troubleshooting](/articles/alpha-platform/bpm-use_case-run-book/a/auditing-monitoring--troubleshooting)
- [Security & Authorization](/articles/alpha-platform/bpm-use_case-run-book/a/security--authorization)
- [Development Methodology](/articles/alpha-platform/bpm-use_case-run-book/a/development-methodology)
- [FAQ & Tips](/articles/alpha-platform/bpm-use_case-run-book/a/faq--tips)

## Overview

Key capabilities:

- Count and find process instances by filters (process name, status, dates, task filters, variable filters, explicit `piids`)
- Discover recursive child process instance IDs
- Generate transaction-wrapped SQL backup scripts for a set of process IDs
- Run full backup (source → backup DB) and restore (backup DB → source) in controlled batches with audit logs
- Delete process instances in bulk (recursive children included)

Constraints and safety:

- At most one backup/restore operation runs at a time; a concurrent request returns a message and an `auditId` you can poll
- Backup deletes matching data from the source after copying to the target; restore deletes matching data from the backup after copying to the source
- Every step writes detailed rows into the `process_audit_logs` table in the backup database for traceability

## Base URL & Docs

- All endpoint paths in this document are relative to `/archivalservice/bpm` unless noted otherwise.
- The base path is configurable via `BASE_PATH` (default: `archivalservice`).
- Swagger (local default): `http://{domain_name}/archivalservice/api-docs`
- Health check (no auth): `GET /archivalservice/ping` → `{ status: 'ok' }`

## Prerequisites & Environment

Databases and schema:

- Primary BPM DB (source): contains jBPM tables (e.g., `processinstancelog`, tasks, variables)
- Backup BPM DB (target): receives backups and stores audit tables
- Startup migrations create or update stored procedures/functions in both DBs and create backup tables in the backup DB

Configuration (service `.env`):

- Primary DB: `DB_HOST`, `DB_PORT`, `DB_USERNAME`, `DB_PASSWORD`, `BPM_DB_NAME`, `BPM_DB_SCHEMA_NAME`, `DB_SSL`, optional `DB_CA_CERT_PATH`/`DB_CA_CERT`
- Backup DB: `BPM_BACKUP_DB_HOST`, `BPM_BACKUP_DB_PORT`, `BPM_BACKUP_DB_USERNAME`, `BPM_BACKUP_DB_PASSWORD`, `BPM_BACKUP_DB_NAME`, `BPM_BACKUP_DB_SCHEMA_NAME`, `BPM_BACKUP_DB_SSL`, optional `BPM_BACKUP_DB_CA_CERT_PATH`/`BPM_BACKUP_DB_CA_CERT`
- Service: `BASE_PATH`, `PORT`
- Security: `IDS_ENABLE`, `IDS_URL`, `IDS_CLIENT_ID`, `IDS_CLIENT_SECRET`, `ALPHA_AUTH_SERVICE_URL`

Health check:

- `GET /archivalservice/ping` returns `{ status: 'ok' }` and is excluded from auth

Config validation:

- On startup, the service validates that primary (`bpm`) and backup (`bpm_backup`) do not point to the same physical database (same host, port, and database name). If they do, the service remains unhealthy:
  - `GET /archivalservice/ping` returns HTTP 503 with `{ status: 'error', errorCode: 'INVALID_DB_CONFIG', errorMessage: '...' }`.
  - Backup/restore endpoints respond with HTTP 503 until configuration is fixed.

## Quick Start

Plan, back up, and track a run end-to-end.

1. Estimate volume

- `POST /processes/count`
    Body:
    Copy CodeCode{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }
    Curl:
    Copy CodeCodecurl -X POST \
    "http://{domain_name}/archivalservice/bpm/processes/count" \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }'

1. Kick off backup (async)

- `POST /processes/backup`
    Body mirrors your filters (e.g., the one above). Best practice: target terminal states only (e.g., `processStatus: "COMPLETED"`) and/or use `beforeNoOfDays` to avoid in‑flight processes. Response:
    Copy CodeCode{ "message": "Backup initiated successfully", "auditId": "<uuid>" }
    Curl:
    Copy CodeCodecurl -X POST \
    "http://{domain_name}/archivalservice/bpm/processes/backup" \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "beforeNoOfDays": 90
    }'

1. Track progress

- Latest: `GET /processes/audits/<auditId>/latest`
- Full timeline: `GET /processes/audits/<auditId>`
    Curl (latest):
    Copy CodeCodecurl -X GET \
    "http://{domain_name}/archivalservice/bpm/processes/audits/<auditId>/latest" \
    -H "Authorization: Bearer <token>"
    Curl (timeline):
    Copy CodeCodecurl -X GET \
    "http://{domain_name}/archivalservice/bpm/processes/audits/<auditId>?pageNumber=1&pageSize=50" \
    -H "Authorization: Bearer <token>"

1. (Optional) Restore similar scope later

- `POST /processes/restore` with the same filters (applied against the backup DB).
    Curl:
    Copy CodeCodecurl -X POST \
    "http://{domain_name}/archivalservice/bpm/processes/restore" \
    -H "Authorization: Bearer <token>" \
    -H "Content-Type: application/json" \
    -d '{
    "processName": "customerOnboarding",
    "beforeNoOfDays": 90
    }'

## Planning an Archival

Objective: select the right scope, estimate volume, understand relationships, and choose the proper execution strategy.

1. Define selection filters

- Use any combination of:
  - `processName` (exact match), `processStatus` (ACTIVE|COMPLETED|ABORTED), `deploymentId`
  - `beforeNoOfDays` (date cutoff), task filters (`taskName`, `taskStatus`, `taskAssignee`)
  - `processVariables`: array of `{ name, value }` filters (AND semantics)
  - `piids`: explicit list of process instance IDs
  - Status guidance: Prefer terminal states (`COMPLETED`, `ABORTED`) for archival/deletion. Avoid `ACTIVE` to prevent removing in‑flight processes. When using explicit `piids`, combine with a status filter to guard against accidental inclusion.

1. Estimate volume

- `POST /processes/count` with filters → returns `totalCount`
- Use `totalCount` to decide batch windows and maintenance windows

1. Sample the IDs

- `POST /processes` (paginated) with the same filters
- Page through to manually spot-check a subset

1. Understand child processes (scope preview)

- `POST /processes/children/find` with `parentProcessInstanceIds` to preview scope.
- Note: Backup/restore automatically fetch and include recursive child processes. Delete-bulk also deletes recursive children automatically. Use `children/find` mainly for planning and verification, not as a required step before running.

1. Dry-run SQL generation (optional for safety)

- `POST /processes/generate-sql` with `processInstanceIds`
- Review the transaction-wrapped SQL before running full backup in production

1. Schedule the operation

- Backups run in batches (up to 100 per iteration; hard cap). Total batches = `ceil(totalCount / 100)`
- Expect the following high-level steps per batch (audit logs will reflect them): count → fetch → children → generate SQL → execute → delete → complete

1. Communicate recovery plan

- Capture `restore` parameters mirroring the same filters; ensure you know how to trace and reverse if needed

## Development Methodology (End Users)

Purpose: a practical, safe way to plan and execute archival and restore jobs so you sleep well after pressing “Run”.

Principles

- Safety first: target terminal states (`COMPLETED`, `ABORTED`) and/or use `beforeNoOfDays` to avoid in‑flight data.
- Predictability: estimate volume with `/processes/count` before starting; run in bounded batches (service caps at 100).
- Observability: track each run by `auditId` and decide based on facts, not guesses.
- Rehearsal: dry‑run with `/processes/generate-sql` and perform a lower‑env rehearsal before production.
- Reversibility: capture filters you used so you can mirror them for restore if needed.
- Concurrency: only one backup/restore runs at a time; avoid parallelism through external automation.

Pre‑flight checklist

- Connectivity and readiness
  - `GET /archivalservice/ping` returns ok.
  - Swagger reachable locally: `http://{domain_name}/archivalservice/api-docs`.
  - Auth token available; environments configured via `.env`.
- Scope definition
  - Choose filters with terminal `processStatus` and `beforeNoOfDays` that reflect your retention policy.
  - Run `POST /processes/count` and record `totalCount` for the window.
  - Optionally `POST /processes` to sample IDs and spot‑check.
  - Optionally `POST /processes/children/find` to preview recursive scope.
- Schedule
  - Plan a window sized as `ceil(totalCount / 100)` batches plus margin.
  - Communicate a recovery plan (the exact filters you would use to restore).

Execution ladder (backup)

1. Kick off `POST /processes/backup` with the selected filters (terminal states recommended). Capture `auditId`.
2. Monitor `GET /processes/audits/{auditId}/latest` every few seconds/minutes.
3. If failure occurs, inspect `errorCode`, `errorSummary`, `errorResolve`, and `errorMessage` in the latest audit row.
  - For unique violations (23505) on the target DB, delete conflicts via `POST /processes/delete-bulk` on the target side and retry.
4. Wait until the final audit row shows `auditStatus=completed`.

Post‑run verification

- Compare `POST /processes/count` on source vs backup (adjusting DB context) for the same filters.
- Sample via `POST /processes` and verify expected records moved.
- Confirm latest audit shows `completed` with no remaining count.

Execution ladder (restore)

1. Mirror the backup filters (applied against the backup DB) and `POST /processes/restore`.
2. Monitor audits as above until `completed`.
3. Verify counts and sample data back in the primary DB for the same scope.

Roll‑back and record‑keeping

- Keep a record of the exact JSON filters used (and the returned `auditId`).
- If you need to reverse a backup wave, reuse the same filters for restore or derive `piids` from the audit logs and restore those explicitly.

Do’s and Don’ts

- Do use `processStatus: COMPLETED` and `beforeNoOfDays` for production backups.
- Do validate “ACTIVE count == 0” when deleting specific `piids`.
- Don’t hand‑pick IDs without a status guard.
- Don’t attempt to run multiple archival jobs at once.

## Backup Runbook (Async)

Kick off a backup:

- `POST /processes/backup` with the selection filters
- Typical response (201 Created) includes `auditId` to track progress

Track progress and outcomes:

- `GET /processes/audits/:auditId/latest` → last status row
- `GET /processes/audits/:auditId` → full timeline (paginated)
- `GET /processes/audits/:auditId/summary` → total number of audit rows

Notes:

- If another backup/restore is already in progress, the service returns a message indicating this and still provides an `auditId`
- Data is deleted from the source DB after being applied to the backup DB for each batch
- For a non-destructive rehearsal, use `generate-sql` on a sample set and run in a lower environment
- Best practice: Scope backups to terminal states (e.g., `processStatus: COMPLETED`) and/or apply `beforeNoOfDays` to avoid capturing in‑flight data.

## Restore Runbook (Async)

Kick off a restore:

- `POST /processes/restore` with filters (applied against the backup DB)
- Typical response (201 Created) includes `auditId`

Tracking mirrors backup:

- Use the same audit endpoints to follow status and errors

Notes:

- Restore applies data to the primary DB and deletes it from the backup DB
- Make sure constraints and schemas on the primary DB match expectations (migrations run at startup and functions/procedures are prepared)
- Validate with `count` and `processes` before and after
- Best practice: Restore only processes that were previously archived in terminal states (e.g., `COMPLETED`), unless there is an explicit business need to reintroduce in‑flight data.

## Delete Bulk Use Case

Endpoint:

- `POST /processes/delete-bulk` with `{ processInstanceIds: number[] }`

Options:

- Pass IDs of parent processes; recursive child processes are automatically included in the deletion.
- `children/find` is optional for planning/preview. Response returns operation status.

Safety:

- Prefer to delete after you have validated that the matching data is safely backed up
- Consider performing a smaller test deletion window before a large wave

Status strategy (preventing accidental deletion):

- Delete-bulk operates on the exact IDs you pass and does NOT filter by status. Always ensure the parent process IDs you supply are in terminal states (`COMPLETED` or `ABORTED`).
- Recommended guardrails:
  - Pre-check for active processes among your candidate IDs:
    - `POST /processes/count` with `{ piids: [...], processStatus: "ACTIVE" }` should return `totalCount = 0`.
  - Prefer to derive the candidate list via filters that enforce terminal states (e.g., `processStatus: "COMPLETED"`, and `beforeNoOfDays`), rather than hand-picking IDs.
  - Children are deleted recursively; verify scope with `/processes/children/find` when needed.

Example safe delete flow:

1. Build candidate set (terminal only)

```code
curl -X POST \  "http://{domain_name}/archivalservice/bpm/processes" \  -H "Authorization: Bearer <token>" \  -H "Content-Type: application/json" \  -d '{    "processName": "customerOnboarding",    "processStatus": "COMPLETED",    "beforeNoOfDays": 30,    "pageSize": 100,    "pageNumber": 1  }'
```

1. Guard: ensure none of these are ACTIVE

```code
curl -X POST \  "http://{domain_name}/archivalservice/bpm/processes/count" \  -H "Authorization: Bearer <token>" \  -H "Content-Type: application/json" \  -d '{    "piids": [/* candidate IDs here */],    "processStatus": "ACTIVE"  }'
```

1. Delete (includes children automatically)

```code
curl -X POST \  "http://{domain_name}/archivalservice/bpm/processes/delete-bulk" \  -H "Authorization: Bearer <token>" \  -H "Content-Type: application/json" \  -d '{ "processInstanceIds": [/* candidate IDs here */] }'
```

## Auditing, Monitoring & Troubleshooting

Audit discovery:

- `GET /processes/audits?auditType=&auditStatus=&processName=&deploymentId=&from=&to=&pageNumber=&pageSize=`
    Copy CodeCodecurl -i -X GET \
    "http://{domain_name}/archivalservice/bpm/processes/audits?auditType=backup&processName=customerOnboarding&pageNumber=1&pageSize=20" \
    -H "Authorization: Bearer <token>"
  - Returns the latest row for each `auditId` matching discovery filters
  - `X-Total-Count` header includes total matches
      Curl (includes headers):

Summaries:

- `GET /processes/audits/summary?...` → total number of audits matching discovery filters
    Curl:
    Copy CodeCodecurl -X GET \
    "http://{domain_name}/archivalservice/bpm/processes/audits/summary?auditType=backup&from=2025-01-01T00:00:00Z&to=2025-02-01T00:00:00Z" \
    -H "Authorization: Bearer <token>"

Log details:

- Server logs include compiled SQL with schema injections (e.g., `"public".process_count_fn_v1(...)`)
- Query failures surface Postgres codes and details in the log (e.g., function missing, permission issues)

Common issues:

- Function missing: confirm startup migrations run and the configured schema names are correct
- Permission errors: validate DB users have `CREATE FUNCTION/PROCEDURE`, `SELECT/INSERT/DELETE` where needed
- Concurrency: only one backup/restore at a time; retry later if another is in progress
- Unique violation (23505) during backup/restore apply: the target DB already contains conflicting data. Use `POST /processes/delete-bulk` to remove the conflicting data from the target DB as indicated by audit/log details, then retry the operation.

Minimal examples (selected):

- Count
  - Request: `POST /processes/count`
      Copy CodeCode{ "processName": "order-fulfillment" }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/count" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "processName": "order-fulfillment" }'
  - Response: `{ "totalCount": 123 }`
- Find (paginated)
  - Request: `POST /processes`
      Copy CodeCode{ "processName": "customerOnboarding", "pageSize": 50, "pageNumber": 1 }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{
      "processName": "customerOnboarding",
      "pageSize": 50,
      "pageNumber": 1
      }'
  - Response: `{ "processInstanceIds": [2001, 2002] }`
- Children preview
  - Request: `POST /processes/children/find`
      Copy CodeCode{ "parentProcessInstanceIds": [201, 205, 210] }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/children/find" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "parentProcessInstanceIds": [201, 205, 210] }'
  - Response: `{ "childProcessInstanceIds": [301, 302, 303] }`
- Generate SQL (dry-run)
  - Request: `POST /processes/generate-sql`
      Copy CodeCode{ "processInstanceIds": [101, 102, 103] }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/generate-sql" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "processInstanceIds": [101, 102, 103] }'
  - Response: `{ "backupSqlScript": ["BEGIN;", "INSERT ...", "COMMIT;"] }`
- Backup (async)
  - Request: `POST /processes/backup`
      Copy CodeCode{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/backup" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }'
  - Response (201): `{ "message": "Backup initiated successfully", "auditId": "<uuid>" }`
  - If busy: `{ "message": "Previous operation is still in progress, please wait for it to complete before retrying", "auditId": "<uuid>" }`
- Restore (async)
  - Request: `POST /processes/restore`
      Copy CodeCode{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/restore" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "processName": "customerOnboarding", "beforeNoOfDays": 90 }'
  - Response (201): `{ "message": "Restore initiated successfully", "auditId": "<uuid>" }`
- Delete-bulk (includes children)
  - Request: `POST /processes/delete-bulk`
      Copy CodeCode{ "processInstanceIds": [12345, 67890] }
      Curl:
      Copy CodeCodecurl -X POST \
      "http://{domain_name}/archivalservice/bpm/processes/delete-bulk" \
      -H "Authorization: Bearer <token>" \
      -H "Content-Type: application/json" \
      -d '{ "processInstanceIds": [12345, 67890] }'
  - Response: `{ "status": "SUCCESS" }` or `{ "status": "FAILURE: <message>" }`

## Security & Authorization

Inbound:

- Bearer tokens via IDS: `Authorization: Bearer <token>`
- Configure via `IDS_ENABLE`, `IDS_URL`, `IDS_CLIENT_ID`, `IDS_CLIENT_SECRET`, `ALPHA_AUTH_SERVICE_URL`
- `/archivalservice/ping` is excluded from auth for health checks

Outbound (service-to-service):

- Not used by this service directly for archival operations, but the broader platform employs a centralized token service for outbound calls

## Development Methodology

Security & docs:

- Annotate new secured endpoints with `@ApiBearerAuth()` and group them via `@ApiTags`
- Ensure RequestUtils is enforcing auth on all non-excluded routes

Operational considerations:

- Keep batch sizes manageable (currently 100) and respect the one-operation-at-a-time rule
- Ensure new SQL is idempotent and safe to re-run in migrations
- Log failures with enough context to diagnose in production without leaking sensitive data

## FAQ & Tips

- Q: Can I run a dry-run of backup?
  - A: Use `generate-sql` on a sample set in a non-production environment and review the generated statements
- Q: How do I predict downtime?
  - A: Use `processes/count` to estimate total volume and multiply by average per-batch duration to derive a window
- Q: What if a batch fails mid-run?
  - A: Inspect `audits/:auditId` for the last successful step, fix the underlying issue (e.g., a constraint), and re-run; operations are batched and audit trails are preserved
- Q: How do I ensure complete deletion?
  - A: For backup/restore, child processes are handled automatically. For deletions, `/processes/delete-bulk` also deletes recursive children; use `children/find` mainly to preview scope when planning.
- Q: How do I verify after restore?
  - A: Compare `processes/count` between environments before/after; sample `processes` endpoints to spot check
