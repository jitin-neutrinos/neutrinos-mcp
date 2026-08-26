# Validate node's properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/validate-node>

The validate node is used for validating the objects in an entity of a data model. Validate node authenticate an object against the schema defined for the data model.

**How to use: **

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Validate node to the canvas.
4. Define the properties in the validate node.

### Validate node's properties

You can find the description of the required and optional properties in validate node below.

**Required Property**

| **Property Name** | **Description** | **Values** |
| --- | --- | --- |
| Name | Unique name for the node. This name will be displayed on the canvas when you save the node. |  |
| Data Model | The data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| [Entity](/smart/project-concepts/entity) | Select the entity for the operation. If your data model consists of multiple entities, the entity list will be displayed in the dropdown. |  |
| Selected Entity's [Attribute](/smart/project-concepts/attributes) | Displays the list of attributes in the selected entity. | This is a read-only property. |
| Validate Object | Refers to the attributes that needs to be validated. | Map this field to bh., bh.input, bh.local, and as is property.Value: Should be an object or a list of object in JSON format. |

**Optional Property**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. | For example, if you specify bh.local.result in this field, then that local property result will hold the response of the HTTP Request. |
