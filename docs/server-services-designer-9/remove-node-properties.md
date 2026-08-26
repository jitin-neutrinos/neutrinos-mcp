# Remove Node Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/remove-node-properties>

The Remove node consists of the following properties.

**Required Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Name | Unique name to identify the Update node. This name will be displayed on the canvas once you save the node. |  |
| Data Model | The data model for which the find nodes are being used. | Select a data model from the drop-down list. |
| Entity | Select the entity for the operation. If the data model consists of multiple entities, the entity list is displayed in the dropdown. |  |
| Selected Entity's Attributes | Displays the list of attributes for the selected entity. | This is a read-only property. |
| Operation Type | Displays the type of operation to be performed on an entity. | Default  [operation types](/smart/project-concepts/operations): remove & removeByID. |
| Result mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. | For example, if you specify bh.local.result in this field, then that local property result will hold the response of the HTTP Request. |

**Optional Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Filter By | You can specify certain search criteria to remove specific rows by adding filter conditions. **Note:** This property is not available for the RemoveById operation type. | See [Filter by](/smart/project-concepts/filter-by) to learn more about this DM property. |
| ID | This attribute is only available when you are using operation type RemoveById. | Map this field to bh.local, bh. , bh.input & properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object. |
