# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/session-node>

A **session node** can be used as a server-side storage of information that is desired to persist throughout the user's interaction with the web site or web application.

### How to use

- Open the Services editor window.
- Click the plus icon to add a new service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **Session **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated attributes

- **Operation type**: The type of operation the session node performs. Select the operation from the drop-down list.
  - **Update**: Updates the session data.![The session node properties](/resources/Storage/server-services-designer-9/session_node.png)
  - **Destroy**: Destroys the session.
  - **Get**: Gets session data.
- **Result Mapping**: The data that you want to pass to the session. This property appears when you choose the** get **and** update **operation. You can map the data to bh.local or bh.input properties. See [properties](/articles/server-services-designer-9/properties-in-server-services) to learn more.
