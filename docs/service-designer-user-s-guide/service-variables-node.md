# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/service-variables-node>

The **Service Variable** node is used to set and get service variables of the flow. These variables are used to store data that can be accessed outside the flow without executing the flow.

### How to Use

- Open the Services editor window.
- Click the** plus **icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Service Variables** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a start node.
- After the flow is created, import the service flow to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

1. **Name****: **The name of the node. This name will display on the canvas when you save the node.
2. **Operation Type: **The type of operation the node should perform.

**Set service variables:** Use this option to set service variables of your flow to any value.**Get service variables**: Use this option to get service variables of your flow and assign it to flow properties.

3. **Variables list**: Displays the list of variables added for the particular operation type.Enter the service variable name.Map the variable to a bh.input or bh.local property, or a **string **value, or choose **as is** and enter a variable name.Click the** plus** icon to add the variable to the list.
