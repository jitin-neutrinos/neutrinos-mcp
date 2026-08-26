# 7.0.2

<https://documentation.neutrinos.com/articles/#!change-log/release-7-0-2>

### 7.0.2

**Date: (2019-02-11)**

### Features:

- **Server Services Designer** is added to this release of Neutrinos Studio.
  - Added a condition to handle operations for the **File Out **node in Server Services Designer.
  - Added support for databases such as **MSSQL**, **MySql**,** MariaDB**,** Oracle**,** and Postgres** in the** SQL **node.
  - Added migration to support new Mongo operations and add the DB category for config nodes.
  - Added a link to view Swagger documents in Server services.
- Added keyboard shortcuts to:
  - Open plugins manager. Use **Ctrl+shift+p** to open plugins manager in Windows. Use **Cmd+shift+p** to open plugins manager in a MAC machine.
  - Switch between Html and Ts editors. Use **Ctrl+0 **in Windows. Use **Cmd+0** in MAC.
  - Switch between tabs. Use **Ctrl+Tab** or **Ctrl+Shift+Tab** in windows. Use the **Cmd+Tab** in a MAC machine.
- Added a feature to **Comment** any component while designing application pages. Click the comment icon in the component to disable code generation of that component.
- Added IDS configuration to authenticate and authorize users using the Neutrino OAuth Strategy or using other OAuth providers such as Google, Azure, and Active Directory. See [Configure IDS](/smart/project-sample-how-to-guide/configure-your-ids) to learn more.
  - Added **Skip Team check** property in the IDS settings for public-facing apps.
- Added **PM2 **configuration in the Settings editor. See [Configure PM2](/smart/project-sample-how-to-guide/configure-pm2) to learn more.
- Enabled canDeactivate property in Routes.
- Added **Client** and **Server** environment types in the Environments editor.
- Added **Live View** Option to preview Client and Server services.
- Disabled Neutrinos Modelr in Neutrinos Studio. This feature can be enabled on request.
- **Client Services Designer:**
  - Added Client-Side migration for start nodes.
  - Added a **Comments **node to the list of nodes.
- Removed the** Initialize Mobile** option from the task drop-down list, and added **Initialize Android** and **Initialize iOS**.
- Tasks drop-down list:
  - New script to **initialize-android** and **initialize-ios** are added to the package.json file.
  - Migration steps are written to handle changes made to the **Tasks **drop-down list for old apps. The migration step executes Cordova platform add <platform-name> instead of executing Cordova prepare.
- Deprecated support for Neutrinos Art. To cleanup ART, the following tasks were performed:
- Removed the art specific methods from the component.ts template
- Commented the** fingerprint-aio** and **neutts** Cordova plugins
- Moved **model.methods.ts** out of the seed app to **/angularSeedUtils** folder
- Changed **neutrinos-module** version to 0.0.53
- Added the following properties in Environments editor:
- Added the **File Logger** configuration in the Neutrinos Studio Settings editor.
- Added **Locales **editor to create applications that can be adapted to different languages and regions.
- Introduced nullable property for typed input.
- Added **External Groups** field to add teams window on the console.
- Added migration for AuthGuard for OAuth-client module which works on Browser and Mobile.
- Added **node type** property in the **Catch** node.

### Enhancements:

- New Icons for **F****etch**, **M****ap/Edit** buttons in Client Services Designer nodes.
- Hide **response body** and **status** fields when the response type is **Next ****Middleware** for **HttpOut** and **MiddlewareEnd** nodes.
- Added Migration steps to fix typos in the code generation of the **MongoDB** node.
- Added different icons for **Map** and **Value** options in the attributes window.
- On app creation, the .npmrc file is created in the app. Also, the auto-migration step now writes a new .npmrc file instead of creating a copy of the file.
- The sourceMap property in the **tsconfig.json** file is changed to false by default. Change it to true during debug mode if required.
- Added Migration for removing invalid style attribute in the** Menu** Component.
- An option to go back to the Login page added to the App menu.
- Updated the config.xml with the info-plist value for N**SBluetoothAlwaysUsageDescription** which was causing app crashes.
- Added Migration for removing invalid **fxLayout** property in the **Sidenav **Component.

### Bug Fixes:

**Service Designer:**

The palette window closes when you edit the configuration of a node.Typo in code generation of MongoDB node.
Deleting/renaming a Server Service flow does not delete its entry from the **UserRoutes** array.Creating .env in Server Service Designer with the same configuration as in angular envs.
In the **Catch** node, the Comments node is also displayed.
Valid inputs are shown as invalid in the field.
Body in the **HTTPOut **node is not mandatory for redirect response
Added XML server node code generation for missing options.
UI alignment of the Global Middleware start node of the default root.
The name is not trimmed to the length that can be displayed on the page container.No validation of the HTTP status codes in the **CORS** node.In the **Call Service** node, selecting different flows from the same service creates two instances of the same service during code generation.Lengthy node name in the **Catch** properties window breaks the UI.
Code generation fails if there is a **Start **node whose name is a substring of another **Start** node.The **Global Session** node secret should be a .env property of type **string** as it is used to encrypt the session_id.Misaligned Service Designer overflow menu icons.
Setting the **Http Only** property to false.
**Ctrl+(click)** in the service designer canvas throws an error.
Incorrect placeholder for Active directory prefix.
The app saves only the dirty workspaces in Server services.
Dragging and dropping** Middleware Start Node** to the chart appends it to the service palette list then switching clears it.Palette toggle button gets disabled after deleting a server service.
Scroll transparency when SSD is opened while the terminal is open.
Two nodes can be dragged when the node goes out of Canvas. Generated code is invalid after migration.HTTP status code can be a typed input.MongoDB Find operation is not working.
The **bh.local **object should be created in the **Middleware Start **node.The **Middleware End** node should not return anything while sending out a request or making a next middleware call.An error is thrown if **Proxy** is configured in the **HttpRequest** node.**Plugins Manager:**The **Richtext editor** component in Neutrinos Store is not working fThe **configNodes.ts** file is missing while saving the Client Services without migration.You cannot install the missing modules while launching Neutrinos Studio for the first time.Cannot remove installed plugins from the Plugins Manager.Installing two plugins at a time opens a pop-up window.Both **Client **and **Server **types are not checked in the editor.Unable to remove plugins.Migration issues while downloading plugins.**Components:** Change cursor state to** move** while moving components within a page.Flickering icons in downloaded components.Invalid isActivated attribute & style, the class is not working in the **Router outlet **component.TS parser failing if a comment is there in @component decorator(fixed).
Removed hardcoded docs.neutrinos.co URL from **AdvanceTabGroups** and **TabContent **files and added the docs link for deprecated components.
Type repeatedly gets appended to the** Switch** node property value
Changed visible flag to false for the **Tooltip **component.
Removed invalid fxLayout attribute from **Sidenav **Component.
Removed Invalid Style attribute form **Menu** Component.JS Error in the **Polar area chart **when fxFlex is being set.Client ID in the **Google** tab should not be required if it is not checked.The editor tray resizes the issue. Assets Editor folder becomes empty on dragging a sub-folder in the tree. Removing **D****ata sources** from settings.Resolved the issue of console window throwing an error when trying to close.
On app creation, now .npmrc is created in-app. Also, migration now does write instead of a copy of .npmrc.Saving a single service does not show a snack bar message.The **configNodes.json** file does not exist error when trying to save client services.Send node id to erroHandler instead of function name since function name is not the same as node id always.Save button remains disabled for **string** type in the Navigation node path field The CreateIndex operation has to have its field renamed to **field** or **spec.** Node-Red does not start even if the disableNodeRed property is set to false in the **settings.json** file.The scrollTo() function is not working in the settings editor of the parent component.App creation fails if you create app names with keywords such as data models, routes, and the environment.The **CreateIndex** operation has to have its field renamed to **field** or **spec**.Deleting a custom task empties the Action bar.Add Terminal button remains disabled when the live-view command is running and one of the tabs is closed.
Cannot run a custom task that is created in the old version of the studio.
On page resizing the attribute window is not resizing the base container.
Global session error when an old app is migrated.

### Known Issue:

- Setting **Streaming** field to **True** in the **File Out** node will give a error while encoding the data.
- Cannot give duplicate values in the query parameter field of the **SQL** node.
- Save button is disabled even after all the fields are enterred in the XML node.
- Entering lengthy value in the class field of any component will not work.
- Cannot give duplicate values in the class field of any component.
