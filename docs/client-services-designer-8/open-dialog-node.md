# Node Properties

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/open-dialog-node>

The **Open Dialog **node is used to select the page which is to be displayed as a dialog window. This node also allows you to configure the appearance and behaviour of the dialog window.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Select a Page:** The page that is to be displayed as a dialog window.
- **Dialog Config:** The properties to configure the dialog window. You can define the properties in the field by using as is or string , or map the properties to the [page or flow variables](/smart/project-page-services-designer-guide/properties-page-designer) that hold the respective values. Configure the following properties.
  - Data: The data that is passed to the dialog window. This data can be an object, string, etc. For example, you can define bh.local.data in this field where bh.local.data is an object defined as below.

-
  - **Result Mapping:** Maps the response received from the dialog window to a flow or page variable after the dialog window gets closed. Select a flow or page property, and enter the variable name that should hold the value.
  - **Aria Described by: **The description to be assigned to the dialog window.
  - **Aria Label: **The label to be assigned to the dialog window. This indicates the ID of the element when the element is inspected. This is used internally by the dialog window and not displayed to the user. You can view the Aria Label of the Dialog window when you inspect the dialog window on Dev-tools.
  - **Aria Labelled By: **The ID of the component that labels the dialog window. This is used internally by the dialog window and not displayed to the user. You can view the Aria Labelled By value of the Dialog window when you inspect the dialog window on Dev-tools.
  - **Auto Focus: **This field decides weather the dialog window should focus the first focusable component on open. Set to True or False. Defaults to True.
  - **Backdrop Class: **The custom class which is to be used to style the backdrop when a dialog window is displayed. Define the class in the [Styles editor](/smart/project-sample-how-to-guide/apply-global-styling).
    - Choose string and enter the CSS class name in the field. Example - class1.
    - Choose as is and enter the array of classes that is to be applied to this field. Example - [class1, class2].
    - Choose page or bh properties and provide the name of the variable which holds the class name.

| ![Information](/resources/Storage/client-services-designer-8/info.png) | You can provide more than one class in this field. Note that Has Backdrop should be set to True for this class to take effect. |
| --- | --- |

- **Close on Navigation: **Whether the dialog window should close when the user goes backwards/forwards in history. Set to True or False.
- **Direction: **Whether the elements inside the dialog are right or left justified. The default is ltr (left-to-right) (ltr), but we can also specify rtl (right-to-left).
- **Disable Close:** Whether the user can use escape or clicking on the backdrop to close the modal. Set to True or False. Defaults to True.
- **Has Backdrop:** Whether the dialog has a backdrop. Set to True or False. If set to True, you can close the dialog window by clicking outside the dialog window.
- **Height:** The height of the dialog window.
- **Max Height:** The maximum height of the dialog window.
- **Min Height: **The minimum height of the dialog window.
- **Width: **The width of the dialog window.
- **Max Width: **The maximum width of the dialog window. Defaults to **80vw**.
- **Min Width:** The minimum width of the dialog window.
- **Panel Class:** The custom class which is to be used to style the overlay pane. Define the class in the [Styles editor](/smart/project-sample-how-to-guide/apply-global-styling).
  - Choose string and enter the CSS class name in the field. Example - panelclass1.
  - Choose as is and enter the array of classes that is to be applied to this field. Example - [panelclass1, panelclass2].
  - Choose page or bh properties and provide the name of the variable which holds the class name.
- **Position: **The position of the dialog window that you want to override. The dialog positions to override are - **bottom**, **top**, **left**, and **right**. Define the position of the dialog window in the [script](/smart/project-page-services-designer-guide/script-node) node and enter the variable which holds the value. For example, the position defined below overrides the bottom position and displays the dialog window 20 pixels above the bottom of the page:

```java
bh.local.position ={bottom: '20px',};
```

- **Restore Focus: **Whether the dialog should restore focus to the previously-focused element of the page, after it is closed. Set to True or False. Defaults to True.
- **Role: **The role of a dialog. The role of a dialog can be alertdialog or dialog. Where a dialog can be used in any scenario to display a dialog window, alertdialog should only be used when an alert, error, or warning occurs. In other words, when a dialog's information and controls require the user's immediate attention.

### Output Ports

This node has four output ports to transfer information from this node to another node.

![](/resources/Storage/client-services-designer-8/flow-designer-guide/open_dialog.png)

Output ports include:

- afterOpened: The event used to notify the user when the dialog window is finished opening.
- afterClosed: The event used to notify the user after the dialog window is closed.
- backdropClicked: The event used to notify the user when the overlay's backdrop has been clicked.
- beforeClosed: The event used to notify the user when the dialog has started closing.

The user can use these notifications to perform any action on the app.

#### Example

To learn how to work with dialog nodes, see [Display a Dialog Window on a Page](/smart/project-how-to-articles/display-a-dialog-window-on-a-page).
