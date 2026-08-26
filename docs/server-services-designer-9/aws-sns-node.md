# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/aws-sns-node>

The **Amazon Simple Notification Service (SNS)** is used to provides message delivery from publishers to subscribers (also known as producers and consumers).

Publishers communicate asynchronously with subscribers by sending messages to a topic, which is a logical access point and communication channel. Clients can subscribe to the SNS topic and receive published messages using a supported protocol, such as Amazon Kinesis Data Firehose, Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile text messages (SMS).

See [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) to learn more.

The AWS Node comprises 4 nodes:

- [Topic](/articles/server-services-designer-9/topic-node)
- [Publish](/articles/server-services-designer-9/publish-node)
- [Subscription](/articles/server-services-designer-9/subscription-node)
- [Get Message](/articles/server-services-designer-9/get-message-node)

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.5.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Download the Plugin from Neutrinos Store. See [Download from Store](/articles/studio-guide-7/import-plugin).
- In the Nodes Palette, search for the installed node and drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**
