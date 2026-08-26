# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/service-variables-node>

This is the default topic template.

The **Service Variables **node is used to set and get the service variables of the flow. These variables are used to store data that can be accessed outside the flow without executing the flow.

### Node Properties

- **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Operation Type:** The type of operation the node should perform.
  - **Set service variables**: Use this option to set service variables of your flow to any value.
  - **Get service variables**: Use this option to get service variables of your flow and assign them to flow properties.
- **Select a Client Service: **Select the client service flow for which you want to get or set service variables.
- **Variables list**: Displays the list of variables added for the particular operation type.
  - To set a service variable:
    - Enter the page variable name that you want to create.
    - Select the [property type](/articles/flow-designer-guide/properties-page-designer) and enter the page or flow variable whose value you want to assign to the service variable.
    - Click the **+** icon to add the variable to the list.
  - To get a page variable:
    - Select the [property type](/articles/flow-designer-guide/properties-page-designer) and enter the service variable name that should store the value of the service variable that you fetch.
    - Enter the service variable name that is to be fetched.
    - Click the **+** icon to add the variable to the list.

To remove the variables added to the list, you can click the** Delete** icon next to the variable.
