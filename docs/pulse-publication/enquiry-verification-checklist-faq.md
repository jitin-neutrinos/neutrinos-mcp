# Project & Case Definition Linkage

<https://documentation.neutrinos.com/articles/#!pulse-publication/enquiry-verification-checklist-faq>

This describes the standard operating procedure for verifying enquiry-related issues. Follow the steps outlined below to diagnose potential configuration, database, and system health problems.

### Project & Case Definition Linkage

First, ensure the project is correctly linked to the specific Case Definition.

- Database Check:
  - Navigate to the table: `<caseserviceSchema>.project `
  - Action: Verify that the cdid (Case Definition ID) of the caseType is present for the specific `<projectId>`.
  - Logic: <projectId> $\rightarrow$ <cdid Of the caseType>
- API Check:
  - all the API: `/project/fetch`
  - Action: Verify that the caseType field is present in the API response.
- Fallback Configuration:

### Dynamic Table Configuration

Verify that the dynamic tables for the specific Project and Case Type combination have been created in the `<enquirySchema>`.

- Step A: Identify Table Names
  - Source Table: `<enquirySchema>.enquiry_config `
  - Lookup Keys: Use the `projectId` and `caseType`.
  - Retrieve Fields: Note down the values for `caseInstanceTableName`, `taskInstanceTableName`, and `signalInstanceTableName`.
- Step B: Verify Table Creation Check if the tables actually exist in the database:
  - Case Instance: `ci_<randomString>` (Contains: cid, caseType, created_at, etc.)
  - Task Instance: `ti_<randomString>` (Contains: cid, etc.)
  - Signal Instance: si_<randomString> (Contains: cid, etc.)

### Column Mapping Verification

- Source Table: `<enquirySchema>.projection_data`
- Action: Retrieve the mapping to translate technical column names to user-readable properties.
- Mapping Logic: Verify mpPath (property path), mpType (data type), and columnName.

### System Health, GTS & Logs

Ensure the backend services and cron jobs responsible for processing enquiries are healthy.

- Deployment Status:
  - Verify if the GTS deployment pod is running.
  - If running, capture and review the logs for errors.
- GTS Configuration:
  - Action: Ensure `FETCH_LOOKBACK_MINUTES` is present in the configuration.
  - Action: Verify if the time value assigned to `FETCH_LOOKBACK_MINUTES` is correct for the current requirements.
- Cron Job Status:
  - Table: `gts_cron_last_run`
  - Action: Ensure there is at least one entry where the column `cron_name` equals `"GTS"`.

### Data Integrity Check

Perform a final check on the specific data instances using the mappings found above.

- Task Verification: Check if the expected taskId exists in the `ti_<randomString>` table.
- Case Verification: Check if the expected cid (Case ID) exists in the `ci_<randomString>` table.
- Filter Logic Verification:
  - If a filter is failing, identify the specific Case Data Property being filtered.
  - Use the mapping from Step 3 to find the corresponding database column.
  - Check that column in the `ci_<randomString>` table for the specific cid to ensure the value matches expectations.
