# How to use

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/on-online-node>

The **On** **Online** node is used to listen to the internet events when the application gains network.

### How to use

1. On the Client services editor, Open an existing service from the service list or click the** plus icon **to add a new Client Service.
2. Select** Plugins**** > Manage Plugins** on the top menu.
3. Search for **Internet** nodes. Select the plugin and click **Add**.
4. On the [Nodes Palette](/articles/client-services-designer-8/palette), you will see a new section called **Internet** with the [internet nodes](/articles/client-services-designer-8/internet-nodes) listed under it.
5. Drag and drop the node with other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field.

### Example

Let's see an example of displaying a snackbar message when online.

This is the simple flow created:

Here the **On Online** node is connected to a **Snackbar** node which displays a **You are online** message.
