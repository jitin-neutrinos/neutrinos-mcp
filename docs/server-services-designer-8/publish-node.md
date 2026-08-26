# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/publish-node>

The AWS SNS** Publish** node is used to send a message to an Amazon SNS topic.

If you send a message to a topic, Amazon SNS delivers the message to each endpoint that is subscribed to the topic. The format of the message depends on the notification protocol for each subscribed endpoint.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Select AWS Config: **The name of the config.
  - If you have an Amazon config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new Amazon config, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for a new Amazon Configuration](/articles/server-services-designer-8/textract-node/a/h3_1541343129) to know what are the properties to configure.
- **TopicArn: **The Amazon Resource Name(ARN) of the topic you want to publish to.
- **Message: **The message you want to send. Choose **string **from the drop-down list and enter the message or map the message to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be an object with the parameters defined.
- **Message Attributes: **Message attributes for publishing action. Create an object and pass the values as key-value pairs.
- **Message Structure: **The structure of the message. Create an object and pass the values as key-value pairs.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | See [Amazon documentation](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html) to learn about message attributes. |
| --- | --- |

- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
