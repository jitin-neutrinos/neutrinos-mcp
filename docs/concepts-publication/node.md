# Node

<https://documentation.neutrinos.com/articles/#!concepts-publication/node>

### Node

A node is a function that defines an action. A Node generates code that is to be executed in the flow of a service. It may change the flow object or execute some code based on the inputs from the user during the execution of the flow.

*Example - On Init node*

Nodes can be added to the workspace by dragging them from the [nodes palette](/articles/concepts-publication/palette/a/h4__1538579060) and dropping them to the editor.

Nodes are joined together by [wires](/articles/concepts-publication/services-designer-elements/a/h3_2085108455) via their ports.

#### Ports

A node can have at most one input port and many output ports.

**Input port:** A node's input port is used to receive information from a node.

**Output port:** A node's output port is used to transfer information to a node.

For example, the **Call Service** node:

#### Attributes Window

You use the attributes window of a node to configure the functionality of the node. For example, the attributes window of the **Call Service** node:

Some nodes may need to connect to external systems to authenticate their credentials and perform CRUD operations. For such nodes, you also enter the configuration details of the external system using the Config field within the node. For example, the database config field in the [MSSQL node](/smart/project-server-side-service-designer/configure-mssql-database).

---

### Nodes on Neutrinos Studio

On Neutrinos Studio, a node is categorized into the following types:

#### Client node

This node is used to create services that perform operations on the app. Client nodes are available for you to use from the [Client Services Designer](/articles/concepts-publication/client-services-designer).

#### Server Node

This node is used to create services that perform operations on the server. Server nodes are available for you to use from the [Server Services Designer](/articles/concepts-publication/server-services-designer).

A server node can be a standalone node or can contain a Config node within it.

**Config** node A configuration node is used to create and share configurations across nodes. This node is not visible in the Services Designer but is a part of the node that needs some configuration. For example, this is how you access the config node used within the [SQL](/smart/project-server-side-service-designer/configure-mssql-database) node. It has the configuration settings required to connect to a SQL server:![](/resources/Storage/concepts-publication/project-node-builder-guide/config1.png)![SQL configuration](/resources/Storage/concepts-publication/project-node-builder-guide/config2.png)

#### Common node

This node is used to perform common functions such as catching node errors, logging variables, etc. on both client and server. Common nodes are available for you to use in [Page designer](/articles/concepts-publication/page-designer), [Client Services Designer](/articles/concepts-publication/client-services-designer), and [Server Services Designer](/articles/concepts-publication/server-services-designer).

#### Page node

This node is used to create page flows to perform any business logic on the page. This is available for you to use from the [Page Flow Designer](/articles/concepts-publication/page-designer/a/h3_520216706).
