# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/switch-node>

The **Switch node** allows you to define conditions and make your flow take different paths based on the conditions that you define.

### How to Use

- Open the Services editor window.
- Click the plus icon to add a new service or open an existing service from the service list.
- In the Nodes palette, drag and drop a **Switch **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with the **Start node **or an **HTTP In node.**

### Associated Attributes

![Switch node properties](/resources/Storage/server-services-designer-8/service-designer-user-s-guide/switch_prop.png)

- **Name:** Unique name for the node. This name will display on the canvas when you save the node.
- **Property:** The property which you want to evaluate against the conditions that you specify in the conditions field. Enter the property and you can map it to bh.input or bh.local properties. See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more.
- **Conditions:** A list of conditions that have to be evaluated against the property mentioned in the property field. The conditions list includes:
  - The condition. For example: is null, ==)
  - The type of property. For example: .bh, number),
  - The value.

Use the **+ Add** button to add a new condition.

Use the drop-down list at the bottom of the attribute window to choose if you want to **check all the conditions** or **stop after the first match**.
