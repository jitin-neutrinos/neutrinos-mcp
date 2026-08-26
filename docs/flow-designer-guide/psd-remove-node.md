# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-remove-node>

This is the default topic template.

The **Remove** node is used to delete a record or records from the object store in the [IndexedDB database](/articles/flow-designer-guide/indexeddb-nodes).

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Store Name**: The object store on which you want to perform transactions. Enter the flow object containing the object store name.**Primary Key Path Value**: The primary key path of the record(s) that you want to delete.**Transaction Object**: Optional. The result mapping variable of the [Transaction](/articles/flow-designer-guide/psd-transaction-node) node.**Result Mapping**: The result of the operation. Enter the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) in which you want to save the result.
