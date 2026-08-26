# Design Server Flows

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/design-server-flows>

When you subscribe to Push notifications, the FCM Subscribe node on the client service flow creates a subscription object. This subscription object will be used to send push messages and must be stored.

In this section, you will be designing server service flows to:

- Store the subscription object with the city name in the Mongo Database if the subscription object does not exist.
- Send weather update notifications of the subscribed city every 5 minutes.
- Delete the subscription object from the Mongo Database when the user unsubscribes from web push notifications.
