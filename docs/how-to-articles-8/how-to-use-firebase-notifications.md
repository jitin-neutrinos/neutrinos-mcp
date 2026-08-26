# How to use Firebase Notifications?

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/how-to-use-firebase-notifications>

## How to use Firebase Notifications?

---

| ![Information](/resources/Storage/how-to-articles-8/info.png) | Firebase Notifications are not supported Neutrinos Platform version 7 and further releases. This article is applicable only till Version 6 of the platform. |
| --- | --- |

**Firebase Cloud Messaging (FCM)**, which is a free cloud service from Google that allows app developers to send notifications and messages to users across a variety of platforms, including Android, iOS, and web applications.

Using Firebase, you can push notifications to both Andriod, and iOS devices. To send and receive messages using FCM, perform the following tasks:

**Step 1: Add the Plugin**

Open the Neutrinos Studio and click** Config XML** to open the app's **Config XML** page.Verify if the phonegap-plugin-push plugin already exists. If not, open the terminal and run the command and the plugin gets added.

Copy CodeMarkdowncordova plugin add phonegap-plugin-push

![config xml](/resources/Storage/how-to-articles-8/config%20XML.png)

The Cordova plugin gets installed in your app to support Firebase notifications.

| ![Warning](/resources/Storage/how-to-articles-8/warning.png) | If you are using Firebase notification service, make sure that your app doesn't have the cordova-plugin-apns-push plugin installed. If the plugin exists in the config.xml file, run cordova plugin remove cordova-plugin-apns-push from the terminal window to remove the plugin. |
| --- | --- |

**Step 2: Create a Project in Firebase**

- On the Neutrinos Studio Application page, open the** Config** editor from the side menu and copy the Widget ID. The widget is in the format of co.neutrinos.<app_name> .
- Sign in to Firebase and click **Create a Project**.
- If you have an existing Google Cloud Platform (GCP) project, you can select the project from the Project name dropdown menu. Otherwise, enter a new Project name. Firebase automatically assigns a unique ID to your Firebase project.
- Follow the remaining setup steps in the Firebase console, then click **Create project. **Firebase provisions resources for your Firebase project. When the process completes, click **Continue**. You'll be taken to the overview page for your Firebase project in the Firebase console.

**Step 3****: Use Firebase Notification for an Android app**

- After you add the plugin and create a project in Firebase, In the Firebase console's project overview page, click the **Android** icon to launch the setup workflow.
- Click **Add app** to display the platform options.
- Enter the widget ID that you copied in Step 1 in the **Android package name** field and click **Register app**.
- Download the **google-services.json file** and save it in the neutrinos-studio\<app_name\app folder in your local machine. replace the file if it already exists.
- Click the **Next** button till you exit the console.
- Click the Andriod app on the project page and click the **Gear** icon to open its settings.
- Select the **Cloud Messaging** tab and copy the **Server Key **and **Sender ID **to your clipboard.
- Navigate back to the Studio Application page, click **Environments**.
- In the [Environments](/smart/project-concepts/environment) window, update the following properties for your DEV and PROD environments:
  1. Set the isNotificationEnabled property to **True**.
  2. Set the pushType to **FCM.**
  3. Update the firebaseSenderId with the Sender ID value that you copied in the clipboard.
  4. Update the firebaseAuthKey with the Server Key that you copied in the clipboard.
- Open your tenant document on MongoDB and update the PushType property to FCM.

Copy CodeJSON"PushType" : "FCM"

**Step 4:**** Use Firebase Notification for iOS app**After you add the plugin and create a project in Firebase, In the Firebase console's project overview page, click the** iOS** icon to launch the setup workflow.Click **Add app** to display the platform options.Enter the widget ID that you copied in Step 1 in the **iOS Bundle ID** field and click **Register app**.Download the **GoogleService-Info.plist** file and save it in the neutrinos-studio\<app_name\app folder in your local machine.Click the **Next** button till you exit the [console](/smart/project-concepts/neutrinos-console).Click the iOS app on the project page and click the **Gear** icon to open its settings.Copy the **Server Key** and **Sender Id** to the clipboard.Scroll down, and enter the **APNs Authentication Key**. This is the key that you download using your Apple Developer account which contains your Auth key, the key ID, and the team ID.Select the **Cloud Messaging** tab and copy the Server Key and Sender ID to your clipboard.Navigate back to the [Studio Application page](/smart/project-concepts/studio-application-page), click **Environments**. In the Environments window, update the following properties for your DEV and PROD environments:Set the isNotificationEnabled property to **True**.Set the pushType to **FCM**Update the firebaseSenderId with the Sender ID value that you copied in the clipboard.Update the firebaseAuthKey with the Server Key that you copied in the clipboard.Open your tenant document on MongoDB and update the PushType property to FCM.Copy CodeJSON"PushType" : "FCM"

| ![Information](/resources/Storage/how-to-articles-8/info.png) | Make sure that the sender ID in the **config.xml **file of your app matches the sender ID that you copied from the Firebase site. |
| --- | --- |
