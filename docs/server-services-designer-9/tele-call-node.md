# Attributes Associated

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/tele-call-node>

The **Tele Call** node is used to make calls using Phone numbers.

### Attributes Associated

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name: ** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Nexmo Config: ** The name of the configuration that connects to the Nexmo APIs.
  - If you have an existing Nexmo configuration, choose that config from the drop-down list.
  - If you want to create a new Nexmo configuration, select **Add new config** from the drop-down list and click the **Map** icon to add a new configuration. See [Attributes for a new Nexmo Config](/articles/server-services-designer-9/communication/a/newnexmoconfig) to learn about the properties to configure.
4. **From: **Enter the Phone number from which the call should be made.
5. **To: **Enter the Phone number to which the call should be made.
6. **NCCO:** Enter the Nexmo Call Control Object(NCCO) to use for this call. See [https://developer.nexmo.com/voice/voice-api/ncco-reference](https://developer.nexmo.com/voice/voice-api/ncco-reference) to learn more.
7. **Result Mapping: **Map the response of the API call to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result.

See [https://developer.nexmo.com/api/voice#createCall](https://developer.nexmo.com/api/voice#createCall) to view different responses of this API call.
