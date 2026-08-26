# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/script-node>

The **Script node** is used to write business logic on the server. The logic is written in TypeScript in the TS editor of the Attributes window.

### How to Use

- Open the Services editor window.
- Click the **plus **icon to add a new service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **Script **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Code Editor****: **Allows you to add the JavaScript code and write the business logic.

For example:

- To call the function `greet` (with a string) and show a greeting message to the user, add this code: greet("hello world");
- To create or update a bh.local property named **modelrApiUrl** and link it to a URL, add this code:

bh.local.modelrApiUrl = 'http://localhost:24483/api/weather';

You can also use the bh. object in the editor to access all the properties. See [Properties](/articles/server-side-service-designer-publication/properties-in-server-services) for a complete list.

- Add your business logic in the editor and click the ![](/resources/Storage/server-side-service-designer-publication/correct.png) button.
