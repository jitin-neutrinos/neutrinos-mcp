# Associated Attributes

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/on-fcm-subscribe>

The **On FCM Subscribe** node is used to emit the currently active subscription associated with the [Service Worker](/smart/project-concepts/service-worker) or null if there is no subscription. This is a **Start** node.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Result Mapping:** The result of the operation. Enter the flow object in which you want to save the subscription details.

An example of subscription details:

```json
PushSubscription {  endpoint: "https://fcm.googleapis.com/fcm/...",                     expirationTime: null,                     options: PushSubscriptionOptions}  endpoint: "https://fcm.googleapis.com/fcm/send/..."  expirationTime: null  options: PushSubscriptionOptions  applicationServerKey: ArrayBuffer(65) {}  userVisibleOnly:True}
```
