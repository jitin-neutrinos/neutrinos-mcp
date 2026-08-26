# Onboarding Tenant

<https://documentation.neutrinos.com/articles/#!hypha/onboarding-tenant-and-schema>

Tenant onboarding in a Hypha environment is the process of provisioning and configuring a new organizational entity (tenant) to securely consume, manage, and operate within the shared data infrastructure.

Schema onboarding is the process of registering, validating, and integrating new data schemas into the fabric's metadata and governance layers. This ensures that new datasets are discoverable, queryable, and compliant with data management standards.

# Onboarding Tenant

Tenant onboarding involves creating a dedicated namespace for a new organization. During this step, provide the organization name and a unique ID to provision the tenant space. The organization ID will be required later when configuring data sources and onboarding schemas. Use the following endpoint to create a tenant:




 **Endpoint**: /tenant-config/create/tenant

**Header**

| **Field  ** | **  Value** |
| --- | --- |
| Authorization (required) | Bearer <Token> |
| x-organization-id (required) | Provide the organization ID |

**Body**

| **Field** | **Value** |
| --- | --- |
| name (required) | Name of the organization |
| organizationId (required) | Provide the organization ID |

Upon successful execution of the above cURL, a tenant space is created for the tenant name and organization ID provided in the request body.

# Create Data Source

After creating a tenant space for the organization, the next step is to create a data source. This data source will be referenced in later steps while onboarding schemas and creating objects. Use the following endpoint to create a Data Source:




 **Endpoint**: /tenant-config/create/datasource

**Header**

| **Field  ** | **  Value** |
| --- | --- |
| Content (required) | application/json |
| Authorization (required) | Bearer <Token> |
| x-organization-id | The organization ID is as provided during the tenant creation process. |

**Body**

| **Field** | **Value** |
| --- | --- |
| name (required) | Specify the name of the data source. This name will be used later to identify the specific data source. |
| type (required) | Type of the Database being used to specify the Data Source |
| Config (required) | An array containing the following details    dbType: The database type.    host: The database host.    port: The port number used by the database host.    username and password: The credentials to authenticate the database transactions.    database: The name of the database to connect to. |

Upon successful execution of the above cURL, a data source ID is returned. This ID will be used later for onboarding schemas.

# Onboarding Schema

In this step, a schema is uploaded to the previously created data source. Each schema is packaged as either a ZIP file or an Excel file containing the structure of an entity (database table), including its fields, relationships, constraints, and other required properties. Each entity within the schema is defined in JSON format. The cURL request accepts form data in the body, where the schema must be uploaded as a ZIP or Excel file.

The sample JSON for an account schema is shown below:

Use the following endpoint to create a schema:




 **Endpoint**: /tenant-config/create/schema/{{dataSourceId}}/{{schemaName}}




 The dataSourceId obtained during data source creation must be passed as a path parameter. Additionally, a schema name must be provided along with the dataSourceId. The schema name should be a valid identifier.

**Header**

| **Field  ** | **  Value** |
| --- | --- |
| Authorization (required) | Bearer <Token> |
| x-organization-id (required) | The organization ID is as provided during the tenant creation process. |

**Body/Form**

| **Field  ** | **  Value** |
| --- | --- |
| Path | Specify the path to the ZIP file or Excel sheet that contains the schema files or related information required for schema creation. |

Upon successful execution of the above cURL command, a schema ID is returned. This ID will be required for all subsequent transactions.
