# Create VAPID Keys

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/create-server-keys>

Neutrinos currently supports only the [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/) push service. To send notifications from this service, we will be using [npm web-push](https://www.npmjs.com/package/web-push) and will be creating VAPID keys for the application.

The VAPID (Voluntary Application Server Identification) keys will allow you to send push messages without having to set up a messaging service. They also identify who is sending the push notification. These keys occur in pairs- one private key and another public key. Learn more about Vapid keys from [here](https://developers.google.com/web/ilt/pwa/introduction-to-push-notifications#identifying_your_service_with_vapid_auth).

Perform the following steps to install the npm web-push package and create VAPID keys:

1. On your computer, open the **Command Prompt**.
2. Run the following commands to install the web-push package globally.Copy CodeJavaScriptnpm install web-push -g ![](/resources/Storage/tutorial-create-a-pwa/2021-06-30_12h46_08.png)
3. Next, run the following command to generate VAPID keys:Copy CodeMarkdownweb-push generate-vapid-keys [--json]
4. The public and private VAPID keys are created and displayed on the command prompt. These are URL Safe Base64 encoded strings. Copy these keys into a notepad. You will be using them when you create service flows.

![](/resources/Storage/tutorial-create-a-pwa/2021-06-30_12h47_06.png)
