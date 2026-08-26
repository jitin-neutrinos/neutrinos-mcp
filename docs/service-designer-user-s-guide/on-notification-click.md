# Associated Attributes

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/on-notification-click>

The **On** **Notification Click** node is used to emit the payloads of the received push notification messages as well as the action the user interacted with. This is a **Start** node.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Result Mapping:** The result of the operation. Enter the flow object in which you want to save the result.

Example of a notification structure with user action:

```json
{  action: ""//the action performed on the notification  notification:  actions: []  badge: ""  body: "Know how to send notifications"  data: {url: "https://medium.com/..."}  dir: "auto"  icon: "https://www.shareicon.net/data/256x256.png"  image: ""  lang: ""  renotify: false  requireInteraction: false  silent: false  tag: ""  timestamp: 1612938814670  title: "Notifications are cool" vibrate: (3) []}
```
