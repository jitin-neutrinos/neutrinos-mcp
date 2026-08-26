# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/yml-node>

The YML node is used to convert between a **YMl formatted ****string** and **Javascript object** representation, or in either way.

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- In the Nodes Palette, drag and drop the **JSON** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In **node.

### Associated Attributes

1. **Name**: The name for the node. This name will display on the canvas when you save the node.![YML node attributes](/resources/Storage/server-services-designer-9/YMl.png)
2. **Source**: The source of the JavaScript object or YML string.

- **bh.input:** Specify the input parameter that holds the source. For example, if you specify bh.input.source in this field, the server-side service fetches the source that is saved.
- **bh.local: **Specify the local parameter that holds the source. For example, if you specify bh.local.source in this field, the server-side service fetches the source that is saved. To learn more about input and local parameters, see [properties](/articles/server-side-service-designer-publication/properties-in-server-services) to know more.

3. **Switch**: Toggle the switch to replace the source itself with the result else you can use the **Result Mapping** attribute to map the result.

4. **Result mapping**: You can map the retrieved data to bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input parameter will hold the content of the file in the selected output format.

### Example

See [Working with Parsers](/articles/how-to-articles/working-with-data-formats).
