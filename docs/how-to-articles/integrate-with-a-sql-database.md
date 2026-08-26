# Integrate with a SQL Database

<https://documentation.neutrinos.com/articles/#!how-to-articles/integrate-with-a-sql-database>

Neutrinos integrates your application with your existing SQL databases such as MariaDB, Oracle SQL, MSSQL, PostgreSQL, and MySQL. This allows you to develop applications that access data on your external database without having to worry about data migration.

The [Server Services Designer (SSD)](/smart/project-concepts/server-services-designer) allows you to configure and connect to these databases to perform database operations by creating server flows.

In this example, you will learn how to create a server endpoint which when called from an application, connects to your existing MSSQL database and inserts a record to your database table. You will also learn how to configure connection pooling parameters when you configure your MSSQL database.

1. Open the **Server Services** editor from the Studio Application page.
2. Open an existing service or click the** Add a Server Service** button to add a new service.
3. From the Nodes Palette, drag and drop an **HTTP In** node to the workspace. The **HTTP In **node allows you to build your own API end-point for creating web services. In this example, we are creating an API endpoint called **sqlinsert**.
4. Double-click the node to open its **Properties** window.
  1. Enter the node name as** Insert a record to MSSQL**.
  2. Select the **PUT** HTTP method.
  3. Enter the path as** sqlinsert**. Click the **Done **icon to save the properties.![HTTP In node](/resources/Storage/how-to-articles/mssql_1.png)
5. Drag and drop a **Script **node next to the **HTTP IN** node and connect the nodes to create a flow. Double-click the node and configure the node.
  1. Enter the name as **key**.
  2. Create the following bh objects (flow objects) in the editor. These flow objects will be used when inserting a record in the MSSQL database.Copy CodeMarkdownbh.keys=["name111","pass"]
     bh.input.keys1=["namekey123","pass123"]
     bh.local.keys2=["namekey1003","pass12300"]
  3. Save the node.
      ![script node](/resources/Storage/how-to-articles/script_1.png)
6. Drag and drop a **SQL** node next to the **Script** node and connect the nodes. Double-click the **SQL **node and configure the node.
7.
  1. Enter the name as **SQL Insert**.
  2. Choose** Add-new-db-config** and click ![add database config](/resources/Storage/how-to-articles/add_db_config.png) to add a new MSSQL connection. In the** Add new ****Database Config** page, enter the following details:
    1. Select the **Database Type** as **mssql** from the drop-down list. The properties to configure the MSSQL database are displayed. Other SQL databases can also be configured using the same node.
    2. Enter a connection name for future reference. For example, **mssql_connection**.
    3. Enter the connection parameters to connect to your existing MSSQL deployment and set basic configurations. Enter the **Host**, **Port**, **Username**, **P****assword**, **Database name, Connection Timeout, and Request Timeout **values.
        ![MSSQL configurations](/resources/Storage/how-to-articles/mssql_2.png)
    4. Configure your connection pool settings by clicking the **Options** drop-down list and entering values for the required fields. ![Connection pooling in mssql](/resources/Storage/how-to-articles/mssql_3.png)
    5. Click **Done**. The app is now connected to your existing MSSQL database.
  3. Enter the query to be executed in the **Query Mapping** field. In this case, let us insert a record into an existing table in MSSQL. For example - **INSERT INTO dbo.[test](name,password)VALUES(@0,@1) **.
  4. Enter the query parameters that are to be inserted in the above query. We had created 3 keys in the** Script** node. Let us pick the values stored in **bh.local.keys2** to be inserted into the database.
  5. In the **R****esult Mapping** field, select bh.input and enter the variable name as **result**. The response of the operation will be saved in this variable. Click the **Done **icon to save the properties.
      ![MSSQL node configuration](/resources/Storage/how-to-articles/mssql_4.png)
8. Drag and drop a **HTTP Response** node next to the **SQL** node and connect the nodes to create the service flow. The flow should look like:![server flow to insert a record in MSSQL DB](/resources/Storage/how-to-articles/mssql_5.png)
9. Double-click the **HTTP Response **node to configure the node.
  1. Enter the node name as **HTTP Response**.
  2. Select **JSON Object **as the **Response Types**.
  3. Enter the **HTTP Code** as **200**.
  4. Map the** Response Body** to string and enter **success**. Save the changes.
      ![HTTP Out node](/resources/Storage/how-to-articles/mssql_6.png)
10. Now when you [call the server flow from the application](/smart/project-how-to-articles/call-a-server-flow-from-page), the document entered in the **MSSQL **node gets inserted into the database.
