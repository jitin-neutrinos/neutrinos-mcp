# 7.8.0

<https://documentation.neutrinos.com/articles/#!change-log/release-7-8-0>

### 7.8.0

**Date: (2021-05-21)**

### Features:

- The **Window** menu option is added to the top menu of the Studio Home page and the Studio Application page using which you can:
  - Open another instance of Neutrinos Studio in a new window.
  - Open a new instance of Plugin Builder in a new window.
- Configure a node to dynamically change its label based on a node's attribute value. See [Edit the label of a node](/smart/project-node-builder-guide/node-attributes/a/h3__668741143) to learn more.

### Enhancements:

- Preserving studio user settings in settings.json file. You can now preserve all the changes that you have made to settings.json file when you move from one studio version to another. Only the studioVersion and the reInstallTemplate property values are updated.
- The **Date **node is now supported for the client-side.

### Bug Fixes:

- The Analytics dev is not running. The same analytics hit was appearing multiple times on the ELK because the JSON file associated with the analytic hit is not deleted after being sent to logstash.
- Extreme slow performance of the color picker throughout Neutrinos Studio.
- Cannot update app details if an app is created with a name in upper cases.
- Installing more than 20 app plugins at the same time in the app is throwing errors and making the Studio irresponsive.
- Angular form control related deprecation warning on opening the IDS editor from the Settings menu.
- Buttons in the create an app, edit app details, and plugins manager windows look disabled.
- The Data models editor is breaking while adding a data model attribute of the type **model**.
- "**The user is not allowed to perform operations on Neutrinos organization resources**" error when saving the IDS settings.
- Plugins Manager:
  - In the UI-only and API-only apps, the plugin dependencies are not deleted when a plugin is removed.
  - If **Common **nodes have node dependencies, then the plugins are not installing in the API-only and UI-only apps.
  - The **Alert** dialog box does not appear for unsaved tab changes while closing the studio.
  - The **Check Updates** window is not getting refreshed with the latest changes.
  - Cannot find the **Close **button when no plugins are added.
- Plugins Builder:
  - The node category is not updated after selecting the **Config Node** checkbox.
  - The editors such as Node Details, Node Dependencies, etc. are not closed after deleting a node.
  - The delete package dialog box doesn't have a **delete** icon.
  - The label of **Upload Image** in the **Node Details** editor should be changed.
  - While saving the package details, the image container shows the image text.
- appPages.json file:
  - The app opens when this file is corrupted.
  - Changes made to this file are blocking the studio from launching.
- Plugins of **studio-package** type are not installed if they are not installed directly to the app.
- Code and dependencies related to Node-Red are not deleted from Studio.
- PWA:
  - "**Are you sure you want to exit the app without saving**" message is displayed while converting an app to a PWA.
  - If an app is converted to a PWA, you cannot install any plugin from the marketplace.
- The app opens on Neutrinos Studio even after revoking the migration for the app.
- While updating plugins on Neutrinos Studio, the processing screen is not displayed.
- The workspace layout is unresponsive at times.
- Default Nodes are not getting installed in the UI-only app.
- A blank page is displayed when you open many new windows of the app using the Windows menu.
- CSS issues:
  - The CSS on the **Cancel** button looks disabled when you choose the **Clone** option on the Data models editor.
  - The CSS on the Custom task **Create** button looks disabled.
- A splash screen is displayed when you open both the windows using the **Window **option.
- When you perform a search, no message is displayed if there are no search results.
- Cannot edit cache config URL properly in the **Cache Config **editor.
- Commented descendant should not be uncommented on uncommenting its ancestor.
- The alignment of the select icons in the Routes editors is incorrect.
- PM2 start build path error due to file names and path not matching.
- SQL packages are not getting added when a **Config** node is correctly configured, unless, it's used in a flow.
- generateSnippet is not getting added to the **Startup script** if a node package contains two startup scripts for two nodes.
- The **Date** node is throwing an error during live view.
- The **Is Between** operation is not working in the** Validate** node.
- The **Locales** editor is missing in the app bundle when migrated from 6.0.1.
- Migration of SRM to 7.7.2 is failing.
- The **Async** node invalid states are inconsistent.
- -The collection property in the **MongoDB** node should support env values.
- The origin property in the CORS node should allow env values.
- Neutrinos Studio gets stuck in the splash screen as the nodemodules folder was not found for the **Google Map** component.
- Not able to map the **result** property to bh.input and bh.local options in the **Internet **nodes.
- Documentation links not working for **Async **and **isOnline** nodes.
- NGMaterial Toolkit error while trying to migrate an app with **Google Map** and **Chart** components.

### Known Issue

After upgrading Neutrinos Studio to the latest version, if you try to install a node from Neutrinos Store, you encounter an error stating that you are running an old version of Neutrinos Studio. This is because the marketplaceUrl property is not updated to the latest version.

**Workaround:**

1. Access the /.neutrinos/settings.json file in your local machine.
2. Update the studio version in the marketplaceUrl property to the installed version of Neutrinos Studio -  https://store.neutrinos.co/api/**<INSTALLED_VERSION_OF_STUDIO>**
3. Save the file and restart Neutrinos Studio.
