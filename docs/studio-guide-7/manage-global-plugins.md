# Default Global Plugins

<https://documentation.neutrinos.com/articles/#!studio-guide-7/manage-global-plugins>

[Neutrinos Store](/smart/project-concepts/neutrinos-store) hosts a range of plugins including components, nodes, directives, and app templates.

### Default Global Plugins

By default, a set of plugins gets installed to your local machine when you install the Neutrinos Studio. The default plugins include:

- **Active Directory**: A Microsoft product that consists of several services that run on Windows Server to manage permissions of the users and their access to the networked resources.
- **AMQP Plugin**: Used to create and produce a stream of messages which can be sent to a queue to be consumed by consumers.
- **CSV Plugin**: Used to convert between a **CSV formatted string** and **Javascript object** representation, or in either way.
- **File Plugin**: Used to perform file operations like read and write.
- **JSON Parser**: Used to convert between a **JSON string** and **Javascript object** representation, or in either way.
- **MongoDB**: Used to connect to and perform operations on the MongoDB database.
- **Session Management Plugin**: Used as server-side storage of information that is desired to persist throughout the user's interaction with the website or web application.
- **SQL Plugin**: Used to connect and perform operations on relational database management systems such as MySQL, MS SQL, MariaDB, Oracle, and PostgreSQL.
- **XML Plugin**: Used to convert between an **XML string** and **Javascript object** representation, or in either way.
- **YML Plugin**: Used to convert between a **YMl formatted ****string** and **Javascript object** representation, or in either way.
- **Email Plugin**: Used to send emails with attachments of images, files, HTML templates. You can also send calendar events.

You can click the drop-down icon to see the details of the plugin. The details include the **Name**, **Version**, and **Type** of the plugin.

### Import a Plugin

If you want to use a [plugin](/articles/concepts-publication/plugin) that is available on Neutrinos Store, you should import the Plugin to Neutrinos Studio. Perform the following steps:

1. Click** Plugins** on the top menu, and click **Go to** **Store**.
2. The Neutrinos Store opens up. In Neutrinos Store, each plugin is listed under a category and displayed as a card. You can click on the categories, and then download the plugin of your choice, or use the search bar to look for a plugin. Click the** Download** icon on the plugin that you want to download.
3. When prompted if you want to open the link in Neutrinos Studio, click **Open **Neutrinos Studio**.**
4. In Neutrinos Studio, when prompted for a confirmation to install, click** Yes**.
5. A progress spinner appears indicating the progress of the installation.
6. Once installed, you can view the installed asset by clicking the **Manage Plugins** option on the action menu.

Any plugin that you import from Neutrinos Store is installed globally and is referred to as a [global plugin](/smart/project-concepts/plugin/a/h4_324098977).

### Remove a Plugin

To remove a global plugin from Neutrinos Studio, on the Plugin Manager, select the **Force ****Remove** checkbox for a plugin and click **Remove **to remove the plugin from your workspace. A plugin uninstalled from the workspace will not be available to use inside any application created on Studio.

### Update a Plugin

To update a global plugin on Neutrinos Studio, open the **Check for updates** tab on the Plugin Manager and check for updates. Select the plugin you want to update and click **Update** to get the latest version.

#### Related Topics

You can also create your own plugins and contribute to Neutrinos Store. See:

- [Widget documentation](/smart/project-create-a-widget/create-component-preface) to create a component.
- [Node Builder documentation](/smart/project-node-builder-guide/node-builder-preface) to create a node.
