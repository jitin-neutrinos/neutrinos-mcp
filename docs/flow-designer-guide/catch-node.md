# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/catch-node>

If a node throws an error while handling a message, the flow will typically halt. In such cases, you can use the **Catch **node to catch errors thrown by nodes on the same service.

If an exception occurs on the server, it returns HTTP Error **500 -Internal server error** as the response to the page through the response object (the information sent from the server as a result of the client's request).

### Node Properties

- **Name**: The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **Catch errors from: **A drop-down list with the following options.
  - **All nodes: **Apply the **Catch** node to all the nodes in the canvas.
  - **Selected nodes: **Apply the **Catch** node to selected nodes that are present on the canvas. If you choose this option, you can manually choose the nodes for which you want to catch errors by enabling the **Toggle** button.

If a node throws an error, the catch node catches the error object and stores it in the bh.error property. See [Properties](/articles/flow-designer-guide/properties-page-designer) to learn more about the bh.error property.

| ![Information](/resources/Storage/flow-designer-guide/project-service-designer-user-s-guide/info.png) | In a flow, if an exception occurs on the node for which the catch node is not enabled, its exception will be passed to its previous node in the flow. |
| --- | --- |
