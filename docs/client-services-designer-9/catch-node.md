# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/catch-node>

In a service flow, if a node throws an error while handling a message, the flow will typically halt. In such cases, you can use the **Catch **node to catch errors thrown by nodes on the same service.

If an exception occurs on the server, it returns HTTP Error **500 -Internal server error** as the response to the client through the response object.

### How to Use

- Open the Services editor window.
- Click the **Add Service** button to add a new service or open an existing service.
- In the Nodes Palette, drag and drop a **Catch **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node**.
- After the flow is created, import the service flow to an app page. See [Import a service flow](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name**: Unique name for the node. This name will display on the canvas when you save the node.
- **Catch errors from: **A drop-down list with the following options.
  - **All nodes: **Apply the **Catch** node to all the nodes in the canvas.
  - **Selected nodes: **Apply the **Catch** node to selected nodes that are present on the canvas.
- If you choose the **Selected nodes** option in the **Catch errors from** the drop-down list, the Service Designer allows you to manually choose the nodes for which you want to catch errors. Select the nodes manually by enabling the **Toggle** button.

If a node throws an error, the catch node catches the error object. This error object is available inside the bh.error property. See [Properties](/articles/service-designer-user-s-guide/service-designer-variables) to learn more about the bh.error property.

| ![Information](/resources/Storage/client-services-designer-9/info.png) | In a flow, if an exception occurs on the node for which the catch node is not enabled, its exception will be passed to its previous node in the flow. |
| --- | --- |

If a node throws an error, the catch node catches the **error** object which is available inside the bh.error property. See [Properties in client Services](/articles/client-services-designer-9/service-designer-variables) to learn more about the error property.
