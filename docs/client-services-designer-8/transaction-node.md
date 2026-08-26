# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/transaction-node>

The** Transaction** node is used to start a transaction with object stores in the [IndexedDB](/articles/client-services-designer-8/indexeddb-nodes) database.

You create a transaction with the IndexedDB database only if you want to create callbacks and perform operations on these callbacks. Else, you need not create a transaction as, by default, Client Services Designer creates one for you.

| ![Information](/resources/Storage/client-services-designer-8/info.png) | You should connect to the IndexedDB using the [connect node](/articles/client-services-designer-8/connect-node) before performing a transaction. |
| --- | --- |

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Store Name:** The store name that the transaction is going to access. For example,** bh.storeName = ['Student']****;**.Provide an array of store names if you are going to access multiple stores.
4. **Connection Instance:** The connection instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/client-services-designer-8/connect-node) node.
5. **Event on Error:** Optional. The callback called when a request returns an error.
6. **Event on Abort:** Optional. The callback called when the transaction is aborted.
7. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/client-services-designer-8/service-designer-variables)in which you want to save the result.
