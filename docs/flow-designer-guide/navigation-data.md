# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/navigation-data>

A **Zone **node is used to execute synchronous tasks inside and outside the angular zone. An Angular zone is an execution context that persists across async tasks. See Angular Zone documentation to learn more.

### Node Properties

1. **Name:** A unique name for the node. This name will display on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Operation Type: **Select the type of operation that the node should perform.
  1. **All Parameters**
  2. **All Query Parameters**:
  3. **Children**:
  4. **First Child:**
  5. **Fragment:**
  6. **Get current Page:**
  7. **Get Parent Route:**
  8. **Get Static Data:**
  9. **Individual Parameter:**
    1. **Get all keys:**
    2. **Get All Values of the Keys:**
      1. **Key:**
    3. **Get Key Value:**
      1. **Key:**
    4. **Is Key Exists:**
      1. **Key:**
4. **Result Mapping:**
