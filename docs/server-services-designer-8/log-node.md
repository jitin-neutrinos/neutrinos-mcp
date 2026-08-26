# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/log-node>

A **Log** node is used to log variables that the user has given in the browser console. The information logged using this node is useful in debugging and auditing. This is an** end **node as it is always added to the end of the flow.

### How to Use

1. Open the Services editor window.
2. Click the** plus icon** to add a new server-service or open an existing service from the service list.
3. Create a Server service flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.
4. Drag and drop a **Log** node to the end of the server service flow.
5. Drag and drop other nodes to create a flow.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node. ![Log node properties](/resources/Storage/server-services-designer-8/lognode.png)
- **Log Level:** Choose the Log Level of the server flow. See **Types of Logs** in the [Configure Logger Settings](/smart/project-sample-how-to-guide/configure-logger) documentation to learn more. Make sure you choose the log level equal to or lesser than the one configured in the **Settings** editor. Else, the log level of this node will be ignored.
- **Log: **Logs information based on the property that you select. You can log the bh. property which is the global object containing input and local properties, or you can:
  - Log the bh.input property
  - Log the bh.local property
  - log the file **as is**
  - Log the file as a **string**

The whole object will be logged if you do not configure the **Log** node (as the bh. type is selected by default). Also, if you select bh.input. and enter **body** as the variable, only the body variable is logged. If you select bh.input. without specifying the variable, then all the input variables are logged.
