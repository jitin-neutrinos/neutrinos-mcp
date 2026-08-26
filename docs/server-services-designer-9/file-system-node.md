# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/file-system-node>

File system node enables you to interact with the file system. It is responsible for all the asynchronous or synchronous file operations.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.3.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**File Operations**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Asynchronous:** Check this field if you want the node to work asynchronously.
4. ** Operation: **Select the type of operation the node should perform.
  - **Delete:** Deletes files and directories.
  - **Copy:** Copies files and directories.
    - **Destination**: Enter the destination path to where the file or the directory should be copied to.
    - **Options**: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
  - **Move: **Moves the data of one file to another.
    - **Destination**: Enter the destination path to where the file or the directory should be moved to.
    - **Options**: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
  - **Write JSON: **Writes an object to a JSON file.
    - **Options**: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
    - **Data**: The data which you want to write to the JSON file.
  - **Read JSON:** Reads a JSON file.
    - **Options: **The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
  - **Output JSON: **This operation is the same as the **Write Json ****operation, **except that if the directory does not exist, then the directory is created.
    - **Options**: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
    - **Data**: The data which you want to output in the JSON file.
  - **Empty Directory: **Ensures that a directory is empty. Deletes directory contents if the directory is not empty.
  - **Ensure File:** Ensures that the file exists. If the file that is requested to be created is in directories that do not exist, these directories are created.
  - **Ensure Directory: **Ensures that the directory exists. If the directory structure does not exist, it is created.
    - Options: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
  - **Ensure Link: **Ensures that the link exists. If the directory structure does not exist, it is created.
    - Destination: Enter the destination of the directory to which the link should be ensured.
  - **Output File:** Same as Write File, except that if the parent directory does not exist, it's created.
    - **Options**: The optional settings that you can perform for this operation. Map the options to bh. or bh.local properties and specify the variable name.
    - **Data**: The data which you want to output file.
  - **Path Exists:** To check if the given path exists by checking with the file system.
5. **Src: **Enter the source of the file or the directory.
6. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.
