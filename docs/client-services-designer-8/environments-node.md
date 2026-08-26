# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/environments-node>

The **Environment** node is used to map environment properties to flow variables such as bh.local and bh.input. The environment properties are part of the **Environments** editor in the Studio Application page. See [Define Environments](/smart/project-sample-how-to-guide/what-is-an-environment) to learn more.

### How to Use

- Open the Services editor window.
- Click the** plus** icon to add a new service or open an existing service from the service list.
- From the Nodes Palette, drag and drop an **Environment** node to the service designer.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start** node.
- After the flow is created, import the service flow to an application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.

- **Map Properties:** Used to map environment properties to a flow variable. To map a property:
  1. Select the type of flow variable that you want to map. The bh.input variable is selected by default. See [properties](/articles/service-designer-user-s-guide/service-designer-variables) to learn more.
  2. Enter the value of the flow variable.
  3. Select the environment property that you want to map the flow variable to.

If you modify any property or add a property in the **Environments** editor, you can click the **R****efresh **icon to get the latest properties to appear in the** Env Property **drop-down list. Click the **+** icon to add the property to the list.
