# Breaking Changes

<https://documentation.neutrinos.com/articles/#!pulse-publication/configuration-migration-guide-faq>

The Case Service configuration has been updated to support custom sorting behavior when retrieving cases. To maintain backward compatibility, the default sorting configuration has been commented out in the deployment values files.

This guide describes the change, its impact, and the steps required to configure your environment accordingly.

### Breaking Changes

**Note**: **Case Service Sort Behavior ** - The default sorting configuration for case retrieval has been modified. If your implementation relies on the previous default sorting behavior (ORDER BY created_at DESC), you must explicitly configure the sort parameters in the deployment values file. To preserve the previous behavior, uncomment the relevant variables.

### Configuration Migration

#### Before - Previous Default Configuration

The following environment variables were active and set these defaults automatically:

```yaml
# Case service sort configuration (active by default) 

CASE_FETCH_ALL_SORT_COLUMN: 'created_at' 

CASE_FETCH_ALL_SORT_ORDER: 'DESC' 
```

#### After — Updated Configuration

The sort variables are now commented out by default. To preserve the previous sorting behavior or apply custom sorting, uncomment and configure the variables as required.

```yaml
# For custom sort behavior, set these variables. 
# To preserve the old sort order, keep this commented out. 
# 
# CASE_FETCH_ALL_SORT_COLUMN: 'created_at'   # created_at | updated_at 
# CASE_FETCH_ALL_SORT_ORDER: 'DESC'           # DESC | ASC 
```

**Note**: **Action Required** - If your application relies on sorting cases by created_at DESC, you must uncomment and explicitly configure both CASE_FETCH_ALL_SORT_COLUMN and CASE_FETCH_ALL_SORT_ORDER in your deployment values file. If these variables remain commented out, the database’s default sort order will be applied.

### Environment Variables

The following table describes the modified environment variables for the alpha-caseservice deployment:

| Environment Variable | Description | Default Value |
| --- | --- | --- |
| CASE_FETCH_ALL_SORT_COLUMN | Sort column for case fetching. Accepted values: created_at, updated_at | 'created_at' (commented out) |
| CASE_FETCH_ALL_SORT_ORDER | Sort order for case fetching. Accepted values: ASC, DESC | 'DESC' (commented out) |

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | **Both variables must be set together**. Setting only one may result in unexpected behavior. |
| --- | --- |

### Configuration Examples

#### Restore Previous Behavior (Recommended for existing deployments)

```yaml
# Explicitly restore original sort behavior 

CASE_FETCH_ALL_SORT_COLUMN: 'created_at' 

CASE_FETCH_ALL_SORT_ORDER: 'DESC' 
```

#### Sort by Last Updated (New capability)

```yaml
# Show most recently modified cases first 

CASE_FETCH_ALL_SORT_COLUMN: 'updated_at' 

CASE_FETCH_ALL_SORT_ORDER: 'DESC' 
```

#### Sort by Oldest First

```yaml
# Show oldest cases first (ascending order) 

CASE_FETCH_ALL_SORT_COLUMN: 'created_at' 

CASE_FETCH_ALL_SORT_ORDER: 'ASC' 
```

### Migration Checklist

1. Review your current values files to determine if you rely on default case sort ordering.
2. If the default sort order is required, uncomment CASE_FETCH_ALL_SORT_COLUMN and CASE_FETCH_ALL_SORT_ORDER
3. Set both variables together — do not configure only one of the two.
4. Validate your deployment configuration before applying it to production environments.
5. Test case listing behaviour in a staging environment after the update.
