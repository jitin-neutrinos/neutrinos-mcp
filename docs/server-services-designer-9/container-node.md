# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/container-node>

A container is a collection of documents and files. The container node helps you create, read, update, and delete items in a container by using methods on the Container object.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select CosmosDB Config:** The name of the config.
  - If you have an existing CosmosDB configuration, choose that config from the drop-down list.
  - If you want to create a new CosmosDB configuration, select **Add new config** from the drop-down list and click the **Map** icon to configure a new config. See [Attributes for a new CosmosDB Config](/articles/server-services-designer-9/cosmosdb-node/a/newcosmosdbconfig) to know what are the properties to configure.
4. **Container Operations: **
  1. **Create a container if it does not exist: **To create a container if the container does not exist.
    - **Container ID:** The ID for the container that you are creating.
  2. **List containers for a container:** To list all the containers for a database account.
  3. **Read a container definition**: To read/display a container.
    - **Container ID**: The container ID on which you want to read or get details.
  4. **Delete a container: **To delete a container.
    - **Container ID**: The container ID of the container that you want to delete.
5. **Partition Key: **Enter the key value associated with the a container.
6. **Options: **The additional options to perform the operation on the containers.
7. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.
