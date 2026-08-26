# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/on-init-node>

This is the default topic template.

The** On Init** node is used to initialize the page and set [page variables](/articles/flow-designer-guide/properties-page-designer/a/h4_1197862820). See [Lifecycle Events](/articles/flow-designer-guide/lifecycle-events) to learn more.

You can also use this node to access the values of the [system variables](/smart/project-service-designer-user-s-guide/system-defined-properties) that are set by Neutrinos Studio (for example, bh.system.environment) and assign them to page variables.

| ![Information](/resources/Storage/flow-designer-guide/info.png) | This node can be called only once per page. |
| --- | --- |

### Node Properties

- **Name: **The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
- **Page Input Variables:** Define the page variables of type **input. **These variables can be accessed using bh.pageInput.<input_variable_name> anywhere within the page flow.
- **Page Output Variables: **Define the page variables of type** output**. These variables can be accessed using bh.pageOutput.<output_variable_name> anywhere within the page flow. If you want to emit any data using these output variables, use the [Output](/articles/flow-designer-guide/output-node) node.
- **Page Local Variables: **Define the page variables of type **local**.
