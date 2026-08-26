# To send push notifications, the server should first generate Public and Private keys. The client app will then use the same public key to subscribe to the push notification from the server.

<https://documentation.neutrinos.com/articles/#!studio-guide-7/send-web-push-notification>

#### To send push notifications, the server should first generate Public and Private keys. The client app will then use the same public key to subscribe to the push notification from the server.

#### Generate the Server Public and Private keys

Perform the following steps to create them:

1. On your computer, open the **Command Prompt**.
2. Run the following commands to install the web-push package globally.
    Copy Code
    JavaScript
    npm install web-push -g
    ![](/resources/Storage/studio-guide-7/project-tutorial-create-a-pwa/2021-06-30_12h46_08.png)
3. Once the installation is complete, run the following command to generate the server keys.
    Copy Code
    Markdown
    web-push generate-vapid-keys [--json]
4. The public and private keys are created and displayed on the command prompt. These are URL Safe Base64 encoded strings. Copy these keys into a notepad. You will be using them when you create server service flows.

![](/resources/Storage/studio-guide-7/project-tutorial-create-a-pwa/2021-06-30_12h47_06.png)

To send push notifications from a server, perform the following steps:



 On the [Server Services Designer](/articles/studio-guide-7/accessing-server-services-designer), create a service or open an existing service. In this example, we have created a service named **notification**.


 From the nodes palette, drag and drop an [HTTP In](/smart/project-server-side-service-designer/http-in) node to the workspace. Name the node. For example, **send**. Set the HTTP method as **POST,** this method creates a new resource with the specified URL**. **Set the URL path to** send**.


 ![](/resources/Storage/studio-guide-7/SP_HttpIn.png)


 Drag and drop a[Script node](/smart/project-server-side-service-designer/script-node) and connect it to the **HTTP In** node. Define:


 Payload. You can send the payload using Swagger, Postman, or any user interface. See [How Push Notifications Work](/articles/studio-guide-7/how-push-notifications-work) to view the typical structure of a payload. The payload that you send will be assigned to the flow variable bh.input.body.


 Logic/query that you want to execute on the database to select which subscribers you want to send the notifications to.


 For example, if you are using the MongoDB database, and want to send notifications to all the subscribers that are on that database, create a flow object called query and assign blank object like this - bh.query={};. Create another flow variable that will contain the payload details. The payload details will be sent to the URL endpoint. For example, bh.notification = bh.input.body.




 Drag and drop a database node or a file system node to select the subscribers of the push notification, and connect it to the Script node. You can use any database or file system to store your subscriber details. In this example, we have used the MongoDB database. We have configured the Mongo DB database connection, selected the operation as **find** and entered the flow variable bh.query to select the subscribers (that we created in the previous Script node). The result variable will contain all the subscriber details.

 ![Mongo DB properties](/resources/Storage/studio-guide-7/2021-07-02_12h11_07.png)

 Drag and drop another **Script **node. This is where you define the logic to send push notifications to the subscribers. For example, In the code editor we have defined the logic to send notifications to all the subscribers by providing the private and public key of the server. The notification is sent to the subscriber only if the public key matches with the public key of the client. Neutrinos Studio uses the [npm webpush notification module](https://www.npmjs.com/package/web-push) to send push notifications.


 Copy CodeMarkdownconst webPush = require('web-push');

const publicVapidKey =
 '<server_public_key>';
const privateVapidKey = '<server_private_key>';
webPush.setVapidDetails(
 'mailto:example@example.com',
 publicVapidKey,
 privateVapidKey
);
let notification = JSON.stringify(bh.notification);
bh.result.forEach((obj) => {
 webPush.sendNotification(obj, notification).catch((error) => {
 console.log(error);
 });
});


 Drag and drop an [HTTP Out](/smart/project-server-side-service-designer/http-out-node) node. In the attributes window, set the status code and status body for the response.


 ![HTTP out properties](/resources/Storage/studio-guide-7/SP_httpout.png)



 After defining the endpoint, send the notification from Swagger, Postman, or any user interface. For example, this is how the notification sent from Postman appears on the notifications window:


 ![notification payload on Postman](/resources/Storage/studio-guide-7/postman_notification.png)

 ![notification appearing on the notification bar](/resources/Storage/studio-guide-7/notification.png)
