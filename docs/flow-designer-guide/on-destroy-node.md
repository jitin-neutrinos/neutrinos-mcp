# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/on-destroy-node>

This is the default topic template.

The **On Destroy **node is used to clean up the** page** component just before it is destroyed or deleted. This node unsubscribes observables and detaches event handlers to avoid memory leaks.

See [Lifecycle Events](/articles/flow-designer-guide/lifecycle-events) to learn more.

| ![Information](/resources/Storage/flow-designer-guide/info.png) | This node can be called only once per page. |
| --- | --- |

### Node Properties

- **Name: **The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
