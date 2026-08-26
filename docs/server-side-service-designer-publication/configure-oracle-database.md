# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/configure-oracle-database>

**Oracle Database** is a proprietary multi-model database management system produced and marketed by Oracle Corporation. It is a database commonly used for running online transaction processing, data warehousing, and mixed database workloads.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a** SQL** node to the workspace. Double click the node. Select Add new db-config from the **Database Configs** drop-down list and click the map icon.
- Select **Oracle** in the **Data options** drop-down list and configure the fields.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Database Configs: **The name of the database connection. ![exist vs new](/resources/Storage/server-side-service-designer-publication/existvsnew.png)
  - If you have a database connection that you have already configured in the [Global Session](/articles/server-side-service-designer-publication/global-session-node) node, choose that connection from the drop-down list.
  - If you want to configure a new database, select **Add new DB-config** from the drop-down list and click the **Map** icon to configure a new database connection. See [Attributes for a new database](/articles/server-side-service-designer-publication/mssql-node/a/newconnectionattr) to know what are the properties to configure for a new database connection.
- **Query Mapping:** Enter a query, or map the query that is to be executed.
  - To map the query, choose bh. or bh.local property from the drop-down list and enter the variable name which contains the query.
  - To enter the query, choose string and enter the query directly. For example, if you choose a string, the query can be INSERT INTO user (name, password) values ("John", "Doe").
- **Query Parameters:** Enter the parameters that are to be inserted in the query. For example, if the query in the** Query Mapping **field is entered as INSERT INTO user (name, password) values (:1, :2), then you enter the keys as** John** and **Doe**. The values **:1** and **:2 **will be replaced with keys in the order in which you have specified the keys. Use the **Plus** icon to add each key individually. You can also map the keys to the bh. or bh.local properties.

- **Result Mapping**: Map the data retrieved from the database to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

### Attributes for a New Database:

- **Disable Database: **Toggle this option to disable the configuration for the particular database connection. You can only disable the existing database configurations. This field does not appear when you are adding a new database configuration.
- **Database Options: **Select the type of database that you want to add. In this case, select **Oracle** as the database option. This field appears only when you are adding a new database configuration. Configure the following fields.
- **Optional**: These are the optional configurations that you can perform for your Oracle connection. For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
  - **Connection String**: A connection string is a string that specifies information about a data source and the means of connecting to it. It includes the source database name, and other parameters needed to establish the initial connection.
  - **Connection Name**: Specify the name of your connection. This name will appear in the drop-down list of **Database Configs**.
  - **Type**: The type of database you are configuring. This is a **read-only** field.
  - **Host**: The host where the database is running.
  - **Port**: The port that is used to connect to the host where the database is running. By default, the port value will be **1521**.
  - **Username**: The username to authenticate your connection for the database.
  - **Password**: The password associated with the username to authenticate your connection to the database.
  - **Service Name**: Service name is a logical representation of the database and is used to connect to the database instance in oracle. There can be more than one service name to a single database. By default, when the new pluggable database is created, the database name will be the service name.
  - **Connection Timeout**: Specify the time by which the server should respond to the connection request. Enter the time in milliseconds(ms). This happens when you connect to the database for the first time. If a client connection does not receive a response from the server after the specified seconds, the request will be timed out and the client will immediately receive a "**Connection timed out"** error message. The default value of the Connection Timeout is **15000**.
  - **Request Timeout**: Specify the time by which the server should respond to the database request. Request Timeout message is a status code with a message that is returned to the client when a request to the server takes longer than the server’s allocated timeout window. The default value of the Request timeout is **15000**.
  - **Synchronize**: Enable this field to make sure that your entities will be synced with the database, every time you run the application. If you choose **boolean** from the drop-down list, enter **true** to enable or **false** to disable this option. By default, the value will be **true**.

After entering the required values, click ![](/resources/Storage/server-side-service-designer-publication/correct.png) to save the connection details. You will see the connection listed in the **Database Config** field.
