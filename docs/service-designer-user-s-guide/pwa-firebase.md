# How to use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/pwa-firebase>

The **PWA Firebase** nodes are used to subscribe and listen to [Web Push Notifications](/smart/project-concepts/web-push-notifications) through the [Service Worker](/smart/project-concepts/service-worker). See [Firefox documentation](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Best_Practices) to learn more.

It comprises the following nodes:

- [FCM Subscribe](/articles/service-designer-user-s-guide/fcm-subscribe)
- [On FCM Subscribe](/articles/service-designer-user-s-guide/on-fcm-subscribe)
- [FCM Unsubscribe](/articles/service-designer-user-s-guide/fcm-unsubscribe)

| ![Warning](/resources/Storage/service-designer-user-s-guide/warning.png) | You see these nodes on Client Services Designer if you have converted your app to a PWA. |
| --- | --- |

### How to use

1. Open the Client Services editor window.
2. Open an existing service from the service list or click the** plus icon **to add a new Client Service.
3. In the Nodes Palette, search for the node and drag and drop it to the canvas.
4. Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **
