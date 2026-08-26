# Update Node Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/update-node-properties>

The Update node consists of the following properties.

**Required Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Name | Unique name to identify the Update node. This name will be displayed on the canvas once you save the node. |  |
| Data Model | The data model for which the find nodes are being used. | Select a data model from the drop-down list. |
| Entity | Select the entity for the operation. If the data model consists of multiple entities, the entity list is displayed in the dropdown. |  |
| Selected Entity's Attributes | Displays the list of attributes for the selected entity. | This is a read-only property. |
| Operation Type | Displays the type of operation to be performed on an entity. | Default [operation types](/smart/project-concepts/operations): find & findByID |
| Filter By | You can specify certain conditions to update specific rows by defining the filter by property in the update node. Note: This property is not available for the UpdateById property type. | See [Filter by](/smart/project-concepts/filter-by) to learn more about this DM property. |
| Update Object |  | Map this field to local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the object. To map it to as is, select the property and enter the value in the following format: {AttributeName: ObjectValue} |
| ID | Refers to the attribute ID. This property is available only when you are using the operation type UpdateById | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object. |

**Optional Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Result mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. |  |
