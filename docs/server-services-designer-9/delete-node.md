# Remove Node

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/delete-node>

This node is used for creating service flows to delete records in an [entity](/smart/project-concepts/entity).

**How to use:**

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Remove node to the canvas.
4. Drag and drop other nodes to create a CRUD request.

**Delete Nodes' Properties:**

You can find the descriptions of the required and optional properties in Delete node below.

**Required Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Name | Unique name for the node. This name will be displayed on the canvas when you save the node. |  |
| Data Model | Select the data model for which you want to perform the delete operation. | Select a data model from the drop-down list. |
| [Entity](/smart/project-concepts/entity) | Select the entity for the operation. If your data model consists of multiple entities, the entity list will be displayed in the dropdown. |  |
| Selected Entity's [Attributes](/smart/project-concepts/attributes) | Displays the list of attributes in the selected entity. | This is a read-only property |
| [Operation Type](/smart/project-concepts/operations) | Displays the type of Update operation you can perform on an entity. | Default [operation types](/smart/project-concepts/operations): remove & removeByID |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map must be an object. | For example, if you specify bh.local.result in this field, then that local property **result** will hold the response of the HTTP Request. |

**Optional Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Filter By | You can specify certain criteria to remove specific rows by adding filter condition.**Note:** The filter by is attribute is not available for RemoveById operation type | See [Filter by](/smart/project-concepts/filter-by) to learn more about this DM property. |
| ID | This attribute is only available when you are using operation type RemoveById | Map this field to bh.local, bh. , bh.input & properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object |
