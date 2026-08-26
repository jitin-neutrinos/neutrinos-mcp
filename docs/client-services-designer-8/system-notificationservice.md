# bh.system.notificationService

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/system-notificationservice>

bh.system.notificationService is used to provide push notifications to the app.

| ![Information](/resources/Storage/client-services-designer-8/info.png) | These Push Notifications were supported for apps built using the older versions of Neutrinos Studio. Push notifications service is disabled starting from Studio version 7. |
| --- | --- |

Within the app's environment, the user will specify which type of push notification service has been enabled in the app. Neutrinos provides FireBase Cloud Messaging(FCM) and Apple Push Notification Service(APNS) notification services. FCM sends notifications to both Andriod and Apple devices using Firebase. Whereas APNs, as the name specifies, sends push notifications to only Apple devices.


 In the app's environments window, you either specify **FCM** or **APNS** as the value of the pushType variables. The variable value will default to FCM.![](/resources/Storage/client-services-designer-8/envi1.png)

**Methods:**



  [enableNotification()](/articles/client-services-designer-8/system-notificationservice/a/enableNotification)
  [initialiseWebPush()](/articles/client-services-designer-8/system-notificationservice/a/initialiseWebPush)
  [checkPermission()](/articles/client-services-designer-8/system-notificationservice/a/checkPermission)
  [initializeNotifications()](/articles/client-services-designer-8/system-notificationservice/a/initializeNotifications)
  [sendRegDetails()](/articles/client-services-designer-8/system-notificationservice/a/sendRegDetails)[getPushType()](/articles/client-services-designer-8/system-notificationservice/a/getPushType)
 **Variables:**


 sessionStorage: [NSessionStorageService](/articles/client-services-designer-8/system-sessionstorageservice);

 appName:The name of the app.**Syntax:**
 Copy CodeJavaScriptappName -> {any}








 enableNotification()



 If the isNotificationEnabled variable is set to True in the environment's window, this method enables push notifications for your application and sends the registration details(device token) of the device to Neutrinos Art.


 **Return type: **void


 **Syntax:**


 Copy CodeJavaScriptenableNotifications() -> {}


 **initialiseWebPush()**


 This method initializes push notifications in a browser, get the device token, and calls the sendRegDetails() method. This is used for Web applications only. If you are using a mobile app, use the initialiseNotification() method to initialize notifications of the app.


 **Return type: **void


 **Syntax:**


 Copy CodeJavaScriptinitialiseWebPush() -> {}




 checkPermission(pushType: any)



 This method checks whether the user has enabled push notifications. This method is used only in mobile apps.










 Properties

 Description






 pushType


 This is an optional attribute which specifies the type of notification service, FCM or APNS. It defaults to FCM.










 **Return type: **Promise<{}>


 **Syntax:**


 Copy CodeJavaScriptcheckPermission(pushType?: any) -> {Promise<{}>}


 **Returns:**


 Returns a Promise.




 initializeNotifications(pushType: any)



 This method initializes push notifications in a mobile app, get the device token, and calls the sendRegDetails() method. If you are using a web app, use the initialiseWebPush() method to initialize notifications in the browser.










 Properties

 Description






 pushType


 This is an optional attribute which specifies the type of notification service, FCM or APNS. It defaults to FCM.










 **Return type: **void


 **Syntax:**


 Copy CodeJavaScriptinitializeNotifications(pushType?: any) -> {}



 sendRegDetails(registrationID: any)



 This method sends the device token to Neutrinos Art .










 Properties

 Description






 registrationID


 The device token of the device in which the app is running.










 **Return type: **void


 **Syntax:**


 Copy CodeJavaScriptsendRegDetails(registrationId: any) -> {}




 getPushType(currPushType: any)



 This method returns the type of push notification enabled on an app. The value can be FCM or APNS.










 Properties

 Description






 currPushType


 The current push notification type. Returns the value as FCM or APNS.










 **Return type: **any


 **Syntax:**


 Copy CodeJavaScriptgetPushType(currPushType: any) -> {any}


 **Returns:**


 Returns the push notification type.
