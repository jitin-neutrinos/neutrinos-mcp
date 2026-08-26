# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/uuid-node>

UUID node is used to generate random UUIDs for the objects.

### Associated Attributes

1. **Name**: The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Operation**: Select the type of operation the node should perform.
  1. Nil: Nil UUID string. All the digits in the UUID will be zeros.
  2. **Parse:** Converts UUID string to an array of bytes.
    - **UUID**: Enter the UUID that has to be converted into an array of bytes.
  3. **Stringify: **Converts array of bytes to a UUID string.
    - **UUID Bytes**: Enter the array of bytes that has to be stringified.
    - **Offset**: Enter the starting index of the array. The default value is 0.
  4. **V1: **Creates version 1 of the UUID.
    - **Options**: Additional options for this operation.
    - **Buffer: **To write a UUID in a byte-form starting at offset.
    - **Offset**: Enter the starting index of the array. The default value is 0.
  5. **V3: **Creates version 3 UUID.
    - **Namespace name**: Enter the name of the namespace specified.
    - **Namespace**: Enter the UUID or array of bytes generated.
    - **Buffer**: To write a UUID in a byte-form starting at offset.
    - **Offset**: Enter the starting index of the array. The default value is 0.
  6. **V4: **Create version 4 UUID.
    - **Options**: Additional options for this operation.
    - **Buffer**: To write a UUID in a byte-form starting at offset.
    - **Offset:** Enter the starting index of the array. The default value is 0.
  7. **V5: **Create version 5 UUID.
    - **Namespace name: **Enter the name of the namespace specified.
    - **Namespace: **Enter the UUID or array of bytes generated.
    - **Buffer: **To write a UUID in a byte-form starting at offset.
    - **Offset: **Enter the starting index of the array. The default value is 0.
  8. **Validate: **To see if the UUID is valid or not.
    - **UUID**: Enter the UUID that has to be validated.
  9. **Version: **To detect a version of a UUID.
    - **UUID**: Enter the UUID for which the version should be generated.
4. **Result Mapping: **Map the retrieved result to bh., bh.input, or bh.local properties. Select the parameter type and enter the variable that should holds the output. For example, if you specify bh.local.result in this field, then that local variable will hold the result.
