# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/mongodb-node>

The** MongoDB **node is used to connect to and perform operations on the MongoDB database.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is enhanced in Neutrinos Studio release 7.1.0. Therefore, you will see more attributes if you are using Studio versions later than 7.0.2. |
| --- | --- |

### How to Use

- Open the **Server Services** editor window.
- Click the** plus icon** to add a new server service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **Mongodb **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **HTTP In** or **Start **node.

### Associated Attributes

- **Name: **Enter a name for the node. This name will display on the canvas when you save the node. ![MongoDB node](/resources/Storage/server-side-service-designer-publication/mongo_node.png)
- **Database Config: **The name of the database connection. If you have a database connection that you have already configured in the [Global Session](/articles/server-side-service-designer-publication/global-session-node) node, choose that connection from the drop-down list. If you want to configure a new database, click the **Map** icon.
  - **Type:** The type of database you are configuring. This is a **read-only** field with **MongoDB **selected by default.
  - **URL:** The MongoDB connection URI used to connect to a MongoDB deployment. The standard MongoDB URI can have following format: mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database] . Where,
      Component
      Description
      mongodb://
      A required prefix to identify that this is a string in the standard connection format.
      username:password@
      Optional. The authentication credentials. If specified, the client will attempt to log in to the specific database using these credentials after connecting.
      host[:port]
      Optional. The host (and optional port number) where the MongoDB instance is running. You can specify a hostname, IP address, or UNIX domain socket.
      /database
      Optional. The name of the database to connect to.
     Or, if you want to connect to the replica set, use mongodb + srv. For example, **mongodb+srv://kay:myRealPassword@cluster0.mongodb.net/test**. From the drop-down list, select **str** and enter the URI, or choose **env** and enter the environment property that contains the URI. The environment properties are created in the [Environments editor](/smart/project-sample-how-to-guide/what-is-an-environment/a/h3__1608926605)of Neutrinos Studio.
  - **Options (Stringified JSON):** An optional query string in name-value pairs. From the drop-down list, select **str** and enter the name-value pair. For example, select **str **and enter {"poolSize":7,"ssl":false}. Or, choose **env** and enter the environment property that contains the stringified JSON object. For the complete list of options, see [MongoDB documentation](https://mongodb.github.io/node-mongodb-native/3.4/api/MongoClient.html#.connect).
  - Click ![](/resources/Storage/server-side-service-designer-publication/correct.png) to save the MongoDB connection.
- **Collection:** The MongoDB collection name. MongoDB stores documents in collections. They are analogous to tables in relational databases. Map the collection to bh. or bh.local properties or select **string** from the drop-down list and enter the collection name.
- **Operation: **The operation that you want to perform on the MongoDB collection. To learn more about the operations that you can perform on MongoDB, navigate to the [MongoDB documentation](https://mongodb.github.io/node-mongodb-native/3.4/api/Collection.html#aggregate) and select the operation on the left pane. Neutrinos also provide Neutrinos specific operations that you can perform on MongoDB. The Neutrinos specific operations are **upload file**, **delete file**, **download file**, and **watch**. See [Examples for Neutrinos Specific operations](/articles/server-side-service-designer-publication/mongodb-node/a/neutrinosspecope) to know more.

**Based on the operation you select, the fields in the Attributes window will be updated. **

**Result Mapping: **Map the retrieved MongoDB records to bh., bh.input, or bh.local properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of the connection.**Options:** The optional settings that you can perform for each operation that you select in the** Operation** field. Map the options to bh. or bh.local properties and specify the variable name. Navigate to the [MongoDB documentation](https://mongodb.github.io/node-mongodb-native/3.4/api/Collection.html#aggregate) and select the operation from the left panel to view the options supported for each operation. For example, the options supported for find operation is documented in [Options for the** find** operation](https://mongodb.github.io/node-mongodb-native/3.4/api/Collection.html#find).![Options for the Find operation](/resources/Storage/server-side-service-designer-publication/find_options.png)

### Examples

#### Generic MongoDB operations

Here are a few examples for MongoDB specific operations configured in the MongoDB node:

#### find

- **Query:** The query to find the MongoDB records. Select bh. or bh.local properties and enter the variable which contains the query, or select** as is** from the drop-down list and enter the query.

![Find operation in MongoDB](/resources/Storage/server-side-service-designer-publication/mongo_find.png)

findOneAndUpdate

- **Filter:** Specify the filter that should be applied to the operation to select the document to update. Select bh. or bh.local properties and enter the variable which contains the filter, or select** as-is** from the drop-down list and enter the filter manually.
- **Update:** Enter the update operations to be performed on the document. Select bh. or bh.local properties and enter the variable which contains the update, or select** as is** from the drop-down list and enter the update manually. For example:

![The findOneAndUpdate operation](/resources/Storage/server-side-service-designer-publication/mongo_find_one_update.png)

countDocuments

- **Query:** The query for the count. Select bh. or bh.local properties and enter the variable which contains the query, or select** as is** from the drop-down list and enter the query.

![Count documents](/resources/Storage/server-side-service-designer-publication/mongo_count_docs.png)

createIndex

- **Field or Spec:** A string, array, or an object used to define the index. Select the bh. or bh.local properties and enter the variable which contains the field, or select** as is** from the drop-down list and enter the field.

![Create index in mongoDB](/resources/Storage/server-side-service-designer-publication/mongo_create_index.png)

dropIndex

- **Index name: **Specify the name of the index to drop. Select bh. or bh.local properties and enter the variable which contains the index name, or select** as is** from the drop-down list and enter the index name.

![](/resources/Storage/server-side-service-designer-publication/mongo_drop_index.png)

updateOne

- **Filter:** Specify the filter that should be applied to the operation to select the document to update. Select bh. or bh.local properties and enter the variable which contains the filter, or select** as is** from the drop-down list and enter the filter manually.
- **Update:** Enter the update operations to be performed on the document. Select bh. or bh.local properties and enter the variable which contains the update, or select** as is** from the drop-down list and enter the update manually.

![Update One operation](/resources/Storage/server-side-service-designer-publication/mongo_update_one.png)

updateMany

- **Filter:** Specify the filter that should be applied to the operation to select the document to update. Select bh. or bh.local properties and enter the variable which contains the filter, or select** as is** from the drop-down list and enter the filter manually.
- **Update:** Enter the update operations to be performed on the document. Select bh. or bh.local properties and enter the variable which contains the update, or select** as is** from the drop-down list and enter the update manually.

![](/resources/Storage/server-side-service-designer-publication/mongo_update_many.png)

insertOne

- **Document: **The document to insert. Select bh. or bh.local properties and enter the variable which contains the document, or select** as is** from the drop-down list and enter the document manually.

![insert one operation](/resources/Storage/server-side-service-designer-publication/mongo_insert_one.png)

deleteOne or deleteMany

- **Filter: **Specify the filter used to select the document to remove. Select bh. or bh.local properties and enter the variable which contains the filter, or select** as is** from the drop-down list and enter the filter.

![Delete one operation](/resources/Storage/server-side-service-designer-publication/mongo_delete_one.png)

![Delete many operation](/resources/Storage/server-side-service-designer-publication/mongo_delete_many.png)

aggregate

- **Pipeline: **Specify the array containing all the aggregation framework commands for the execution.

![Aggregate operation](/resources/Storage/server-side-service-designer-publication/mongo_aggregate.png)

#### Neutrinos Specific operations

Here are a few examples of Neutrinos specific operations configured on the MongoDB node:

uploadFile

- **File name**: The name for the file that you want to upload.
- **File path**: The path of the file that you want to upload. The path of the file can be a bh., a bh.input parameter, or a bh.local parameter.

![the upload file operation](/resources/Storage/server-side-service-designer-publication/mongodb-node-2020-02-24.png)

downloadFile

- **Filter**: Specify the filter used to select the document to remove. Select bh. or bh.local properties and enter the variable which contains the filter, or select** as is** from the drop-down list and enter the filter.

![the download file operation](/resources/Storage/server-side-service-designer-publication/mongodb-node-2020-02-24-2.png)

deleteFile

- **Document Id**: Specify the unique id of the document that you need to delete.

![the delete operation](/resources/Storage/server-side-service-designer-publication/mongodb-node-2020-02-24-4.png)

watch

- **pipeline**: Specify the array containing all the aggregation framework commands for the execution.

![the watch operation](/resources/Storage/server-side-service-designer-publication/mongodb-node-2020-02-24-3.png)
