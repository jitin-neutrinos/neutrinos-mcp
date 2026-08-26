# Integrate with a NoSQL Database

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/working-with-databases>

The applications built on Neutrinos can be easily integrated with your existing NoSQL databases without having to worry about data migration.

[Server services Designer (SSD](/smart/project-concepts/server-services-designer)) allows you to connect to NoSQL databases such as MongoDB to perform database operations by creating server flows.

In this example, you will learn how to create a server endpoint which when called from an application, connects to your existing MongoDB database and inserts a record into your database collection.

1. Open the **Server Services** editor from the Studio Application page.
2. Open an existing service or click the** Add a Server Service** button to add a new service.
3. From the Nodes Palette, drag and drop an **HTTP In** node to the workspace. The **HTTP In **node provides an API end-point for creating web services. In this example, we are creating an API endpoint called **mongoinsert**.
4. Double-click the node to open its **Properties** window.
  1. Enter the node name as** Insert record**.
  2. Select the **PUT** HTTP method.
  3. Enter the path as** mongoinsert**. Click the **Done **icon to save the properties.
      ![](/resources/Storage/how-to-articles-8/mong_httpin.png)
5. Drag and drop a **MongoDB** node next to the **HTTP IN** node and connect the nodes to create a flow. Double-click the **MongoDB **node and configure the node.
  1. Enter the name as **mongodb insert**.
  2. Click ![add database config](/resources/Storage/how-to-articles-8/add_db_config.png) to add a new MongoDB connection. In the **DB Config Properties** page, enter the following details:
    1. Enter a Database name. For example, **My DB settings**.
    2. Enter the MongoDB connection URI that you want to use to connect to your MongoDB deployment. For example- **mongodb://localhost:XXXX/ssd-mongo-node**.
    3. Click the **Done** icon.
        ![MongoDB configuration](/resources/Storage/how-to-articles-8/mong_conf.png)
  3. Enter the MongoDB **collection name**. For example - **data123**.
  4. Select **insertOne** as the operation.
  5. In the **Document** field, select **as is** and enter **{ _id: 16, "item" : "something", "qty" : 200 } **as the document to be inserted. If you have a bh.local or bh.input object that contains the document that you want to insert, you can select that property and enter the variable name.
  6. In the **Result mapping **field, select bh.input and enter the variable name as **res**. The response of the operation will be saved in this variable. Click the **Done **icon to save the properties.
      ![Mongo DB node configuration](/resources/Storage/how-to-articles-8/mongo_props.png)
6. Drag and drop an **HTTP Response** node next to the **Mongo DB** node and connect the nodes to create the service flow. The flow should look like this:
    ![server flow to insert a record in Mongo DB](/resources/Storage/how-to-articles-8/mongo_flow.png)
7. Double-click the **HTTP Response **node to configure the node.
  1. Enter the node name as **HTTP Response**.
  2. Select the **JSON Object **as the **Response Types**.
  3. Enter the **HTTP Code** as **200**.
  4. Map the** Response Body** to bh.input. res . Save the changes.
8. Now when you [call the server flow from the application](/articles/how-to-articles-8/call-a-server-flow-from-page), the document entered in the **MongoDB **node gets inserted into the database.
