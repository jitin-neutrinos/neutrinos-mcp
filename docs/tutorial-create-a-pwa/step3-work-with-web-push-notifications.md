# Step 3: Configure Push Notifications

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/step3-work-with-web-push-notifications>

In this section, you will update the weather app to work with push notifications. Push notifications are clickable pop-up messages that appear on the user's device. They can be triggered locally by an application, or they can be pushed from the server to the user (even when the app is not running).

Why do you need them? They allow client apps to opt-in to timely updates and allow you to effectively re-engage users with customized content.

Neutrinos currently supports [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/) push service and provides [PWA Firebase](/smart/project-service-designer-user-s-guide/pwa-firebase) nodes to work with push notifications.

To learn more about how push notifications work, see [How Push Notifications Work](/smart/project-sample-how-to-guide/how-push-notifications-work).

In this app, we will create a **Subscribe** page using which a user can enter the name of a city and subscribe to weather updates of that city. We will create a scheduler to trigger the weather update notification every ten minutes, updating the user about the weather of the subscribed city. We will also create flows to unsubscribe from weather notifications. The user will be able to unsubscribe from the weather updates at any point in time by clicking the **Unsubscribe** button on the **WeatherSearch** page.
