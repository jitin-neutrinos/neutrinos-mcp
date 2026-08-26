# How to Handle Exceptions in Server Apps?

<https://documentation.neutrinos.com/articles/#!how-to-articles/handle-exceptions-in-a-server-app>

## How to Handle Exceptions in Server Apps?

---

The [Server Services Designer(SSD)](/smart/project-concepts/server-services-designer) allows you to perform service-level exception handling by using the [Catch](/smart/project-server-side-service-designer/catch-node) node.

By default, if an exception occurs when a server flow is executed, the server flow halts and returns the **Internal server error - 500 error** as the response to the client. If you want to catch the exception and return some message to the client, you should include the **Catch **node in Server Services Designer.

When you drag and drop a **Catch **node to a canvas, it catches exceptions of all the nodes in that service.

You can customize this node and manually choose the nodes on which you want to catch errors. In such cases, if the** Catch** node is not enabled on the node on which the exception occurred, then, its exception will be passed to its previous node in the flow.

Every flow starts with an [HTTP IN](/smart/project-server-side-service-designer/http-in) node or a [Start](/smart/project-server-side-service-designer/start-node) node.

If the server flow starts with an **HTTP In** node, make sure that you have enabled the Catch node for the **HTTP In** node of the flow even if you have not enabled it for all the nodes in the flow. This is because In a server flow if an exception on the node is not caught, it will be passed to its previous node in the flow. So, the **HTTP In **node catches all the exceptions of the flow.If the server flow starts with the **Start** node, you need not enable exception handling for the nodes on the flow. Instead, you enable exception handling on the [Call Service](/smart/project-server-side-service-designer/call-service-node) node that calls the flow that was created with the Start node. This is recommended because of the bh.input.req (request object) and bh.input.res (response object) exists only in the flow which has the **HTTP In** and **HTTP Out** nodes. when you use the **Call Service** node to call an existing flow, the exception is caught and sent back to the user using the response object of the **HTTP Out** node.

You can also create a flow after the** Catch** node to send a specific response back to the client, to send messages based on the type of error, etc.

But you should make sure that you never enable exception handling for the nodes in this flow. Catching the error of the node that is connected to the Catch node will result in an infinite recursion.
