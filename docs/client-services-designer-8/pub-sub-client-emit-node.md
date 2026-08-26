# How to use

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/pub-sub-client-emit-node>

The **Emit node** allows you to emit an event from anywhere in the app. You use the [Listen node](/smart/project-server-side-service-designer/listen) to listen to the event.

| ![Information](/resources/Storage/client-services-designer-8/project-server-side-service-designer/info.png) | This node is available from Neutrinos Studio Release 7.5.0. |
| --- | --- |

### How to use

- Open the **Client** **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- On Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- On the Nodes Palette, search for the node. The node is listed under the **Events** section. Drag and drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/client-services-designer-8/call-service-node) node.
3. **Event Name:** The name of the event/topic that the node should emit. Choose String and enter the key directly, or map the key-value to the [flow property](/articles/client-services-designer-8/service-designer-variables) or an **environment** property and enter the variable name. The variable name that you map should contain the name of the event/topic.
