# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-cursor-node>

This is the default topic template.

The **Cursor** node is used to iterate an index or an object within the [IndexedDB database](/articles/flow-designer-guide/indexeddb-nodes) using a key range. An object store is sorted internally by key. Given a query, a cursor traverses the object store and returns one key/value at a time.

Cursors are used as an alternate to the Get operation (which returns an array of keys/values). If the object storage is bigger than the available memory, then the **Get** operation will fail to get all records as an array. In such situations, cursors are used to traverse the object storage, given a query, and return one key/value at a time, thus saving memory.

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Store Name**: The store on which you want to perform transactions. Enter the flow object containing the object store name.**Connection Instance**: The connection Instance that you acquired after connecting to the indexedDB database using the [Connect](/articles/flow-designer-guide/psd-connect-node) node.**On Success Callback**: The event to be returned on the success of the operation.**Where**: The key or key range that identifies the record to be retrieved. For example, if you enter IDBKeyRange.Bound(1,3), then **3** records are retrieved.**Key Index Name**: Optional. You can retrieve records in an object store through the primary key or by using an index. An index lets you look up records in an object store using properties of the values in the object stores records other than the primary key. Enter the name of the Index (that you have configured in the [IndexedDB connection](/articles/flow-designer-guide/psd-connect-node/a/h4_1029794690)) that is to be used to search records.**Transaction Object**: Optional. The result mapping variable of the [Transaction](/articles/flow-designer-guide/psd-transaction-node) node.
