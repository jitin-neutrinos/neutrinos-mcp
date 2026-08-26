# Modeler Elements

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/modeler-elements>

## Modeler Elements

To work with Neutrinos Modelr, you require these basic elements:

- [Nodes](/articles/neutrinos-modelr-guide/modeler-elements/a/h3_701845979)
- [Wires](/articles/neutrinos-modelr-guide/modeler-elements/a/h3__1499176760)
- [Flows](/articles/neutrinos-modelr-guide/modeler-elements/a/h3__2138058983)
- [Sub flows](/articles/neutrinos-modelr-guide/modeler-elements/a/h3_1864735701)

### Nodes

A node is a functionality which defines an action. Nodes can be added to the workspace by either:

- dragging them from the palette
- or importing from the library or clipboard

Nodes are joined together by wires via their ports. A node can have at most one input port and many output ports. A port may have a label that is displayed when the mouse hovers over it. A node may specify labels, for example, the Switch node shows the rule that matches the port. The labels can also be customized in the node edit dialog.

Some nodes display a status message and icon below the node. This is used to indicate the runtime state of the node - for example, the MQTT nodes indicate if they are currently connected or not.

![Node elements](/resources/Storage/neutrinos-modelr-guide/flow1.png)

If a node has any undeployed changes, it displays a blue circle above it. If there are errors with its configuration, it displays a red triangle.

Some nodes include a button on either its left or right edge. These allow some interaction with the node from within the editor. The Inject and Debug nodes are the only core nodes that have buttons.

#### Editing Node Configuration

A node’s configuration can be edited by double-clicking on the node or pressing `Enter` when the workspace has focus.

![Node Properties](/resources/Storage/neutrinos-modelr-guide/edit_inject_node.png)

The **Properties** section shows the edit form specific to the node type being edited.

#### Configuration Nodes

A Configuration (config) Node is a special type of node that holds a reusable configuration that can be shared by regular nodes in a flow.

For example, the **MQTT** In and Out nodes use an MQTT Broker config node to represent a shared connection to an MQTT broker.

The Configuration Nodes Sidebar can be used to manage all config nodes.

![The Config tab](/resources/Storage/neutrinos-modelr-guide/config.png)

---

### Wires

Nodes are wired together by pressing the mouse button on a node’s port, dragging to the destination node, and releasing the mouse button.

Alternatively, if the `Ctrl/Command` key is held down, the left-mouse button can be clicked (and released) on a node’s port and then clicked on the destination. If the `Ctrl/Command` key remains held and the just-wired destination node has an output port, a new wire is started from that port. This allows a set of nodes to be quickly wired together.

#### Moving wires

To disconnect a wire from a port, select the wire by clicking on it, then press and hold the `Shift` key when the left-mouse button is pressed on the port. When the mouse is then dragged, the wire disconnects from the port and can be dropped on another port. If the mouse button is released over the workspace, the wire is deleted.

#### Deleting wires

To delete a wire, first select it by clicking on it and then press the D`elete` key.

---

### Flows

A flow is a logical set of connected nodes which defines a task. You connect one or more nodes using wires, to create a flow.

To add a new flow, click ![](/resources/Storage/neutrinos-modelr-guide/add.png) in the top bar. To delete a flow, click the** Delete** button in the Flow Properties dialog.

#### Editing Flow Properties

To edit a flow’s properties, double-click on its tab in the top bar. This will open the Flow Properties dialog.

![Flow properties editor](/resources/Storage/neutrinos-modelr-guide/edit_flow.png)

Within the dialog, the flow’s name and description can be set. The description can use Markdown syntax for formatting and will appear in the [Information sidebar](https://nodered.org/docs/user-guide/editor/sidebar/info).

The Status property can be used to disable or enable the flow.

---

### SubFlows

A subflow is a collection of nodes that are collapsed into a single node in the workspace. They can be used to reduce some visual complexity of a flow, or to package up a group of nodes as a reusable flow used in multiple places.

Once created, the subflow is added to the palette of available nodes. Individual instances of the subflow can then be added to the workspace just like any other node.

#### Creating an Empty Subflow

A subflow can be created by selecting the **Subflow -> Create subflow** option in the menu. This will create a blank subflow and open it in the workspace.

#### Converting Nodes to a subflow

It is also possible to convert the current selection of nodes to a subflow by selecting the **Subflow -> Selection to Subflow** option in the menu. The nodes will be moved to a new subflow and replaced by a subflow instance node within the flow.

![Creating a subflow](/resources/Storage/neutrinos-modelr-guide/subflow.png)

This is only possible if any wires coming into the selection are connected to one node - as the resulting subflow node can itself only have at most one input.

#### Editing a Subflow

There are two ways to open a subflow to edit its contents. Either double click its node in the palette or click the **Edit flow template **button in the edit dialog of a subflow instance node.

The subflow is opened in the workspace as a new tab. Unlike regular flow tabs, subflow tabs can be closed to hide them.
