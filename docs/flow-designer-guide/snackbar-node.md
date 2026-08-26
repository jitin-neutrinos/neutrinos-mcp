# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/snackbar-node>

This is the default topic template.

The **Snackbar **node is used to display snack bar notifications on the page UI. Snack bars provide brief messages about app processes. They inform users of a process that an app has performed or will perform. They appear temporarily and do not interrupt the user experience.

### Node Properties

- **Name:** The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **SnackBar Message: **The message to be displayed on the snack bar. Choose String and enter the message. Or, map the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) that contains the message.
- **Action Text: **The label for the snack bar action. Choose String and enter the action text. Or, map the variable that contains the action text.
- **Snackbar Duration: **The length of time in milliseconds to wait before automatically dismissing the snack bar. You can input a number, or map the variable that contains the duration.
- **Horizontal Position:** The horizontal position to place the snack bar. You can:
  - Choose an option from the drop-down list. Options include start, end, center, left, and right. By default, the snack bar is positioned from left to right. You can disable the **Left to Right** toggle button to reverse this positioning.
  - You can also click the **Map** icon and map the variable that contains the position value.
- **Vertical Position:** The vertical position to place the snack bar. You can:
  - Choose the **Vertical Position** from the drop-down list. Options include **Top** and **Bottom**.
  - Or, click the **Map** icon and map this field to a variable that contains the position value.
- **Custom Class List:** A comma (,) separated list of custom CSS classes to change the default appearance of the snack bar. Choose String and enter the custom classes or map the flow variable that contains these classes. Before you enter the class names, define the classes in the [Styles editor](/smart/project-sample-how-to-guide/apply-global-styling).
