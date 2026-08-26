# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/call-service-node>

The **Call Service node** is used to call an existing flow in Server Services.

### How to Use

- Open the Services editor window.
- Click the **plus** icon to add a new server-service or open an existing server-service from the service list.
- In the Nodes Palette, drag and drop a **Call Service **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

### 

- **Name**: Unique name for the node. This name will display on the canvas when you save the node.
- **Service: **Choose a server service that you want to call from the drop-down list.
- **Flow Name: **Choose the flow that you want to call in the service that you selected in the **Service **field.

If you have enabled the **Accept flow object **toggle button in the **Start **node of the flow that you are calling, you will see a text that displays sending the flow object.

![Start node with flow object](/resources/Storage/server-services-designer-8/cs_3.png)![call service using flow object](/resources/Storage/server-services-designer-8/cs_4.png)

If you did not enable the toggle button in the Start node of the flow that you are calling, then you can define input and output properties in this node.

- **Input/Output properties:** Based on the service that you select, the **Call Service** node displays all the bh. properties that you would have created in the called service and auto-fills the **Key** field. In the **Value** field, you can select the following property type and then enter the property name.

![Start node with input property](/resources/Storage/server-services-designer-8/cs_1.png)![call service node with input parameters](/resources/Storage/server-services-designer-8/cs_2.png)
