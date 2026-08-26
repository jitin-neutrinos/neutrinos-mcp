# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/soap-node>

SOAP is a messaging protocol specification for exchanging structured information in the implementation of web services in computer networks. Its purpose is to provide extensibility, neutrality, verbosity, and independence.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available from Neutrinos Studio Release 7.3.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**SOAP node**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **SOAP Config**: The name of the config.
  - If you have a Soap config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new Soap config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new Soap config. See [Attributes for a new Soap Config](/articles/server-side-service-designer-publication/soap-node/a/soapconfig) to know what are the properties to configure.
4. **Services**: The service that is uploaded in the WSDL file. This field gets auto-filled when you select the Soap Config.
5. **Service ****Versions**: Select the version of the service from the drop-down list.
6. **Operations**: Select the operations that are available for the selected service from the drop-down list.
7. **Operation**** Parameters**: The parameters for the operations. Depending on the type of operation that you select, the parameters are dynamically generated.
8. **Options**
  - **Authentication Type**: The type of authentication you want to use.
    - **Basic Auth**
    - **Token**
      - **Token: **Enter the token to authenticate your config.
  - **Auth Config**: The name of the Authentication config.
    - **Username**: Username for the authentication.
    - **Password**: Password for the authentication.
  - **Other Options**: Additional options that you want to add to the service.
  - **Extra Headers: **Set of extra headers of the service. These headers accept pairs of names and their corresponding values as key-value pairs. Map this field to bh.local, bh, bh.input or string properties, and input the variable name.
9. **Result Mapping**: Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

### Attributes for a new Soap Config

- **Name**: The name of the config.
- **WSDL File: **Upload a WSDL file. A WSDL file is an XML format file that describes a network service as a set of endpoints.
- **XSD File**: Upload an XSD File for your Soap config. An XSD file is used to define what elements and attributes may appear in an XML document. XSD files are the supporting files for the WSDL file.
- **Use Url**: Toggle this to use the URL for the WSDL file.
- **WSDL Url**: Enter the URL where the WSDL file is hosted.
