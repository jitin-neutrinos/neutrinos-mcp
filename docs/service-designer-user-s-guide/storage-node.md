# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/storage-node>

A** Storage** node is used to store, retrieve, or manipulate data in the local or session storage of the browser. The data is stored in **key-value** pairs, and you can only store a string value.

- **Local storage** is a type of web storage that allows websites and apps to store and access data right in the browser with no expiration date. This means the data stored in the browser will persist even after the browser window has been closed.
- **Session storage** is similar to local storage; the only difference is while data stored in the local storage has no expiration time, the data stored in session storage gets cleared when the page session ends.

### How to Use

- Open the Services editor window.
- Click the** plus** icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Switch **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with the **Start** node.
- After the flow is created, import the service flow to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

1. **Name**: A unique name for the node. This name will display on the canvas when you save the node.
2. **Operation Type**: The type of operation the node should perform. Select an operation type from the drop-down list. The fields to configure the operation changes depending on the operation type that you select. ![](/resources/Storage/service-designer-user-s-guide/get_item.png) 2. **Set Item****:** This method allows you to store values in the browser's local storage object. Fields to configure for this operation type:  3. **Remove Item**: This method allows you to remove a value from the browser's local storage object. The field to configure for this operation type:  4. **Clear**: This method, when invoked clears the entire storage of all records for that domain.
  1. **Get Item**: This method allows you to access the data stored in the browser’s local storage object. Fields to configure for this operation type:
  - **Storage type**: Select a storage type from the drop-down list. You can get the item from local storage or session storage.
  - **Key**: The element from which you want to retrieve the data. Select string as the key type and enter the key value. Or select the bh.local or bh.input property from the drop-down list and enter the variable name.
  - **Result mapping**: The element to which you want to map the data. You can map the retrieved data to bh.local or bh.input parameters.
