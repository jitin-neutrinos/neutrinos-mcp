# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/snackbar-node>

A **Snackbar** node is used to display snack-bar notifications. Snackbars provide brief messages about app processes on the screen. They inform users of a process that an app has performed or will perform. They appear temporarily and do not interrupt the user experience.

### How to Use

- Open the Services editor window.
- Click the** plus **icon to add a new service or open an existing service in the service list.
- From the Nodes Palette, drag and drop a **Snackbar** node to the service designer.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start** node.
- After the flow is created, import the service flow to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.
- **Snackbar Message: **The message to show in the snackbar. You can assign a string value, or map this field to bh.input or bh.local variables and enter the variable name which contains the snackbar message.

- **Action Text:** The label for the snackbar action. You can assign a string value, or map this field to bh.input or bh.local variables and enter the action label.
- **Snackbar Duration: **The length of time in **milliseconds** to wait before automatically dismissing the snackbar. You can input a number, or mapa bh.input or bh.local propety to a variable which contains the duration.
- **Horizontal Position:** The horizontal position to place the snack bar.
  - Choose the **Horizontal Position** from the drop-down list. Options include **start**, **end**, **center**, **left**, and **right**. The snackbar, by default, is positioned from left to right. You can use the **Left to Right** toggle button to reverse this positioning.
  - You can also map this field to a bh.input or bh.local variable and define the position by clicking the **Map** icon, selecting the property type, and entering the variable name which contains the value.
- **Vertical Position: **The vertical position to place the snack bar.
  - Choose the **Vertical Position** from the drop-down list. Options include **Top **and **Bottom**.
  - You can map this field to bh.input or bh.local variables and define the position by clicking the **Map** icon, selecting the property type, and entering the variable name which contains the value.
- **Custom Class List: **A comma (,) separated list fo custom classes to be assigned to the snackbar. You can assign a string value, or map this field to a bh.input or bh.local variable.
