# General Best Practices

<https://documentation.neutrinos.com/articles/#!best-practices-8/best-practices-for-using-server-services>

# 

# 

Follow these best practices while using the [Server Service Designer](/smart/project-concepts/server-services-designer). ![the server icon](/resources/Storage/best-practices-8/Artboard%2031%4072x-100.jpg)

### General Best Practices

- Organize related services within a single folder for easy navigation.
- Avoid giving multiple outputs from a single output port as the flow is not executed parallelly and the order of execution is not consistent. This may cause some unusual behavior in the flow.
- In the AMQP [producer](/smart/project-server-side-service-designer/amqp-producer-node) and [consumer](/smart/project-server-side-service-designer/amqp-consumer-node) nodes, do not assert a different queue option for an existing queue. The AMQP 0-9-1 standard does not allow it and throws errors.
- Use the [Async](/smart/project-server-side-service-designer/async-node) node when you want to execute flows that are independent of other flows.

### Middlewares configuration

[Middleware sequences](/smart/project-concepts/middleware-sequence) are used to change the behavior of the HTTP flow. Neutrinos provide you with some default middleware flows that you can further configure according to the functionality that you want to perform.

On Neutrinos Studio, once you enable the IDS settings for your server application, you can see some default [IDS service](/smart/project-server-side-service-designer/ids-services) flows created on the server service designer. The [global middleware sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) is updated with three nodes, a CORS node, a custom middleware node, and a global session node where you can configure only the CORS and Global session nodes and add custom functionalities that you desire.

### Creating reusable flows

Neutrinos enables you to make your app development life cycle easy and more efficient by allowing you to create reusable flows.

You can create server flows on the server Services Designer to perform a specific functionality and call it (reuse it) anywhere in your server flows where the functionality is to be executed.

To create a reusable flow, you use the **Start node**. This is because the start node generates the function name that denotes the flow and can be called from any other flow.

For example, here is a flow to which performs the **Get Authorization Params** functionality.

To reuse this flow in any other server flow, you make use of the [Call service](/smart/project-service-designer-user-s-guide/call-service-node) node.

![start node flow](/resources/Storage/best-practices-8/1.png) ![function name](/resources/Storage/best-practices-8/2.png)

In the call service node, select the **Service Name** and the **Flow Name** of the server flow that you want to reuse.

![reuse the flow](/resources/Storage/best-practices-8/get%20param%20reuse.png)

For example, if you have enabled **IDS **settings for the server application, you can see [ids](/smart/project-server-side-service-designer/ids-sequence)and **[idsutil](/smart/project-server-side-service-designer/ids-utility-sequence)** services created by default in the server services designer. These services have this best practice implemented in them. The **idsutil** server flows are reused in the **ids** server flows.

### Exception handling

You can perform node-level exception handling by using the [Catch](/smart/project-server-side-service-designer/catch-node) node.

By default, if an exception occurs when a server flow is executed, the server flow halts and returns the **Internal server error - 500 error** as the response to the client. If you want to catch the exception and return some message to the client, you should include the **Catch **node in your server flows.

When you drag and drop a **Catch **node to a canvas, it is configured to catch exceptions of all the nodes in that service.

You can customize this node and manually choose the nodes on which you want to catch errors.

If the** Catch** node is not enabled on the node on which the exception has occurred, then, its exception will be passed to its previous node in the flow.

If the server flow starts with an **HTTP In** node, make sure that you have enabled the **Catch** node for the **HTTP In** node of the flow even if you have not enabled it for all the nodes in the flow. This is because In a server flow if an exception on the node is not caught, it will be passed to its previous node in the flow. So, the **HTTP In **node catches all the exceptions of the flow.If the server flow starts with the **Start** node, you need not enable exception handling for the nodes on the flow. Instead, you enable exception handling on the [Call Service](/smart/project-server-side-service-designer/call-service-node) node that calls the flow that was created with the Start node. This is recommended because the bh.input.req (request object) and bh.input.res (response object) exists only in the flow which has the **HTTP In** and **HTTP Out** nodes. When you catch an exception in a [Call Service](/smart/project-server-side-service-designer/call-service-node) node in a flow, the caught exception can be used to send the response to the client using the **HTTP Out** node connected to the** Catch** node.

For example:

![Catch with HTTP Out node](/resources/Storage/best-practices-8/catch_http.png)

| ![Information](/resources/Storage/best-practices-8/info.png) | Do not enable exception handling for nodes in the flow that starts with the **Catch** node. Catching the error of the node that is connected to another Catch node will result in an infinite recursion. |
| --- | --- |

---

### Storage nodes

You can drag and drop server nodes in the **Storage **section of the palette list, and configure server flows to integrate with Relational Database Management Systems such as MSSQL, MySQL, MariaDB, PostgreSQL, and Oracle SQL or connect to NoSQL databases such as MongoDB.

Follow these best practices to add a connection to the database:

- Give descriptive names for the configurations.
- Make use of the [Log node](/smart/project-server-side-service-designer/log-node) in the services that you create which are further useful for debugging and auditing.

![the log node in the flow](/resources/Storage/best-practices-8/log%20node.png)

- Use the [env](/smart/project-server-side-service-designer/properties-in-server-services/a/h3_224841753) property to avoid duplication and typos of the configurations. You can select the env property type for the configurations. Make sure that the environment property is already added to the [Environments](/articles/app-builder-s-user-guide/what-is-an-environment) editor before you specify it in the fields.

![The env settings](/resources/Storage/best-practices-8/ENV%20settigs.png) ![mongo db settings](/resources/Storage/best-practices-8/mongo.png)
