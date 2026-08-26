# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/call-service-node>

A **Call Service** node is used to call an existing flow in the Client-side Services editor.

### How to Use

- Open the Services editor window.
- Click the plus icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Call Service **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with the Start node.
- After the flow is created, import the service to the application page. See [Import a service](/smart/project-sample-how-to-guide/import-client-services-to-the-page-ui) to learn more.

### Associated Attributes

- **Name**: Unique name for the node. This name will display on the canvas when you save the node.
- **Service: **Select the client service in the drop-down list from which you want to call the flow.** If you delete the client service in the future, you have to make sure that you manually update this field. Else your flow will break. **
- **Flow: **Select the flow which you want to call. **If you delete the flow in the future, you have to make sure that you manually update this field. Else your client service flow will break. **
- **Input/Output properties:** Based on the service flow that you select, the **Call Service **node displays all the properties that you would have created in the **Start** node of the called service and auto-fills the **Key** field. In the **Value** field, you can select the property type and then enter the variable name to which you want to map the input/output property. See [Properties](/articles/client-services-designer-9/service-designer-variables) to learn more.
