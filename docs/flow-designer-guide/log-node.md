# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/log-node>

This is the default topic template.

The **Log** node is used to log the page and flow variables on the browser console. The information logged on the console can be used for debugging and auditing purposes.

Log is an end node. It should be added to the end of the flow.

### Node Properties

- **Name:** The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **Log:** Logs the information of the variable that you specify.

If you drag and drop a** Log** node to the flow, and not make any changes, then all the variables assigned to the [page properties](/articles/flow-designer-guide/properties-page-designer/a/h3_545829551) are logged on the browser console as page. property is selected by default.

If you specify a property and enter the variable name (for example - bh.input.cityName) , then that variable will be logged. If you specify the property without specifying the name (for example - bh.input.), then all the variables of bh.input. type are logged.
