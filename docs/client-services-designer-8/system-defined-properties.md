# System-defined Properties

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/system-defined-properties>

The Neutrinos Platform provides a set of predefined system variables which includes system-defined variables and services that can be used across apps. You can call these variables using bh.system.<system_variable>.



 System variables and services include:











 **Variable or Service**


 **Summary**






 bh.system.currentUser


 Provides information about the currently logged-in user. This will be undefined if the app does not use authentication or if no user has logged in.




 bh.system.environment

 Provides information about the current environment that the app is built on. For example- Dev, Prod.




 bh.system.tokenService


 Provides methods for authentication token management on the front end.




 bh.system.deviceService


 Provides methods and variables to get the application and platform-specific information.







 bh.system.localStorageSystem


 Provides access to the data stored in the local storage of the client.




 bh.system.loginservice


 Provides methods and variables for a user to log in to an application.







 bh.system.logoutService


 Provides methods and variables for a user to log out of the application.








 bh.system.notificationService



 Provides push notifications to the app.







 bh.system.pubsubService


 Provides methods to publish and subscribe to events with various types of callbacks.







 bh.system.httpLoaderService


 Listens to HTTP requests and indicates its progress.




















 System variables:


 System variables are specific to a system or a platform in which you create your app.


 **Syntax:**


 Copy CodeJavaScriptbh.system.<system_variable>;





 **Returns:**


 The value associated with the variable at that particular time. For example, bh.systsem.environment returns information about the current environment that the app is built on.



 System Services


 The following are the pre-defined system services that you can use across your apps:


 [bh.system.deviceService](/articles/client-services-designer-8/system-deviceservice)

 [bh.system.tokenService](/articles/client-services-designer-8/system-tokenservice)

 [bh.system.httpLoaderService](/articles/client-services-designer-8/system-httploaderservice)

 [bh.system.dataModelService](/articles/client-services-designer-8/system-datamodelservice)

 [bh.system.localStorageService](/articles/client-services-designer-8/system-localstorageservice)




 [bh.system.loginService](/articles/client-services-designer-8/system-loginservice)




 [bh.system.logoutService](/articles/client-services-designer-8/system-logoutservice)




 [bh.system.notificationService](/articles/client-services-designer-8/system-notificationservice)




 [bh.system.pubSubService](/articles/client-services-designer-8/system-pubsubservice)







 Access system variables from a UI Service


 You can access the system variables from any flow by using bh.system.<variable>. For example, if you have a service which requires Neutrinos Art authentication, then you can drag and drop a **Script** node to your flow, and use the [bh.system.loginService.login()](/articles/client-services-designer-8/system-loginservice) method.
