# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/xml-node>

The **XML node** is used to convert between an **XML string** and **Javascript object** representation, or in either way.

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **and add a new Server Service.
- In the Nodes Palette, drag and drop the **XML** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

1. **Name**: The name for the node. This name will display on the canvas when you save the node. ![The sttributes of xml node](/resources/Storage/server-services-designer-9/xml.png)
2. **Source**: The source of the XML string or javascript object.
  - **bh.input:** Specify the input parameter that holds the source. For example, if you specify bh.input.source in this field, the server-side service fetches the source that is saved.
  - **bh.local: **Specify the local parameter that holds the source. For example, if you specify bh.local.source in this field, the server-side service fetches the source that is saved. To learn more about input and local parameters, see [properties](/articles/server-side-service-designer-publication/properties-in-server-services) to know more.
3. **Attribute key**: Prefix value that is used to access the attributes. By default, the attribute key is "**$**".
4. **Character Key**: Prefix value that is used to access the character content. By default, the character key is "**_**"(underscore). For example, the following XML will be converted to javascript object: Copy CodeXML<p class="tag">Hello World</p> Copy CodeJavaScript{
    "p": {
    "$": {
    "class": "tag"
    },
    "_": "Hello World"
    }
   }
5. **Parse options**: This is an optional property that can be used to pass options that are used to convert to and from XML. This is done by creating an object in the script node and specifying the options inside the object created. Refer to this [link](https://www.npmjs.com/package/xml2js#options) and know the options that can be specified.
6. **Switch**: Toggle the switch to replace the source itself with the result else you can use the **Result Mapping **attribute to map the result.
7. **Result Mapping**: You can map the retrieved data to bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input parameter will hold the content of the file in the selected output format.

### Example

See [Working with Parsers](/articles/how-to-articles/working-with-data-formats) to view a similar example of working with a **YML** node. You can replace the** YML** node with a **CSV** node and create a similar flow to convert data from XML to JSON String format.
