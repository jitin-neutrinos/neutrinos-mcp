# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/start-node>

The **Start node** is the entry point for a flow. You can use this node to initialize the bh.local and bh.input properties and create a function for the flow. The function created in the start node represents the flow and can be called by the **Call Service** node. See [Properties in Server Services](/articles/server-services-designer-8/properties-in-server-services) to learn more about the bh. properties.

### How to Use

- Open the Services editor window.
- Click the** plus icon** to add a new service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **Start** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **an HTTP In node.**

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.![Start node properties](/resources/Storage/server-services-designer-8/start_latest.png)
- **Function Name****: **This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-services-designer-8/call-service-node) node.

- **Accept flow object: ** Enable this toggle button to use the flow object defined in the flow that calls the **Start** node. Keep this toggle button disabled if you want to define new flow objects to be used. Flow objects include:

**Input variables****:** Use this field to initialize the input variables for the flow. These variables provide input to the flow. After creating these variables, you can call the flow from the [Call Service](/articles/server-services-designer-8/call-service-node) node using the function name generated, and pass the variables to that function. To add an input variable:

- Enter an input key
- Choose the type of value to be associated with the key. You can select **string**, **number**, **boolean**, or **null**.
- Enter a value to be associated with the key.
- If you want the output of the function to return the input variables, toggle the **Output** button to true.
- Click the **+ icon **to add the variables.

**Local variables:** Use this field to initialize the local variables for the flow. Local variables are private to the flow and cannot be accessed outside the flow. If you want to access this variable outside the flow, you should set the variables as output variables. To add a local variable:

Once created, these variables can be referred to as bh.input and bh.local variables, See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects.
