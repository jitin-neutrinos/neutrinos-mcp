# Integrate with a Relational Database

<https://documentation.neutrinos.com/articles/#!studio-guide-7/integrate-with-databases>

Neutrinos provides seamless integrations with major database systems such as MSSQL Server, Oracle, MySQL, MariaDB, PostgreSQL, and MongoDB.

Using these integrations, your time and efforts on integration projects are hugely reduced, providing you more time to concentrate on app designing.

Integrations to databases come with an advantage of connection pooling where **connection pool** is a set of idle, open, and reusable database connections maintained by the database server so that the connections can be reused when the database receives future requests for data, instead of exclusively opening a new connection.

This reduces the application and database system overhead for creating or destroying a connection.

### Integrate with a Relational Database

You use the [SQL node](/smart/project-server-side-service-designer/mssql-node) in the Server Services Designer to integrate with SQL databases such as MSSQL Server, Oracle, MySQL, MariaDB, and PostgreSQL.

To integrate with a SQL database:

1. In the Server Services Designer, drag and drop the **SQL node** to the workspace.
    ![SQL node](/resources/Storage/studio-guide-7/sql_1.png)
2. Double click the node.
3. Select **Add new db-config** from the **Database Configs** drop-down list and click the **map** icon.
    ![Add database configuration](/resources/Storage/studio-guide-7/sql_2.png)
4. Select the SQL database that you want to integrate with and configure respective properties. For example, select **MSSQL**.
    ![Select a SQL database](/resources/Storage/studio-guide-7/sql_3.png)
5. After you select the database, you can configure the connection pooling parameters using the attributes window. For example, connection pooling properties in the MSSQL database:
    ![Connection pooling parameters](/resources/Storage/studio-guide-7/sql_4.png)

### Integrate with a NoSQL Database

To integrate with the MongoDB database:

1. In the Server Services Designer, drag and drop the **MongoDB node** to the workspace.![MongoDB node](/resources/Storage/studio-guide-7/mongo_1.png)
2. Double click the node. Select **Add new db-config** from the **Database Configs** drop-down list and click the **map** icon to configure the MongoDB database.
    ![MongoDB configuration](/resources/Storage/studio-guide-7/mongo_2.png)
3. Enter the MongoDB connection URI used to connect to a MongoDB deployment and use the **Options** drop-down list to configure connection pooling or add query strings.
    ![Connection pooling in mongoDB](/resources/Storage/studio-guide-7/mongo_3.png)
4. After the MongoDB connection is set up, perform any DB operation on the MongoDB database using this node. For example:
    ![Count docs operation](/resources/Storage/studio-guide-7/mongo_count_docs.png)

---

| **Learn More:** |
| --- |
| [MongoDB node](/smart/project-server-side-service-designer/mongodb-node)    [Example: Integrate with a NoSQL DB](/smart/project-how-to-articles/working-with-databases)    [SQL node](/smart/project-server-side-service-designer/mssql-node) |
