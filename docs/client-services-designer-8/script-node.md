# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/script-node>

A **Script** node is used to write business logic depending on the app requirement. The logic is written in TypeScript in the TS editor of the Attributes window.

### How to Use

- Open the Services editor window.
- Click the** plus **icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Script **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow always starts with a **Start node.**
- After the flow is created, import the service to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Code Editor****: **Allows you to add the JavaScript code and write the business logic of the **Script** node.

For example:

- To call the function `greet` (with a string) and show a greeting message to the user, add this code: greet("hello world");
- To create or update a bh.local property named **modelrApiUrl** and link it to a URL, add this code:

bh.local.modelrApiUrl = 'http://localhost:24483/api/weather';

Add your business logic using the editor and click the ![](https://firebasestorage.googleapis.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LKzvFgTTOBWB9Q4L_jd%2F-LgRseO4bHq7Tw23db9B%2F-LgRxJ805PYlQ6b1u0Z-%2Ftick.png?alt=media&token=56d95525-d6fe-468b-ad27-eae7cac0ce85) button.
