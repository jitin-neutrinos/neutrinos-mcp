# Server Services Designer

<https://documentation.neutrinos.com/articles/#!studio-guide-7/new-in-neutrinos-studio-versio-7-1-0>

## 

## 

Here is a list of new features introduced in Neutrinos Studio version 7.1.0.

### 

### Server Services Designer

The following nodes are added to the Server Services Designer (SSD):

- [Async block node](/smart/project-server-side-service-designer/async-node): Used to execute flows asynchronously.
- [AMQP Producer node](/smart/project-server-side-service-designer/amqp-producer-node): Used to create and produce a stream of messages that can be sent to a queue and consumed by a compatible AMQP 0-9-1 broker.
- [Child Process node](/smart/project-server-side-service-designer/child-process-node): Used to spawn [child processes](https://nodejs.org/dist/latest-v12.x/docs/api/child_process.html).
- [Email out](/smart/project-server-side-service-designer/email-out-node): Used to send emails with attachments which include images, files, HTML templates, and also send calendar events.

The following nodes are updated in SSD:

- [MongoDB node](/smart/project-server-side-service-designer/mongodb-node): Updated to support more operations on the MongoDB collection.
- [SQL node](/smart/project-server-side-service-designer/mssql-node): Updated to support databases such as Oracle, PostgreSQL, MSSQL, and MariaDB.

### Client Services Designer

The following nodes are added to the Client Services Designer (CSD):

- [Async block node](/smart/project-service-designer-user-s-guide/async-node): Used to create flows that execute in asynchronously.
- [Call Server API node](/smart/project-service-designer-user-s-guide/call-server-api-node): Used to send or receive data from a server API.

### Create Client and Server Nodes

With every release of Neutrinos Studio, more and more client and server nodes are being added to Neutrinos Studio to enable you to perform a wide range of functionalities. Along with this, starting from this release, Neutrinos also enables you to create your own Client and Server nodes using the Node SDK. The basic skills required to create these nodes include JavaScript and JQuery. See the [Create Client and Server Nodes](http://docs1.neutrinos.co/articles/create-client-and-server-nodes) documentation to get started.

After creating nodes, you can test them on Neutrinos Studio, and publish them to [Neutrinos Store](http://store.neutrinos.co/) (the marketplace of Neutrinos) for other developers to use.

### Components

Three new components are added to the Neutrinos Studio palette list. They are:

- [Chips](/smart/project-components-documentation-copy/chips): used to display a list of values as chips. Example:

![The chip component](/resources/Storage/studio-guide-7/chip.png)

- [Autocomplete](/smart/project-components-documentation-copy/autocomplete): used as a special input control to show all possible matches to a custom input. Example:

![Autocomplete component](/resources/Storage/studio-guide-7/autocomplete1.png)

[Paginator](/smart/project-components-documentation-copy/pagination): used to provide navigation for paged information.



 ![paginator](/resources/Storage/studio-guide-7/paginator.png)

**Neutrinos Identity Server (IDS)**

**Login template**

A new [Login template](/smart/project-components-documentation-copy/neutrinos-login-templates) is added to Neutrinos Store.

 This template uses [Neutrinos Identity Server (IDS)](/articles/concepts-publication/identity-server) and is, by default, configured with the Neutrinos OAuth Strategy to authenticate your app users. You can retain the Neutrinos OAuth strategy or edit the IDS Settings to opt for the following auth strategies:



 [Google](/articles/studio-guide-7/configure-ids-with-google)


 [Active Directory](/articles/studio-guide-7/configure-ids-with-active-directory)


 [Azure](/articles/studio-guide-7/configure-ids-with-azure)



 Watch this video to learn how to configure Neutrinos IDS using the login template.




 **Skip Team Check Option**


 In the** IDS Settings** editor, you can select the **Skip Team Check** option if you are creating a public-facing app.

 ![Skip team check](/resources/Storage/studio-guide-7/Skiptc.png)

 This option allows external users to log in to the app through whichever OAuth strategy you select in the IDS setting. It also eliminates performing user management on Neutrinos Console.


 **isLoggedIn Property**


 The isLoggedIn property is added as an OAUTH property. You can use this property in the TS editor to check if the user has logged in to the application or not. It returns True if the user has logged in. Else, returns False.


 Redirect Web App Users


 Post login or logout, if you want to redirect your web app users to specific pages, you can perform the steps documented in the [Redirecting web app users](/articles/studio-guide-7/use-ids/a/h3_1722131387) topic.

### Plugins Manager

Starting from version 7.1.0, when you open the Plugins Manager in Neutrinos Studio, a set of plugins are pre-installed. They are:

- [Active Directory](/smart/project-server-side-service-designer/active-directory-node)
- [AMQP](/smart/project-server-side-service-designer/amqp-producer-node)
- [CSV](/smart/project-server-side-service-designer/csv-node)
- File which includes [File in](/smart/project-server-side-service-designer/file-in-node) and [File out](/smart/project-server-side-service-designer/file-out-node)
- [JSON Parser](/smart/project-server-side-service-designer/json-node)
- [MongoDB](/smart/project-server-side-service-designer/mongodb-node)
- [Session Management](/smart/project-server-side-service-designer/session-node)
- [SQL](/smart/project-server-side-service-designer/mssql-node)
- [XML](/smart/project-server-side-service-designer/xml-node)
- [YML](/smart/project-server-side-service-designer/yml-node)
- [Email](/smart/project-server-side-service-designer/email-out-node)

##
