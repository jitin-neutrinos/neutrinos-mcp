# IndexDB configuration parameters

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-connect-node>

This is the default topic template.

The **Connect** node is used to establish a connection with the [IndexedDB database](/articles/flow-designer-guide/indexeddb-nodes). Once the connection is successful, the database returns a connection instance. You use this connection instance to perform any operation on the database.

#### IndexDB configuration parameters

This is the format of the configuration that is to be used to connect to the database:

```markdown
bh.configObj ={  name: ".<db_name>",  //The name of the db  version: 1,  //version of the db  objectStoresMetaByVersion: [    {      version: 1,      ObjectStoreMetadataArr: [        {          storeName: "<store_name>", //name of the store          storeConfig: {              keyPath: "<store_id>",  //path to an obj property that Indexed DB will use as a key, e.g. id              autoIncrement: true //if true,then the key for a newly stored obj is generated automatically          },          storeIndexes: [              // {              //     indexName: "indx_name",//the name ofDb index              //     keypaths: ["store_id"],               //     options: { //Accepts unique and multiEntry properties              //         unique: true,              //                       //     },              //     operation: 1               // }          ],          operation: 1 //operation which you want to perform(Choose 1 for CREATE,2 for DELETE,3 for UPDATE)        }                   ]    }  ]}
```

### Node Properties

**Name:** A unique name for the node.




 **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.




 **Config Object**: The object containing the configuration to the database. In your service flow, create an object using the [Script](/articles/flow-designer-guide/script-node) node and assign the IndexedDB configuration parameters to it. You can then specify the **Config object** name in this field and map it to the flow object. For example, in the **Script** node, you can assign the config parameters to an object named **ConfigObj** and call it in this field:

 ![Config object defined in the Script node](/resources/Storage/flow-designer-guide/script_connect.png)
 ![Config Object defined in the connect node](/resources/Storage/flow-designer-guide/config%20obj.png)




 **Connection Instance Mapping**: As a result of the connection, IndexedDB returns a connection instance. This instance can be used to perform operations on the database. Select the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) which should store this connection instance.
