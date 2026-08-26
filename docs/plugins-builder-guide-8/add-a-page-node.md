# Example

<https://documentation.neutrinos.com/articles/#!plugins-builder-guide-8/add-a-page-node>

| ![Information](/resources/Storage/plugins-builder-guide-8/info.png) | Before you add a node, learn about the [types of nodes](/smart/project-concepts/node/a/h3__1155479691) in Neutrinos Studio. |
| --- | --- |

To add a page node that can be used to create page flows:

1. Expand **Nodes** and click the plus icon next to the **page **option.
    ![Add a page node](/resources/Storage/plugins-builder-guide-8/page_pb1.png)
2. Enter the name of the node that you want to create and press the **Enter **button. Make sure you name the node based on its functionality. The node gets added under the pages section. Expand the node to view the editors that you can use to customize the node.
    ![Adding a node name](/resources/Storage/plugins-builder-guide-8/page_pb2.png)
3. Enter the [node details](/articles/plugins-builder-guide-8/node-details).
4. Define the [node attributes](/articles/plugins-builder-guide-8/node-attributes).
5. Add the [node dependencies](/articles/plugins-builder-guide-8/node-dependencies).
6. Define the [code generation](/articles/plugins-builder-guide-8/code-generation) logic.
7. [Publish](/articles/plugins-builder-guide-8/publish-the-node-package) the node package to test the node in the respective designer.
8. [Export to Production Publish](/articles/plugins-builder-guide-8/export-for-production-publish) to send the node to Neutrinos.

### Example

Let us look at an example of creating a page node called **Emit**. When you are [reusing the Page UI](/smart/project-sample-how-to-guide/views) as **Views** on Studio, this node is added to the child page (the view that is reused) to emit an event and send some data to the parent page.

Perform the following steps:

1. Open Plugins Builder by clicking **Plugins > Plugin Builder** on the top menu of the Studio page.
2. Click **Packages > Package Details** and enter the details of the package:
  1. Display name: **Emit**
  2. Version: **1.0.0**
  3. Generated package name: **neutrinos-emit. Make sure that the package name is unique.** Else, you will not be able to upload the package to Neutrinos Store.
3. Expand **Nodes** and click the plus icon next to the **page **option.
4. Enter the name of the node as **Emit** and press the **Enter **button. The node gets added under the pages section. Expand the node to view the editors to customize the node.
5. Open the **Node Details** editor and enter the following details. See  [node details](/articles/plugins-builder-guide-8/node-details) to learn more about each field.
    ![Emit node details](/resources/Storage/plugins-builder-guide-8/emit_node_details.png)
6. Open the **Node Attributes** editor and define the node details. See [node attributes](/articles/plugins-builder-guide-8/node-attributes) to learn about the fields to configure. The Emit node has two fields:
  1. Event Name - The event using which you will emit the data.
  2. Data - The data to be sent to the parent page.
7. The configuration of both the fields look like this:
    ![Event Name - Node attributes](/resources/Storage/plugins-builder-guide-8/emit_node_attr.png)
    ![date - attributes](/resources/Storage/plugins-builder-guide-8/emit_node_attr2.png)
8. Add [node dependencies](/articles/plugins-builder-guide-8/node-dependencies) if any. This node has no dependencies.
9. Define the [code generation](/articles/plugins-builder-guide-8/code-generation) logic. Here, the logic is written to validate the data assigned to the node. If the data is present, it is emitted. Else, no data is emitted by the node and it is assigned a NULL value internally.
    ![Code generation of Emit node](/resources/Storage/plugins-builder-guide-8/emit_codegen.png)
10. Save the changes and click** Publish this Package** on the Plugins Builder to publish the package locally and test its working.
    ![Publishing the node package locally](/resources/Storage/plugins-builder-guide-8/publish_package.png)
11. Import the node to an application using the Plugins Manager.
    ![Add the plugin to an app](/resources/Storage/plugins-builder-guide-8/emit_add_plugin.png)
12. Test the appearance of the node and its attributes window on the Flow designer. Also, test it's working by creating page flows.
    ![Using the Emit node in a page flow](/resources/Storage/plugins-builder-guide-8/image.png)
    ![Attributes of the Emit node](/resources/Storage/plugins-builder-guide-8/emit_attr.png)
13. Fix errors (if any).
14. After thoroughly testing the working of the node, click **Export for Production Publish** on the Plugins Builder and create the node package. See [Export for Production Publish](/articles/plugins-builder-guide-8/export-for-production-publish) to learn more.
