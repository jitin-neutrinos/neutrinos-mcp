# Insert Node

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/insert-node>

Insert node is used for creating service flows to insert a new record in an [entity](/smart/project-concepts/entity) of a Data Model.

**How to use**

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Insert node to the canvas.
4. Drag and drop other nodes to create a CRUD request.

**Insert Nodes' Properties **

You can find the descriptions of the required and optional properties in insert node below.

**![](/resources/Storage/server-services-designer-8/server-services-designer-preface-2022-02-28.png)**

**Required Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Name | Unique name for the node. This name will be displayed on the canvas when you save the node. |  |
| Data Model | The data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| [Entity](/smart/project-concepts/entity) | Select the entity for the operation. If your data model consists of multiple entities, the entity list will be displayed in the dropdown. |  |
| Selected Entity's [Attributes](/smart/project-concepts/attributes) | Displays the list of attributes in the selected entity. | This is a read-only property |
| Insert Object | refers to the attribute that you want to insert in the entity. | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the ObjectTo map it to as is, select the property and enter the value in the following format: {AttributeName: ObjectValue}See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects |

**Optional Properties**

| **Name ** | **Description** | **Value** |
| --- | --- | --- |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map must be an object. | For example, if you specify bh.local.result in this field, then that local property will hold the response of the HTTP Request. |
