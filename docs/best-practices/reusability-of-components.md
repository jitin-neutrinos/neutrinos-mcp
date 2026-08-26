# Best Practices to Reuse Components

<https://documentation.neutrinos.com/articles/#!best-practices/reusability-of-components>

# Best Practices to Reuse Components

---

As developers, we are always interested in making the app development lifecycle as easier as possible and more effective. To achieve this, all development frameworks and languages provide some form of **sub-module/sub-component** support to create unit blocks of functional reusability.

Neutrinos Platform also provides ways to do the same and help in component reusability:

1. By using views
2. By using existing components from Neutrinos Store.

### Views

Using Views, you can divide app pages into pieces or reusable blocks that can be configured from the parent page to change its behavior and view. It can also emit events to make the parent page aware of user interactions. For example, let us assume that you have created an app with a view that includes a set of address fields. If you want to create a second view that needs the same address fields, you can reuse the first view. In both cases, the app is using an instance of the view.

To start using views and understand how to work with them, refer to the [Views documentation](/articles/app-builder-s-user-guide/views).

### Marketplace Components

Neutrinos Store is the center of all pre-built digital assets including widgets, micro-services, smart app templates, components, and pre-defined data models. Navigate to [Neutrinos Store](https://store.neutrinos.co/web/catalog/featured) to download and use the existing assets while building your application.

To import assets from Neutrinos Store and use them across apps that you create on Neutrinos Studio, perform the following steps:

1. On the Neutrinos Studio home page, click** Plugins** on the action menu and click **Go to ****Store**.
2. The Neutrinos Store opens up. Click the **Download** icon on the asset that you want to download.
3. When prompted if you want to open the link in Neutrinos Studio, click **Open **Neutrinos Studio**.**
4. InNeutrinos Studio, when prompted for a confirmation to install, click** Yes**.
5. A progress spinner appears indicating the progress of the installation.
6. Once installed, you can view the installed asset by clicking the **Manage Plugins** option on the action menu. If you have downloaded a component, you can search for the component by using the search bar in your palette list.

Neutrinos Store also supports sharing Angular libraries, Studio page components, and Neutrinos Modelr nodes. All of which can be bundled into a Studio package. To know how to contribute to Neutrinos Store by creating your own component, Angular library, Neutrinos Modelr, or a combination of them, see [Creating a Plugin](/articles/components-guide-for-release-6/release-6-0-2).
