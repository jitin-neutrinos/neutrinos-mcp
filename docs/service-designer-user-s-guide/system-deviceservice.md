# bh.system.deviceService Resolver

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/system-deviceservice>

The bh.system.deviceService provides methods and variables to access the application and platform-specific information.




 **Methods:**

[isAndroid()](/articles/service-designer-user-s-guide/system-deviceservice/a/isAndroid)


 [getAndroidVersion()](/articles/service-designer-user-s-guide/system-deviceservice/a/getAndroidVersion)


 [isIOS()](/articles/service-designer-user-s-guide/system-deviceservice/a/isIOS)


 [getTenantUrl()](/articles/service-designer-user-s-guide/system-deviceservice/a/getTenantUrl)


 [getAuthUrl()](/articles/service-designer-user-s-guide/system-deviceservice/a/getAuthUrl)


 [getProxyUrl()](/articles/service-designer-user-s-guide/system-deviceservice/a/getProxyUrl)


 [getAppUrl()](/articles/service-designer-user-s-guide/system-deviceservice/a/getAppUrl)


 [getDataModelUrl()](/articles/service-designer-user-s-guide/system-deviceservice/a/getDataModelUrl)


 [getVal(key)](/articles/service-designer-user-s-guide/system-deviceservice/a/getVal)



 **Variable:**


 deviceType: Returns the type of device the app is running on.


 **Syntax:**






 Copy Code


 JavaScript





 deviceService.deviceType → any;











 isAndriod()


 **Return type: **Boolean


 **Syntax:**


 Copy CodeJavaScriptisAndroid() → {boolean}







 **Returns:**


 True if the application is being run on an Android platform.



 isIOS()


 **Return type: **Boolean


 **Syntax:**


 Copy CodeJavaScriptisIOS() → {boolean}





 **Returns:**


 True if the application is being run on an IOS platform.





 getAndriodVersion()


 **Return type:** String


 **Syntax:**


 Copy CodeJavaScriptgetAndroidVersion() → {string}





 **Returns:**


 Returns the android version of the platform. If no information is found, it returns an empty string.



 getTenantUrl()


 **Return type: **String


 **Syntax:**


 Copy CodeJavaScriptgetTenantUrl() → {string}





 **Returns:**


 Returns the ART Url for a tenant if the application is migrated from previous versions of Studio which used Neutrinos Art.



 getAuthUrl()


 **Return type: **String


 **Syntax:**


 Copy CodeJavaScriptgetAuthUrl() → {string}





 **Returns:**


 Returns the ART Authentication Url for a tenant if the application is migrated from previous versions of Studio which used Neutrinos Art.



 getProxyUrl()


 **Return type: **String


 **Syntax:**


 Copy CodeJavaScriptgetProxyUrl() → {string}





 **Returns:**


 Returns the ART proxy Url for a tenant if the application is migrated from previous versions of Studio which used Neutrinos Art.



 getAppUrl()


 **Return type: **String


 **Syntax:**


 Copy CodeJavaScriptgetAppUrl() → {string}





 **Returns:**


 Returns the ART application proxy Url for a tenant if the application is migrated from previous versions of Studio which used Neutrinos Art.



 getDataModelUrl()


 **Return type: **String


 **Syntax:**


 Copy CodeJavaScriptgetDataModelUrl() → {string}





 **Returns:**


 Returns the ART data model Url for an application if the application is migrated from previous versions of Studio which used Neutrinos Art.



 getVal(key)


 **Return type: **String





 **Properties**


 **Description**






 key


 Any environment variables that you specify. If you want the method to return all the environment properties, then you pass 'properties' as the key. See [Define Environments](/smart/project-sample-how-to-guide/what-is-an-environment) to learn about the environment properties.





 **Syntax:**


 Copy CodeJavaScriptgetVal(key) → {string}





 **Returns:**


 Returns the environment values for a key configured under environments. If key = properties, then the method returns all the properties of the environment. If no properties are found, then the method returns undefined.
