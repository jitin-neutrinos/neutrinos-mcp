# 8.0.0

<https://documentation.neutrinos.com/articles/#!change-log/release-8-0-0>

### 8.0.0

**Date: ( 20/08/2021)**

### Features

The PostgreSQL package is upgraded to [pg 8.7.1](https://packages.tools.medtronicconnect.com/feeds/NPM/pg/8.7.1).


 [Flow designer](/smart/project-concepts/page-designer/a/h3_520216706) is added to the **Page** editor to design the business logic of the page by creating page flows.


 The [page explorer](/smart/project-sample-how-to-guide/page-explorer) is enhanced with a tree-view structure to display the **UI** and **Flow** designers of a page.


 Folders are added to the page explorer to organize application pages.


 An experimental dark mode is added to the Studio. You can switch the Studio to dark mode by selecting **View > Invert Color (Experimental Dark Mode)** from the top menu.


 The **Plugins Builder** is enhanced to allow users to create custom, reusable page nodes. See [Add a Page Node](/smart/project-node-builder-guide/add-a-page-node) to learn more.


 The **Search nodes** drop-down is added to the Studio Application page to easily search any node added to the application and quickly navigate to it on the respective designer. See [Search Nodes](/smart/project-sample-how-to-guide/search-nodes) to learn more.


 Some attributes in the properties window of a component are updated with the** Flow Picker** icon to allow users to bind a page/client flow to that attribute. See [Bind Page Flows to a Component's Attribute](/smart/project-sample-how-to-guide/bind-page-flows-to-components) and [Call a Client Service Flow on the Page UI](/smart/project-sample-how-to-guide/import-client-services-to-the-page-ui) to learn more.


 An emit node called [Output](/smart/project-page-services-designer-guide/output-node) is added for output variables to emit data to the parent page from the child page.


 When a user drags and drops any palette component, the system auto manages the relevant imports. The following import configurations are added to the **Input** and **Table** components:






 **Toolkit Page Component**



 **Modules**




 **Library**






 Input




 [formControl], Validators,and FormBuilder




 @angular/form






 Table




 MatSort and SortDirection




 @angular/material/sort






 Table Paginator




 MatPaginator




 @angular/material/paginator








 The following configurations are added to the [HttpRequest](/smart/project-service-designer-user-s-guide/http-request-node) node:


 **Observe:** Determines the return type, according to what you want to observe.


 **Report Progress:** Determines whether this request should be made to expose progress events.


 **With Credentials:** Determines whether the HTTP request should be sent with outgoing credentials (cookies).




 A new node called [Use Dependency](/smart/project-service-designer-user-s-guide/use-dependency-node) is added to the [Client Services Designer](/smart/project-concepts/client-services-designer) to import custom dependencies and use them within a client service flow or a page flow.

### Bug Fixes

**Plugins Manager** - A blank editor is displayed when you clone (export and import) a service flow containing a config node from App A to App B, and uninstall the config node from App B.


 **Plugins Builder** - The env type in the typed input field of the **Node Attributes** window should be displayed as **client env **and** server env** respectively depending on the node that the user is trying to create.


 The marketplaceURL property is not overridden when the user upgrades to a higher version of Neutrinos Studio.


 **Asset editor **- The editor does not allow the drag and drop of assets from one folder to another.


 The generated Identity Server flows are not visible in the Server Services Designer editor.


 Invalid PM2 settings can be saved on Studio.



 When you insert a **Card** component inside a **Row** component, it expands beyond the **Row** component.




 The same App can be opened in two windows in certain scenarios



 The default values are not getting assigned to input properties in the called **Start** node.


 Other Changes



 The **1****-click Deploy **icon is hidden by default from the Studio Application page. See [Enable 1-click Deploy](/smart/project-sample-how-to-guide/deploying-an-application-on-cloud/a/h4__1051527422) to change this setting.

Known IssueBefore Studio 8.0, if no value is mapped to an input property in the **Call Service** and **Async** nodes, the value was assigned as Null. From 8.0, the value will be assigned as Undefined. This might change the behavior of some flows where input properties were assigned a default value. If you have a logic written in your app to check that input property against a Null value, once the app is migrated, that logic will fail as the default value has changed.
