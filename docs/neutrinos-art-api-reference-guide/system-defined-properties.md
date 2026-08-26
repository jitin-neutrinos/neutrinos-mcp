# Manage Data Models

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/system-defined-properties>

## Manage Data Models

Manage data models in Neutrinos Art using these APIs:


 GET/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}




 PUT/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}




 DELETE/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}




 PATCH/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}




 GET/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}




 DELETE/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}




 PATCH/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}









 GET/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}



 The API to get data for a data model.





 **Parameters:**





 Name


 Description


 Required?






 tenantName


 The tenant provided by the Neutrinos administrator.


 Yes




 appName


 The name of the app.


 Yes




 datasource


 The name of a connection from the Neutrinos Art server to a tenant-specific database.





 Yes




 dataModelName


 The data model name of the specified app.

 Yes




 filter



 A MongoDB query assigned to qparam value. The value defaults to {}.


 The documents returned by the API call will be filtered based on the specified condition. Only documents that match the condition are retrieved.














 key


 Projections to be applied on MongoDB.













 sort


 The sort to be applied to the query results. Defaults to {}.













 pagenumber


 Page number for paginated queries. Defaults to 1.













 page size


 The size of each page to be returned. Defaults to 100.














 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 406


 Invalid Params




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 PUT/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}






 API to add data to a data model. Upserts the resource identified by the request URL. If the resource does not already exist, the PUT request creates it by setting its state as specified in the request JSON body. If the resource exists, the PUT request sets the resource state as specified in the request JSON body.


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




 datamodel


 (body)






 The data model object to be saved.



 Yes





 **Responses:**





 **Code**


 **Description**




 201


 The object is written for the specified dataModelName.




 500


 Object Writing failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 DELETE/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}






 The API to delete a data model based on the filter query.


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




 filter


 String(query)






 The MongoDB filter query parameter which allows specifying conditions on the documents to delete.


 This query is assigned as the variable qparam value.






 Yes





 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 404


 Data model ID not found




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 PATCH/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}






 The API to add or update multiple objects to a data model.


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




 datamodel


 String(query)






 The Data Model object to be saved.



 Yes



 **Responses**






 **Code**


 **Description**


 **Example**




 200



 Operation Successful




 **Example:**Value:Copy CodeJSON{
 "n": 44,
 "nModified": 44,
 "ok": 1
}Model:Copy CodeJavaScriptdmpatchs
{
 n:
 integer
 example: 44
 nModified:
 integer
 example: 44
 ok:
 integer
 example: 1
}






 500


 Operation failed











 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 GET/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}






 The API to get a data model based on the data model ID.


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




 dataModelId


 String(path)






 Unique identifier for the instance of the data model.






 Yes





 **Responses:**





 **Code**


 **Description**




 200


 Operation successful



 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 DELETE/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}






 The API to delete a data model based on the data model ID.


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




 dataModelId


 String(path)









 Id of the data model that needs to be deleted.



 Yes





 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 404


 Data model ID not found




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 PATCH/{tenantName}/datamodel/{datasource}/{appName}/{dataModelName}/{dataModelId}






 The API to add or update the data model attributes based on the data model ID.


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




 dataModelId


 String(path)






 Unique identifier for the instance of the data model.






 Yes




 dataModel


 (body)


 The data model object to be saved.




 Yes





 **Responses:**





 **Code**


 **Description**


 **Example**




 200


 Operation Successful



 **Example:**


 Value:


 Copy CodeJSON{
 "n": 44,
 "nModified": 44,
 "ok": 1
}




 Model:


 Copy CodeJSONdmpatchs
{
 n:
 integer
 example: 44
 nModified:
 integer
 example: 44
 ok:
 integer
 example: 1
}




 406


 invalid datamode Id or invalid json input










 500


 Operation failed













 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.
