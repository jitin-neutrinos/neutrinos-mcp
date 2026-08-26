# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/async-node>

The async node allows you to invoke two or more flows asynchronously, and await their completion.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio release 7.1.0. You can access it from both Server Services Designer and Client Services Designer. |
| --- | --- |

### How to use

- Open the **Client/****Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- In the Nodes Palette, drag and drop the **Async block** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node**.

### Associated Attributes

1. **Name:** The name of the node. This name will display on the canvas when the node is saved. ![async node properties](/resources/Storage/server-services-designer-8/asyncnode.png)
2. **Result Mapping:** You can map the retrieved data from the execution of flows to bh, bh.local or bh.input properties. Select the parameter type and enter the variable that should hold the output. For example, if you specify bh.input.result in this field, then that input parameter will hold the result of the variable in the selected output format.
3. **Flows to be called: **Select the flows to be called from the services in the order of execution.
