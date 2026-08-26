# Validate Entity Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/validate-entity-properties>

**Required Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Name | Unique name to identify the Update node. This name will be displayed on the canvas once you save the node. |  |
| Data Model | The data model for which the find nodes are being used. | Select a data model from the drop-down list. |
| Entity | Select the entity for the operation. If the data model consists of multiple entities, the entity list is displayed in the dropdown. |  |
| Selected Entity's Attributes | Displays the list of attributes for the selected entity. | This is a read-only property. |
| Validate Object | Refers to the attribute that has to be validated. | Map this field to bh., bh.input, bh.local, and as is property. Value: Should be an object or a list of objects in JSON format. |

**Optional Properties**

| **Property** | **Description** | **Values** |
| --- | --- | --- |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. | If you specify bh.local.result in this field, then that local property result will hold the response of the HTTP Request. |
