# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/topic-node>

The AWS SNS Topic node is used to create a topic to which notifications can be published. An Amazon SNS topic is a logical access point that acts as a communication channel. You use the **Topic** node to:

- Create a topic
- List topics
- Delete a topic
- Get topic attributes
- Set topic attributes

The first task to perform in an AWS SNS node is to create a topic. You create a topic to broadcast the messages of a message-producer system (for example, an e-commerce website) working with multiple other services that require its messages (for example, checkout and fulfillment systems).

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Select AWS Config: **The name of the config.
  - If you have an Amazon config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new Amazon config, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for a new Amazon Configuration](/articles/server-services-designer-9/textract-node/a/h3_1541343129) to know what are the properties to configure.
- **Select Operation:** Select the operation to be performed. See [Operations on a Topic](/articles/server-services-designer-9/topic-node/a/h3_1818896831). Based on the operation you choose, the attributes list will differ.

### Operations on a Topic

#### Create Topic

Creates a topic to which notifications can be published. If the requester already owns a topic with the specified name, that topic's ARN is returned without creating a new topic. See [the Amazon documentation on Create Topic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html) to learn more.

- **Topic Name:** The name of the topic. Select the **bh** object that holds the topic name, or select **string** and enter the topic name.
- **Attributes: **The list of attributes to be added to the topic. Create an object and pass the values as key-value pairs. See [Create topic attributes](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SNS.html#createTopic-property) to learn about the attributes that you can set.
- **Tags:** The list of tags to add to a new topic. Create an object and pass the values as key-value pairs. See [Create topic attributes](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/SNS.html#createTopic-property) to learn about the tags that you can add to the topic.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### List Topics

Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. See the [Amazon documentation on List Topics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) to learn more.

- **Next Token:** This parameter is returned if the number of topics is more than 100. Use this parameter in a new ListTopics call to get further results.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### Delete a Topic

Deletes a topic and all its subscriptions. See the [Amazon documentation on Delete Topic](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html) to learn more.

- **TopicArn: **The Amazon Resource Name(ARN) of the topic you want to delete.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### Get Topic Attributes

Returns all of the properties of a topic. See the [Amazon documentation on Get Topic Attributes](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html) to learn more.

- **TopicArn: **The ARN of the topic you want to get details of.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### Set Topic Attributes

Allows a topic owner to set an attribute of the topic to a new value. See the [Amazon documentation on Set Topic Attributes](https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html) to learn more.

- **TopicArn: **The ARN of the topic you want to set details of.
- **Attribute name:** The attribute you want to set for the topic.
- **Attribute Value: **The value of the attribute.
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
