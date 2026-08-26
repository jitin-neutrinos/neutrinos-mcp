# Executing the Sequence

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/configure-middlewares>

When you create an application, Neutrinos Studio creates a default [middleware sequences](/smart/project-concepts/middleware-sequence). You can further use the middleware workspace to configure the default sequence or create a new middleware sequence.

**Creating a Middleware Flow**

If you create a service flow using the **Middleware Start **node in that service, that middleware flow appears as a node under the **Service** category in the nodes palette of the **Middlewares workspace**. For example, if you have created a service named **check** and have created a service flow with the **Middleware Start **node named **userRole **in that service, you will see the node named **check:userRole** appear in the middleware nodes palette.

**Configuring the Middleware Flow**

You can drag and drop Middleware flows to the middleware workspace and add it to a global or route middleware sequence.

![service flow in middleware](/resources/Storage/app-builder-s-user-guide/server-side-service-designer-publication/mid_ser_flow.png)

If added to the global middleware sequence, this service flow is executed for every incoming HTTP request.

If added to a route middleware sequence, the service flow is executed for the HTTP endpoints that are configured to use this middleware sequence.

You can link the middleware sequence to the HTTP endpoints by configuring the **sequence id** in the **HTTP In** node.

![select middleware sequence](/resources/Storage/app-builder-s-user-guide/server-side-service-designer-publication/mid_seq.png)

### Executing the Sequence

The execution of the service flow in the middleware sequence depends on the placement of the flow. If you drag and drop the service flow before the **Next** node, the service flow will be executed before calling the other HTTP flows of the middleware sequence. If the service flow is dragged and dropped after the **Next **node, the HTTP flows in the global or route flows are executed before executing the service flow.
