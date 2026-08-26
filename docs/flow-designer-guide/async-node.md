# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/async-node>

This is the default topic template.

The **Async **node allows you to select flows that should execute in an asynchronous manner, check if you are breaking the execution thread, and return the result as a promise array.

### Node Properties

- **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Result Mapping:** Map the data retrieved from the execution of flows to a [flow variable](/articles/flow-designer-guide/properties-page-designer).
- **Client Service Flow: **Toggle this button to True to select a flow designed on the [Client Services Designer](/smart/project-concepts/client-services-designer).
- **Select a Flow:** Select the flow that is to be executed asynchronously and click the **Add** button. You can select both a client flow and a page flow on the same **Async** node.
  - To select a client flow, enable the **Client Service Flow **toggle button.
  - After selecting the client flow, to select a page flow, disable the **Client Service Flow** button and select a page flow.
  - If you only want to select a page flow, keep the **Client Service Flow **toggle button disabled to view the list of page flows that are available to select.

If the flow (client, page, or both) that you have selected has input variables, they are displayed as a list below the selected flow. You can use the input variables as is, or assign them to a page or a bh object of this flow.

An example of selecting both client and page flow on the Async node:

![Async node with page and client flow selected](/resources/Storage/flow-designer-guide/async_both.png)
