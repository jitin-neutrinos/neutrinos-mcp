# Schema APIs

<https://documentation.neutrinos.com/articles/#!pulse-publication/schema-apis>

To integrate Content repository Schema APIs, follow the steps below:

1. **Create Schema**:
    The initial step is to create a schema, which serves as a template for the content that will be used in subsequent steps.
    Use the OpenAPI 3.0 standards to define the schema, as illustrated in the sample below:
    Copy CodeJSON{
    "schemaName": "Test3",
    "schema": {
    "type": "object",
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "description": "Schema for user data validation",
    "tags": [
    "tag1"
    ]
   }
    After the successful execution of the above JSON, the system returns a success message along with the schema ID. The output will appear similar to the sample shown below:
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": *****,
    "schemaName": "Test3",
    "activeVersion": "1.0.0",
    "description": "Schema for user data validation",
    "schema": {
    "type": "object",
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    },
    "required": [
    "age",
    "name",
    "PersonDetails"
    ]
    },
    "createdAt": "2025-10-28T09:10:05.339Z"
    },
    "timestamp": "2025-10-28T09:10:05.467Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema being created. Provide a valid and descriptive name that represents the purpose or structure of the schema. In this example, the schema name is specified as TestTry.
  - The schema is curated based on the specific requirements and designed in accordance with OpenAPI 3.0 standards. Each object within the schema defines the data type and format of the values it can contain. The format can include user input types such as number, email, JSON, or Markdown.
  - **Description**: Provides a brief description of the schema or template. It helps users understand the purpose of the schema and its intended use.
  - **Tags**: This is an optional field that allows you to specify a tag for each version of the schema.
2. **Update Schema**:
    This operation updates one or more fields within a schema or template. It requires the schema ID generated from the Create Schema API as a parameter. You must also provide the schema name that was specified in the Create Schema request. For example, the following JSON illustrates a sample request for updating a schema.
    Copy CodeJSON{
    "id": *****,
    "schemaName": "TestTry-update",
    "schema": {
    "type": "object",
    "properties": {
    "phone": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    },
    "info": {
    "type": "string",
    "format": "markdown"
    }
    },
    "required": [
    "phone",
    "name",
    "PersonalDetails"
    ]
    },
    "description": "Schema for user data validation"
   }
    After the successful execution of the above JSON, a success message is displayed, and the updated JSON is returned as the output.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": *****,
    "schemaName": "TestTry-update",
    "activeVersion": "1.0.3",
    "description": "Schema for user data validation",
    "schema": {
    "type": "object",
    "properties": {
    "phone": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    },
    "info": {
    "type": "string",
    "format": "markdown"
    }
    },
    "required": [
    "phone",
    "name",
    "PersonalDetails",
    "info"
    ]
    },
    "createdAt": "2025-10-28T09:11:25.665Z"
    },
    "timestamp": "2025-10-28T09:11:25.665Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **id**: Specifies the schema ID returned from the Create Schema API call.
  - **schemaName**: Specifies the schema name provided during the Create Schema API call.
  - Update a specific field or multiple fields as required. Note: Ensure that the names of the updated fields are also modified in the required section at the end of the JSON. This section lists all the fields defined in the schema.
3. **Fetch All**:
    This API retrieves all existing schemas available on the platform. The following JSON illustrates a sample request for this API:
    Copy CodeJSON{
    "pageNumber": 1,
    "pageSize": 20,
    "searchKey": "TestTry",
    "orderBy": {
    "option": "asc",
    "field": "createdAt"
    }
   }
    Upon successful execution of the above JSON, the output displays a list of all available schemas based on the specified searchKey. If no value is provided, the response returns all available schemas on the platform. The following JSON shows a sample response for the successful execution of the API request.
    Copy CodeJSON{
    "success": true,
    "meta": {
    "totalCount": 1,
    "totalPages": 1,
    "pageNumber": 1,
    "pageSize": 20
    },
    "data": [
    {
    "id": *****,
    "schemaName": "TestTry-update",
    "createdAt": "2025-10-24T06:38:08.689Z",
    "description": "Schema for user data validation",
    "activeVersion": "1.0.3",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "author": "",
    "tags": [],
    "versions": [
    {
    "id": *****,
    "tags": [],
    "version": "1.0.3",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails",
    "info"
    ],
    "properties": {
    "info": {
    "type": "string",
    "format": "markdown"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-28T09:11:25.647Z",
    "updatedAt": "2025-10-28T09:11:25.647Z"
    },
    {
    "id": *****,
    "tags": [],
    "version": "1.0.2",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-27T12:06:48.827Z",
    "updatedAt": "2025-10-27T12:06:48.827Z"
    },
    {
    "id": *****,
    "tags": [],
    "version": "1.0.1",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:42:06.350Z",
    "updatedAt": "2025-10-24T06:42:06.350Z"
    },
    {
    "id": *****,
    "tags": [
    "tag1"
    ],
    "version": "1.0.0",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "age",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:38:08.689Z",
    "updatedAt": "2025-10-24T06:38:08.689Z"
    }
    ]
    }
    ],
    "timestamp": "2025-10-28T10:55:53.458Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **pageNumber**: Specifies the page number from which the available schemas are to be retrieved.
  - **pageSize**: Specifies the number of schemas to be displayed on a single page.
  - **searchKey**: Specifies the search key used to filter and retrieve schemas. This is an optional field.
  - **orderBy**: Sorts the list of schemas retrieved from the platform based on the specified field and order. The order can be either asc (ascending) or desc (descending).
4. **Fetch By Id**:
    This API retrieves a specific schema from the platform using the schema ID provided in the request body. The schema ID corresponds to the one returned when the schema is created through the Create Schema API. The following JSON shows a sample request for this API call:
    Copy CodeJSON{
    "id": *****
   }
    Upon successful execution of the above JSON, the output displays the schema that matches the ID specified in the request body. If no matching schema is found, an error message is returned indicating that no records match the provided ID. The following JSON shows a sample response for this API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": *****,
    "schemaName": "TestTry-update",
    "createdAt": "2025-10-24T06:38:08.689Z",
    "description": "Schema for user data validation",
    "activeVersion": "1.0.3",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "versions": [
    {
    "id": *****,
    "version": "1.0.0",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "age",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:38:08.689Z",
    "updatedAt": "2025-10-24T06:38:08.689Z",
    "tags": [
    "tag1"
    ]
    },
    {
    "id": *****,
    "version": "1.0.1",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:42:06.350Z",
    "updatedAt": "2025-10-24T06:42:06.350Z",
    "tags": []
    },
    {
    "id": *****,
    "version": "1.0.2",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-27T12:06:48.827Z",
    "updatedAt": "2025-10-27T12:06:48.827Z",
    "tags": []
    },
    {
    "id": *****,
    "version": "1.0.3",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails",
    "info"
    ],
    "properties": {
    "info": {
    "type": "string",
    "format": "markdown"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-28T09:11:25.647Z",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "tags": []
    }
    ]
    },
    "timestamp": "2025-10-28T10:57:41.240Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **id**: Specify the schema ID in the request body to retrieve the corresponding schema. This ID is the same as the one returned when the schema is created.
5. **Fetch by Name**:
    This API retrieves a specific schema from the platform using the schema name provided in the request body. The schema name must match the one specified during the creation of the schema through the Create Schema API. The following JSON shows a sample request for this API call.
    Copy CodeJSON{
    "schemaName": "TestTry-update"
   }
    Upon successful execution of the above JSON, the output displays the schema that matches the name specified in the request body. If no matching schema is found, an error message is returned indicating that no records match the provided name. The following JSON shows a sample response for this API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": *****,
    "schemaName": "TestTry-update",
    "createdAt": "2025-10-24T06:38:08.689Z",
    "description": "Schema for user data validation",
    "activeVersion": "1.0.3",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "versions": [
    {
    "id": *****,
    "version": "1.0.0",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "age",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:38:08.689Z",
    "updatedAt": "2025-10-24T06:38:08.689Z",
    "tags": [
    "tag1"
    ]
    },
    {
    "id": *****,
    "version": "1.0.1",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:42:06.350Z",
    "updatedAt": "2025-10-24T06:42:06.350Z",
    "tags": []
    },
    {
    "id": *****,
    "version": "1.0.2",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails"
    ],
    "properties": {
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-27T12:06:48.827Z",
    "updatedAt": "2025-10-27T12:06:48.827Z",
    "tags": []
    },
    {
    "id": *****,
    "version": "1.0.3",
    "schemaDefinition": {
    "type": "object",
    "required": [
    "phone",
    "name",
    "PersonalDetails",
    "info"
    ],
    "properties": {
    "info": {
    "type": "string",
    "format": "markdown"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "phone": {
    "type": "string",
    "format": "input"
    },
    "PersonalDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-28T09:11:25.647Z",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "tags": []
    }
    ]
    },
    "timestamp": "2025-10-28T10:59:05.906Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specify the schema name in the request body to retrieve the corresponding schema. The name must match the one provided during schema creation. Note: The schema name is case-sensitive, and the API retrieves only the schema that exactly matches the name provided in the request body.
6. **Fetch by Name and Version**:
    This API retrieves a specific schema from the platform using the schema name and version provided in the request body. The schema name must match the one specified during schema creation through the Create Schema API, and the version must correspond to the one available on the platform. The following JSON shows a sample request for this API call.
    Copy CodeJSON{
    "name": "TestTry-update",
    "version": "1.0.0"
   }
    Upon successful execution of the above JSON, the output displays the schema that matches the name and version specified in the request body. If no matching schema is found, an error message is returned indicating that no records match the provided name and version. The following JSON shows a sample response for this API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": *****,
    "activeVersion": "1.0.3",
    "schemaName": "TestTry-update",
    "version": "1.0.0",
    "description": "Schema for user data validation",
    "schema": {
    "type": "object",
    "required": [
    "age",
    "name",
    "PersonDetails"
    ],
    "properties": {
    "age": {
    "type": "string",
    "format": "input"
    },
    "name": {
    "type": "string",
    "format": "input"
    },
    "PersonDetails": {
    "type": "string",
    "format": "json"
    }
    }
    },
    "createdAt": "2025-10-24T06:38:08.689Z",
    "updatedAt": "2025-10-28T09:11:25.647Z",
    "tags": [
    "tag1"
    ]
    },
    "timestamp": "2025-10-28T11:01:38.279Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **name**: Specify the name of the schema in the request body to retrieve the corresponding schema. Note: The schema name is case-sensitive, and the API retrieves only the schema that exactly matches the name provided in the request body.
  - **version**: Specify the schema version in the request body to retrieve the corresponding schema. Note: The specified version must exist for the schema name provided in the request.
7. **Remove**:
    This API deletes a specific schema from the platform using the schema name provided in the request. The schema name must exactly match the name of an existing schema on the platform.
    Copy CodeJSON{
    "schemaName": "TestTry-update"
   }
    Upon successful execution of the above JSON, the output displays a success message indicating that the schema with the corresponding name is removed successfully. The following JSON shows a sample response for this API call.
    Copy CodeJSON{
    "success": true,
    "message": "Schema removed successfully"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specify the schema name in the request body to delete the corresponding schema. Note: The schema name is case-sensitive, and the API deletes only the schema that exactly matches the name provided in the request body.
