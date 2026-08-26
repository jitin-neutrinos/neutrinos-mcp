# Attributes Associated

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/get-instance-node>

The **Get Instance** node returns the instance of the class that is exposed by the Nexmo npm package. It is used to access all the other functionalities provided by Nexmo, such as sending messages, that are not available as nodes on Server Services Designer.

See [Nexmo npm instance](https://www.npmjs.com/package/nexmo#constructor) to learn more.

### Attributes Associated

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name: ** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Nexmo Config: ** The name of the configuration that connects to the Nexmo Service APIs.
  - If you have an existing Nexmo configuration, choose that config from the drop-down list.
  - If you want to create a new Nexmo configuration, select **Add new config** from the drop-down list and click the **Map** icon to add a new configuration. See [Attributes for a new Nexmo Config](/articles/server-services-designer-8/communication/a/newnexmoconfig) to know what are the properties to configure.
4. **Result Mapping: **Map the data retrieved to the bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property **result** will hold the data retrieved from the database.
