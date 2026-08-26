# Node Properties

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/use-dependency-node>

As the name indicates, the **Use Dependency** node is used to import a custom dependency to the client service. Before you use the dependency, you should [add the custom dependency](/smart/project-sample-how-to-guide/manage-app-dependencies/a/h3_1506476317) to the app using the [Plugins Manager](/smart/project-sample-how-to-guide/manage-plugins-dependencies).

### Node Properties

- **Name:** The name of the node. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Library: **The library that you want to import to the client service. You can import an Angular library, an npm library, or any legacy service. The syntax is as follows:
  - To import an Angular material library, use @angular/material/<library name>
  - To import a legacy service, use app/services/<service-name>/< service name>. service

| ![Information](/resources/Storage/client-services-designer-9/project-page-services-designer-guide/info.png) | To import a client or server service, use the [Call Service](/articles/client-services-designer-9/call-service-node) node. |
| --- | --- |

- **Import All: **Enable this toggle button if you want to use all the modules in the library. Enter an alias name that you want to use for this library and assign it to a [flow variable](/articles/client-services-designer-9/service-designer-variables). After adding the alias, to reference a particular module of the library, you can use <aliasname>.<modulename> on your page.
   **Example:** To import all the modules from the Angular bottom-sheet library.![Use all modules as dependency](/resources/Storage/client-services-designer-9/project-page-services-designer-guide/use_dep1.png)
   To reference the MatBottomSheet module which is a part of the bottom-sheet library, enter bottomsheetLib.MatBottomSheet anywhere in the client flow.
- **Modules:** If you do not want to import all the modules in your library, you can add specific modules to the client service. Enter the module name and assign it to a flow variable. Make sure that the module names are unique. If a module or service is injectable, toggle **Injectable** to True.
   **Example: **To import specific modules from the Angular bottom-sheet library.![Use specific modules](/resources/Storage/client-services-designer-9/project-page-services-designer-guide/use_dep2.png)
