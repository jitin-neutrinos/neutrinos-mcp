# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-get-node>

This is the default topic template.

The **Get** node is used to fetch specific records from an object store in the [IndexedDB database](/articles/flow-designer-guide/indexeddb-nodes).

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Store Name**: The object store on which you want to perform transactions. Enter the flow object containing the object store name.**Connection Instance**: The connection Instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/flow-designer-guide/psd-connect-node) node.**Where**: The key or key range that identifies the record to be retrieved. For example, if you enter IDBKeyRange.Bound(1,3), then **3 records** are retrieved.**Limit**: Optional. The number of records that the operation should return. For example, if we set the limit as **2**, only two records will be retrieved.**Key Index Name**: Optional. You can retrieve records in an object store through the primary key or by using an index. An index lets you look up records in an object store using properties of the values in the object stores records other than the primary key. Enter the name of the Index (that you have configured in the [IndexedDB connection](/articles/flow-designer-guide/psd-connect-node/a/h4_1029794690)) that is to be used to search records.**Transaction Object**: Optional. The result mapping variable of the Transaction node.**Result Mapping**: The result of the operation. Enter the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) which should store the result.
