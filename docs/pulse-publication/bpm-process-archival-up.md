# Base URL

<https://documentation.neutrinos.com/articles/#!pulse-publication/bpm-process-archival-up>

Enterprise-grade BPM archiving and recovery APIs for jBPM-backed process data. These APIs provide endpoints to count and retrieve processes, access child processes, generate backup SQL, perform batch backup and restore operations between databases, and safely delete processes with full audit tracking.

For end-to-end guidance on planning archival and restore operations, refer to the [Use Case](/smart/project-alpha-platform/bpm-use_case-run-book) topic.

## Base URL

All endpoints are served under a configurable base path. By default,

- **Base path**: `/archivalservice`
- **Controller prefix**: `/bpm`
- **Full API base**: `/archivalservice/bpm`

Example: `POST http://{domain_name}/archivalservice/bpm/processes/count`

## Swagger / OpenAPI

- Live docs (auto-generated from NestJS decorators):` http://{domain_name}/archivalservice/api-docs`
- All endpoints are documented via DTO and controller annotations in `src/app/**.`

## Environment variables

Create a local `.env` from the provided example and adjust values as needed:

```bash (unix shell)
cp backend/alpha-archival/.env.example backend/alpha-archival/.env
```

### Key variables

- **BPM database**: `DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, BPM_DB_NAME, BPM_DB_SCHEMA_NAME, DB_SSL`
  - **Optional certs**: `DB_CA_CERT_PATH` or `DB_CA_CERT`
- **Backup database**: `BPM_BACKUP_DB_HOST, BPM_BACKUP_DB_PORT, BPM_BACKUP_DB_USERNAME, BPM_BACKUP_DB_PASSWORD, BPM_BACKUP_DB_NAME, BPM_BACKUP_DB_SCHEMA_NAME, BPM_BACKUP_DB_SSL`
  - **Optional certs**: `BPM_BACKUP_DB_CA_CERT_PATH` or `BPM_BACKUP_DB_CA_CERT`
- **Service**: `BASE_PATH, PORT`

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | Do not commit secrets. Prefer local `.env` files and environment injection in CI/CD. |
| --- | --- |

## Table of Contents

- [Authentication](/articles/pulse-publication/bpm-process-archival-up/a/h2__55841322)
- [Operational Checklist](/articles/pulse-publication/bpm-process-archival-up/a/h2__424495486)
- [Endpoints](/articles/pulse-publication/bpm-process-archival-up/a/h2__691415180)
  - [Count Processes](/articles/pulse-publication/bpm-process-archival-up/a/h3_1035812684)
  - [Get Audit Logs](/articles/pulse-publication/bpm-process-archival-up/a/h2__168061396)
  - [Find Processes](/articles/pulse-publication/bpm-process-archival-up/a/h2__1164346748)
  - [Find Child Processes](/articles/pulse-publication/bpm-process-archival-up/a/h2_1025542618)
  - [Delete Processes](/articles/pulse-publication/bpm-process-archival-up/a/h2__2100547968)
  - [Generate SQL Backup](/articles/pulse-publication/bpm-process-archival-up/a/h2_1907204723)
  - [Backup Processes](/articles/pulse-publication/bpm-process-archival-up/a/h2_2135229242)
  - [Restore Processes](/articles/pulse-publication/bpm-process-archival-up/a/h2_2135229242)

## Authentication

All endpoints require Bearer token authentication:

```code
Authorization: Bearer <your-access-token>
Content-Type: application/json
```

All endpoint paths below are relative to `/archivalservice/bpm` unless specified otherwise.

Enable/Configure auth via environment variables:

- `IDS_ENABLE`(true|false): if false, requests are allowed without auth (local/dev only).
- `IDS_URL`(true|false): IDS issuer URL for token validation.
- `IDS_CLIENT_ID, IDS_CLIENT_SECRET`(true|false): IDS client credentials for token introspection/flows.
- `ALPHA_AUTH_SERVICE_URL`(true|false): Auth service base URL for cookie session validation (optional fallback).

### Health check

- `GET /archivalservice/ping` is excluded from authorization and returns ` { status: 'ok', timestamp: '<iso>' } ` when healthy.
- If primary and backup DBs point to the same host/port/database, ping returns HTTP 503 with `{ status: 'error', errorCode: 'INVALID_DB_CONFIG', errorMessage: '...' }`.

## Operational Checklist

A “sleep-well” approach for planning and executing archival operations.

- Pre-flight
  - Swagger reachable: `http://{domain_name}/archivalservice/api-docs`
  - Valid auth token ready: `.env` configured.
  - Ping returns healthy.
- Scope
  - Choose terminal states `(COMPLETED/ABORTED)` and/or `beforeNoOfDays`.
  - Get volume with `POST /processes/count`.
  - Optional: preview IDs with `POST /processes` and children with `POST /processes/children/find`.

## Endpoints

### Count Processes

Count process instances that match specific criteria.

**`POST /processes/count`**

### Request Body

```code
{
    "processName": "order-fulfillment",
    "processStatus": "ACTIVE",
    "deploymentId": "dep-54321",
    "beforeNoOfDays": 30,
    "taskName": "Process Payment",
    "taskStatus": "PENDING",
    "taskAssignee": "john.doe@example.com",
    "processVariables": [{ "name": "customerId", "value": "CUST-12345" }],
    "piids": [1001, 1002, 1003]
}
```

| **Field** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `processName` | string | No | Filter by **process definition name** (e.g., `order-fulfillment`) |
| `processStatus` | enum | No | Process state: `ACTIVE`, `COMPLETED`, or `ABORTED` |
| `deploymentId` | string | No | Filter by **deployment version ID** (e.g., `dep-54321`) |
| `beforeNoOfDays` | number | No | Return processes that started **before X days ago from now** |
| `taskName` | string | No | Filter by **task name** within the process (e.g., `Process Payment`) |
| `taskStatus` | string | No | Task state (e.g., `PENDING`, `COMPLETED`, etc.) |
| `taskAssignee` | string | No | Filter by **assignee** (email/username of the person responsible) |
| `processVariables` | array | No | Array of **key-value filters** on process variables. Uses **AND** logic. |
| `piids` | number[] | No | Explicit list of **process instance IDs** to check |

### Curl

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/count" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{
    "processName": "order-fulfillment",
    "beforeNoOfDays": 30
  }'
```

## Get Audit Logs

Fetch audit trail entries for a given `auditId` produced by backup/restore operations.

**`GET /processes/audits/{auditId}`**

Query params:

- `from` (ISO 8601, optional): start timestamp inclusive
- `to` (ISO 8601, optional): end timestamp inclusive
- `pageNumber` (number, default 1)
- `pageSize` (number, default 50)

Example:

```code
curl -X GET \n  "http://{domain_name}/archivalservice/bpm/processes/audits/a4c1e8f2-56c0-4a2d-9a05-12e1c90a8d77" \n  -H "Authorization: Bearer <token>"
```

Response (200):

```code
[
    {
        "auditId": "a4c1e8f2-56c0-4a2d-9a05-12e1c90a8d77",
        "auditType": "backup",
        "auditStatus": "started",
        "remainingProcessCount": 200,
        "batchName": "process_count",
        "batchStatus": "inprogress",
        "createdAt": "2025-01-01T12:00:00.000Z"
    }
]
```

Errors:

- `400 Bad Request` if `auditId` is not a valid UUID.
- `401/403` if authentication/authorization fails.

Latest-only shortcut:

- `GET /processes/audits/{auditId}/latest` → returns the most recent row or 404 if not found.

Summary endpoint:

- `GET /processes/audits/{auditId}/summary?from=&to=` → returns `{ totalCount }` for the matching audit rows.

Discovery endpoint:

- `GET /processes/audits?auditType=&auditStatus=&processName=&deploymentId=&from=&to=&pageNumber=&pageSize=` → returns the latest row for each auditId matching filters, allowing clients to enumerate `auditId`s without prior knowledge. Includes `X-Total-Count` header with total matches.

```code
curl -i -X GET \n  "http://{domain_name}/archivalservice/bpm/processes/audits?auditType=backup&processName=customerOnboarding&pageNumber=1&pageSize=20" \n  -H "Authorization: Bearer <token>"
```

Discovery summary:

- `GET /processes/audits/summary?auditType=&auditStatus=&processName=&deploymentId=&from=&to=` → returns `{ totalCount }` for discovery filters.

```code
curl -X GET \n  "http://{domain_name}/archivalservice/bpm/processes/audits/summary?auditType=backup&from=2025-01-01T00:00:00Z&to=2025-02-01T00:00:00Z" \n  -H "Authorization: Bearer <token>"
```

### Response

```code
{
    "totalCount": 1523
}
```

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `totalCount` | number | The **total number of process instances** matching filters |

### Possible Errors

The `/processes/count` endpoint supports filtering by `processVariables` and `piids`.
 During validation and execution, the following error scenarios may occur:

### 1. Array Cardinality Mismatch

If the request body includes `processVariables` with mismatched `name`-`value` pairs it returns a validation error.

**Example Request:**

```code
{
    "processVariables": [
        { "name": "status", "value": "OPEN" },
        { "name": "", "value": "APPROVED" },
        { "name": "priority", "value": "" }
    ]
}
```

**Example Response:**

```code
{
    "message": ["processVariables.1.name should not be empty", "processVariables.2.value should not be empty"]
}
```

### 2. Non-numeric piids

The DTO automatically converts string `piids` into numbers.
 If non-numeric values are provided, validation fails before reaching the database.

**Example Request:**

```code
{
    "piids": ["123", "456", "abc"]
}
```

**Example Response:**

```code
{
    "message": ["piids.2 must be a number conforming to the specified constraints"]
}
```

### 3. Invalid Filters

- Unknown field names in `processVariables` may return **zero results** instead of throwing an error.
- Invalid date formats in date filters will result in **400 Bad Request** with a validation error.

### Find Processes

Retrieve process instance IDs with filtering and pagination.

**`POST /processes`**

**Request Body:**

```code
{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "deploymentId": "dep-xyz-789",
    "beforeNoOfDays": 30,
    "taskName": "approveApplication",
    "taskStatus": "PENDING",
    "taskAssignee": "john.doe@example.com",
    "processVariables": [{ "name": "customerId", "value": "CUST-12345" }],
    "piids": [2001, 2002],
    "pageSize": 50,
    "pageNumber": 1
}
```

**Response:**

```code
{
    "processInstanceIds": [2001, 2002, 2003]
}
```

## Find Processes

Retrieves a paginated list of process instances that match the given filter criteria.

`POST /processes`

### Request Body

```code
{
    "processName": "order-fulfillment",
    "processStatus": "ACTIVE",
    "deploymentId": "dep-54321",
    "beforeNoOfDays": 30,
    "taskName": "Process Payment",
    "taskStatus": "PENDING",
    "taskAssignee": "john.doe@example.com",
    "processVariables": [{ "name": "customerId", "value": "CUST-12345" }],
    "piids": [1001, 1002, 1003]
}
```

| **Field  ** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `processName` | string | No | Filter by process definition name |
| `processStatus` | enum | No | `ACTIVE`, `COMPLETED`, or `ABORTED` |
| `deploymentId` | string | No | Deployment/external ID |
| `beforeNoOfDays` | number | No | Started before N days from now |
| `taskName` | string | No | Human task name |
| `taskStatus` | string | No | Human task status |
| `taskAssignee` | string | No | Human task assignee |
| `processVariables` | array | No | Array of `{ name, value }` filters; AND semantics across elements |
| `piids` | number[] | No | Explicit process instance IDs |
| `pageSize` | number | No | Page size (default 50) |
| `pageNumber` | number | No | 1-based page index (default 1) |

### Curl

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "pageSize": 50,
    "pageNumber": 1
  }'
```

### Response

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `processInstanceIds` | number | The **process instances ids** for matching filters |

### Possible Errors

The `/processes` endpoint supports filtering by `processVariables` `pageNumber` and `piids`.
 During validation and execution, the following error scenarios may occur:

### 1. Array Cardinality Mismatch

Occurs when `processVariables` contains entries with missing `name` or `value`.

**Example Request:**

```code
{
    "processVariables": [
        { "name": "status", "value": "OPEN" },
        { "name": "", "value": "APPROVED" },
        { "name": "priority", "value": "" }
    ]
}
```

**Example Response:**

```code
{
    "message": ["processVariables.1.name should not be empty", "processVariables.2.value should not be empty"]
}
```

### 2. Non-numeric piids

DTO converts numeric strings into numbers automatically.
 If non-numeric strings are included, validation fails.

**Example Request:**

```code
{
    "piids": ["123", "456", "abc"]
}
```

**Example Response:**

```code
{
    "message": ["piids.2 must be a number conforming to the specified constraints"]
}
```

### 3. Page Number Overflow

If `pageNumber` exceeds PostgreSQL integer range (`> 2147483647`), Postgres throws **22003: out of range**.

**Example Request:**

```code
{
    "processName": "order-fulfillment",
    "pageNumber": 2147483648
}
```

**Example Response:**

```code
{
    "status": 500,
    "message": "value \"2147483648\" is out of range for type integer"
}
```

## Find Child Processes

Fetch child process instances for the given parent process instance IDs.

**`POST /processes/children/find`**

### Request Body

```code
{
    "parentProcessInstanceIds": [1001, 1002]
}
```

| **Field  ** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `parentProcessInstanceIds` | number[] | Yes | List of **parent process instance IDs** to fetch children for |

### Curl

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/children/find" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{ "parentProcessInstanceIds": [1001, 1002] }'
```

### Response

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `childProcessInstanceIds` | number[] | The child process instance IDs found |

### Possible Errors

The `/processes/children/find` endpoint validates input arrays and interacts with PostgreSQL.
 The following error scenarios may occur:

### 1. Non-integer input (22P02)

If non-integer values are provided in `parentProcessInstanceIds`, validation fails.

**Example Request:**

```code
{
    "parentProcessInstanceIds": ["abc"]
}
```

**Example Response:**

```code
{
    "statusCode": 400,
    "message": ["each value in parentProcessInstanceIds must be an integer number"]
}
```

### 2. Integer overflow (22003)

If a value exceeds the Postgres `INT` range, the query fails.

**Example Request:**

```code
{
    "parentProcessInstanceIds": [9999999999]
}
```

**Example Response:**

```code
{
    "statusCode": 500,
    "message": "Internal server error"
}
```

### 3. Payload too large (22001)

If the array size exceeds **1 million elements**, the request is rejected.

**Example Request:**

```code
{
  "parentProcessInstanceIds": [123, 123, ..., 123] // >1,000,000 items
}
```

**Example Response:**

```code
{
    "statusCode": 413,
    "message": "request entity too large"
}
```

## Delete Processes

Delete process instances and their related data from the system.

**`POST /processes/delete-bulk`**

### Request Body

```code
{
    "processInstanceIds": [12345, 67890]
}
```

| **Field  ** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `processInstanceIds` | number[] | Yes | List of **process instance IDs** to be permanently deleted |

### Curl

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/delete-bulk" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{ "processInstanceIds": [12345, 67890] }'
```

### Response

```code
{
    "status": "SUCCESS"
}
```

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `status` | string | 'SUCCESS' on completion, or 'FAILURE: [error message]' if an error occurs. |

### Possible Errors

The `/processes/delete-bulk` endpoint requires a valid `processInstanceIds` array.
 If missing or invalid, the following error scenarios may occur:

### 1. Missing processInstanceIds

If the request body is not provided, validation fails.

**Example Request:**

```code
{}
```

**Example Response:**

```code
{
    "statusCode": 400,
    "message": ["each value in processInstanceIds must be an integer number"]
}
```

### 2. Empty processInstanceIds

If an empty array is passed, validation fails.

**Example Request:**

```code
{
    "processInstanceIds": []
}
```

**Example Response:**

```code
{
    "statusCode": 400,
    "message": ["processInstanceIds should not be empty"]
}
```

## Generate SQL Backup

Generate a SQL script backup for selected process instances.

**`POST /processes/generate-sql`**

### Request Body

```code
{
    "processInstanceIds": [1001, 1002, 1003]
}
```

| **Field  ** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `processInstanceIds` | number[] | Yes | List of **process instance IDs** to generate backup |

### Curl

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/generate-sql" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{ "processInstanceIds": [1001, 1002, 1003] }'
```

### Response

```code
{
    "backupSqlScript": ["BEGIN;", "INSERT INTO ...;", "COMMIT;"]
}
```

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `backupSqlScript` | string[] | Generated SQL script lines (BEGIN..COMMIT) |

### Possible Errors

The `/processes/generate-sql` endpoint requires `processInstanceIds`.
 During validation, the following error scenarios may occur:

### 1. Missing processInstanceIds

If the request body is missing or empty, validation fails.

**Example Request:**

```code
{}
```

**Example Response:**

```code
{
    "statusCode": 400,
    "message": ["each value in processInstanceIds must be an integer number"],
    "error": "Bad Request"
}
```

### 2. Empty Array for processInstanceIds

If `processInstanceIds` is passed as an empty array, validation fails.

**Example Request:**

```code
{
    "processInstanceIds": []
}
```

**Example Response:**

```code
{
    "statusCode": 400,
    "message": ["processInstanceIds should not be empty"],
    "error": "Bad Request"
}
```

## Backup / Restore Processes

Initiates a backup or restore of specified process instances between source and target databases. The payload structure is the same for both operations. The process runs asynchronously, and an `auditId` is returned to track progress.

- **`POST /processes/backup`** — Backup from source **BPM_DB_NAME → BPM_BACKUP_DB_NAME**
- **`POST /processes/restore`** — Restore from target **BPM_BACKUP_DB_NAME → BPM_DB_NAME**

### Request Body

```code
{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "deploymentId": "dep-xyz-789",
    "beforeNoOfDays": 30,
    "taskName": "approveApplication",
    "taskStatus": "PENDING",
    "taskAssignee": "john.doe@example.com",
    "processVariables": [{ "name": "customerId", "value": "CUST-12345" }],
    "piids": [2001, 2002, 2003]
}
```

| **Field  ** | **  Type  ** | **  Required  ** | **  Description** |
| --- | --- | --- | --- |
| `processName` | string | No | Filter by **process definition name** |
| `processStatus` | enum | No | Process state: `ACTIVE`, `COMPLETED`, or `ABORTED` |
| `deploymentId` | string | No | Filter by **deployment version ID** |
| `beforeNoOfDays` | number | No | Return processes that started **before X days ago from now** |
| `taskName` | string | No | Filter by **task name** within the process |
| `taskStatus` | string | No | Task state (e.g., `PENDING`, `COMPLETED`) |
| `taskAssignee` | string | No | Filter by **assignee** (email/username of the person responsible) |
| `processVariables` | array | No | Array of **key-value filters** on process variables. Uses **AND** logic |
| `piids` | number[] | No | Explicit list of **process instance IDs** to backup or restore |

### Curl (Backup)

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/backup" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "beforeNoOfDays": 30
  }'
```

### Curl (Restore)

```code
curl -X POST \n  "http://{domain_name}/archivalservice/bpm/processes/restore" \n  -H "Authorization: Bearer <token>" \n  -H "Content-Type: application/json" \n  -d '{
    "processName": "customerOnboarding",
    "processStatus": "COMPLETED",
    "beforeNoOfDays": 30
  }'
```

### Response

```code
{
    "message": "Backup/Restore initiated successfully",
    "auditId": "3f49e17a-5121-4f2e-86e2-8d2e3f45c91f"
}
```

| **Field  ** | **  Type  ** | **  Description** |
| --- | --- | --- |
| `message` | string | Indicates that the backup or restore has been successfully initiated |
| `auditId` | string | Unique identifier to track the operation asynchronously |

### Operation Steps & Audits

### Batch Audit Flow

For **backup/restore operations**, processes are handled in **batches of 100**. Each **batch corresponds to one row** in `process_audit_logs` and is **updated sequentially** as operations complete.

### Audit Row Lifecycle (One Row per Batch)

| **Step  ** | **  Operation  ** | **  Audit Field Updates  ** | **  Description** |
| --- | --- | --- | --- |
| 1 | **Batch Start** | `audit_status` → `"inprogress"`, `remaining_process_count` → number of processes in this batch, `batch_name` → `"batch-X"` | Marks the start of processing for this batch |
| 2 | **Process Fetch** | `processInstanceIds` → list of fetched parent process IDs, `batch_status` → `"fetch_process"` | Fetch processes from source DB (backup) or target DB (restore) |
| 3 | **Child Process Fetch** | `childProcessInstanceIds` → list of child process IDs, `batch_status` → `"fetch_child_process"` | Fetch all child processes related to parent processes |
| 4 | **Generate SQL Backup / Restore Script** | `batch_status` → `"generating_backup_sql"`, `error_summary` / `error_message` populated if generation fails | Generate SQL statements for backup (to target DB) or restore (to source DB) |
| 5 | **Execute Backup / Restore SQL** | `batch_status` → `"executing_backup_sql"`, errors recorded in `error_code`, `error_message`, `error_resolve` if execution fails | Execute SQL on target DB (backup) or source DB (restore) |
| 6 | **Delete Source Data** | `batch_status` → `"delete_process"`, `processInstanceIds` removed from source DB | Delete processes that were successfully backed up/restored |
| 7 | **Batch Completion** | `batch_status` → `"completed"`, `remaining_process_count` → 0 | Marks the end of processing for this batch |

### Full Operation Timeline for 200 Processes

| **Row  ** | **  Audit Type  ** | **  Batch Name  ** | **  Batch Status (step updates)  ** | **  Process IDs  ** | **  Child Process IDs  ** | **  Remaining Count  ** | **  Error Summary** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | backup/restore | start | `"started"` | [] | [] | 200 | None |
| 2 | backup/restore | processCount | `"completed"` | [] | [] | 200 | None |
| 3 | backup/restore | batch-1 | `"fetch_process → fetch_child_process → generating_backup_sql → executing_backup_sql → delete_process → completed"` | [1–100] | [101–150] | 0 | Populated if any step fails |
| 4 | backup/restore | batch-2 | `"fetch_process → fetch_child_process → generating_backup_sql → executing_backup_sql → delete_process → completed"` | [101–200] | [151–200] | 0 | Populated if any step fails |
| 5 | backup/restore | complete | `"completed"` | [] | [] | 0 | None |

> Each batch row is **updated in-place**, reflecting the **current operation step** in `batch_status` and any errors.

### Possible Errors per Operation

### 1. Process Count

- **Audit fields updated:** `batch_status`, `remaining_process_count`
- **Errors:**
  - Missing or invalid filters
      Copy CodeCode{
      "statusCode": 400,
      "message": ["each value in processInstanceIds must be an integer number"]
     }
  - No matching processes found → `remaining_process_count` → 0

### 2. Process Fetch (Batch Start)

- **Audit fields updated:** `processInstanceIds`, `batch_status`
- **Errors:**
  - Invalid `piids` or process variables
      Copy CodeCode{
      "statusCode": 400,
      "message": ["processVariables.1.name should not be empty", "piids.2 must be a number"]
     }
  - Database query failure → `batch_status` → `"processFetch failed"`, `error_summary`/`error_message` populated

### 3. Child Process Fetch

- **Audit fields updated:** `childProcessInstanceIds`, `batch_status`
- **Errors:**
  - Invalid parent process IDs → `batch_status` → `"childProcessFetch failed"`, `error_summary` populated
  - Database query failure → SQL errors or timeout, `error_code` / `error_message` / `error_resolve` populated

### 4. Generate Backup / Restore SQL

- **Audit fields updated:** `batch_status`, `error_summary`, `error_message`
- **Errors:**
  - SQL generation failure (missing columns, null values) → `error_summary` → `"SQL generation failed"`
  - Empty batch → `batch_status` → `"generateBackupSQL skipped"`

### 5. Execute Backup / Restore SQL

- **Audit fields updated:** `batch_status`, `error_summary`, `error_message`, `error_code`
- **Errors:**
  - SQL execution error (syntax, constraint, missing table/column)
      Copy CodeCode{
      "error_code": "22003",
      "error_message": "integer overflow in piid",
      "error_resolve": "Check piid range in source DB"
     }
  - Connection/timeout errors → `batch_status` → `"executeSQL failed"`

### 6. Delete Source Data

- **Audit fields updated:** `batch_status`, `processInstanceIds`, `error_summary`
- **Errors:**
  - Constraint violation → `error_summary` → `"Delete failed due to foreign key constraint"`
  - Empty process list → `batch_status` → `"deleteProcess skipped"`

### 7. Batch Completion

- **Audit fields updated:** `batch_status` → `"completed"`, `remaining_process_count` → 0
- **Errors:** Audit row update failure → `error_summary` → `"Audit row update failed"`

**Notes:**

- Each **batch row** is updated **in-place** as steps complete.
- **Error fields** (`error_summary`, `error_code`, `error_message`, `error_resolve`) are populated **per batch**.
- **Asynchronous operation** ensures other batches continue even if one batch fails.
