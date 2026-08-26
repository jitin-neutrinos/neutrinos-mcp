# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/uuid-node>

The UUID (universally unique identifier) node is used to generate random UUIDs for the objects.

It is a 128-bit number used to identify information in computer systems. When generated according to the standard methods, UUIDs are, for practical purposes, unique. UUIDs are generally used for identifying information that needs to be unique within a system or network thereof. Their uniqueness and low probability of being repeated make them useful for being associative keys in databases and identifiers for physical hardware within an organization.

| ![](/resources/Storage/server-services-designer-8/info.png) | This node is a common node across the Server Services Designer and Client Services Designer.This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services/Client Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**UUID**** node**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Operation:** Select the type of operation the node should perform.
  1. **Nil: **Nil UUID string. All the digits in the UUID will be zeros.
  2. **Parse:** Converts UUID string to an array of bytes.
    - **UUID**: Enter the UUID that has to be converted into an array of bytes.
    - For example, if the given UUID is **6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b **then the parsed UUID will be in the following format:
    - Copy CodeMarkdown[
       '6e', 'c0', 'bd', '7f',
       '11', 'c0', '43', 'da',
       '97', '5e', '2a', '8a',
       'd9', 'eb', 'ae', '0b'
       ]
  3. **Stringify: **Converts array of bytes to a UUID string.
    - **UUID Bytes**: Enter the array of bytes that has to be stringified.
    - **Offset**: Enter the starting index of the array. The default value is 0.
    - For example, if the given string is as below, then the result will be **6ec0bd7f-11c0-43da-975e-2a8ad9ebae0b**.
    - Copy CodeMarkdownuuidBytes = [
        0x6e,
        0xc0,
        0xbd,
        0x7f,
        0x11,
        0xc0,
        0x43,
        0xda,
        0x97,
        0x5e,
        0x2a,
        0x8a,
        0xd9,
        0xeb,
        0xae,
        0x0b,
       ];
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
4. **Result Mapping: **Map the retrieved result to bh., bh.input, or bh.local properties. Select the parameter type and enter the variable that should holds the output. For example, if you specify bh.local.result in this field, then that local property will hold the result.
