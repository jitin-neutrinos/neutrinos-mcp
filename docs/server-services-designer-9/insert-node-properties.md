# Insert Node Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/insert-node-properties>

The Insert node consists of the following properties.

![](/resources/Storage/server-services-designer-9/Insertprops.png)

**Required Properties**

| Property | Description | Values |
| --- | --- | --- |
| Name | Unique name to identify the Insert node. This name will be displayed on the canvas once you save the node. |  |
| Data Model | The data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| Entity | Select the entity for the operation. If the data model consists of multiple entities, the entity list is displayed in the dropdown. |  |
| Selected Entity's Attributes | Displays the list of attributes for the selected entity. | This is a read-only property. |
| Insert Object | refers to the attribute that you want to insert in the entity. | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object. To map it to as is, select the property and enter the value in the following format: {AttributeName: ObjectValue} See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects. |

**Optional Properties**

| **Property** | **Description** | **Value** |
| --- | --- | --- |
| Result mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map must be an object. | For example, if you specify bh.local.result in this field, then that local property will hold the response of the HTTP Request. |
