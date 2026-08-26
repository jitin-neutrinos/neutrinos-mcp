# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/mqtt-publish>

The **MQTT** **Publish** node is used to send a message to a topic in the MQTT broker.

If you send a message to a topic, the MQTT broker delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the protocol for each subscribed endpoint.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **MQTT Config: **The name of the config.
  - If you have an MQTT broker that is already configured, choose that config from the drop-down list.
  - If you want to configure a new MQTT broker, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for MQTT Configuration](/articles/server-services-designer-9/mqtt/a/h3_1457337614) to learn the properties to configure.
- **Topic: **The topic you want to publish to. Choose **string **from the drop-down list and enter the topic or map the topic to the bh. bh.input or bh.local property, and enter the variable name.
- **Message:** The message you want to send. Choose **string **from the drop-down list and enter the message or map the message to the bh. bh.input or bh.local property, and enter the variable name.
- **Option: **The options to publish the message with. See the [NPM documentation](https://www.npmjs.com/package/mqtt#publish) to learn about the options you can pass in this field. Choose **string **and define the options or map the options to the bh. bh.input or bh.local property, and enter the variable name. The variable name should be an object with the options defined.
