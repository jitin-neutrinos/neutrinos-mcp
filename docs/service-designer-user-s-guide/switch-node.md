# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/switch-node>

A **Switch node** allows you to define conditions and make your flow take different paths based on the conditions that you define.

### How to Use

- Open the Services editor window.
- Click the plus icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Switch **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a Start node.
- After the flow is created, import the service to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

![Switch node properties](/resources/Storage/service-designer-user-s-guide/switch_prop.png)

- **Name:** Unique name for the node. This name will display on the canvas when you save the node.
- **Property:** The property which you want to evaluate against the conditions that you specify using the conditions field. Map to input or local parameters and enter the property name. See [Properties](/articles/service-designer-user-s-guide/service-designer-variables) to learn more.
- **Conditions:** A list of conditions that have to be evaluated against the property mentioned in the property field. The conditions list includes:
  - Select the condition. For example: is null, ==)
  - Select the type of property. For example, .bh, number
  - Enter the value to check for the condition.

Use the **+ Add **button to add a new condition.

Use the drop-down list at the bottom of the attribute window to choose if you want to **check all the conditions** or **stop after the first match**.
