# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/storage-node>

This is the default topic template.

The **Storage** node is used to store, retrieve, or manipulate data in the local or session storage of the browser. The data is stored in key-value pairs, and can only store a string value.

- **Local storage** is a type of web storage that allows websites and apps to store and access data right in the browser with no expiration date. This means the data stored in the browser will persist even after the browser window has been closed.
- **Session storage** is similar to local storage; the only difference is while data stored in the local storage has no expiration time, the data stored in session storage gets cleared when the page session ends.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Operation Type: **The type of operation the node should perform. Select an operation type from the drop-down list. The fields to configure the operation changes depending on the operation type that you select.
  - **Get Item: **This method allows you to access the data stored in the browser’s local storage object. Fields to configure for this operation type are:
    - **Storage type:** Select a storage type from the drop-down list. You can get the item from local storage or session storage.
    - **Key: **The element from which you want to retrieve the data. Select string as the key type and enter the key value. Or, select the property type and enter the [variable](/articles/flow-designer-guide/properties-page-designer) which holds the value.
    - **Result mapping: **The element to which you want to map the data. You can map the retrieved data to any property type.
  - **Set Item:** This method allows you to store values in the browser's local storage object. The fields to configure for this operation type are:
    - **Storage type: **Select a storage type from the drop-down list. You can set the item to local storage, session storage, or both.
    - **Key:** The element to which you want to store the data. Select string as the key type and enter the key value. Or, select the property type and enter the [variable](/articles/flow-designer-guide/properties-page-designer) which holds the value.
    - **Value: **The data that you want to store.
  - **Remove Item: **This method allows you to remove a value from the browser's local storage object. The fields to configure for this operation type are:
    - **Storage type:** Select a storage type from the drop-down list. You can remove the item from local storage, session storage, or both local and session storage.
    - **Key:** The element which contains the data to be removed. Select string as the key type and enter the key value. Or, select the property type and enter the [variable](/articles/flow-designer-guide/properties-page-designer) which holds the value.
  - **Clear Storage: **This method clears the entire storage of all records for that domain.
    - **Storage type: **Select a storage type from the drop-down list. You can clear the data stored in local storage, session storage, or both.
