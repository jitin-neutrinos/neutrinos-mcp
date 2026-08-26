# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/listen>

The **Listen node** allows you to listen to the event emitted by the [Emit node](/articles/server-services-designer-9/emit). It is a **s****tart **node, but does not initialize the .bh object. Instead, it accepts the .bh object from the** Emit **node.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Attributes Associated

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name: ** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Event Name:** The name of the event/topic the node should listen to. Choose String and enter the key directly, or map the key-value to the **environment** property and enter the variable name. The variable name that you map should contain the name of the event/topic.
