# How Push Notifications Work

<https://documentation.neutrinos.com/articles/#!studio-guide-9/how-push-notifications-work>

Each browser manages push notifications through its own system, called a **push service**. When a user subscribes to a push notification, the browser's push service creates a subscription object that contains the **endpoint URL** of the push service, which is different for each browser, and a public key (see the example below).

You send your push messages to this endpoint URL, encrypted with the public key, and the push service sends it to the right client. A typical subscription object looks like this:

```javascript
{"endpoint":"https://fcm.googleapis.com/fcm/send/dpH5lCsTSSM:APA91bHqjZxM0VImWWqDRN7U0a3AycjUf4O-byuxb_wJsKRaKvV_iKw56s16ekq6FUqoCF7k2nICUpd8fHPxVTgqLunFeVeB9lLCQZyohyAztTH8ZQL9WCxKpA6dvTG_TUIhQUFq_n","keys": {"p256dh":"BLQELIDm-6b9Bl07YrEuXJ4BL_YBVQ0dvt9NQGGJxIQidJWHPNa9YrouvcQ9d7_MqzvGS9Alz60SZNCG3qfpk=","auth":"4vQK-SvRAN5eo-8ASlrwA=="}}
```

How does the push service know which client to send the message to? The **endpoint URL **contains a unique identifier. This identifier is used to route the message that you send to the correct device, and when processed by the browser, identifies which service worker should handle the request.

Because push notifications are paired with a [service worker](/smart/project-concepts/service-worker), apps that use push notifications must be on HTTPS or Localhost (if you are testing the app). This ensures that the communication channel between your server and the push service is secure, and from the push service to the user is also secure.

The following summarizes the process of sending and receiving a push message and then displaying a push notification.

**On the client:**

1. Subscribe to the push service
2. Receive subscription object
3. Send the subscription object to the server

See [Subscribe to Web Push Notifications](/articles/studio-guide-9/subscribe-web-push-notifications) to learn how to do this.

**On the server:**

1. Generate the data that you want to send to the user
2. Verify the endpoint URL against the user public and private key
3. Send the payload to the endpoint URL

A typical payload looks like this:

```javascript
{  "notification": {    "actions": NotificationAction[],    "badge": USVString,    "body": DOMString,    "data": any,    "dir": "auto"|"ltr"|"rtl",    "icon": USVString,    "image": USVString,    "lang": DOMString,    "renotify": boolean,    "requireInteraction": boolean,    "silent": boolean,    "tag": DOMString,    "timestamp": DOMTimeStamp,    "title": DOMString,    "vibrate": number[]  }}
```

See [Send Web Push Notification](/articles/studio-guide-9/send-web-push-notification) to learn how to send push notifications.

The payload is routed to the user's device. This wakes up the browser, which finds the service worker and invokes a **push** event.

Now, on the client:

1. Receive the push message
2. Show the push notification
3. Perform some action on the notification

That completes the path from server push to user notification.
