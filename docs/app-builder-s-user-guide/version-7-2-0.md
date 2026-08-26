# Upload Folder option in Assets Editor

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/version-7-2-0>

Here is a list of new features introduced in Neutrinos Studio 7.2.0

#### Upload Folder option in Assets Editor

The Assets editor contains images to be used on the frontend application. In the Assets Editor of the Neutrinos Studio, you can upload assets to the app that you create and use it.

You can now upload assets as a folder to the application. See [Assets editor](/articles/app-builder-s-user-guide/add-assets) to learn more.

#### Preview image for an app

While creating an app, you can now upload and preview the image for the app and view it in the Create app dialog box.

#### Open last used app

From Neutrinos Version 7.2.0, when you open the Studio, the recently used app opens by default. If you close the studio from the workspace, workspace opens by default. you to open the last used app when you close and relaunch the Neutrinos Studio.

#### Global MongoDB Session node

The Global MongoDB Session node is added to the Server Service Designer of the Neutrinos Studio to configure how sessions should work in a server using the **MongoDB** database.

See [Global MongoDB session node](/smart/project-server-side-service-designer/global-mongodb-session-node) to learn more.

#### Function Name for nodes

For every node on both Client Services Designer and Server Services Designer, the **Function name** is automatically generated when you enter the name of the node. If the name is not entered, a **unique id** (random string) is generated and used as the function name for code generation of the end app. Note that this is only applicable for nodes that generate function names.

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | All the apps create 720 will output angular 9 apps. For every app created before 720, auto migration will upgrade the app to angular 9. |
| --- | --- |

| ![Warning](/resources/Storage/app-builder-s-user-guide/warning.png) | While migrating your app to Neutrinos Version 7.2.0, [here](/smart/project-migration-guide/migration-from-7-1-0-to-7-2-0) is something that you have to keep in mind. |
| --- | --- |
