# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/zone-node>

A **Zone **node is used to execute synchronous tasks inside and outside the angular zone. An Angular zone is an execution context that persists across async tasks. See [Angular Zone](https://angular.io/guide/zone) documentation to learn more.

### How to Use

- Open the Services editor window.
- Click the** plus **icon to add a new service or open an existing service in the service list.
- From the Nodes Palette, drag and drop a **Zone **node to the service designer.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start** node.
- After the flow is created, import the service flow to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.
- **Function Name: **This is a read-only field. The function name gets generated based on the label name that you enter in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.

- **Operation Type: **Select the type of operation that the node should perform.
  - **Run**: Executes the flow synchronously within the angular zone and returns the result value.
  - **Run Task**: Executes the flow synchronously within the angular zone as a task and returns the result value.
  - **Run Guarded**: Executes the flow synchronously while catching errors and returns the result value with errors if any.
  - **Run Outside Angular**: Executes the flow synchronously outside the angular zone and returns the result value.
- **Select a Client Flow: **Select a client flow to be executed.
