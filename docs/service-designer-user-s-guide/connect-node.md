# IndexDB configuration parameters:

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/connect-node>

The** Connect** node is used to establish a connection with the [IndexedDB database](/articles/service-designer-user-s-guide/indexed-db-node). Once the connection is successful, the database returns a connection instance. You use this connection instance to perform any operation on the database.

#### IndexDB configuration parameters:

This is the format of the configuration that is to be used to connect to the database:

```javascript
bh.configObj ={    name: ".<db_name>",  //The name of the db    version: 1,  //version of the db    objectStoresMetaByVersion: [        {            version: 1,            ObjectStoreMetadataArr: [                {                    storeName: "<store_name>", //name of the store                    storeConfig: {                        keyPath: "<store_id>",  //path to an obj property that Indexed DB will use as a key, e.g. id                        autoIncrement: true //if true,then the key for a newly stored obj is generated automatically                    },                    storeIndexes: [                        // {                        //     indexName: "indx_name",//the name ofDb index                        //     keypaths: ["store_id"],                         //     options: { //Accepts unique and multiEntry properties                        //         unique: true,                        //                                 //     },                        //     operation: 1                         // }                    ],                    operation: 1 //operation which you want to perform(Choose 1 for CREATE,2 for DELETE,3 for UPDATE)                }                         ]        }    ]}
```

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Config Object:** The object containing the configuration to the database. In your service flow, create an object using a [Script](/articles/service-designer-user-s-guide/script-node) node and assign the [IndexDB configuration parameters](/articles/service-designer-user-s-guide/connect-node/a/h4__2068264276) to it. You can then specify the Config object name in this field and map it to the [flow object](/articles/service-designer-user-s-guide/service-designer-variables). For example, in the [Script](/articles/service-designer-user-s-guide/script-node)node, you can assign the config parameters to an object named **ConfigObj **and call it in this field:
    ![config parameters in script node](/resources/Storage/service-designer-user-s-guide/script_connect.png)![Config object in connect node](/resources/Storage/service-designer-user-s-guide/config%20obj.png)
4. **Connection Instance Mapping: **As a result of the connection, IndexedDB returns a connection instance. This instance can be used to perform operations on the database. Select the [flow object](/articles/service-designer-user-s-guide/service-designer-variables) which should store this connection instance.
