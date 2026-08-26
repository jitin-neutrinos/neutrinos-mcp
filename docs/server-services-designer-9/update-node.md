# Update Node

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/update-node>

This node is used for creating service flows to update records in an [entity](/smart/project-concepts/entity).

**How to use:**

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Update node to the canvas.
4. Drag and drop other nodes to create a CRUD request.

**Update Node's Properties:**

You can find the descriptions of the required & optional properties in the update node below.

**Required Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Name | Unique name for the node. This name will be displayed on the canvas when you save the node. |  |
| Data Model | Select the data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| [Entity](/smart/project-concepts/entity) | Select the entity for the operation. If your data model consists of multiple entities, the entity list will be displayed in the dropdown. |  |
| Selected Entity's [Attributes](/smart/project-concepts/attributes) | Displays the list of attributes in the selected entity. | This is a read-only property |
| [Operation Type](/smart/project-concepts/operations) | Displays the type of Update operation you can perform on an entity. | Allowed [operation types](/smart/project-concepts/operations): update & updateByID |
| Filter By | You can specify certain conditions to update specific rows by defining the filter by property in update node**Note:** The filter by attribute is not available for UpdateById operation type | See [Filter by](/smart/project-concepts/filter-by) to learn more about this DM property. |
| Update Object |  | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object To map it to as is, select the property and enter the value in the following format: {AttributeName: ObjectValue} |
| ID | Refers to the Attribute ID**Note:** This property is only available when you are using the operation type UpdateById | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object |

**Optional Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map must be an object. | For example, if you specify bh.local.result in this field, then that local property **result** will hold the response of the HTTP Request. |
