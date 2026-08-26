# Push Notification Terms

<https://documentation.neutrinos.com/articles/#!studio-guide-9/work-with-push-notifications>

Push notifications are clickable pop-up messages that appear on the user's device. Notifications can be triggered locally by an application, or they can be pushed from the server to the user (even when the app is not running).

Why do you need them? They allow client apps to opt-in to timely updates and allow you to effectively re-engage users with customized content.

Neutrinos currently supports [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/) push service and provides [PWA Firebase](/smart/project-service-designer-user-s-guide/pwa-firebase) nodes to work with push notifications.

Before we work with Push Notifications, get familiar with the common terms.

### Push Notification Terms

- **Push Message** – a message sent from the server to the client. Push notifications are created in response to a push message.
- **Push Service** – a system for routing push messages from a server to a client. Each browser implements its own push service.
- **Web Push Protocol **– describes how an application server or user agent interacts with a push service. The **Web Push protocol** is the formal standard for sending push notifications destined for the browser. It describes the structure and flow of how to create your push message, encrypt it, and send it to a Push messaging platform. The protocol abstracts the details of which messaging platform and browser the user has.

**Topics:**

1. [How Push Notifications Work](/articles/studio-guide-9/how-push-notifications-work)
2. [Subscribe to Push Notifications](/articles/studio-guide-9/subscribe-web-push-notifications)
3. [Send Push Notifications from Server](/articles/studio-guide-9/send-web-push-notification)
4. [Unsubscribe from Push Notifications](/articles/studio-guide-9/unsubscribe-from-web-push-notifications)
