# Use Catch node to handle Errors

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/dm-processor-properties>

| **Property** | **Description** |
| --- | --- |
| Name | Unique name to identify DM Processor. This name will be displayed on the canvas once you save the node. |
| Bh Variable | While using Processor Nodes, by default a pre-defined set of flow variables(bh variables) get created to access data model properties(model, filter, pagesize, offset, orderBy, data and input. When you use a pre-flow( before database operation) and post-flow (after database operation) in a database operation endpoints, these variables hold the data fetched from the data model in a key value pair. |
| **Bh Variable** |  |
| **Key** | **Output** |
| Model | Data model for which the processor node is being used. |
| Filter | Filter condition defined for the CRUD request. |
| PageSize | Number of rows that will be displayed on the page. |
| Offset | The offset clause specified for the CRUD request, which means the number of rows to be skipped before returning the response. |
| OrderBy | The order (Ascending or Descending) in which the value of the attributes are returned. |
| Data | Data that gets persisted through the service flow. |
| Input | Refers to the input variable. |

Local variables


 This field is used to initialize the local variables for the flow. Local variables are private to the flow and cannot be accessed outside the flow. If you want to access this variable outside the flow, you should set the variables as output variables.


 To add a local variable:




 Enter a local key.




 Choose the type of value that has to be associated with the key. The available values are:






 String




 Number




 Boolean




 Null






 Enter a value to be associated with the key.




 To set the variable as an output variable, toggle the Output button to true.




 Click the + icon to add the variable.



 Once created, these variables can be referred to as bh.input and bh.local variables, See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects.

#### Use Catch node to handle Errors

When you use the DM processor node to create a custom CRUD request that interacts with a database or a third-party application, a

Catch

node can be used to capture any exception that has occurred during the flow. If an exception occurs on the server, it returns HTTP Error 500 - Internal server error as the response to the client through the response object.
