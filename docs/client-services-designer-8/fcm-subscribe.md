# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/fcm-subscribe>

The **FCM Subscribe **node is used to subscribe to [Web Push Notifications](/smart/project-concepts/web-push-notifications), after authorizing the user on a server using the Server Public key.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Server Public Key:** The public key registered on the server to allow authorization of the user on a server. Choose String and enter the key directly or map the key-value to the [flow property](/articles/client-services-designer-8/service-designer-variables)and enter the variable name. The variable name that you map should contain the server public key.
4. **Result Mapping:** Returns a new subscription object. Enter the flow object in which you want to save the subscription object.

Example of a subscription object returned by the node:

```json
PushSubscription {  endpoint: "https://fcm.googleapis.com/fcm/...",                     expirationTime: null,                     options: PushSubscriptionOptions}  endpoint: "https://fcm.googleapis.com/fcm/send/..."  expirationTime: null  options: PushSubscriptionOptions  applicationServerKey: ArrayBuffer(65) {}  userVisibleOnly:True}
```
