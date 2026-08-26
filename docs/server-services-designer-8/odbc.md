# Prerequisites

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/odbc>

**Open Database Connectivity(ODBC) **is a gateway that provides access to different databases to applications. It is a relational database management language that manipulates the data stored in a database.

It allows maximum interoperability where an application can access data in diverse RDBMS through a single node.It helps in translating the commands of the client application into queries that are understood by the accessed database.SQL is a standard language that is used to retrieve data from a database.

The ODBC node package comprises 2 nodes:

- [ODBC](/articles/server-services-designer-8/odbc-node)
- [Transaction](/articles/server-services-designer-8/odbc-transaction-node)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.7.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### Prerequisites

Perform these steps before using the ODBC node to connect to your database:

- If you are using a **Unix/Linux** system, install unixODBC and unixODBC-devel packages. The compilation of the ODBC node on your system requires these packages to provide the correct headers:
  - Ubuntu/Debian:Copy CodeMarkdown sudo apt-get install unixodbc unixodbc-dev
  - RedHat/CentOS: Copy CodeMarkdownsudo yum install unixODBC unixODBC-devel
  - OSX:
    - macports.org: Copy CodeMarkdownsudo port unixODBC
    - using brew: Copy CodeMarkdownbrew install unixODBC
  - IBM i (requires [yum](http://ibm.biz/ibmi-rpms)): Copy CodeMarkdownyum install unixODBC unixODBC-devel
- If you are using a **Windows** system, install ODBC drivers for the target database. Most database management system providers offer ODBC drivers for their products. See the website of your DBMS for more information.
- Install odbc.ini and odbcinst.ini files: These files define your DSNs (data source names) and ODBC drivers, respectively. They must be set up for ODBC functions to correctly interact with your database.

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Download the Plugin from Neutrinos Store. See [Download from Store](/articles/studio-guide-7/import-plugin).
- In the Nodes Palette, search for the installed node and drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### ODBC Configuration

Use these attributes to create a new ODBC connection.

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name:** A display name for the ODBC configuration.
- **Disable Database:** Toggle this option to disable the configuration of a particular database connection. You can only disable the existing database configurations. **This field does not appear when you are adding a new database configuration.  **
- **Connection String:** The connection string to connect to the database.
  - Choose string and enter the connection string. For example: DSN=odbctest_dsn; DATABASE=odbctest.
  - Choose **as is **and enter the object as is.
  - Choose **env** and enter the environment property that contains the value. Make sure that the environment property is added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before calling this property here.
- **Connection Timeout: **Optional. The wait time (in seconds) for an idle connection to close.
- **Login timeout: **Optional.The wait time (in seconds) before the connection process attempts to connect before timing out.
- **Initial Size:** Optional. The initial number of connections created in the connection pool.
- **Increment Size:** Optional. The additional connections to create when all of the Pool's connections are taken.
- **Max Size: **Optional. The maximum number of open Connections the Pool will create.
- **Shrink:** Optional. Enable the toggle button to shrink the number of connections to **Initial Size** as they free up.
