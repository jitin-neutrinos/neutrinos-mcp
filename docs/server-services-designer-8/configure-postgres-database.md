# PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance.

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/configure-postgres-database>

##### PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance.

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a** SQL** node to the workspace. Double click the node. Select Add new db-config from the **Connection Name** drop-down list and click the map icon.
- Select **Postgres** in the **Data options** drop-down list and configure the fields.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Database Config: **The name of the database connection. ![exist vs new](/resources/Storage/server-services-designer-8/existvsnew.png)
  - If you have a database connection that you have already configured in the [Global Session](/articles/server-services-designer-8/global-session-node) node, choose that connection from the drop-down list.
  - If you want to configure a new database, select **Add new DB-config** from the drop-down list and click the **Map** icon to configure a new database connection. See [Attributes for a new database](/articles/server-services-designer-8/mssql-node/a/newconnectionattr) to know what are the properties to configure for a new database connection.
- **Query Mapping:** Enter a query, or map the query that is to be executed. ![postgres 1](/resources/Storage/server-services-designer-8/postgres1.png)
  - To map the query, choose bh. or bh.local property from the drop-down list and enter the variable name which contains the query.
  - To enter the query, choose string and enter the query directly. For example, if you choose a string, the query can be INSERT INTO user (name, password) values ("John", "Doe").
- **Query Parameters:** Enter the parameters that are to be inserted in the query. For example, if the query in the** Query Mapping **field is entered as INSERT INTO user (name, password) values ($1, $2), then you enter the keys as** John** and **Doe**. The values **$1** and **$1 **will be replaced with keys in the order in which you have specified the keys. Use the **Plus** icon to add each key individually. You can also map the keys to the bh. or bh.local properties.

- **Result Mapping**: Map the data retrieved from the database to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

### Attributes for a New Database:

- **Disable Database: **Toggle this option to disable the configuration for the particular database connection. You can only disable the existing database configurations. This field does not appear when you are adding a new database configuration.
- **Database Options: **Select the type of database that you want to add. In this case, select **Postgres** as the database option. This field appears only when you are adding a new database configuration. Configure the following fields:

- **Connection Name: **Specify the name of your connection. This name will appear in the drop-down list of database configs.![Postgres configuration](/resources/Storage/server-services-designer-8/postgresconfig.png)
- **Type:** The type of database you are configuring. This is a read-only field.
- **Host**: The host where the database is running.
- **Port:** The port that can be used to connect to the host where the database is running.  The default port is **5432**.
- **Username:** The username to authenticate your database connection.
- **Password: **The password associated with the username to authenticate your connection to the database.
- **Database Name: **The name of the database in **Postgres** that you want to connect to.
- **Schema**: Schema is a namespace that contains named database objects such as tables, data types, functions, and operators. The default value is **public**.
- **Optional:** These are the optional configurations that you can perform for your Postgres connection. For every option, you can choose the env type and enter the environment property that holds the value, or choose the datatype that the respective filed supports. Make sure that the environment property isalready added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.After entering the required values, click ![](/resources/Storage/server-services-designer-8/correct.png) to save the connection details. After saving the configuration, you will see the connection listed in the **Database Config **field.
  - **UUID Extension**: A Universally Unique IDentifier(UUID) is written as a sequence of lower-case hexadecimal digits, in several groups separated by hyphens, specifically a group of 8 digits followed by three groups of 4 digits followed by a group of 12 digits, for a total of 32 digits representing the 128 bits. For example,a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11
  - **Synchronize**: Enable this field to make sure that your entities will be synced with the database, every time you run the application. If you choose **boolean** from the drop-down list, enter **true** or **false** to enable or disable this option. By default, the value will be **true**.
