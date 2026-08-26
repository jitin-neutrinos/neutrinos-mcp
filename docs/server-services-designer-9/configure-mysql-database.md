# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/configure-mysql-database>

**MySQL** is a freely available open-source RDBMS that uses Structured Query Language (SQL). SQL is used for adding, accessing, and managing content in a database.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a** SQL** node to the workspace. Double click the node. Select **Add new db-config** from the **Database Configs** drop-down list and click the map icon.
- Select **MySQL i**n the **Data options** drop-down list and configure the fields.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Database Configs: **The name of the database connection. ![exist vs new](/resources/Storage/server-services-designer-9/existvsnew.png)
  - If you have a database connection that you have already configured in the [Global Session](/articles/server-services-designer-9/global-session-node) node, choose that connection from the drop-down list.
  - If you want to configure a new MySQL database, select **Add new DB-config** from the drop-down list and click the **Map** icon to configure a new database connection. See [Attributes for a new database](/articles/server-services-designer-9/mssql-node/a/newconnectionattr) to know what are the properties to configure for a new database connection.
- **Query Mapping:** Enter the query or map the query that is to be executed. ![mysql](/resources/Storage/server-services-designer-9/mysql1.png)
  - To map the query, choose bh. or bh.local property from the drop-down list and enter the variable name which contains the query.
  - To enter the query, choose string and enter the query directly. For example, if you choose a string, the query can be INSERT INTO dbo.[user] (name, password) values ("John", "Doe").
- **Query Parameters:** Enter the parameters that are to be inserted in the query. For example, if the query in the** Query Mapping **field is entered as INSERT INTO user (name, password) values (?1, ?2), then you enter the keys as** John** and **Doe**. The values **?****1** and **?2** will be replaced with keys in the order in which you have specified the keys. Use the **Plus** icon to add each key individually. You can also map the keys to the bh. or bh.local properties.

- **Result Mapping**: Map the data retrieved from the database to bh. or bh.local properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of the connection.

### Attributes for a New Database

### These are the properties to configure a new database connection:

- **Disable Database: **Toggle this option to disable the configuration for the particular database connection. You can only disable the existing database configurations. **This field does not appear when you are adding a new database configuration. **
- **Database Options: **Select the type of database that you want to add. In this case, select **MySQL** as the database option. **This field appears only when you are adding a new database configuration****.** Configure the following fields: ![Mssql config](/resources/Storage/server-services-designer-9/mysql1.png)

- **Connection Name:** Specify the name of your MySQL connection. This name will appear in the drop-down list of Database config field.
- **Type:** The type of database you are configuring. This is a read-only field.
- **Host:** The host where the database is running.
- **Port:** The port used to connect to the host where the database is running. By default, the port value will be **1521.**
- **Username:** The username to authenticate your connection.
- **Password: **The password associated with the username to authenticate your connection to the database.
- **Database Name: **The name of the database in **MySQL **that you want to connect to.
- **Optional:** These are the optional configurations that you can perform for your MySQL connection. For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective filed supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
  - **Synchronize**: Enable this field to make sure that your entities will be synced with the database every time you run the application. If you choose **boolean** from the drop-down list, enter **true** to enable or **false** to disable this option. By default, the value will be **true.** ![Optional config for MSSQL connection](/resources/Storage/server-services-designer-9/MYSQL%20optional.png)
  - **Charset**: The charset for the connection. This is of type string. The default charset is `UTF8_GENERAL_CI. `
  - **Timezone**: The timezone configured on the MySQL server. This can be **local**, **Z** or an offset in the form **+HH: MM** or **-HH: MM**. The default timezone is **local**.
  - **Connection Limit**: Number of simultaneous connections that can be made to the database. The default limit is set to 10 and the maximum limit can be 150.
  - **Connection Timeout: **Specify the time by which the server should respond to the connection request. Enter the time in **milliseconds(ms)**. This happens when you connect to the database for the first time. If a client connection does not receive a response from the server after the specified seconds, the request will be timed out and the client will immediately receive a **Connection timed out** an error message. The default value of the Connection Timeout is **10000**.
  - **Acquire Timeout**: The milliseconds before a timeout occurs during the initial connection to the MySQL server. The default value is **10000**.
  - **Insecure Auth (Boolean)**: Allows connecting to MySQL that asks for the old (insecure) authentication method. This defaults to **False**.
  - **Support Big Numbers (Boolean)**: Enable this option when you are dealing with big numbers ( BIGINTand DECIMALcolumns) in the database. The default value is set to **True**.
  - **Big Number Strings (Boolean)**: Enable both **Support Big Numbers** and **Big Number String** to always return big numbers as JavaScript String objects. The default value is set to **True**. This option is ignored if **Support Big Numbers** is disabled.
  - **Date Strings (Boolean)**: Enable this field to return date types (`TIMESTAMP`, `DATETIME`, `DATE`) as strings. The default value is set to **False**.
  - **Debug (Boolean)**: Prints the debug trace on the **Live View (Server)** terminal. The default value is set to **False**.
  - **Trace (Boolean)**: Prints the connection stack traces on the **Live View (Server)** terminal. **T****race** is used to help diagnose problems in managing the databases. The default value is set to **True**.
  - **Multiple Statements (Boolean)**: If set to** True**, allows multiple MySQL statements per query. This could increase the scope of SQL injection attacks. The default value is set to **False**.
  - **Flags**: List of connection flags to use other than the default ones. It is also possible to blacklist default ones. It is of type string. See [Connection Flags](https://github.com/mysqljs/mysql#connection-flags) to know more.

After entering the required values, click ![](/resources/Storage/server-services-designer-9/correct.png) to save the connection details. After saving the configuration, you will see the connection listed in the **Database Configs** field and you can select the connection from the drop-down list.
