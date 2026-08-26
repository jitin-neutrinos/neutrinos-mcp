# Server Services Designer (SSD)

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/new-in-neutrinos-studio-version-7>

## 

Here is a list of new features introduced in Neutrinos Studio version 7.0.2:

### Server Services Designer (SSD)

From Neutrinos Studio release 7.0.2, you can create API endpoints for your applications by creating server flows using the** Server Services Designer (SSD)**. All over the world, companies leverage APIs to transfer vital information, processes, transactions, and more. Endpoints specify where resources can be accessed by APIs and play a key role in guaranteeing the correct functioning of the software that interacts with it.

Using Server Services Designer you can create **HTTP endpoints** which can perform the following:

- **Interact with databases** where you can drag and drop a server node and configure a server flow to integrate with relational database management systems such as MSSQL, MySQL, MariaDB, Oracle SQL, Postgres SQL to perform CRUD operations. You can also connect to NoSQL databases such as MongoDB. This comes with support to **Connection Pooling** where a cache of database connections is maintained by server services so that the connections can be reused when future requests to the database are required.
- You can use HTTP endpoints to Identity authentication and create and manage the sessions for your application.
- You can configure how your server should handle every incoming request through the Global middleware sequence.
- You can parse data from one format to another by using **Parser nodes** that can parse and serialize data during message transfer between systems such as IIB or translate messages. These nodes provide the capability to connect message processing applications like Kafka regardless of message formats or protocols.

The Server Service Designer provides a list of service nodes that you can drag and drop to create a service flow. See the [Server Services Designer](/smart/project-server-side-service-designer/server-services-designer-preface) guide to learn how server services work and how to create service flows using the Server Services Designer.

**Neutrinos Identity Server (IDS)**

Neutrinos Identity Server (IDS) is a standards-compliant OAuth 2.0 authorization standalone and a certified OpenID Connect provider. Every application that you build on Neutrinos Studio should have its client registered on IDS using the Neutrinos Studio.

Starting from Neutrinos Studio release 7.0.2, you can use the default Neutrinos Auth Strategy or connect to OAuth providers such as Active Directory, Google, or Azure AD.

Neutrinos performs both, authentication and authorization of apps after the IDS is enabled. See [Configure IDS](/articles/app-builder-s-user-guide/configure-your-ids) to learn more about IDS configuration.

### Internationalization (I18N)

Internationalization, also called Localization, is added to the Neutrinos Studio which allows you to create applications that can be adapted to different languages and regions. You use the** Locales** settings in the editor pane to set the locale-specific information by using keys and languages.

The Neutrinos Studio translator converts the keyword to the language of your choice and displays it on the screen. See [Localization](/articles/app-builder-s-user-guide/apply-internationalization) to learn more.

### Logger Settings

Neutrinos Studio allows you to configure logger settings for the server apps that you create using Neutrinos Studio. Log files are useful in debugging and auditing applications and their flows. To access Logger settings, click **Settings** on Neutrinos Studio and select **Logger**. See [Logger settings](/articles/app-builder-s-user-guide/configure-logger) to learn more.

**Neutrinos Console**

The Neutrinos Console is upgraded to perform user management of applications for an organization. Using the Console, you authenticate and authorize users to access applications created on Neutrinos Studio.

See [Perform User Management](/articles/app-builder-s-user-guide/perform-user-management) to learn more.

### PM2

**PM2** is a daemon process manager that helps you in managing and keeping your application online. It manages your application states so that you can start, stop, restart and delete processes. Starting from the 7.0.2 release of Neutrinos Studio, you can configure the process management workflow for your application using the PM2 Settings.

See [Configure PM2](/articles/app-builder-s-user-guide/configure-pm2) to learn more.

### New Nodes in Client Services

New nodes such as **Catch** and **Comments** nodes are added to **Client services**.

- The [Catch](/smart/project-service-designer-user-s-guide/catch-node) node is used to catch errors thrown by nodes on the same service.
- The [Comments](/smart/project-service-designer-user-s-guide/comments-node) node is used to write a description or comment for the server flows.

### Keyboard Shortcuts in Neutrinos Studio

The following shortcuts are added to the studio for ease of use:

- Use **Ctrl + W** to close the current tab
- If you are working on an application page, use **Ctrl + 0 **to toggle between the Typescript view and the HTML view of the page.

### Neutrinos ART

The support for Neutrinos Art is disabled from Neutrinos Studio release 7.

Neutrinos Art was used for storing and managing applications, data models, security constraints, and configurations built on Neutrinos Studio. Starting from release 7.0.2, these tasks are easily handled with the help of Neutrinos IDS and Server Services.

### Comment Icon in Components

The** Comment** icon is added to all components in Neutrinos Studio. You can use this icon to comment a component. if commented, code generation for that component will not happen. That is, this component will not be part of your end app. You can uncomment the component to include it in your end app.

If you comment a component, all components that you drag and drop inside the commented component will also be commented.

##
