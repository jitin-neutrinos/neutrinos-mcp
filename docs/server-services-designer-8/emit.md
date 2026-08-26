# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/emit>

The **Emit node** allows you to emit an event from anywhere in the app. You use the [Listen node](/articles/server-services-designer-8/listen) to listen to the event.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.4.0. |
| --- | --- |

### How to use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- On the Nodes Palette, search for the node. It is listed under the **Events **section. Drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Event Name:** The name of the event/topic the node should emit. Choose String and enter the key directly, or map the key-value to the [flow property](/smart/project-service-designer-user-s-guide/service-designer-variables) or an **environment** property and enter the variable name. The variable name that you map should contain the name of the event/topic.
