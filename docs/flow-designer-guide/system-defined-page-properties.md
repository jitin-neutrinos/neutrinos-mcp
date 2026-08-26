# System-defined page properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/system-defined-page-properties>

The Neutrinos Platform provides a set of predefined system variables which includes system-defined variables and services that can be used across apps. You can call these variables using this.page.system.The this.page.system variable contains all the variables and services that are pre-defined by the Neutrinos Platform.
**Variable or Service****Summary**this.page.system.currentUserProvides information about the currently logged-in user. This will be undefined if the app does not use authentication or if no user has logged in.this.page.system.environmentProvides information about the current environment that the app is built on. For example- Dev, Prod.this.page.system.tokenServiceProvides methods for authentication token management on the front end. this.page.system.deviceServiceProvides methods and variables to get the application and platform-specific information.
this.page.system.localStorageSystemProvides access to the data stored in the local storage of the client. this.page.system.loginserviceProvides methods and variables for a user to log in to an application.
this.page.system.logoutServiceProvides methods and variables for a user to log out of the application.
this.page.system.notificationServiceProvides push notifications to the app.
this.page.system.httpLoaderServiceListens to HTTP requests and indicates its progress.
