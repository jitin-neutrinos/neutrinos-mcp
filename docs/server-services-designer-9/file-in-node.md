# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/file-in-node>

The** File In **node is used to read the contents of a file. The file format can be **buffer**, **stream**, or **encoded**.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **File In **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or an **HTTP In **node**.**

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **File Path: **The path of the file that you want to read. The path of the file can be a string, an input parameter, or a local parameter.
  - **String: **Specify the path of the file you want to read. The filename should be an absolute path.
  - **bh.input:** Specify the input parameter that holds the file path. For example, if you specify bh.input.filepath in this field, the server-side service fetches the file path that is saved as the value of that parameter in the flow.
  - **bh.local: **Specify the local parameter that holds the file path. For example, if you specify bh.local.filepath in this field, the server-side service fetches the file path that is saved as the value of that parameter in the flow.
  - **bh.**: Specify any **bh.** parameter that holds the file path.

See [Properties](/articles/server-services-designer-9/properties-in-server-services) to learn more about the bh. property.

- **Format:** Choose the format in which you want to read the file. A file format can be **Buffer**, **Stream**, or **Encoded**. If you choose **Encoded** as your file format, a drop-down appears from where you can choose the type of encoding that is to be applied to the file.
    ![Information](/resources/Storage/server-services-designer-9/info.png)
    Encoding of the file can be specified only if the output format is **String**.
- **File Data Mapping: **The input or local parameter to which you want to pass the data of the file. For example, if you specify bh.input.result in this field, then that input parameter will hold the content of the file in the selected output format.

![Information](/resources/Storage/server-services-designer-9/info.png)


 Make sure that you have defined the input and local parameters in the flow before calling them from the **File Path** and **File Data Mapping** fields.

### Example

See [Working with Parsers](/smart/project-how-to-articles/working-with-data-formats).
