# Subscribe to Push Notifications from a Server

<https://documentation.neutrinos.com/articles/#!studio-guide-9/subscribe-web-push-notifications>

Before you can send a push message, you must first subscribe to a push service. Subscribing to a push service returns a **subscription object.**

Neutrinos currently supports only the [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/) push service which follows the Web Push Protocol. You use the [PWA Firebase](/smart/project-service-designer-user-s-guide/pwa-firebase) nodes to subscribe and get push notifications.

#### Subscribe to Push Notifications from a Server

You subscribe to a server to receive any push notifications that the server sends. Follow the steps below to subscribe to a server and receive the subscription object. Perform the following steps:

1. On the **Client Services** **Designer**, create a service or open an existing service. In this example, we have created a service named **test**.
2. From the nodes palette, drag and drop a [Start](/smart/project-service-designer-user-s-guide/start-node) node to the workspace. Name the node. For example, **requestSubscription**. A method gets created by the same name in the **Function name** field. You will be binding this method to the UI of the page to invoke this client service flow on the front-end. Create a local variable to store the subscription object. For example, **result**. Enable the **output** toggle button to access the local variable outside the flow.
    ![](/resources/Storage/studio-guide-9/project-how-to-articles/req_strt.png)
3. Drag and drop the [FCM Subscribe](/smart/project-service-designer-user-s-guide/fcm-subscribe) node. This node subscribes to the server and returns the subscription object. Connect the node to the above **Start **node to create a flow.
4. In the attributes window of the **FCM Subscribe **node, enter the Server Public Key of the server from which you want to receive notifications. Store the response of this operation in the local variable that you created in the **start **node.
    ![](/resources/Storage/studio-guide-9/project-how-to-articles/fcm_sub.png)
5. On the HTML front, [bind the client service flow to any user action](/articles/studio-guide-9/import-client-services-to-the-page-ui). In this example, on the **Home** page, we have created a button named **Get Notifications **and have called the **requestSubscription **client service flow on click of this button.
    ![Request subscription](/resources/Storage/studio-guide-9/project-how-to-articles/req_sub.png)

The app requests the subscription to the server to which the Server Public key belongs. On successful authorization, the server returns the subscription object which is stored in the **result** variable.

Take this subscription object and store it at a location of your choice. See the following section to store the object in a database.

### Store the Subscription Object in a Database

The **subscription object** is a critical piece of the process to send push messages. It tells the developer to which push service push messages must be sent. The subscription object also details which client the push service should route the messages to. Finally, the subscription object contains the public key to encrypt the data so that it is delivered securely to the user.

Perform the following steps to store the object in a MongoDB database. Alternatively, you can store the subscription object in your local machine or any other database of your choice.

1. On the **Server Services** **Designer**, create a service or open an existing service.
2. From the nodes palette, drag and drop an HTTP In node to the workspace. Name the node. For example, **Subscription Object**. Select the Method as **POST** and provide a URL **path**. For example,** subscribe**.
3. To store the subscription object on a MongoDB database, drag and drop a [Mongo DB](/smart/project-server-side-service-designer/mongodb-node) node and connect it to the HTTP In node. In the attributes window, configure the MongoDB database, set the collection, select the operation as **insertOne, **enter the flow variable that contains the document, and store the result of the operation.
4. Drag and drop an [HTTP Out](/smart/project-server-side-service-designer/http-out-node) node. In the attributes window, set the status code and status body for the response.
