# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/insert-node>

The** Insert** node is used to insert a record into an object store in the [IndexedDB](/articles/client-services-designer-9/indexeddb-nodes) database.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Connection Instance**: The connection Instance that you acquired after connecting to the IndexedDB database using the [Connect](/articles/client-services-designer-9/connect-node) node.
4. **Transaction Object: **Optional. The result mapping variable of the [Transaction](/articles/client-services-designer-9/transaction-node) node.
5. **Insert Data:** The record that you want to insert into the object store. It accepts an array of objects with the Object store name and record. Enter the [flow object](/articles/client-services-designer-9/service-designer-variables)containing the array. For example, the array can be: Copy CodeJavaScriptbh.insertData = [
    {
    objectStoreName: 'Student',
    record: {
    name: 'John',
    address: 'Bangalore'
    }
    }
   ];
    **Note:** Object store names are case-sensitive. Make sure to use the right casing when you enter the object store name in the array.
6. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/client-services-designer-9/service-designer-variables)in which you want to save the result.
