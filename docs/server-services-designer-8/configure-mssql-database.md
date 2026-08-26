# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/configure-mssql-database>

**Microsoft SQL Server(MS SQL) **is a relational web hosting database that is used to store web site information such as blog posts or user information. MS SQL is the most popular type of database on Windows servers.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the services list.
- In the Nodes Palette, drag and drop a** SQL** node to the workspace. Double click the node. Select **Add new db-config** from the **Database Configs** drop-down list and click the **map** icon.
- Select **MSSQL** in the **Data options** drop-down list and configure the fields.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Database Configs: **The name of the database connection. ![exist and new db](/resources/Storage/server-services-designer-8/existvsnew.png)
  - If you have a database connection that you have already configured in the [Global Session](/articles/server-services-designer-8/global-session-node) node, choose that connection from the drop-down list.
  - If you want to configure a new MS SQL database, select **Add new DB-config** from the drop-down list and click the **Map** icon to configure a new database connection. See [Attributes for a new database](/articles/server-services-designer-8/configure-mssql-database/a/h3__231854724) to know what are the properties to configure a new database connection.

- **Query Mapping:** Enter a query, or map the query that is to be executed. ![mssql](/resources/Storage/server-services-designer-8/1234467t857856746585.png)
  - To map the query, choose bh. or bh.local property from the drop-down list and enter the variable name which contains the query.
  - To enter the query, choose string and enter the query directly. For example, if you choose a string, the query can be INSERT INTO dbo.[user] (name, password) values ("John", "Doe").
- **Query Parameters:** Enter the parameters that are to be inserted in the query. For example, if the query in the** Query Mapping **field is entered as INSERT INTO dbo.[user] (name, password) values (@1, @2), then you enter the keys as** John** and **Doe**. The values **@1** and **@2 **will be replaced with keys in the order in which you have specified the keys. Use the **Plus** icon to add each key individually. The values you enter in the fields will be interpreted as string literals. You can also map the keys to the bh. or bh.local properties.

- **Result Mapping**: Map the data retrieved from the database to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

### Attributes for a New Database:

These are the properties to configure a new database connection:

- **Disable Database: **Toggle this option to disable the configuration of a particular database connection. You can only disable the existing database configurations. **This field does not appear when you are adding a new database configuration. **
- **Database Options: **Select the database type that you want to add. In this case, select **MSSQL** as the database option. This field appears only when you are adding a new database configuration. Configure the following fields:![mssql 2](/resources/Storage/server-services-designer-8/mssql2.png)
- **Connection Name**: Specify the name of your MSSQL connection. This name will appear in the drop-down list of connections in the **Database Configs** field.
- **Type**: The type of database that you are configuring. This is a read-only field.
- **Host**: The host where the database is running.
- **Port**: The port that can be used to connect to the host where the database is running. By default, the port value will be **1433. **
- **Username**: The username to authenticate your connection.
- **Password**: The password associated with the username to authenticate your connection with the database.
- **Database Name**: The name of the database in **MSSQL** that you want to connect to.
- **Connection Timeout**: Specify the time by which the server should respond to the connection request. Enter the time in **milliseconds(ms)**. This happens when you connect to the database for the first time. If a client connection does not receive a response from the server after the specified seconds, the request will be timed out and the client will immediately receive a **Connection timed out** an error message. The default value of the Connection Timeout is **15000**.
- **Request Timeout**: Specify the time by which the server should respond to the database request. An HTTP status code will be returned to the client when a request to the server takes longer than the server’s allocated timeout window. The default value of the Request timeout is **15000**.
- **Max.pool connections**: The maximum number of connections the pool can contain. That is, the maximum collection of reusable database connections. By default, the maximum number will be 10.
- **Min.pool connections**: The minimum number of connections the pool can contain. By default, the value is 0.
- **Optional**: These are the optional configurations that you can perform for your MSSQL connection. For every option, you can choose the env type and enter the environment property that holds the value, or choose the datatype that the respective filed supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.![mssql options](/resources/Storage/server-services-designer-8/MSSQLINST.png)
   After entering the required values, click ![](/resources/Storage/server-services-designer-8/correct.png) to save the connection details. After saving the configuration, you will see the connection listed in the **Database Configs **field.
  - **Synchronize**: Enable this field to make sure that your entities will be synced with the database every time you run the application. If you choose **boolean** from the drop-down list, enter **true** to enable or **false** to disable this option. By default, the value will be **true**.
  - **Server Instance name**: The server instance name which you receive while setting up the named instance of the database. To find your instance name, perform the following:
    - Open the Microsoft SQL Server Management Studio, Right-click the database connection and select **Properties**.
    - Server properties window appears and click **View connection properties**. You can see the **Instance name** mentioned in the properties.
  - **Max.pool waiting clients**: The Maximum number of waiting requests allowed.
  - **Pool FIFO(Boolean)**: If set to **true, **the oldest resource in the pool will be allocated first. If set to **false, **the most recently released resource will be allocated first.
  - **Pool priority range**: This can be an integer value between 1 to X. Users can specify their relative priority in the queue if there are no resources available. The default priority range is 1.
  - **Pool auto start (Boolean)**: If set to **true**, the pool starts creating resources once the constructor is called. By default, the auto start is set to **true**.
  - **Pool Eviction Run Interval Milliseconds**: Set intervals to specify how often the eviction checks should run. By default, the value is set to **0** which means it does not run the eviction checks.
  - **Pool number of tests per run**: Number of resources to check for each eviction run. The default value is 3.
  - **Pool soft idle timeout milliseconds**: The amount of time an object will sit idle in the pool before it is eligible for eviction. The default value is **-1** which means nothing can be evicted.
  - **Cancel Timeout**: The number of milliseconds before the cancel of a request is considered to be failed. By default, it is set to** 5000**ms.
  - **Packet size**: The size of Tabular Data Stream(TDS) packets. It should be a power of 2. The default packet size is **4096**.
  - **Use UTC(Boolean)**: Determines whether to pass time values in Coordinated Universal Time(UTC) or local time. By default, it is set to **true**.
  - **Local Address**: Indicates which network interface (IP address) to use when connecting to SQL Server.
  - **Read-only intent(Boolean)**: Determines whether the connection will request read-only access from a SQL Server Availability Group. By default, it is set to **false**.
  - **Encrypt(Boolean)**: Determines whether the connection should be encrypted or not. Set to **true** if you are on **Windows Azure**. By default, it is set to **false**.
