# Manage Data Model Indexes

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/manage-data-model-indexes>

## 

---

## Manage Data Model Indexes

A data model index is any data structure that improves the performance of the data model lookup. You manage data model indexes in Neutrinos Art using these APIs:



 PUT/{tenantName}/datamodelIndex/{datasource}/{appName}/{dataModelName}




 DELETE/{tenantName}/datamodelIndex/{datasource}/{appName}/{dataModelName}/{indexName}




PUT/{tenantName}/datamodelIndex/{datasource}/{appName}/{dataModelName}




 This API allows you to create the indexes of your database collection.If the index does not already exist, the PUT request creates it and sets its state as specified in the request JSON body. If the index exists, the PUT request sets the resource state as specified in the request JSON body.
 **Parameters:**NameTypeDescriptionRequired?tenantNameString(path)The tenant provided by the Neutrinos administrator.YesappNameString(path)

The name of the app.YesdatasourceString(path)

The name of a connection from the Neutrinos Art server to a tenant-specific database.

Yes dataModelName String(path)

The data model name of the specified app.YesdmIndex(body)

The data model index to be configured.Yes**Responses:****Code****Description****Example**201The Index is configured for the specified dataModelName. **Example:**Value:Copy CodeJSON{
 "fieldOrSpec": {},
 "options": {}
}Model:Copy CodeJSONdmIndex
{
 fieldOrSpec: {...}
 options: {...}
}500Index creation failed



 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 DELETE** /{tenantName}/datamodelIndex/{datasource}/{appName}/{dataModelName}/{indexName}**







 The API to delete a data model index based on the index name.

 **Parameters:**





 Name


 Type


 Description


 Required?







 tenantName



 String(path)


 The tenant provided by the Neutrinos administrator.


 Yes




 appName


 String(path)





 The name of the app.


 Yes




 datasource


 String(path)





 The name of a connection from the Neutrinos Art server to a tenant-specific database.





 Yes




 dataModelName


 String(path)





 The data model name of the specified app.


 Yes




 indexName

 String(path)






 The name of the index that is to be deleted.



 Yes





 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 404

 Index not found




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.
