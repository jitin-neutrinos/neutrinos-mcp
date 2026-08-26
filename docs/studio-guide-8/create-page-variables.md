# Create Page Variables in the Page Variables node

<https://documentation.neutrinos.com/articles/#!studio-guide-8/create-page-variables>

You can create [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h4_1197862820) in the **Page Variables** and **Script** nodes of a flow.

#### Create Page Variables in the Page Variables node

See [Page Variables](/smart/project-page-services-designer-guide/page-variables-node) node documentation.

#### Create Page Variables in the Script node

To create page variables on the [Script](/smart/project-page-services-designer-guide/script-node) node, perform the following steps:

1. Drag and drop a **Script** node.
2. In the **Code Editor**, add the code to create one or more variables. If a variable exists, its value will be updated, else a new variable will be created. For example:Copy CodeJavaScriptpage.ApiURL='http://localhost:24483/';
   page.city='Goa';
