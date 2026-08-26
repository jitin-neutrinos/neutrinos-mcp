# Attributes Associated

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/get-call-recording-node>

The **Get Call Recording** node allows you to get details of the call that is placed.

### Attributes Associated

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name: ** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Nexmo Config: ** The name of the configuration that connects to the Nexmo Service APIs.
  - If you have an existing Nexmo configuration, choose that config from the drop-down list.
  - If you want to create a new Nexmo configuration, select **Add new config** from the drop-down list and click the **Map** icon to add a new Nexmo configuration. See [Attributes for a new Nexmo Config](/articles/server-services-designer-9/communication/a/newnexmoconfig) to know what are the properties to configure.
4. **File Id/URL: **Enter the file id or the URL from where the call recording should be fetched after creating a call.
5. **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

Refer [https://developer.nexmo.com/api/voice#getCall](https://developer.nexmo.com/api/voice#getCall) to learn about the responses.
