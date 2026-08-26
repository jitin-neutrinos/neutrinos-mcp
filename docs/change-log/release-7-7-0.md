# 7.7.0

<https://documentation.neutrinos.com/articles/#!change-log/release-7-7-0>

### 7.7.0

**Date: (2021-03-07)**

### Features:

- **Progressive Web Apps(PWA): **You can now convert any app to a PWA on Neutrinos Studio. After converting, you can:
  - Change its appearance to suit your branding guidelines.
  - Cache URL in service workers using the **Cache Config** editor.
  - Use [PWA Firebase](/smart/project-service-designer-user-s-guide/pwa-firebase) and [PWA SW-Events](/smart/project-service-designer-user-s-guide/pwa-sw-events) nodes and design flows on the Client Services Designer to work with web push notifications and update notifications.
- A [Startup Script](/smart/project-node-builder-guide/startup-script) is added to the Plugins Builder to specify logic that is to be executed at the start of a server node.

### Enhancements:

- Added help links to Plugins Builder
- Assets and Client Services Designer editor are validated before converting an app to a PWA.
- A loader is displayed when client or server services are being saved.
- A splash screen is displayed when Neutrinos Studio is taking more than 30 seconds on its first launch.
- Support for fork is added in the **[child-process](/smart/project-server-side-service-designer/child-process-node)** node.
- Parse operation type options are added to the **[CSV](/smart/project-server-side-service-designer/csv-node) **node.

### Bug Fixes:

- Error on opening the Server Services Designer after reopening the studio.
- The Search UI breaks in the Services Designer when a terminal is open.
- The** Back to login **button is not working after selecting login with google.
- Studio times out when removing plugins one after the other time.
- The **Call Service** node list is not visible.
- In the Middleware workspace, the** Save** option of the context menu is not working.
- By default, the publisher name should be the organization of the user.
- In Plugins Builder, the Client and Common Node Utility files are being copied to the server folder.
- Node app does not start on adding the database configuration for PostgreSQL server with version >= 12.x.
- The save functionality becomes extremely slow due to bad regex and bad logic used to generate service imports. Mostly affects services with a large number of nodes.
- Navigation issue in the **Locales **editor.
- The baseClass component subscription issue in the **Locales **editor.
- The** Startup script **breaks the tree by adding utils to the startup script node.
