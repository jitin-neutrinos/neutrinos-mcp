# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/redis-operations-node>

The** Redis Database **node is used to connect to and perform operations on the Redis database.

### Associated Attributes

- **Name: **Enter a name for the node. This name will display on the canvas when you save the node.
- **Redis Config: **The name of the database connection. If you have a database connection that you have already configured in the [Global Session](/articles/server-services-designer-8/global-session-node) node, choose that connection from the drop-down list. If you want to configure a new database, click the **Map** icon. See [Attributes for a new configuration](/articles/server-services-designer-8/redis/a/h3_964573856) to learn about the database parameters.
- **Operation: **The operation that you want to perform on the Redis database.
  - **Set: **This operation stores a record in the Redis database. If a key already holds a value, it will be overwritten.
  - **Get: **This operation only handles string values. It fetches the value of a key. If the key does not exist, it will return null.
- **Key: **An arbitrary string that holds the value. Choose the bh., bh.input, or bh.local property and enter a variable that holds the key, or choose string and enter the key.

**Result Mapping: **Map the retrieved data to bh., bh.input, or bh.local properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of the connection.
