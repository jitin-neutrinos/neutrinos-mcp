# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/amqp-producer-node>

The **Advanced Message Queueing Protocol (****AMQP) Producer** node is used to create and produce a stream of messages which can be sent to a queue to be consumed by consumers.

A message can be a JSON object, a string, or a buffer.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to Use

- Open the Services editor window.
- Click the** plus icon** to add a new server-service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **AMQP** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with any **Start node** or an **HTTP In** node.

### Associated Attributes

- **Name****: **The name of the node. This name will display on the canvas when you save the node.
- **AMQP Config: **The name of the AMQP producer configuration. ![AMQP Connection](/resources/Storage/server-side-service-designer-publication/amqp_conn.png)
  - If you have an AMQP connection that you have already configured, choose that connection from the drop-down list.
  - If you want to configure a AMQP configuration, select **Add new AMQP-config** from the drop-down list and click the **Edit** icon to configure a new AMQP connection. See [Attributes to Configure an AMQP Connection](/articles/server-side-service-designer-publication/amqp-producer-node/a/h3__1857489592) to know what are the properties to configure a new connection. You can connect to the RabbitMQ broker using this configuration.
- **Producer Queue: **The queue to which the message is to be sent. ![AMQP node](/resources/Storage/server-side-service-designer-publication/amqp3.png)
- **Assert Queue Options: **Options to assert a queue. if the queue does not exist, a new queue will be created. See [Assert options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_assertQueue) to learn about the options supported in this field.
   Create an **options** object in the script node and assign it to the desired variable on the bh property. Select bh. , bh.local, or bh.input property type and enter the variable name which contains the options object. For example, if you specify bh.local.builderQOptions in this field, then the **local **property **builderQOptions** holds the option.

![Information](/resources/Storage/server-side-service-designer-publication/info.png)


 You should not assert a different queue option to an existing queue. The AMQP 0-9-1 standard does not allow it and throws errors.

- **M****essage Type**: The type of message you want to send to the queue. You can select the following options from the drop-down list.
- **Message:** The message to be sent to the queue. Select the bh. , bh.local or bh.input property type and enter the variable that holds the message.
- **Publish Options:** The options to publish the message. See [Publish options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_publish) to learn about the options supported in this field.
   Select bh. , bh.local, or bh.input property type and enter the variable name which contains the publish options object.

### Attributes to Configure an AMQP Connection

- **Name: **The name of the AMQP producer configuration.![A new AMQP producer configuration](/resources/Storage/server-side-service-designer-publication/amqp2.png)
- **Hostname: **The IP address of the Rabbit MQ broker to which you want to connect and send messages.
- **Port:** The port where the Rabbit MQ broker is running.
- **Username:** The username to connect to the broker.
- **Password:** The password to connect to the broker.
- **Frame Max:** The size in bytes of the maximum frame allowed over the connection. If you enter 0 in this field, it means no limit. But since frames have a size field which is an unsigned 32-bit integer, the minimum allowed value is 4 KB.
- **Heartbeat:** The period of the connection heartbeat, in seconds. This field checks for the liveness of the connection. If you enter **0** as the heartbeat parameter, the server value is used. This means that you can only disable the heartbeat if the server value is also **0**.
    If you enter a non-zero period in seconds as the heartbeat parameter, the connection will be monitored for liveness repeatedly for that interval. If the client fails to read the data from the connection for two successive intervals, the connection will emit an error and close.
- **vHost:** The virtual host of the AMQP connection. For convenience, the absent path segment **/** is interpreted as the virtual host with an empty name, which does not exist. When specifying another virtual host, remember that its name must be escaped.
    For example, the virtual host named /foo is %2Ffoo.
