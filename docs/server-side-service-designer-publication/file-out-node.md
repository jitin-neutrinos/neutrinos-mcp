# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/file-out-node>

The** File Out **node is used to write the data saved in the **File Data Mapping** field to a file. The data can be written either by creating the file, adding content to the end of the file or by replacing the file content.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **File Out **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or an **HTTP In **node.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.![file out properties](/resources/Storage/server-side-service-designer-publication/fileoutnew.png)
- **File Path: **The path of the file that you want to write to. Enter the path of the file and you can map it to string or local and input parameters. Options include:
  - **String: **Specify the path of the file that you want to modify. For example: **C:\Users\admin\Pictures\Screenshots\filein.txt**. The filename should be an absolute path.
  - **bh.input:** Specify the input parameter that holds the path of the file that you want to modify.
  - **bh.local: **Specify the local parameter that holds the path of the file that you want to modify.
  - **bh.**: Specify any bh. parameter that holds the file path.

See [Properties](/articles/server-side-service-designer-publication/properties-in-server-services) to learn more about these parameters.

- **File data Mapping: **The bh., bhinput, or bh.local parameter which has the data that you want to write to the file.
- **Create directory:** Toggle this button if you want to create a new file and add content to it. This option will also create the complete directory path provided in the **File Path** field if it does not exist.
- **Overwrite:** Toggle this button if you want to overwrite an existing file. If the file does not exist, a new file will be created in the specified path.
- **Streaming**: If any node is sending a result in the form of stream datatype, then toggle this field. Refer [Stream](https://nodejs.org/docs/latest/api/stream.html) documentation to learn more.
- **Append EOL: **Enable the toggle button to append an **End Of Line(EOL)** character at the end of the file. This field will not appear when the** Streaming** field is enabled.

![Information](/resources/Storage/server-side-service-designer-publication/info.png)

 If you do not choose **Create Directory**, **Overwrite**, or **Append EOL** operations, and if the file specified in the **File Path** field exists, then the data gets added at the end of the file. If the file does not exist, a new file will be created by default.If you enable the **Create Directory**, **Overwrite**, and **Append EOL** operations, and if the file specified in the **File Path** field exists, then the data gets overwritten. If the file does not exist, a new file will be created.

- **Encoding:** Choose the type of encoding that you want to apply to the file from the drop-down lists.

### Example

See [Working with Parsers](/smart/project-how-to-articles/working-with-data-formats).
