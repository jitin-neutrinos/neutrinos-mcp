# Import a Plugin from Neutrinos Store

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/import-dependencies-from-neutrinos-store>

## Import a Plugin from Neutrinos Store

Plugins are reusable components that help speed up app delivery time. A single plugin can be a combination of a toolkit (a set of Studio palette components), an angular library, and a modelr node. Neutrinos Store contains many such plugins that you can download. It is the marketplace of Neutrinos.

Using the Plugins Manager, you can import and manage assets at the workspvn nm,ace-level and at the app-level.

- You can import and manage templates and themes in the Neutrinos Studio workspace and use them across apps.
- You can also import and manage components and dependencies in any application.

### Import Plugins to the Studio Workspace

To import assets from Neutrinos Store and use them across apps that you create on Neutrinos Studio, perform the following steps:

1. On the Neutrinos Studio home page, click** Plugins** on the action menu and click **Go to** **Store**.
2. The Neutrinos Store opens up. Click the** Download** icon on the asset that you want to download.
3. When prompted if you want to open the link in Neutrinos Studio, click **Open **Neutrinos Studio**.**
4. InNeutrinos Studio, when prompted for a confirmation to install, click** Yes**.
5. A progress spinner appears indicating the progress of the installation.
6. Once installed, you can view the installed asset by clicking the **Manage Plugins** option on the action menu. If you have downloaded a component, you can search for the component by using the search bar in your palette list.

---

#### Manage plugins from the Studio Workspace

A set of plugins gets installed by default to your local machine when you install the Neutrinos Studio. The plugins that are installed are:

- **Active Directory**: A Microsoft product that consists of several services that run on Windows Server to manage permissions of the users and their access to the networked resources.
- **AMQP Plugin**: Used to create and produce a stream of messages which can be sent to a queue to be consumed by consumers.
- **CSV Plugin**: Used to convert between a **CSV formatted string** and **Javascript object** representation, or in either way.
- **File Plugin**: Used to perform file operations like read and write.
- **JSON Parser**: Used to convert between a **JSON string** and **Javascript object** representation, or in either way.
- **MongoDB**: Used to connect to and perform operations on the MongoDB database.
- **Session Management Plugin**: Used as server-side storage of information that is desired to persist throughout the user's interaction with the web site or web application.
- **SQL Plugin**: Used to connect and perform operations on relational database management systems such as MySQL, MS SQL, MariaDB, Oracle, and PostgreSQL.
- **XML Plugin**: Used to convert between an **XML string** and **Javascript object** representation, or in either way.
- **YML Plugin**: Used to convert between a **YMl formatted ****string** and **Javascript object** representation, or in either way.
- **Email Plugin**: Used to send emails with attachments of images, files, HTML templates. You can also send calendar events.

Click the drop-down icon to see the details of the plugin dependencies. These details include the **Name**, **Version**, and **Type** of the sub plugin.

![plugins manager workspace dependencies](/resources/Storage/components-guide-for-release-6/pm1.png)

---

To manage installed assets from Neutrinos Studio workspace, click** Plugins** in the action menu, and click **Manage Plugins**. The **Manage Plugins **window opens up displaying all the available plugins. In this window, you can manage your workspace plugins.

1. Select the **Remove** checkbox for a plugin and click **Remove Dependencies** to remove the template from your workspace.
2. Click the **Check for updates** tab to check for template updates. Select the template you want to update and click Update to get the latest version.
3. Click the **Templates** tab to view the templates that you have already downloaded. Select a template and click** Remove** to remove the template from the workspace.

---

### Manage Plugins in your Application

**Add a custom app dependency**

You can add custom dependencies, either npm or Angular, to your app. Perform the following steps:

1. Navigate to theNeutrinos Studio Application page.
2. Click** Plugins **on the Action menu. The plugins manager opens up.
3. Click the **Add Dependency** tab.
4. Select the type of dependency.
5. If you choose npm, enter a valid npm package name and the associated version. Click **Add Dependency**.

1. If you choose Angular, enter a valid Angular package name, version, and the Angular library to be added, and click the **+** icon.

Click the drop-down next to the Angular library. You will see the module input field displayed where you can enter the module to import from the Angular package. Click the** forRoot** checkbox to enter the** forRoot **configuration. Click **Add Dependency**.

---

#### Manage custom app dependencies

To manage custom app dependencies, perform the following steps:

1. Click the** Custom Dependency** tab.
2. To edit a dependency, select the dependency. The page takes you back to the **Add Dependency **tab where you can make changes to the dependency.
3. To remove the dependency, select the dependency, and click **Remove Dependencies**.

---

#### Check the Workspace Plugins to Install

1. A set of plugins are installed to your local machine when you install the Neutrinos Studio. The plugins that are installed are:

- **Active Directory**: A Microsoft product that consists of several services that run on Windows Server to manage permissions of the users and their access to the networked resources.
- **AMQP Plugin**: Used to create and produce a stream of messages which can be sent to a queue to be consumed by consumers.
- **CSV Plugin**: Used to convert between a **CSV formatted string** and **Javascript object** representation, or in either way.
- **File Plugin**: Used to perform file operations like read and write.
- **JSON Parser**: Used to convert between a **JSON string** and **Javascript object** representation, or in either way.
- **MongoDB**: Used to connect to and perform operations on the MongoDB database.
- **Session Management Plugin**: Used as server-side storage of information that is desired to persist throughout the user's interaction with the web site or web application.
- **SQL Plugin**: Used to connect and perform operations on relational database management systems such as MySQL, MS SQL, MariaDB, Oracle, and PostgreSQL.
- **XML Plugin**: Used to convert between an **XML string** and **Javascript object** representation, or in either way.
- **YML Plugin**: Used to convert between a **YMl formatted ****string** and **Javascript object** representation, or in either way.
- **Email Plugin**: Used to send emails with attachments of images, files, HTML templates. You can also send calendar events.

2. Click the drop-down icon to see the details of the plugin dependencies. These details include the **Name**, **Version**, and **Type** of the sub plugin.

![plugins manager workspace dependencies](/resources/Storage/components-guide-for-release-6/pm1.png)

3. Click **Add** and the plugins will get installed to your app.

You can also add any workspace plugin to your app from the Neutrinos Store, perform the following steps to do so:

1. In the Manage Plugins window, select the **Workspace Plugins **tab. You can see the plugins that are mentioned above are installed to your app by default.
2. If you want to remove any plugins that you don't want to use for the app, you can remove those plugins. Select **App plugins** and select the that the workspace plugin that you don't want to use for your app and click **Remove****. **

![](/resources/Storage/components-guide-for-release-6/appplugs.png)

If you want to reinstall the removed plugins, perform the following:

1. Navigate back to the workspace plugin tab.
2. Select the plugin that you have remove and click **Add**.

### Remove Installed Plugins

To remove an installed plugin, perform the following steps:

1. In the Manage Plugins window, select the** App Plugins** tab.
2. Select the plugin you want to delete, and click **Remove Dependencies**.

### Install Missing Plugins

If you remove a plugin that your app was dependant on, your app starts throwing errors. To install such missing plugins back to the app, perform the following steps:

- In the Manage Plugins window, select the **Missing Workspace Plugins** tab.
- Select the plugins to install and click **Add Dependencies**.

This tab appears only if there is a missing plugin in the app. It also prompts for version mismatches between workspace and app plugins (if any).

### Check for Template Updates

To check for template updates, perform the following steps:

1. In the Manage Plugins window, select the **Check for updates** tab.
2. If there is an update for a template that you have installed in your app, it appears in this tab. Select the template and click** Update**.

The template gets updated in the app and the workspace.

### Remove App Templates

To remove an app template:

1. In the Manage Plugins window, select the **Templates** tab.
2. Select the template and click **Remove**.

![](/resources/Storage/components-guide-for-release-6/1-4-import-from-neutrinos-store-img0011.png)

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Note that the plugins downloaded using the Studio Application page will be installed as both an app and a workspace plugin. This plugin can be used in other apps by installing it from the plugins manager. |
| --- | --- |
