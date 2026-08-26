# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/item-node>

An Item is a document or a file stored in a container. Each Item must include an id key with a value that uniquely identifies the item within the container. The Item node allows you to perform operations on the items stored inside a container.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select CosmosDB Config:** The name of the config.
  - If you have an existing Cosmos DB configuration, choose that config from the drop-down list.
  - If you want to create a new CosmosDB configuration, select **Add new config** from the drop-down list and click the **Map** icon to configure a new config. See [Attributes for a new CosmosDB Config](/articles/server-services-designer-9/cosmosdb-node/a/newcosmosdbconfig) to know what are the properties to configure.
4. **Container ID: **The container ID in which the item resides.
5. **Item Operations: **Select the type of operation this node should perform.
  1. **Create items: **To create an item inside a container.
    - **Input**: Enter the file that has to be created.
  2. **Read all items in a container**: To read all items from a container.
  3. **Read an item by ID**: To read a particular item by item ID.
    - **Items ID**: Enter the ID of the item which you want to read.
    - Partition Key: Enter the key value associated with the item in a container.
  4. **Delete an Item**: Select this operation to delete an item inside a container.
    - **Item ID**: Enter the ID of the item which you want to delete.
    - Partition Key: Enter the key value associated with the item in a container.
  5. **Replace an item**: To replace one item with another item inside a container.
    - **Item ID**: Enter the ID of the item which you want to replace.
    - **Replace item**: Enter the item that has to be replaced with the item ID you have entered.
    - Partition Key: Enter the key value associated with the item in a container.
  6. **Query for documents**: To perform SQL operations on the item.
    - **Query**: Enter the query you want to perform.
    - **Parameters Array**: Enter the parameters you want to pass for the query.
6. **Options: **The additional options to perform the operation on the items.
7. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.
