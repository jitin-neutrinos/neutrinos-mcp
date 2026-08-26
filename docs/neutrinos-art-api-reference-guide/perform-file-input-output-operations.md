# Perform File Input and Output Operations

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/perform-file-input-output-operations>

## Perform File Input and Output Operations

Perform operations on a document using these APIs:
 POST/{tenantName}/fileio/{datasource}/{appName}/{entityName}GET/{tenantName}/fileio/{datasource}/{appName}/{entityName}DELETE/{tenantName}/fileio/{datasource}/{appName}/{entityName}DELETE/{tenantName}/fileio/{datasource}/{appName}/{entityName}/{fileId}GET/{tenantName}/fileio/{datasource}/{appName}/{entityName}/{fileId}






 POST/{tenantName}/fileio/{datasource}/{appName}/{entityName}

 An entity is a group of files. This API is used to create a file within the specified entity.




 **Parameters:**NameTypeDescriptionRequired?tenantNameString(path) The tenant provided by the Neutrinos administrator.YesappNameString(path)
The name of the app.YesdatasourceString(path)
The name of a connection from the Neutrinos Art server to a tenant-specific database.
Yes EntityName String(path)
The name of the entity.Yesfile(body)
The file to be added to the entity.Yesmetadatafile (formdata)
The body of the API call.**Example:**Value:Copy CodeJSON{
 "key": "abc@gmail.com"
}
Model:Copy CodeJSONfileioobject
{
 key: string
 example: abc@gmail.com
}Yes


 **Responses:**




 **Code**

 **Description**
 **Example**

 200

 Operation Successful Value:Copy CodeJSON{
 "_id": "59b0f135e99ee51b405dabdb",
 "length": 19972,
 "chunkSize": 261120,
 "uploadDate": "2017-09-07T07:11:49.701Z",
 "md5": "5e42ea8d27bcd28bcf67a9a1841ad6ef",
 "filename": "jatah.png",
 "contentType": "image/png",
 "aliases": [
 "jatah.png"
 ],
 "metadata": {
 "key": "abc@gmail.com",
 "originalname": "jatah.png",
 "mimetype": "image/png"
 }
}
Model:Copy CodeJSONfileioResponse{
 length: integer
 example: 19972
 filename: string
 example: jatah.png
 chunkSize: integer
 example: 261120
 uploadDate: string
 example: 2017-09-07T07:11:49.701Z
 metadata: {
 key: string
 example: abc@gmail.com
 originalname: string
 example: jatah.png
 mimetype: string
 example: image/png
}
contentType: string
example: image/png
_id: string
example: 59b0f135e99ee51b405dabdb
md5: string
example: 5e42ea8d27bcd28bcf67a9a1841ad6ef
aliases: [string
 example: jatah.png]
}

 500
Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.



 GET/{tenantName}/fileio/{datasource}/{appName}/{entityName}API to get the file based on the entity name and the metadata filter.


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




 entityName


 String(path)




 The name of the entity

 Yes




 metadataFilter

 object(query)




 The metadata defined when the file was created.

 Yes





 **Responses:**





 **Code**


 **Description**




 200

 Operation successful




 500

 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.



 DELETE/{tenantName}/fileio/{datasource}/{appName}/{entityName}The API to delete a file based on the entity name and the metadata filter.

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




 entityName


 String(path)




 The name of the entity

 Yes




 metadataFilter


 object(query)







 The metadata defined when the file was created.





 Yes





 **Responses:**




 **Code**

 **Description**
 **Example**

 200

 Operation Successful Value:Copy CodeJSON[
 "59b0f135e99ee51b405dabdb"
]
Model:Copy CodeJSON[string
example: 59b0f135e99ee51b405dabdb]


 500

 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.



 DELETE/{tenantName}/fileio/{datasource}/{appName}/{entityName}/{fileId}The API to delete a file based on the file ID.

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




 entityName


 String(path)





 The name of the entity.

 Yes




 fileId

 String(path)






 The unique ID of the file to be deleted.


 Yes



 **Responses**





 **Code**

 **Description**

 **Example**


 200


 Operation Successful


 **Example:**Value:Copy CodeJSON[
 "59b0f135e99ee51b405dabdb"
]Model:Copy CodeJSON[string
example: 59b0f135e99ee51b405dabdb]



 500Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.



 GET/{tenantName}/fileio/{datasource}/{appName}/{entityName}/{fileId}The API to get a file based on the file ID.

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




 entityName


 String(path)





 The data model name of the specified app.


 Yes




 fileId

 object(path)






 The unique ID of the file.





 Yes





 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.
