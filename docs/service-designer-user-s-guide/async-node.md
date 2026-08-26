# How to use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/async-node>

The **Async block node** allows you to create flows that execute in an asynchronous manner and checks that you are not breaking any execution thread. This also makes sure that the result is returned in the form of a promise array.

| ![Information](/resources/Storage/service-designer-user-s-guide/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to use

- Open the **Client Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.![async node properties](/resources/Storage/service-designer-user-s-guide/asyncnode.png)
- In the Nodes Palette, drag and drop the **Async block** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node**.

### Associated Attributes

1. **Name:** The name for the node. This name will display on the canvas when the node is saved.
2. **Result Mapping:** You can map the retrieved data from the execution of flows to bh, bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input parameter will hold the result of the variable in the selected output format.
3. **Flows to be called: **Select the flows to be called from the services in the order of execution.
  - **Select a service: **Select the service name in which the flow that you want to call exists. The drop-down list contains all the services that you have created in the client services.
  - **Select a flow: **Select the flow which you want to execute from the service that you have previously selected. The drop-down list contains all the flows created in the particular service that you select in the **Select a service** field.
