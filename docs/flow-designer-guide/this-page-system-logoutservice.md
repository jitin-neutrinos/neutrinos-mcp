# this.page.system.logoutService

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/this-page-system-logoutservice>

bh.system.logoutService provides methods and variables for a user to log out of the application.




 ![Information](/resources/Storage/flow-designer-guide/info.png)


 logout service is disabled starting from the Studio version 8.

**Methods:**


 [logout()](/smart/project-service-designer-user-s-guide/system-logoutservice/a/logout) **Variables:**SessionStorage:[NSessionStorageService](/smart/project-service-designer-user-s-guide/system-sessionstorageservice)**Syntax:**
 Copy CodeJavaScriptloginCompleted -> EventEmitter<{}>



 logout()



 This method logs the user out of the application.

 **Return type: **Boolean

 **Syntax:**
 Copy CodeJavaScriptlogout() -> {Boolean}

 **Returns:**
 Returns True if the user has logged out successfully.
