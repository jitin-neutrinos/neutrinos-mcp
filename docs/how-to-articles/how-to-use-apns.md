# How to use the Apple Push Notification service?

<https://documentation.neutrinos.com/articles/#!how-to-articles/how-to-use-apns>

## How to use the Apple Push Notification service?

---

| ![Information](/resources/Storage/how-to-articles/info.png) | Apple Push Notifications are not supported Neutrinos Platform version 7 and further releases. This article is applicable only till Version 6 of the platform. |
| --- | --- |

**Apple Push Notification service (APNs)**, is a cloud service that allows app developers to send notifications to Apple devices over a secure connection.

### 

To send and receive messages using APNs, perform the following tasks:

**Step 1: Add the Plugin**

| ![Warning](/resources/Storage/how-to-articles/warning.png) | Ensure that your app doesn't have the phonegap-plugin-push plugin installed. If the plugin exists in the config.xml file, run cordova plugin remove phonegap-plugin-push command from the terminal window to remove the plugin. |
| --- | --- |

In the Neutrinos Application home page, click **Config XML** to open the app's config.xml page. Verify if the cordova-plugin-apns-push plugin already exists. If not, open the terminal and run the following command:

```markdown
cordova plugin add cordova-plugin-apns-push
```

The Cordova plugin gets installed in your app to support APNs notifications.

**Step 2: Configure your Authentication Certificate**

#### For your app to communicate with APNs, it must employ a valid authentication key certificate (for token-based connection trust). Register with the Apple developer account to obtain the certificate. See Obtain an Encryption Key and Key ID from Apple for more details.

#### Step 3: Update the Environment Settings

In the Neutrinos Studio [Application page](/smart/project-concepts/studio-application-page), click **[Environments](/smart/project-concepts/environment)**. Update the following properties for your DEV and PROD environments:

1. Set the isNotificationEnabled property to **True.**
2. Set the pushType to **APNS.**

![Environments window](/resources/Storage/how-to-articles/environments.png)

**Step 4: Update your Tenant Document**

Open your tenant document on MongoDB and update the PushType property to APNS.

```json
"PushType" : "APNS","apnsConfig" : {"teamId" : "XXXXXXXXX","keyId" : "XXXXXXXXX","authFileAsString" : "---start **Use \n to insert new line if required** end----"                 }
```

![Tenant document](/resources/Storage/how-to-articles/apns.png)
