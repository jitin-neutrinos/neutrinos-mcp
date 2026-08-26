# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/on-notification>

The **On Notification** node is used to emit the payloads of the received push notification messages. This is a **Start **node.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Result Mapping:** The result of the operation. Enter the flow object in which you want to save the emitted payloads.

Example of a notification structure:

```json
{  "notification":   {    "actions": NotificationAction[],    "badge": USVString    "body": DOMString,    "data": any,    "dir": "auto"|"ltr"|"rtl",    "icon": USVString,    "image": USVString,    "lang": DOMString,    "renotify": boolean,    "requireInteraction": boolean,    "silent": boolean,    "tag": DOMString,    "timestamp": DOMTimeStamp,    "title": DOMString,    "vibrate": number[]  }}
```
