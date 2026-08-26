# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/open-dialog-node>

This is the default topic template.

The **Open Dialog **node is used to select the page which is to be displayed as a dialog window. This node also allows you to configure the appearance and behaviour of the dialog window.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Select a Page:** The page that is to be displayed as a dialog window.
- **Dialog Config:** The properties to configure the dialog window. You can define the properties in the field by using as is or string , or map the properties to the [page or flow variables](/articles/flow-designer-guide/properties-page-designer) that hold the respective values. Configure the following properties.
  - **Data:** The data that is passed to the dialog window. This data can be an object, string, etc. For example, you can define bh.local.data in this field where bh.local.data is an object defined as below. Copy CodeJavaScriptbh.local.data = {
      name: "Dialog Window"
     }
  - **Result Mapping:** Maps the response received from the dialog window to a flow or page variable after the dialog window gets closed. Select a flow or page property, and enter the variable name that should hold the value.

### Output Ports

This node has four output ports to transfer information from this node to another node.

Output ports include:

- afterOpened: The event used to notify the user when the dialog window is finished opening.
- afterClosed: The event used to notify the user after the dialog window is closed.
- backdropClicked: The event used to notify the user when the overlay's backdrop has been clicked.
- beforeClosed: The event used to notify the user when the dialog has started closing.

The user can use these notifications to perform any action on the app.

#### Example

To learn how to work with dialog nodes, see [Display a Dialog Window on a Page](/smart/project-how-to-articles/display-a-dialog-window-on-a-page).
