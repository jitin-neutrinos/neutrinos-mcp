# Manage Authentication and Authorization

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/manage-authorization>

## Manage Authentication and Authorization

Manage authentication and authorisation for users on Neutrinos Art using these APIs:





 POST/{tenantName}/auth/{appName}




 POST/{tenantName}/auth/{appName}/refresh




 PUT/{tenantName}/auth/{appName}/register




 GET/{tenantName}/auth/{appName}/users




 POST/{tenantName}/auth/{appName}/reset/{userKey}




 PATCH/{tenantName}/auth/{appName}/changePassword




 PATCH/{tenantName}/auth/{appName}/update/{userKey}




 PATCH/{tenantName}/auth/{appName}/group




 DELETE/{tenantName}/auth/{appName}/delete/{userKey}











 POST/{tenantName}/auth/{appName}


 This API to authenticate users on Neutrinos Art .




 **Parameters:**





 Name


 Type


 Description


 Required?






 tenantName



 string(path)


 The tenant name provided by the Neutrinos administrator.



 Yes





 appName



 string(path)




 The name of the app.



 Yes





 body


 object(body)





 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "uuid": "string",
 "username": "string",
 "password": "string"
}




 Model:


 Copy CodeJSONAuthObject
{
 uuid: string
 username: string
 password: string
}



















 **Responses:**





 **Code**


 **Description**


 **Example**




 200



 Operation Successful



 **Example:**


 Value:


 Copy CodeJSON{
 "accessToken": "string",
 "refreshToken": "string",
 "tempPasswordFlag": true
}

 Model:


 Copy CodeJSONAuthResponse
{
 accessToken: string
 refreshToken: string
 tempPasswordFlag: boolean
}







 500




 Operation failed













 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.










 POST

 ** /{tenantName}/auth/{appName}/refresh**



 This API to refresh the authorization token of the user.



 **Parameters:**





 Name


 Type


 Description


 Required?






 tenantName


 string(path)


 The tenant name provided by the Neutrinos administrator.


 Yes




 appName


 string(path)




 The name of the app.


 Yes




 body


 object(body)





 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "uuid": "string",
 "userKey": "string",
 "refreshToken": "string"
}




 Model:


 Copy CodeJSONAuthRefreshObject
{
 uuid: string
 userKey: string
 refreshToken: string
}










 **Responses:**





 **Code**


 **Description**


 **Example**




 200


 Operation Successful



 **Example:**


 Value:


 Copy CodeJSON{
 "accessToken": "string",
 "refreshToken": "string",
 "tempPasswordFlag": true
}

 Model:


 Copy CodeJSONAuthResponse
{
 accessToken: string
 refreshToken: string
 tempPasswordFlag: boolean
}






 500


 Operation failed











 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.










 PUT/{tenantName}/auth/{appName}/register



 This API creates a new user on Neutrinos Art .


 **Parameters:**





 Name


 Type


 Description


 Required?







 tenantName




 String(path)



 The tenant name provided by the Neutrinos administrator.



 Yes





 appName



 String(path)






 The name of the app.



 Yes





 body


 object(body)







 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "userKey": "string",
 "firstName": "string",
 "lastName": "string",
 "username": "string",
 "displayName": "string",
 "password": "string",
 "groupList": [
 null
 ]
}

 Model:


 Copy CodeJSONAuthRegister
{
 userKey: string
 firstName: string
 lastName: string
 username: string
 displayName: string
 password: string
 groupList: [
 ]
}















 **Responses:**





 **Code**


 **Description**




 201


 User created




 406


 User already exists




 500



 Operation failed








 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.








 GET/{tenantName}/auth/{appName}/users




 The API to get a list of existing users on Neutrinos Art .



 **Parameters:**





 Name


 **Type**


 Description


 Required?






 tenantName


 string(query)


 The tenant provided by the Neutrinos administrator.


 Yes




 appName


 string(query)




 The name of the app.


 Yes




 filter


 string(query)





 A MongoDB query assigned to qparam value. The value defaults to {}.


 The documents returned by the API call will be filtered based on the specified condition. Only documents that match the condition are retrieved.














 sort


 string(query)




 The sort to be applied to the query results. Defaults to {}.













 pagenumber


 string(query)




 Page number for paginated queries. Defaults to 1.













 pagesize


 string(query)




 The size of each page to be returned. Defaults to 100.














 **Responses:**





 **Code**


 **Description**




 200


 Operation Successful




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.










 POST/{tenantName}/auth/{appName}/reset/{userKey}




 The API to reset the user's password.



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







 userKey


 String(path)







 The user ID.






 Yes






 **Responses:**





 **Code**


 **Description**




 200



 Operation Successful





 404


 The user does not exist




 500



 Operation failed








 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.










 PATCH/{tenantName}/auth/{appName}/changePassword



 The API to set a new user password.


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








 body


 object(body)



 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "userKey": "string",
 "firstName": "string",
 "lastName": "string",
 "username": "string",
 "displayName": "string",
 "password": "string",
 "groupList": [
 null
 ]
}

 Model:


 Copy CodeJSONAuthChangePasswordObject
{
 userKey: string
 password: string
 sendMail: boolean
 sendMailKey: string
}











 **Responses:**





 **Code**


 **Description**




 202


 Password changed successfully





 500



 Operation failed








 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.







 PATCH/{tenantName}/auth/{appName}/update/{userKey}






 The API to update the user account objects such as first name, last name, etc.





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





 userKey


 String(path)






 The user ID


 Yes







 body


 object(body)




 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "firstName": "string",
 "lastName": "string",
 "displayName": "string"
}Model:

 Copy CodeJSONAuthUpdateObject
{
 firstName: string
 lastName: string
 displayName: string
}











 **Responses:**





 **Code**


 **Description**




 202


 User updated





 500



 Operation failed








 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.





 PATCH/{tenantName}/auth/{appName}/group





 The API to update a user to a group.





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




 userKey


 String(path)





 The user ID





 Yes




 body


 object(body)



 The body of the API call.


 **Example:**


 Value:


 Copy CodeJSON{
 "userKey": "string",
 "groupList": [
 null
 ]
}Model:

 Copy CodeJSONAuthUpdateGroupObject
{
 userKey: string
 groupList: [...]
}










 **Responses:**





 **Code**


 **Description**




 202


 Group list updated




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.





 DELETE/{tenantName}/auth/{appName}/delete/{userKey}






 The API to delete the user.





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




 userKey


 String(path)





 The user ID.





 Yes





 **Responses:**





 **Code**


 **Description**




 202


 User removed




 500


 Operation failed







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.
