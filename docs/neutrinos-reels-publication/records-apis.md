# Records APIs

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/records-apis>

Once the schema is created, the next step is to act on the records-related APIs. To integrate Content repository Records APIs, follow the steps below:

1. **Add Records**:
    This API adds records to a schema on the platform. It accepts the schema name, version, and field values as parameters in the request body. The following example illustrates a sample request for the Add Records API call.
    Copy CodeJSON{
    "schemaName": "Test3",
    "version": "1.0.0",
    "data": {
    "name": "*****",
    "age": "32",
    "PersonDetails":
    "{\"city\":\"Atp\",\"country\":\"India\"}"
    }
   }
    Upon successful execution of the API call, a success message is returned along with the data added to the schema and the ID of the newly created record. The following example shows a sample response for the Add Records API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "name": "*****",
    "age": "32",
    "PersonDetails": "{\"city\":\"Atp\",\"country\":\"India\"}",
    "id": "2ffb3cdf-4de5-4b97-a0d7-39a4b84e8aa8",
    "disabled": false,
    "createdAt": "2025-10-28T09:20:58.719Z",
    "updatedAt": "2025-10-28T09:20:58.719Z"
    },
    "timestamp": "2025-10-28T09:20:58.726Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema on the platform to which the records are to be added.
  - **version**: Specifies the version of the schema on the platform to which the records are to be added.
  - **data**: Specifies the data for the schema on the platform to which the records are added. The data must strictly adhere to the structure defined in the schema created on the platform.
2. **Update Record**:
    This API updates records within a schema. It accepts the schema name, version, record ID, and the complete set of data fields as parameters in the request body to update the record. Note: If the provided record ID does not match any existing record, an error message is returned indicating that no matching record was found. The following example illustrates a sample request for the Update Records API call.
    Copy CodeJSON{
    "schemaName": "Test3",
    "version": "1.0.0",
    "recordId": "2ffb3cdf-4de5-4b97-a0d7-39a4b84e8aa8",
    "data": {
    "name": "*****",
    "age": "26",
    "PersonDetails": "{\"City\":\"AP\"}"
    }
   }
    Upon successful execution of the API call, a success message is returned along with the updated data for the record. The following example shows a sample response for the Update records API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": "2ffb3cdf-4de5-4b97-a0d7-39a4b84e8aa8",
    "name": "*****",
    "age": "26",
    "PersonDetails": "{\"City\":\"AP\"}",
    "updatedAt": "2025-10-29T04:27:50.405Z",
    "disabled": false
    },
    "timestamp": "2025-10-29T04:27:50.405Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema on the platform for which the record needs to be updated.
  - **version**: Specifies the version of the schema on the platform that contains the record to be updated.
  - **recordId**: Specifies the record ID of the entry in the schema that needs to be updated. The value of this field is the same as the one generated for the record when it was created using the Add Records API.
  - **data**: Specifies the fields of the records in the schema that need to be updated. The fields are based on the schema configuration.
3. **Fetch All**:
    This API fetches all the records within a schema. It accepts schemaName, version, pageNumber, pageSize, searchKey as body parameters to fetch the record. Note: If the provided schemaName or version does not match any existing schema, an error message is returned indicating that no matching schema was found. The following example illustrates a sample request for the Fetch All Records API call.
    Copy CodeJSON{
    "schemaName": "Test3",
    "version": "1.0.0",
    "pageNumber": 1,
    "pageSize": 10,
    "searchKey": ""
   }
    Upon successful execution of the API call, a success message is returned along with the data of all records fetched from the schema. The following example shows a sample response for the Fetch All Records API call.
    Copy CodeJSON{
    "success": true,
    "data": [
    {
    "id": "0658d289-8b4f-4ada-9170-919b3e0dca9c",
    "age": "26",
    "name": "*****",
    "disabled": false,
    "createdAt": "2025-10-29T05:04:26.908Z",
    "updatedAt": "2025-10-29T05:04:26.908Z",
    "PersonDetails": "{\"city\":\"Atp\",\"country\":\"India\"}"
    },
    {
    "id": "6e84b956-e3df-411f-acd0-312d82a7107d",
    "age": "26",
    "name": "*****",
    "disabled": false,
    "createdAt": "2025-10-29T04:51:09.763Z",
    "updatedAt": "2025-10-29 04:53:47.801691+00",
    "PersonDetails": "{\"City\":\"AP\"}"
    }
    ],
    "meta": {
    "totalCount": 2,
    "pageNumber": 1,
    "pageSize": 10
    },
    "timestamp": "2025-10-29T05:15:12.668Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema on the platform from which the record needs to be fetched.
  - **version**: Specifies the version of the schema on the platform from which the records are to be fetched.
  - **pageNumber**: Specifies the page number from which the records are to be fetched in the schema on the platform.
  - **pageSize**: Specifies the number of records to be retrieved per page when fetching records from the schema on the platform.
  - **searchKey**: Specifies the search key used to fetch records from the schema. The search key can be a complete or partial value used to locate specific records. The API returns all records that match the specified search key. If no search key is provided, the API returns all records present in the schema.
4. **Fetch Specific Record**:
    This API fetches a specific record from the schema based on the record ID obtained when the record was added to the schema, which is passed as a body parameter. Along with the record ID, the schemaName and version must also be included in the body parameters. The following example shows a sample request for the Fetch One Record API call.
    Copy CodeJSON{
    "schemaName": "Test3",
    "version": "1.0.0",
    "recordId": "0658d289-8b4f-4ada-9170-919b3e0dca9c"
   }
    Upon successful execution of the API call, a success message is returned along with the data of the matching record from the schema. The following example shows a sample response for the Fetch One Record API call.
    Copy CodeJSON{
    "success": true,
    "data": {
    "id": "0658d289-8b4f-4ada-9170-919b3e0dca9c",
    "age": "26",
    "name": "*****",
    "disabled": false,
    "createdAt": "2025-10-29T05:04:26.908Z",
    "updatedAt": "2025-10-29T05:04:26.908Z",
    "PersonDetails": "{\"city\":\"Atp\",\"country\":\"India\"}"
    },
    "timestamp": "2025-10-29T05:36:22.831Z"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema on the platform from which the record needs to be fetched.
  - **version**: Specifies the version of the schema on the platform from which the records are to be fetched.
  - **recordId**: Specifies the record ID of the specific entry in the schema from which the record is to be fetched.
5. **Delete**:
    This API deletes a specific record from the schema based on the record ID obtained when the record was added to the schema, which is passed as a body parameter. Along with the record ID, the schemaName and version must also be included in the body parameters. The following example shows a sample request for the Delete Record API call.
    Copy CodeJSON{
    "schemaName": "Test3",
    "version": "1.0.0",
    "recordId": "32d29286-2941-4e9c-909b-f680c13f6549"
   }
    Upon successful execution of the API call, a success message is returned indicating that the record with the specified ID has been deleted from the schema. The following example shows a sample response for the “Delete Record” API call.
    Copy CodeJSON{
    "success": true,
    "message": "Record with ID 32d29286-2941-4e9c-909b-f680c13f6549 disabled successfully"
   }
    **Note**: In this example, a centralized token generated from the platform is used and passed in the request header with the key token to authorize the API call. Alternatively, an IDS token can also be used.
  - **schemaName**: Specifies the name of the schema on the platform from which the record is to be deleted.
  - **version**: Specifies the version of the schema on the platform from which the records are to be deleted.
  - **recordId**: Specifies the record ID of the entry in the schema from which the record is to be deleted.
