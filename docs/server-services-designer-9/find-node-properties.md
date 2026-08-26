# Find Node Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/find-node-properties>

The Find node consists of the following properties.

**Required Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Name | Unique name to identify the Find node. This name will be displayed on the canvas once you save the node. |  |
| Data Model | The data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| Entity | Select the entity for the operation. If the data model consists of multiple entities, the entity list is displayed in the dropdown. |  |
| Selected Entity's Attributes | Displays the list of attributes for the selected entity. | This is a read-only property. |
| Operation Type | Displays the type of operation to be performed on an entity. | Default [operation types](/smart/project-concepts/operations): find & findByID |
| Result mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. | For example, if you specify bh.local.result in this field, then that local property result will hold the response of the HTTP Request. |

**Optional Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| FilterBy | You can specify certain search criteria to retrieve specific rows by adding filter clauses in JSON format. If no filter clauses are specified, all rows will be returned. Note: This property is not available for findById operation type. |  |
| OffSet | Specifies how many rows will be skipped from the result set of the query. |  |
| Order By | Indicates whether the attribute value must be sorted in ascending or descending order. | Map this field to bh.local, bh. , bh.input by clicking the Map icon, selecting the property, ASC or DESC Default value : ASC |
| Page Size | Specifies how many numbers of rows will be displayed on the page. This property is not available for findById. operation type. | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object. |
