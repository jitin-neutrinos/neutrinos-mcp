# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/page-variables-node>

This is the default topic template.

The **Page Variables** node is used to **get** and **s****et** page variables. See [Page properties](/articles/flow-designer-guide/properties-page-designer/a/h3_545829551) to learn more.

### Node Properties

- **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Operation Type: **The type of operation the node should perform.
  - **Set Page variables:** Use this option to set/add page variables.
  - **Get Page variables:** Use this option to get page variables and assign them to [flow variables](/articles/flow-designer-guide/properties-page-designer).
- **Variables list:** Displays the list of variables added for the particular operation type.
  - To set a [page variable](/articles/flow-designer-guide/properties-page-designer/a/h3_545829551):
    1. Enter the page variable name that you want to create.
    2. Select the [property type](/articles/flow-designer-guide/properties-page-designer) and enter the page or flow variable whose value you want to assign to the page variable. Or, select as is or string and enter the value of the page variable directly.
    3. Click the **+** icon to add the variable to the list.
  - To get a page variable:
    1. Select the property type
    2. Enter the variable name that should store the value of the page variable that you fetch.
    3. Enter the page variable name that is to be fetched.
    4. Click the **+** icon to add the variable to the list.

To remove the variables added to the list, you can click the **Delete** icon next to the variable.
