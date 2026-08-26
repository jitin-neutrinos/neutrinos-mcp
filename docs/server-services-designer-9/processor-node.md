# Use Catch node to handle Errors

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/processor-node>

When you generate HTTP endpoints for the data model [operations](/smart/project-concepts/operations). Operation properties gives you the option to interpolate custom flows that gets executed during the operation. for example, you might want to execute some query before or after the database operation takes place.

Using DM processor node you can define such flows and later select them as pre/post operation flow in the [operation properties](/smart/project-concepts/operations).

DM processor node can also be used to create service flows that can be used as the processor flow for the [abstract data models](/smart/project-concepts/abstract).

**How to use:**

1. Open the Server Services editor window.
2. Open an existing server service or click the Add a Server Service button to add a new service.
3. In the Data Model Nodes Palette, drag and drop the Processor node to the canvas.

**Processor Nodes' Properties:**

The processor nodes property description is provided below:

**Name:** Unique name for the node. This name will be displayed on the canvas once you save the node.

**Bh Variables:** When you use processor node for a data model, a list of system-defined flow level variables (**bh variables**) gets created by default to access data model properties such as **model**, **filter**, **pageSize**, **offset**, **orderBy**, **data**, and **input**. When you use a pre/post flow in a database operation endpoints, these variables holds the data that are fetched from the data model in a key value pair.

**Note: **Bh variables in the processor node are defined as output variable by default.

| **Key** | **Description** |
| --- | --- |
| model | refers to the data model for which the processor node is being used. |
| filter | refers to the filter condition defined for the CRUD request |
| pageSize | refers to the numbers of rows will be displayed on the page |
| offset | refers to the offset clause specified for the CRUD request, which means the number of rows to be skipped before returning the response |
| orderBy | refers to the order (Ascending or Descending) in which the value of the attributes are returned |
| data | Refers to the data that gets persisted through the service flow |
| input | Refers to the input variable |

**Local variables:** Use this field to initialize the local variables for the flow. Local variables are private to the flow and cannot be accessed outside the flow. If you want to access this variable outside the flow, you should set the variables as output variables.

To add a local variable:

- Enter a local key.
- Choose the type of value to be associated with the key. You can select string, number, boolean, or null.
- Enter a value to be associated with the key.
- To set the variable as an output variable, toggle the Output button to true.
- Click the + icon to add the variable.

Once created, these variables can be referred to as bh.input and bh.local variables, See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects.

### Use Catch node to handle Errors

When you use the DM processor node to create a custom CRUD request that interacts with a database or a third-party application, you can use [Catch](/articles/server-services-designer-9/catch-node) node to capture any exception that has occurred during the flow. If an exception occurs on the server, it returns HTTP Error 500 -Internal server error as the response to the client through the response object.
