# Associated Attributes

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/get-node>

The** Get** node is used to fetch specific records from an object store in the [IndexedDB](/articles/service-designer-user-s-guide/indexed-db-node) database.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Store Name:** The object store on which you want to perform transactions. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)containing the object store name.
4. **Connection Instance**: The connection Instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/service-designer-user-s-guide/connect-node) node.
5. **Where: **The key or key range that identifies the record to be retrieved. For example, if you enter IDBKeyRange.Bound(1,3), then 3 records are retrieved.
6. **Limit:** Optional. The number of records that the operation should return. For example, if we set the limit as 2, only two records will be retrieved.
7. **Key Index Name:** Optional. You can retrieve records in an object store through the primary key or by using an index. An index lets you look up records in an object store using properties of the values in the object stores records other than the primary key. Enter the name of the Index (that you have configured in the [IndexedDB connection](/articles/service-designer-user-s-guide/connect-node/a/h4__2068264276)) that is to be used to search records.
8. **Transaction Object:** Optional. The result mapping variable of the [Transaction](/articles/service-designer-user-s-guide/transaction-node) node.
9. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)in which you want to save the result.
