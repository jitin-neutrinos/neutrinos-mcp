# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-transaction-node>

This is the default topic template.

The** Transaction** node is used to start a transaction with object stores in the IndexedDB database. You create a transaction with the IndexedDB database only if you want to create callbacks and perform operations on these callbacks. Else, you need not create a transaction as, by default, the Page Flow Designer creates one for you.

![Information](/resources/Storage/flow-designer-guide/info.png)

 Before performing a transaction, you should connect to the IndexedDB database using the [Connect](/articles/flow-designer-guide/psd-connect-node) node.

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Store Name**: The store name that the transaction is going to access. For example, page.storeName = ['Student'];.Provide an array of store names if you want to access multiple stores.**Connection Instance**: The connection instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/flow-designer-guide/psd-connect-node) node.**Event on Error**: Optional. The callback called when a request returns an error.**Event on Abort**: Optional. The callback called when the transaction is aborted.**Result Mapping**: The result of the operation. Map the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) which should save the result.
