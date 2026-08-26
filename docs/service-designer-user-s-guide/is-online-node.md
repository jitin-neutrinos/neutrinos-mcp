# How to use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/is-online-node>

The **is****Online** node is used to return a boolean value indicating the status of the network. True indicates that the network is available and False indicates that the network is not available.

| ![Warning](/resources/Storage/service-designer-user-s-guide/warning.png) | This event shouldn't be used to determine the availability of a particular website. Network problems or firewalls might still prevent the website from being reached. |
| --- | --- |

### How to use

1. On the Client services editor, Open an existing service from the service list or click the** plus icon **to add a new Client Service.
2. Select** Plugins**** > Manage Plugins** on the top menu.
3. Search for **Internet** nodes. Select the plugin and click **Add**.
4. On the [Nodes Palette](/smart/project-concepts/palette/a/h4__1538579060), you will see a new section called **Internet** with the [internet nodes](/articles/service-designer-user-s-guide/internet) listed under it.
5. Drag and drop the node with other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field.
3. **Result Mapping:** The result of the event. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)in which you want to save the result. Example:![](/resources/Storage/service-designer-user-s-guide/online.PNG)

### Example

Let's see an example of displaying a snackbar message depending on the status of the network.

This is the simple flow created:

Here the **Is Online** node is connected to a **Snackbar** node which displays a **Connection found** message.
