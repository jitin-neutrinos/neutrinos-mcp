# Find Nodes' Properties:

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/find-node>

This node is used for creating service flows that retrieve the records of an [entity](/smart/project-concepts/entity) of a data model based on specified criteria defined in the node's properties.

**How to use: **

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Find node to the canvas.
4. Drag and drop other nodes to create a CRUD request.

## Find Nodes' Properties:

You can find the description of the required and optional properties in find node below.

**Required Properties**

| **Property Name** | **Description ** | **Value** |
| --- | --- | --- |
| Name | Unique name for the node. This name will be displayed on the canvas when you save the node. |  |
| Data Model | The data model for which you want to perform the create operation. | Select a data model from the drop-down list. |
| [Entity](/smart/project-concepts/entity) | Select the entity for the operation. If your data model consists of multiple entities, the entity list will be displayed in the dropdown. |  |
| Selected Entity's [Attributes](/smart/project-concepts/attributes) | Displays the list of attributes in the selected entity. | This is a read-only property |
| [Operation Type](/smart/project-concepts/operations) | Displays the type of find operation you can perform on an entity. | Default [operation types](/smart/project-concepts/operations): find & findByID |
| Result Mapping | The bh. or bh.local property to which you want to pass the result of the CRUD request. The variable that you map should be an object. | For example, if you specify bh.local.result in this field, then that local property **result** will hold the response of the HTTP Request. |

**Optional Properties**

| **Property Name** | **Description** | **Value** |
| --- | --- | --- |
| Filter By | You can specify certain search criteria to retrieve specific rows by adding filter clauses in JSON format. If no filter clauses are specified, all rows will be returned.Note: This property is not available for findById operation type | See [Filter by](/smart/project-concepts/filter-by) to learn more about this DM property. |
| Page Number | It specifies the number of the page which will be displayed.This property is not available for findById operation type | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object |
| Order By | Indicates whether the attribute value must be sorted in an ascending or descending order.This property is not available for findById operation type | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the ObjectPossible Values: ASC or DESCDefault values: ASC |
| Page Size | It specifies how many numbers of rows will be displayed on the page.This property is not available for findById operation type | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object |
| ID | This attribute is only available when you use the operation type FindById | Map this field to bh.local, bh. , bh.input properties by clicking the Map icon, selecting the property, and inserting the variable name which contains the Object |

**Note:** If you are using MSSQL and want to use **Page Size** and **Page Number**, you must specify the **Order By** attribute as well.
