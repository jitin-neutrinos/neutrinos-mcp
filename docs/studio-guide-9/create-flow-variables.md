# Create Flow Variables in the Start node

<https://documentation.neutrinos.com/articles/#!studio-guide-9/create-flow-variables>

You can create[flow variables](/smart/project-page-services-designer-guide/properties-page-designer) in the [Start](/smart/project-page-services-designer-guide/start-node) and [Script](/smart/project-page-services-designer-guide/script-node) nodes of a flow.

#### Create Flow Variables in the Start node

1. Drag and drop a **Start** node to the Page Designer editor.
2. Create input variables in the** Input variables** field.
  1. Enter an input key
  2. Enter the value to be associated with the key.
  3. If you want to access this variable outside the flow, assign it to be an output variable by toggling the **Output **field to True.
  4. Click the **Add** icon to add the variable to the node.
3. Create local variables in the **Local Variables** field.
  1. Enter a local key
  2. Enter the value to be associated with the key
  3. If you want to access the local variable outside the flow, assign it to be an output variable by toggling the **Output** field to True.
  4. Click the **Add** icon to add the variable to the node.

If you want to set input or local variable as type Output (so that the variable can be accessed outside the flow), then you can create the variable only in the Start node and toggle the

Output

to

Tru

e.

#### Create Flow Variables in the Script node

To create bh.input and bh.local variables on the [Script](/smart/project-page-services-designer-guide/script-node) node, perform the following steps:

1. Drag and drop a **Script** node.
2. In the **Code Editor**, add the code to create one or more variables. If a variable exists, its value will be updated, else a new variable will be created. For example:Copy CodeJavaScriptbh.input.ApiURL='http://localhost:24483/';
   bh.local.city='Goa';

You cannot create flow variables of type **output **in the** Script** node. You have to use the **Start **node to do this operation.
