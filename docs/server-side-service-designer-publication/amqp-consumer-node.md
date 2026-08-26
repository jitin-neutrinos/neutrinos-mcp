# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/amqp-consumer-node>

The **Advanced Message Queueing Protocol (****AMQP) Consumer** node is used to consume the stream of messages that are sent from the subscribed AMQP producer.

The message can be a JSON object, a string, or a buffer.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available for you to use from Neutrinos Studio release 7.5.0. |
| --- | --- |

### How to Use

- Open the Services editor window.
- Add a new server-service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **AMQP** **Consumer **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

- **Name****: **The name of the node. This name will display on the canvas when you save the node.
- **AMQP Config: **Select the AMQP consumer configuration.
  - If you have an existing AMQP connection that you have already configured, choose that connection from the drop-down list.
  - If you want to configure a new configuration, select **Add new AMQP-config** from the drop-down list and click the **Edit** icon to configure a new AMQP connection. See [Attributes to Configure an AMQP Connection](/articles/server-side-service-designer-publication/amqp-producer-node/a/h3__1857489592) to know what are the properties to configure a new connection. You can connect to the RabbitMQ broker using this configuration.
- **Consumer Queue: **The queue from which the message is to be consumed. See [consume options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_consume) to learn about the options supported in this field.![AMQP node](/resources/Storage/server-side-service-designer-publication/amqp%20consumer.png)
  - Select bh. and enter the variable name which contains the name of the consumer queue.
  - Select env and enter the environment property that holds the name of the consumer queue. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
  - Select string and enter the consumer queue from which you want to consume the message.
- **Message Queue options: **Options to configure the message received from the consumer queue. This is an optional field. See [consume options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_consume) to learn about the options supported in this field. Enter the queue options as is. For example, { noAck : true }.
- **Assert Queue Options: **Options to assert a queue. This is an optional field. If the queue does not exist, a new queue will be created. See [Assert options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_assertQueue) to learn about the options supported in this field. Enter the queue options as is. For example, { exclusive : false }.

### Attributes to Configure an AMQP Connection

- **Name: **The name of the AMQP consumer configuration.![A new AMQP producer configuration](/resources/Storage/server-side-service-designer-publication/consumer.png)
- **Hostname: **The IP address of the Rabbit MQ broker to which you want to connect and receive messages.
- **Port:** The port where the Rabbit MQ broker is running.
- **Username:** The username to connect to the broker.
- **Password:** The password to connect to the broker.
- **Frame Max:** The size in bytes of the maximum frame allowed over the connection. If you enter 0 in this field, it means no limit. But since frames have a size field which is an unsigned 32-bit integer, the minimum allowed value is 4 KB.
- **Heartbeat:** The period of the connection heartbeat, in seconds. This field checks for the liveness of the connection. If you enter **0** as the heartbeat parameter, the server value is used. This means that you can only disable the heartbeat if the server value is also **0**.
   If you enter a non-zero period in seconds as the heartbeat parameter, the connection will be monitored for liveness repeatedly for that interval. If the client fails to read the data from the connection for two successive intervals, the connection will emit an error and close.
- **vHost:** The virtual host of the AMQP connection. For convenience, the absent path segment **/** is interpreted as the virtual host with an empty name, which does not exist. When specifying another virtual host, remember that its name must be escaped.
   For example, the virtual host named /foo is %2Ffoo.
