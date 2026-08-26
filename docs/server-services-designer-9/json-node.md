# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/json-node>

The **JSON node** is used to convert between a **JSON string** and **Javascript object** representation, or in either way.

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- In the Nodes Palette, drag and drop the **JSON** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

1. **Name:** The name for the node. This name will display on the canvas when the node is saved. ![Json node](/resources/Storage/server-services-designer-9/json_node.png)
2. **Source:** The source of the JavaScript object or JSON string. Select a parameter type and enter the source.This name will display on the canvas when you save the node.
  - **bh.input:** Specify the input parameter that holds the source. For example, if you specify bh.input.source in this field, the server-side service fetches the source that is saved.
  - **bh.local: **Specify the local parameter that holds the source. For example, if you specify bh.local.source in this field, the server-side service fetches the source that is saved. To learn more about input and local parameters, see [properties](/articles/server-services-designer-9/properties-in-server-services) to know more.
3. **Switch:** Toggle the switch to replace the source itself with the result else you can use the result mapping to map the result.
4. **Result Mapping:** You can map the retrieved data to bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input parameter will hold the content of the file in the selected output format.

### Example

See [Converting JSON Object to JSON String](/smart/project-how-to-articles/working-with-data-formats).
