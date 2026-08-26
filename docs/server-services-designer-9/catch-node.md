# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/catch-node>

In a service flow, if a node throws an error while handling a message, the flow will typically halt. In such cases, you can use the **Catch **node to catch errors thrown by nodes on the same service.

If an exception occurs on the server, it returns HTTP Error 500 -Internal server error as the response to the client through the response object.

### How to Use

- Open the Services editor window.
- Click the **plus icon** to add a new server service or open an existing service from the service list.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.
- From the Nodes Palette, drag and drop a **Catch **node to the workspace and enable the node to catch exceptions on all nodes or specific nodes.

### Associated Attributes

- **Name**: Unique name for the node. This name will display on the canvas when you save the node.
- **Catch errors from: **A drop-down list with the following options.
- If you choose the **Selected nodes** option in the **Catch errors from** the drop-down list, the Server-side Service Designer allows you to manually choose the nodes on which you want to catch errors. Select the nodes manually by enabling the **Toggle** button.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | In a server flow, if the Catch node is not enabled for a node, its exception will be passed to its previous node in the flow. |
| --- | --- |

If a node throws an error, the catch node catches the **error** object which is available inside the bh.error property. See [Properties in Server-side Services](/articles/server-side-service-designer-publication/properties-in-server-services) to learn more about the error property.

You can also create a flow after the** Catch** node to send a response back to the client. For example:

![Catch with HTTP Out node](/resources/Storage/server-services-designer-9/catch_http.png)

You should make sure that you never enable exception handling for the nodes to the **Catch **node. For example, the HTTP Out node in the above screenshot. Catching the error of the node that is connected to the Catch node will result in an infinite recursion.
