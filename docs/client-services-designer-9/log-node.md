# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/log-node>

A **Log node** is used to log variables that the user has given in the browser console. The information logged using this node is useful in debugging and auditing. This is an end node as it is always added to the end of the flow.

### How to Use

- Open the Services editor window.
- Click the **plus** icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Log **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start n**ode.
- After the flow is created, import the service to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.
- **Log:** Logs information based on the property that you select. You can log the bh. property which is the global object containing input, system, and local properties, or you can:
  - Log the bh.input property
  - Log the bh.local property
  - log the file **as is**
  - Log the file as a **string**

The whole object will be logged if you do not configure the **`Log`** node (as the `bh.` type is selected by default). Also, if you select `bh.input.` and enter **body **as the variable, only the body variable is logged. If you select bh.input. without specifying a variable, then all the input variables are logged.
