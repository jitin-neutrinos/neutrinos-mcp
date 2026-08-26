# Middleware Sequences

<https://documentation.neutrinos.com/articles/#!concepts-publication/middleware-sequence>

## Middleware Sequences

**Mi****ddleware Sequences **are flows that change the behavior of an HTTP request coming(from the client). It is used to modify the HTTP flow.

Apart from modifying HTTP requests, the middleware sequence also gives you access to the next() function (denoted by the **Next** node in the sequence) which is used to pass the control to the next middleware sequence in the flow before the request ends.

Middleware sequences are of two types:

- [Global Middleware Sequence](/articles/concepts-publication/middleware-sequence/a/h3_1547994352)
- [Route Middleware Sequence](/articles/concepts-publication/middleware-sequence/a/h3__1478205622)

---

### Global Middleware Sequence

By default, the middleware workspace contains a global middleware flow with four nodes - **Global middleware Start**, **CORS**, **Global next**, and **Global middleware End**. This default flow is called the global middleware sequence and is executed for each incoming HTTP request from the client.

Only the CORS node in this sequence is editable. CORS stands for Cross-Origin Resource Sharing. See [CORS](/smart/project-server-side-service-designer/cors-node) documentation to learn how to configure this node.

| ![Information](/resources/Storage/concepts-publication/project-server-side-service-designer/info.png) | You cannot configure properties for the default nodes in the Global Middleware sequence (Global middleware start, Global Next, Global Middleware end). |
| --- | --- |

---

### Route Middleware Sequence

Route Middleware Sequences are used to modify a particular HTTP request coming from the client. You can create a route-level middleware sequence by clicking the "**Add sequence**" button on the top of the middleware workspace. The **Add sequence **button adds a flow with three default nodes to the workspace. The three nodes for the route-level sequence are **Route middleware Start**, **Next**, and **Route middleware End**. You can only configure properties for the **Route middleware Start**. You cannot delete them.

**![Route middleware sequence](/resources/Storage/concepts-publication/project-server-side-service-designer/route_mid_seq.png)
**

On adding the **route middleware sequence**, the name of the **R****oute middleware start **node is auto-generated with a** sequence id**. You can double-click the node to change its name.
