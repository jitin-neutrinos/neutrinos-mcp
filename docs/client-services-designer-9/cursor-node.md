# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/cursor-node>

The **Cursor **node is used to iterate an index or an object within the [IndexDB database](/articles/client-services-designer-9/indexeddb-nodes) using a key range. An object store is sorted internally by key. Given a query, a cursor traverses the object-store and returns one key/value at a time.

Cursors are used as an alternate to the [Get](/articles/client-services-designer-9/get-node) operation (which returns an array of keys/values). If the object storage is bigger than the available memory, then the **Get** operation will fail to get all records as an array. In such situations, cursors are used to traverse the object storage, given a query, and return one key/value at a time, thus saving memory.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Store Name:** The store on which you want to perform transactions. Enter the [flow object](/articles/client-services-designer-9/service-designer-variables)containing the object store name.
4. **Connection Instance:** The connection Instance that you acquired after connecting to the indexedDB database using the [Connect](/articles/client-services-designer-9/connect-node) node.
5. **On Success Callback:** The event to be returned on the success of the operation.
6. **Where: **The key or key range that identifies the record to be retrieved. For example, if you enter IDBKeyRange.Bound(1,3), then 3 records are retrieved.
7. **Key Index Name:** Optional. You can retrieve records in an object store through the primary key or by using an index. An index lets you look up records in an object store using properties of the values in the object stores records other than the primary key. Enter the name of the Index (that you have configured in the [IndexedDB connection](/articles/client-services-designer-9/connect-node/a/h4__2068264276)) that is to be used to search records.
8. **Transaction Object:** Optional. The result mapping variable of the [Transaction](/articles/client-services-designer-9/transaction-node) node.
