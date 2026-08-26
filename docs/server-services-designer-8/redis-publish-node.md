# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/redis-publish-node>

The **Redis** **Publish** node is used to send a message to a Redis channel.

Redis Pub/Sub implements the messaging system where the publishers send the messages while the subscribers receive them. The link by which the messages are transferred is called a **channel**.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | You cannot subscribe to a channel to which you publish messages. |
| --- | --- |

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Redis Config: **The name of the configuration.
  - If you have an existing Redis configuration, select it from the drop-down list.
  - If you want to configure a new Redis configuration, select **Add new Redis config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for Redis Configuration](/articles/server-services-designer-8/redis/a/h3_964573856) to learn about the properties you need to configure.
- **Channel: **The channel to which you want to publish the messages. Choose String from the drop-down list and enter the topic or map the topic to the bh. bh.input or bh.local property, and enter the variable name.
- **Message:** The message you want to publish/send. Choose **string **from the drop-down list and enter the message or map the message to the bh. bh.input or bh.local property, and enter the variable name.
