# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/environments-node>

This is the default topic template.

The **Environment** node is used to map environment properties to the [flow variables](/articles/flow-designer-guide/properties-page-designer). The environment properties are defined in the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment)[editor](/smart/project-sample-how-to-guide/what-is-an-environment) of the [Studio Application page](/smart/project-concepts/studio-application-page).

### 

### Node Properties

- **Name:** The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **Map Properties:** Map environment properties to the flow variables. To map a property:
  1. Select the [property](/articles/flow-designer-guide/properties-page-designer) that you want to map.
  2. Enter a variable name.
  3. Select the [environment property](/smart/project-concepts/environment/a/h3_709278163) that you want to map to the flow variable.
  4. Click the **Add** icon to add the selection to the list.

If you modify or add a property in the **Environments** editor, click the **R****efresh **icon in the **Map properties** field to view the updated list.
