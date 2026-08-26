# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/amqp-rpc-node>

The **Advanced Message Queueing Protocol (****AMQP) Remote Procedure Call (RPC)** node allows you to communicate between processes on different workstations in the AMQP network.

![Amqp rpc diagram](/resources/Storage/server-side-service-designer-publication/AMQP_RPC.png)

This is how the RPC works:

- When the Client service is started, it creates an anonymous exclusive callback queue.
- For an RPC request, the Client server sends a message with two properties, one to the callback queue, and the other is set to a unique value for every request.
- The request is sent to an RPC queue.
- The RPC server is waiting for requests on that queue. When a request appears, it does the job and sends a message with the result back to the Client.
- The client waits for data on the callback queue. When a message appears, it checks the property and If it matches the value from the request it returns the response to the application.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to Use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download (In this case AMQP RPC).
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Associated Attributes

- **Name****: **The name of the node. This name will display on the canvas when you save the node.
- **Function Name**: This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. To call the flow, you can use this function name in the component where the service is injected.
- **AMQP Config: **The name of the AMQP configuration. If you have an AMQP connection that you have already configured, choose that connection from the drop-down list.
  - If you want to configure an AMQP configuration, select **Add new AMQP-config** from the drop-down list and click the **Edit** icon to configure a new AMQP connection. See [Attributes to Configure an AMQP Connection](/articles/server-side-service-designer-publication/amqp-producer-node/a/h3__1857489592) to know what are the properties to configure a new connection. You can connect to the RabbitMQ broker using this configuration.
- **Sender Queue: **The queue to which the message is to be sent. Select bh. and enter the variable name which contains the name of the producer queue.
  - Select env and enter the environment property that holds the name of the producer queue. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
  - Select string and enter the producer queue to which you want to send the message.
- **M****essage Type**: The type of message you want to send to the queue. You can select the following options from the drop-down list.
- **Message**: The message to be sent to the queue. Select the bh. , bh.local or bh.input property type and enter the variable that holds the message.
- **result**: You can map the retrieved result to bh. , bh.local or bh.input properties. Select the parameter type and enter the variable that should holds the result.
- **Message Queue Options: **Options to configure the message received from the consumer queue. This is an optional field. See [consume options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_consume) to learn about the options supported in this field. Enter the queue options as is. For example, { noAck : true }.
- **Publish Options:** The options to publish the message. See [Publish options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_publish) to learn about the options supported in this field.
    Select bh. , bh.local, or bh.input property type and enter the variable name which contains the publish options object.
- **Assert Queue Options: **Options to assert a queue. if the queue does not exist, a new queue will be created. See [Assert options](https://www.squaremobius.net/amqp.node/channel_api.html#channel_assertQueue) to learn about the options supported in this field.
    Create an **options** object in the script node and assign it to the desired variable on the bh property. Select bh. , bh.local, or bh.input property type and enter the variable name which contains the options object. For example, if you specify bh.local.builderQOptions in this field, then the **local **property **builderQOptions** holds the option.
- **defaultTimeout**: Specify the waiting time for the response. The default timeout value is 120 seconds.

---

### Attributes to Configure an AMQP Connection

- **Name: **The name of the AMQP producer configuration.
- **Hostname: **The IP address of the Rabbit MQ broker to which you want to connect and send messages.
- **Port:** The port where the Rabbit MQ broker is running.
- **Username:** The username to connect to the broker.
- **Password:** The password to connect to the broker.
- **Frame Max:** The size in bytes of the maximum frame allowed over the connection. If you enter 0 in this field, it means no limit. But since frames have a size field that is an unsigned 32-bit integer, the minimum allowed value is 4 KB.
- **Heartbeat:** The period of the connection heartbeat, in seconds. This field checks for the liveness of the connection. If you enter **0** as the heartbeat parameter, the server value is used. This means that you can only disable the heartbeat if the server value is also **0**.
    If you enter a non-zero period in seconds as the heartbeat parameter, the connection will be monitored for liveness repeatedly for that interval. If the client fails to read the data from the connection for two successive intervals, the connection will emit an error and close.
- **vHost:** The virtual host of the AMQP connection. For convenience, the absent path segment **/** is interpreted as the virtual host with an empty name, which does not exist. When specifying another virtual host, remember that its name must be escaped.
    For example, the virtual host named /foo is %2Ffoo
