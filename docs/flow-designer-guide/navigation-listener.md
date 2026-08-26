# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/navigation-listener>

A **Zone **node is used to execute synchronous tasks inside and outside the angular zone. An Angular zone is an execution context that persists across async tasks. See Angular Zone documentation to learn more.

### Node Properties

1. **Name:** A unique name for the node. This name will display on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Operation Type: **Select the type of operation that the node should perform.
  - **All Parameters**:
  - **All Query Parameters**:
  - **Children**:
  - **First Child:**
  - **Fragment: **
  - **Get current Page:**
  - **Get Parent Route:**
  - **Get Static Data:**
  - **Individual Parameter:**
    - **Get all keys:**
    - **Get All Values of the Keys:**
      - **Key:**
    - **Get Key Value: **
      - **Key:**
    - **Is Key Exists:**
      - **Key:**
4. **Select a Page Flow:** Select a page flow that has to be executed.
5. **Result Mapping**:
