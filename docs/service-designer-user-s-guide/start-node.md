# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/start-node>

A **Start node** is the entry point for a flow. Every service or flow should start with a **Start** node.

When you create a **Start** node and call the flow, a system-defined object called bh is created by default. When you create input and local properties in the **Start **node, they are added to the bh object. Therefore, every input property can be referenced using bh.input.<property> and every local property can be referenced using bh.local.<property> from the node's attributes window. If you want to access the local and input properties outside the flow, you should set them as output variables. See [Setting a property as an output variable](/articles/service-designer-user-s-guide/service-designer-variables/a/h4__1268874902) to learn more.

### How to Use

- Open the Services editor window.
- Click the** Plus **icon to add a new service or open an existing service in the service list.
- From the Nodes Palette, drag and drop a **Start** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a Start node.
- After the flow is created, import the service to an application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name: **A unique name for the node. This name will display on the canvas when you save the node.
- **Function Name****: **This is a **read-only** field. The function name gets generated based on the name of the node that you entered in the **Name **field. To call the flow, you can use this function name in the component where the service is injected.

- **Input Properties****:** Use this field to specify input parameters for the flow. These parameters provide input to the flow. After creating these parameters, you can call the flow (from a page or a service) using the function name generated, and pass the parameters to that function. To add an input parameter:
  - Enter an input key. For example, cityname
  - Choose the type of value to be associated with the key. You can select **string**, **number**, **boolean**, or **null**.
  - Enter a value to be associated with the key.
  - If you want to access the property outside the flow, toggle the **Output** button to true.
  - Click **+ **icon to add the property.
- **Local Properties: **Use this field to specify local parameters for the flow. Local parameters are private to the flow and cannot be accessed outside the flow. If you want to access this variable outside the flow, you should set the variables as output variables. To add a local parameter:

After the properties are defined, you can reference the input property by using

bh.input.<property_name>

and the local property by using the bh.local.>property_name> in any node of the flow.
