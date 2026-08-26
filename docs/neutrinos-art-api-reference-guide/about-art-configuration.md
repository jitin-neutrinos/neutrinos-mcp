# Configure Neutrinos Art

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/about-art-configuration>

## Configure Neutrinos Art

Using Neutrinos Art, you can set up multiple tenants in an environment. Each tenant can have multiple applications configured.

| ![Information](/resources/Storage/neutrinos-art-api-reference-guide/info.png) | To set up the ART environment, you must have the administrator privileges. |
| --- | --- |

This is a sample tenant document of the MongoDB bhive-art-config database. You customize this document according to your configuration:

Copy CodeJSON{
 "_id" : ObjectId("588c5f753f88ea3293112acb"),
 "tenantName" : "organizatioName",
 "datasource" : [
 {
 "name" : "database-rt",
 "type" : "mongodb",
 "url" : "mongodb://localhost:XXXXX/database-rt"
 },
 ],

 "apps" : {
 "app1" : {
 "namespace" : "com.jatahworx.organizatioName.appName",
 "appName" : "app1",
 "firebase" : {
 "senderId" : "4XXXXXX9593",
 "authKey" : "AAAAXXXX-XXXXCChwt"
 },

 "authentication": {
 "strategy" : "basicAuth",
 "username" :"",
 "password" : ""
 }

 },

 "app2" : {
 "namespace" : "com.jatahworx.organizatioName.appName",
 "appName" : "app2",
 "firebase" : {
 "senderId" : "4556372xxx3",
 "authKey" : "AAAAahYY_Fk:AXXXX-XsaAXXXXXXQpGbCChwt"
 }

 },

 "user-admin-portal" : {
 "appName": "user-admin-portal",
 "authentication": {
 "strategy" : "localAuth",
 "datasource_uri" : "mongodb://localhost:2XXXX7/database-rt",
 "reset" : {
 "options" : {
 "from" : "",
 "subject" : "Password Reset",
 "text" : "This is test with password %%token%%",
 "html" : "<h5>This is test with password %%token%%</h5>"
 }

 },

 "change" : {
 "options" : {
 "from" : "",
 "subject" : "Password Change",
 "text" : "This is test with password %%token%%",
 "html" : "<h5>This is test with password %%token%%</h5>
 }

 },

 "secretKey": ""

 }

 }

 }

 }

To customize the tenant document for your apps, configure the following:

#### Update the tenantName property

This property is linked to the setup of an application and is required to access Neutrinos APIs that are specific to a tenant.

```json
"tenantName": "<organizationName>"
```

#### Update the Data Sources

The data sources available for all applications under a tenant are configured as a list. The list contains:

- **Name:** Specify the name of the data source
- **Type:** Specify the type of database
- **Url: **Specify the connection URL to the database

```json
"datasource": [
 {  "name": "<databaseName-rt>",
  "type": "<databaseType>",
  "url": "<databaseType>://03RNB-DevXXXI01:27017/<databaseName-rt>"
 }
]
```

#### Configure Apps

All applications under a tenant are configured as app objects under the apps property. These applications have to be configured for the below properties:

- **Namespace:** Specify the namespace of the application

```json
"namespace": "com.neutrinos.<organizationName>.<appName>"
```

- **App name:** Specify the name of the application

```json
"appName": "<appName>"
```

- **Notifications (Firebase): **Specify the properties required for Firebase push notifications. The values to these properties are configured from Firebase application account.

```json
"firebase":{
  "senderId": "9XX89asXXXX08",
  "authKey": "AAAA3aFRXXXXX:APA91bXXXJiq"
}
```

- **Authentication:** Specify properties for an authentication strategy used within the application. Below are the strategies available for configuration:
  - **Active Directory: **Specifies properties that are used to authenticate a user with an active directory.
  - **Local auth:** Specify properties that are used to authenticate a user with a local user store
  - **Basic auth: **Specify properties that are used for basic authorization
