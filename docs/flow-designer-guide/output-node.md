# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/output-node>

This is the default topic template.

When you are [reusing the Page UI](/smart/project-sample-how-to-guide/views) as **Views** on Studio, the **Output** node is added to the child page (the view that is reused) to emit an event and send some data to the parent page.

### Node Properties

- **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you enter in the **Name** field. It is used to identify the node while debugging.
- **Event Name: **The event using which you will emit the data. The event name should already be defined in the [On Init](/articles/flow-designer-guide/on-init-node) node of the page before calling it in this node. When added in the **On Init** node, the event name will be saved in the bh.pageOutput.<event_name> property shortly displayed as Output. in this node.
   ![Output type](/resources/Storage/flow-designer-guide/output_type.png)
   If you want to map the event name to a string, a flow variable, or a page variable, select the  respective type from the drop-down list and enter the variable name which should store the event name.
- **Data:** The data to be sent to the parent page. You can map the data to any variable in the drop-down list. See [Properties in Page Designer](/articles/flow-designer-guide/properties-page-designer) to learn more about the property types.
