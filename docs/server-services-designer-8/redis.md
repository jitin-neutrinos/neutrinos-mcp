# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/redis>

Redis stands for **Re**mote **Di**ctionary** S**erver. It is an open-source, in-memory, key-value data store primarily used as a cache or message broker. The Redis node package consists of these nodes:

- [Redis Session node](/articles/server-services-designer-8/redis-session-node) - which will be displayed in the [Global nodes](/articles/server-services-designer-8/global-nodes) palette.
- [Redis Operations node](/articles/server-services-designer-8/redis-operations-node)
- [Redis Publish node](/articles/server-services-designer-8/redis-publish-node)
- [Redis Subscribe node](/articles/server-services-designer-8/redis-subscribe-node)

### How to Use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Attributes for a new Redis configuration

If you choose the env type, make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: The name of the new configuration.
- **Disable Database**: Toggle this option to disable the configuration of a particular database connection. You can only disable the existing database configurations.
- **Enable URL:** To connect to the Redis database, you can enter either enter the Host, and Port parameters, or enter the URL parameter. If you want to do the latter, toggle this field to True.
  - **URL: **The URL of the Redis server. The default format is [redis:]//[[user][:password@]][host][:port][/db-number][?db=db-number[&password=bar[&option=value]]].
- **Host: **The IP address of the Redis server. The default host is **127.0.0.1**.
- **Port: **The port of the Redis server. The default port is **6379**.
- **Path: **The UNIX socket string of the Redis server.
- **String Numbers: **If set to True, this field will return Redis number values as String instead of javascript Numbers. It is useful if you need to handle big numbers.
- **Return Buffers (**False**):** If set to True, all replies will be sent to callbacks as Buffers instead of Strings.
- **Detect Buffers** **(**False**)**: If set to True, replies will be sent to callbacks as Buffers. To use this field, the key (of type **Buffer**) should be defined in the [Script](/articles/server-services-designer-8/script-node) node and called here.
- **Socket keepalive** **(**True**)**: By default, the keep-alive functionality is enabled on the underlying socket. Keep-alive is a message sent by one device to another to check that the link between the two is operating.
- **Socket Initial Delay:** The initial delay in milliseconds. Defaults to **0**. It sets the delay between the last data packet received and the first keepalive probe.
- **No Ready Check (**False**): **When a connection is established to the Redis server, the server might still be loading the database from the disk. While loading, the server will not respond to any commands. To work around this, you can set this field to True to send the INFO command to the server. The response from the INFO command indicates whether the server is ready for more commands. When ready, the database emits a ready event.
- **Enable Offline Queue (**True**):** By default, if there is no active connection to the Redis server, commands are added to a queue and are executed once the connection has been established. Setting this field to False will disable this feature and the callback will be executed immediately with an error, or an error will be emitted if no callback is specified.
- **Retry Unfulfilled Commands (False): **If set to True, all commands that were unfulfilled while the connection is lost will be retried after the connection has been reestablished. Use this with caution if you use state-altering commands. This is especially useful if you use blocking commands.
- **User: **The Access Control List (ACL) user. Access Control List is the feature that allows certain connections to be limited in terms of the commands that can be executed and the keys that can be accessed.
- **Password: **If set, the client will run the Redis AUTH command to connect to the Redis database.
- **Db:** The database to connect to. A Redis instance supports 16 logical databases. These databases are not interlinked with one another, and when you run a command in one database it doesn't affect any of the data stored in other databases in your Redis instance.
- **Family: **Defaults to **IPv4**. You can also select **IPv6** from the drop-down list.
- **Disable Resubscribing (**False**):** If set to True, a client won't resubscribe after disconnecting.
- **Prefix: **A string used to prefix all used keys. For example, namespace:test.
- **Connect Timeout: **The timeout for connecting to the Redis database. Defaults to **3600000** milliseconds.
