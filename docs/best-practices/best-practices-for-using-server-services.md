# Best Practices for Working with Server Services Designer

<https://documentation.neutrinos.com/articles/#!best-practices/best-practices-for-using-server-services>

# 

# Best Practices for Working with Server Services Designer

---

Follow these best practices while using the server service designer to create server flows for your apps: ![the server icon](/resources/Storage/best-practices/Artboard%2031%4072x-100.jpg)

### Middlewares configuration

Middleware sequences are used to change the behavior of the HTTP flow. Neutrinos provide you with some default middleware flows that you can further configure according to the functionality that you want to perform.

In Neutrinos Studio, once you enable the IDS settings for your server application, you can see some default flows created in the Middlewares services of the server service designer. The global middleware sequence is updated with three nodes, a CORS node, a custom middleware node, and a global session node. You can configure the CORS and Global session nodes.

You can customize these flows and configure the configurable nodes in these flows and add any functionalities.

### Creating reusable flows

Neutrinos enables you to make your app development life cycle easy and more efficient by allowing you to create reusable flows.

You can create server flows on the server Services Designer to perform a specific functionality and call it (reuse it) anywhere in your server flows where the functionality is to be executed.

To create a reusable flow, you use the **Start node**. This is because the start node generates the function name that denotes the flow and can be called from any other flow.

For example, here is a flow to which performs the **Get Authorization Params** functionality.

To reuse this flow in any other server flow, you make use of the **[Call service](/smart/project-service-designer-user-s-guide/call-service-node)** node.

![start node flow](/resources/Storage/best-practices/1.png) ![function name](/resources/Storage/best-practices/2.png)

In the call service node, select the **Service Name** and the **Flow Name** of the server flow that you want to reuse.

![reuse the flow](/resources/Storage/best-practices/get%20param%20reuse.png)

For example, if you have enabled **IDS **settings for the server application, you can see **[ids](/smart/project-server-side-service-designer/ids-sequence)**and **[idsutil](/smart/project-server-side-service-designer/ids-utility-sequence)** services created by default in the server services designer. These services have this best practice implemented in them. The **idsutil** server flows are reused in the **ids** server flows.

### Exception handling for server services

Server Services Designer(SSD) allows you to perform service-level exception handling by using the [Catch](/smart/project-server-side-service-designer/catch-node) node.

By default, if an exception occurs when a server flow is executed, the server flow halts and returns the **Internal server error - 500 error** as the response to the client. If you want to catch the exception and return some message to the client, you should include the **Catch **node in Server Services Designer.

When you drag and drop a **Catch **node to a service editor, it catches exceptions of all the nodes in that service.

You can customize this node and manually choose the nodes on which you want to catch errors. In such cases, if the** Catch** node is not enabled on the node on which the exception occurred, then, its exception will be passed to its previous node in the flow.

Every flow starts with an [HTTP IN](/smart/project-server-side-service-designer/http-in) node or a [Start](/smart/project-server-side-service-designer/start-node) node.

If the server flow starts with an **HTTP In** node, make sure that you have enabled the Catch node for the **HTTP In** node of the flow even if you have not enabled it for all the nodes in the flow. This is because In a server flow if an exception on the node is not caught, it will be passed to its previous node in the flow. So, the **HTTP In **node catches all the exceptions of the flow.If the server flow starts with the **Start** node, you need not enable exception handling for the nodes on the flow. Instead, you enable exception handling on the [Call Service](/smart/project-server-side-service-designer/call-service-node) node that calls the flow that was created with the Start node. This is recommended because the bh.input.req (request object) and bh.input.res (response object) exists only in the flow which has the **HTTP In** and **HTTP Out** nodes. when you use the **Call Service** node to call an existing flow, the exception is caught and sent back to the user using the response object of the **HTTP Out** node.

You can also create a flow after the** Catch** node to send a specific response back to the client, to send messages based on the type of error, etc. For example:

![Catch with HTTP Out node](/resources/Storage/best-practices/catch_http.png)

But you should make sure that you never enable exception handling for the nodes in this flow. Catching the error of the node that is connected to the Catch node will result in an infinite recursion.

### Storage nodes

Using Neutrinos Studio, you can drag and drop server nodes in the Storage Nodes section of the palette list, and configure server flows to integrate with Relational Database Management Systems such as MSSQL, MySQL, MariaDB, PostgreSQL, and Oracle SQL or connect to NoSQL databases such as MongoDB.

Follow these best practices while using the storage nodes to add a connection for a database:

- Give descriptive names for the configurations.
- Make use of Log node in the services that you create which are further useful for debugging and auditing.

![the log node in the flow](/resources/Storage/best-practices/log%20node.png)

- Use env property to avoid duplication and typos of the configurations. You can select the env property type for the configurations. Make sure that the environment property is already added to the [Environments](/articles/app-builder-s-user-guide/what-is-an-environment) editor before you specify it in the fields.

![The env settings](/resources/Storage/best-practices/ENV%20settigs.png) ![mongo db settings](/resources/Storage/best-practices/mongo.png)

Avoid giving multiple outputs from a single output port because the flow is not executed parallelly and the order of execution is not consistent due to which you can expect unusual behavior of the flow.

### Messaging nodes

**AMQP node**

In the AMQP node, you should not assert a different queue option for an existing queue. The AMQP 0-9-1 standard does not allow it and throws errors.
