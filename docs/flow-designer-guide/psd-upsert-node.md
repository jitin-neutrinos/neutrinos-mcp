# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/psd-upsert-node>

This is the default topic template.

The **Upsert** node is used to update a record (if the record exists) or create a new record in an object store of the IndexedDB database.

### Node Properties

**Name:** A unique name for the node.**Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.**Connection Instance**: The connection Instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/flow-designer-guide/psd-connect-node) node.**Transaction Object**: Optional. The result mapping variable of the [Transaction](/articles/flow-designer-guide/psd-transaction-node) node.**Upsert Data**: The record that you want to update or insert into the object store. It accepts an array of objects with the Object store name and record. Enter the flow object containing the array. For example, the array can be:Copy CodeMarkdownbh.upsertData = [
 {
 objectStoreName: 'Student',
 record: {
 name: 'John',
 address: 'Bangalore'
 }
 }
];**Result Mapping**: The result of the operation. Enter the [page or flow variable](/articles/flow-designer-guide/properties-page-designer) which should store the result.



 ![Information](/resources/Storage/flow-designer-guide/info.png)

 Object store names are case-sensitive. Make sure to use the right casing when you enter the object store name in the array.
