# Node variables

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/start-node>

This is the default topic template.

The **Start **node is an entry point to a flow.

When you use this node, a system-defined object called bh is created by default. When you [create flow variables](/smart/project-sample-how-to-guide/create-flow-variables), they are added to this object. Therefore, every input variable can be referenced using bh.input. and every local variable can be referenced using bh.local. from the node's attributes window. If you want to access these variables outside the flow, you should set them as **output** variables. See [flow variables](/articles/flow-designer-guide/properties-page-designer/a/h3__1075892433) to learn more.

### Node variables

- **Name:** A unique name for the node.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. To call this flow on the UI, you use the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.
- **Input variables: **Use this field to specify input variables for the flow. These variables provide input to the flow. After creating them, you can call the flow (from a page) using the function name generated, and pass them to that function. If you want to access this variable outside the flow, you should set them as output variables by toggling the **Output** button to true.
- **Local variables:** Use this field to specify the local variables of the flow. Local variables are private to the flow and cannot be accessed outside the flow. If you want to access this variable outside the flow, you should set them as output variables by toggling the **Output** button to true.

To learn how to add input and local variables to the

Start

node, see

Create flow variables

.
