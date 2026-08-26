# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/mssql-node>

The **SQL **node is used to connect and perform operations on relational database management systems such as MySQL, MS SQL, MariaDB, Oracle, and PostgreSQL.

You can configure the following databases using the SQL node.

- [MSSQL](/articles/server-services-designer-9/configure-mssql-database)
- [MySQL](/articles/server-services-designer-9/configure-mysql-database)
- [MariaDB](/articles/server-services-designer-9/configure-mariadb-database)
- [Oracle](/articles/server-services-designer-9/configure-oracle-database)
- [PostgreSQL](/articles/server-services-designer-9/configure-postgres-database)

You can also configure a **Connection pool** in the MS SQL database. Where **connection pool** is a set of idle, open, and reusable database connections maintained by the database server so that the connections can be reused when the database receives future requests for data, instead of exclusively opening a new connection.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is enhanced in Neutrinos Studio release 7.1.0. Therefore, you will see more attributes if you are using Studio versions later than 7.0.2. |
| --- | --- |

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a** SQL** node to the workspace. Double click the node to configure its properties.
- Choose the database you want to configure.
- Drag and drop other nodes to create a flow. Make sure the flow starts with an **HTTP In** or **Start **node.
