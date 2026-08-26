# Working with Contexts

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/working-with-contexts>

## Working with Contexts

Modelr provides a way to store information that can be shared between different nodes without using the messages that pass through a flow. This is called **context**. The **scope** of a particular context value determines who it is shared with. There are three context scope levels:

- **Node** - only visible to the node that set the value
- **Flow** - visible to all nodes on the same flow (or tab in the editor)
- **Global** - visible to all nodes

The choice of scope for any particular value will depend on how it is being used. If a value only needs to be accessed by a single node, such as a **Function** node, then **Node** context is sufficient.

More often context allows some sort of state to be shared between multiple nodes. For example, a sensor may publish new values regularly in one flow and you want to create a separate HTTP triggered flow to return the most recent value. By storing the sensor reading in context it is then available for the HTTP flow to return. By default, context is stored in memory. It is also possible to create custom store plugins to save the data elsewhere.

---

### Context in a Flow

The easiest way to set a value in context is to use the **Change** node. For example, the following **Change** node rule will store the value of msg.payload in flow context under the key of myData.

![Context setting](/resources/Storage/neutrinos-modelr-guide/context.png)

Various nodes can access context directly. For example, the **Inject **node can be configured to inject a context value and the **Switch** node can route messages based on a value stored in context. If you have multiple context stores configured, the UI will allow you to pick which store a value should be stored in. The [Working with Functions](/articles/neutrinos-modelr-guide/writing-functions) topic describes how to use context in the **Function** node. Context can be permanently deleted by using a **Change** node set to delete.
