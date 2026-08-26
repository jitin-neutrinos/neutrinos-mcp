# Debug Server Flows

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/debug-server-flows>

To debug server flows that you create in an application, you should set the sourceMap variable in the **tsconfig.json** file to True. Perform the following steps:

1. Open the tsconfig.json file in your app folder. It is located in the **server** folder of your app.![server floder](/resources/Storage/app-builder-s-user-guide/project-how-to-articles/server_folder.png)
2. Update the value of the sourceMap variable to True and save the file.![sourceMap in tsconfig.json file](/resources/Storage/app-builder-s-user-guide/project-how-to-articles/source_map.png)
3. Use a debugger (Chrome debugger or VS Code debugger) to start debugging your server flows.
