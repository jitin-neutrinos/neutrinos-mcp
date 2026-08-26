# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/path-node>

The **Path **node provides methods to work with files and directories.

| ![](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.6.0.    You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**Path**** node**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Method:** The action that the node should perform**. **
  1. **Base Name: **Returns the last portion of the path. For example, if the path for this method is /foo/bar/baz/asdf/quux.html, then the method will return quux.html as the result.
    - **Extension**: Enter the optional file extension.
  2. **Directory name: **Returns the directory name of the path. For example, if the path is /foo/bar/baz/asdf/quux, then the method will return /foo/bar/baz/asdf as the result.
  3. **Extension name:** Returns the extension of the path. For example, if the path is index.html, then the method will return .html as the result.
  4. **Format: **Returns a path string from an object.
    - **Path Object**: Define the path in the script node of the flow and enter the object name in this field.
  5. **Absolute: **Determines if the path is an absolute path or not.
  6. **Join: **Joins all the given path segments together using separators like delimiter and then normalizes the resulting path. For example, if the given path is '/foo', 'bar', 'baz/asdf', 'quux', '..', then this method will return /foo/bar/baz/asdf as the result.
    - **Path Array**: Enter the array of paths. Define the array in the script node and mention the object name in this field.
  7. **Relative:** Returns the relative path from source to destination based on the current working directory.
    - **Source: **Enter the **from** path.
    - **Destination:** Enter the **to **path.
  8. **Normalize: **Normalizes the given path by eliminating ".." or "." segments. For example, if the given path is /foo/bar//baz/asdf/quux/.., then this method will return /foo/bar/baz/asdf as the result.
  9. **Parse: **Returns an object whose properties represent significant elements of the path. For example, if the given path is C:\\path\\dir\\file.txt, then this method will return the following result:
  10. **Resolve:** Resolves a sequence of path or path segments to an absolute path. The given path is processed from right to left until the absolute path is constructed. For example, if the given segments are /foo, /bar, baz, then this method will return /bar/baz as the result.
    - **Path Array**: Enter the array of paths. Define the array in the script node and mention the object name in this field.
  11. **Namespaced Path:** Returns an equivalent namespaced-prefixed path for the given path. If the path is not a string, the path will be returned without any modifications. This method works only on the Windows system.
4. **Path:** Enter the path on which the method is to be performed. This field does not appear if you select **Relative **as the method in the **Method **field.
5. ** Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of the methods.
