# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-insert-node>

This is the default topic template.

The **Insert** node is used to insert a record into an object store in the [IndexedDB database](/articles/flow-designer-guide/indexeddb-nodes).

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Connection Instance**: The connection Instance that you acquired after connecting to the IndexedDB database using the Connect node.**Transaction Object**: Optional. The result mapping variable of the [Transaction](/articles/flow-designer-guide/psd-transaction-node) node.**Insert Data**: The record that you want to insert into the object-store. It accepts an array of objects with the Object store name and record. Enter the flow object containing the array. For example, the array can be: Copy CodeMarkdownbh.insertData = [
 {
 objectStoreName: 'Student',
 record: {
 name: 'John',
 address: 'Bangalore'
 }
 }
];**Result Mapping**: The result of the operation. Enter the flow object in which you want to save the result.



 ![Information](/resources/Storage/flow-designer-guide/info.png)

 Object store names are case-sensitive. Make sure to use the right casing when you enter the object store name in the array.
