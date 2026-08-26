# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/mqtt-subscribe>

The** MQTT Subscribe** node is used to subscribe to a topic or topics in the MQTT broker.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **MQTT Config: **The name of the config.
  - If you have an MQTT broker that is already configured, choose that config from the drop-down list.
  - If you want to configure a new MQTT broker, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for MQTT Configuration](/articles/server-services-designer-9/mqtt/a/h3_1457337614) to learn the properties to configure.
- **Topic: **The topic(s) you want to subscribe to. Choose **string **from the drop-down list and enter the topic name or map the topic to the bh. bh.input or bh.local property, and enter the variable name.
- **Option: **The options with which you want to subscribe to the topic(s). See the [NPM documentation](https://www.npmjs.com/package/mqtt#subscribe) to learn about the options you can pass to this field.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the received data.
