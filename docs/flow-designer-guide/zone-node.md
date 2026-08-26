# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/zone-node>

A **Zone **node is used to execute synchronous tasks inside and outside the angular zone. An Angular zone is an execution context that persists across async tasks. See Angular Zone documentation to learn more.

### Node Properties

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.

- **Operation Type: **Select the type of operation that the node should perform.
  - **Run**: Executes the flow synchronously within the angular zone and returns the result value.
  - **Run Task**: Executes the flow synchronously within the angular zone as a task and returns the result value.
  - **Run Guarded**: Executes the flow synchronously while catching errors and returns the result value with errors if any.
  - **Run Outside Angular**: Executes the flow synchronously outside the angular zone and returns the result value.
- **Select a Page Flow:** Select a page flow that has to be executed.
