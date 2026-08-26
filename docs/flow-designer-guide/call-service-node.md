# Node properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/call-service-node>

This is the default topic template.

The **Call Service **node is used to call an existing flow on Page Designer or on [Client Services Designer](/smart/project-concepts/client-services-designer).

### Node properties

- **Name: **The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **Client Service flow**: Enable this toggle button to select the flow created on [Client Services Designer](/smart/project-concepts/client-services-designer).
- **Flow selector**:
  - **Client Service flow**: If you enabled the **Client Service flow** toggle button, then select the client service flow you want to call from this node.
  - **Page flow**: Select the page flow you want to call from this node.

- **Input/Output Variables**: The input and output variables in the **Start** node of the called service. In the **Value** field, select the variable type and then enter the name to which you want to map the variable of the called service. See [Properties](/articles/flow-designer-guide/properties-page-designer) to learn more about the variables.

| ![Information](/resources/Storage/flow-designer-guide/info.png) | If you delete the flow that is called from this node, make sure you update or delete this node. Else, your flow will break. |
| --- | --- |
