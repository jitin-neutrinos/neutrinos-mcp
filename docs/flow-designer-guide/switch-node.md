# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/switch-node>

This is the default topic template.

The **Switch** node is used to define conditions and make your flow take different paths based on these conditions.

### Node Properties

- **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Property**: The [page or flow variable](/articles/flow-designer-guide/properties-page-designer) that you want to evaluate against the conditions that you specify in the **Conditions** field.
- **Conditions: **A list of conditions that are to be evaluated against the variable specified in the **Property **field. To add a condition:
    For example:
    ![switch node conditions](/resources/Storage/flow-designer-guide/switch_conditions.png)
  1. Select a condition.
  1. Choose what is to be validated against the condition. Select number, string, or as is, and enter the value. Or, select the type of property and enter the variable name.
  2. Click the **Add** button.
- **Condition match:** If you have entered more than one condition, choose if you want to **check all the conditions** or **stop after the first match**.
