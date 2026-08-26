# Features

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/version-7-7-0>

### Features

Here is a list of new features added to Neutrinos Studio version 7.7.0:

**Progressive Web Apps (PWAs)**

From Neutrinos Studio version 7.7.0, you can [convert any app to a PWA](/articles/app-builder-s-user-guide/convert-to-progressive-web-app) using the PWA editor. After converting the app, you can:

- Change the appearance of the app by using the **Appearance** editor.
- [Cache URLs in Service Worker](/articles/app-builder-s-user-guide/cache-url) by using the **Cache Config **editor.
- Use PWA Firebase and SW-Events nodes to work with notifications.
  - **PWA Firebase **nodes: Used to subscribe and listen to [Web Push Notifications](/smart/project-concepts/web-push-notifications) through the [Service Worker](/smart/project-concepts/service-worker). It includes:
    - [FCM Subscribe](/smart/project-service-designer-user-s-guide/fcm-subscribe)
    - [On FCM Subscribe](/smart/project-service-designer-user-s-guide/on-fcm-subscribe)
    - [FCM Unsubscribe](/smart/project-service-designer-user-s-guide/fcm-unsubscribe)
  - **PWA SW-Events** nodes are used to work with [Service Worker](/smart/project-concepts/service-worker) events in a [Progressive Web App (PWA)](/smart/project-concepts/progressive-web-app). It includes:
    - [Update Available](/smart/project-service-designer-user-s-guide/update-available)
    - [Activate Update](/smart/project-service-designer-user-s-guide/activate-update)
    - [Check for Update](/smart/project-service-designer-user-s-guide/check-for-update)
    - [Is SW Registered?](/smart/project-service-designer-user-s-guide/is-sw-registered)
    - [On Notification](/smart/project-service-designer-user-s-guide/on-notification)
    - [On Notification Click](/smart/project-service-designer-user-s-guide/on-notification-click)

**Startup Script**

A [Startup Script](/smart/project-node-builder-guide/startup-script) editor is added to the Plugins Builder. Using this editor you can specify any node-specific logic that is to be executed every time an application starts. This is an optional step and is applicable only when [adding Server nodes](/smart/project-node-builder-guide/add-a-server-node).

Refer to the [Changelog](/smart/project-change-log/release-7-7-0) to learn about the enhancements and bug fixes in this release.
