# Manage Notifications

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/manage-notifications>

## Manage Notifications

Manage your app notifications on Neutrinos Art using these APIs:
 DELETE/{tenantName}/notification/{appName}/registerPOST/{tenantName}/notification/{appName}/registerPOST/tenantName/notification/{datasource}/{appName}/stage




 DELETE/{tenantName}/notification/{appName}/registerThis API deletes the Firebase or APNS registration ID from Neutrinos Art.


 **Parameters:**




 Name
 Type
 Description

 Required?




 tenantName
 string(path)
 The tenant provided by the Neutrinos administrator.

 Yes


 appName
 string(path)

 The name of the app.

 Yes


 deleteReg(body)
The registration ID of your device that is saved on Neutrinos Art .**Example:**Value:Copy CodeJSON{
 "key": "string",
 "uuid": "string"
}
Model:Copy CodeJSONDeleteReg
{
 key: string
 uuid: string
}











 **Responses:**




 **Code**

 **Description**


 200

 Operation Successful








 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.






 POST** /{tenantName}/notification/{appName}/register**This API saves the Firebase or APNS registration ID to Neutrinos Art .**Parameters:**NameTypeDescriptionRequired?tenantName string(path)The tenant provided by the Neutrinos administrator.YesappNamestring(path)
The name of the app.Yesregister(body)
The registration ID to be saved.**Example:**Value:Copy CodeJSON{
 "key": "string",
 "uuid": "string",
 "fbRegId": "string"
}
Model:Copy CodeJSONRegister
{
 key: string
 uuid: string
 fbRegId: string
} **Responses:****Code****Description**200Operation Successful See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.




 POST** /{tenantName}/notification/{appName}/stage**A stage is a batch of notifications to be sent to Neutrinos Art. This API stages the notifications before they are sent to the users.
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

 datasourcestring(path)The name of a connection from the Neutrinos Art server to a tenant-specific database.
Yesbody(body)




 The notification body. **Example:**Value:Copy CodeJSON[
 {
 "key": "string",
 "subject": "string",
 "message": "string"
 }
]
Model:Copy CodeJSON[NotificationBody
 {
 key: string
 subject: string
 message: string
}]
 Yes





 **Responses:**




 **Code**

 **Description**


 200Operation Successful







 See [Status Codes](/articles/neutrinos-art-api-reference-guide/status-codes) for more information about HTTP status codes.
