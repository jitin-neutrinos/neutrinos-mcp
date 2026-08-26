# bh.system.loginService

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/system-loginservice>

bh.system.loginService provides methods and variables for a user to log in to an application.

**Methods:**




 [login()](/articles/client-services-designer-8/system-loginservice/a/login)[isLoggedIn()](/articles/client-services-designer-8/system-loginservice/a/isLoggedIn) **Variables:**
 loginUrl: Neutrinos Art authentication URL if the application is migrated from previous versions of Studio which used Neutrinos Art.
  appvariables: Current environment variables of the app.
  systemService: [system.deviceService](/articles/client-services-designer-8/system-deviceservice)
  nSessionStorage: [NSessionStorageService](/articles/client-services-designer-8/system-sessionstorageservice)

  uuid: Stores the UUID (Universal Unique Identifier) of the device. UUID is a 128-bit number used to uniquely identify the device on the Internet.

  details: Contains the username, password, and the platform details on which the app is running.**Syntax:**

 Copy CodeJavaScriptloginCompleted -> EventEmitter<{}>





 login(userName: any, password: any, isRemember?: any)



 This method allows users to log in to the application using their credentials. variablesDescriptionuserNameThe user name to log in to the application.passwordThe password associated with the user name to log in to the application.isRemember?Optional. A Boolean value which indicates if the logged in user should be remembered across tabs.


 **Return type: **Observable<any>


 **Syntax:**


 Copy CodeJavaScriptlogin(userName: any, password: any, isRemember?: any) -> {Observable<Object>}


 **Returns:**


 Returns the result of the operation as an Observable.





 isLoggedIn()



 This method returns true if a user has logged in to the application.










 **Return type: **Promise<boolean>


 **Syntax:**


 Copy CodeJavaScriptisLoggedIn() -> {Promise<boolean>}**Returns:**Returns a Promise.
