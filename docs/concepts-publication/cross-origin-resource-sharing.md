# Cross-Origin Resource Sharing (CORS)

<https://documentation.neutrinos.com/articles/#!concepts-publication/cross-origin-resource-sharing>

### Cross-Origin Resource Sharing (CORS)

**CORS **is a mechanism that uses additional HTTP headers to tell browsers to give a web application running at one origin, access to selected resources from a different origin.

A web application executes a cross-origin HTTP request when it requests a resource that has a different origin (domain, protocol, or port) from its own.

To prevent websites from tampering with one another, web browsers implement a security measure known as the same-origin policy. This policy lets resources such as JavaScript interact with resources from the same domain, but not with resources from different domains.

In cases where cross-domain scripting is desired, Cross-origin resource sharing (CORS) allows web developers to work around the same-origin policy and adds HTTP headers that instruct web browsers on how to use and manage cross-domain content. The browser then allows or denies access to the content based on its security configuration.

### How CORS Works

When a browser executes a script that references a resource on another domain, it requests the content directly from the second domain. The second domain determines whether or not to serve the content by validating the first domain, which is included as part of the request. The second domain then returns either the content or an error message back to the browser, bypassing the first domain entirely.

### A Preflight Request in CORS

A CORS preflight request is a CORS request that checks to see if the CORS protocol is understood and a server is aware of using specific methods and headers. It is an OPTIONS request, using three HTTP request headers: **Access-Control-Request-Method**, **Access-Control-Request-Headers**, and the **Origin header**.

A preflight request is automatically issued by a browser and in normal cases, front-end developers don't need to craft such requests themselves. It appears when a request is qualified as "to be preflighted" and omitted for simple requests.

For example, a browser might be asking a server if it would allow a **DELETE** request, before sending a **DELETE** request, by using a preflight request. For example,

OPTIONS /resource/foo

Access-Control-Request-Method: DELETE

Access-Control-Request-Headers: origin, x-requested-with

Origin: https://foo.bar.org

If the server allows it, then it will respond to the preflight request with an **Access-Control-Allow-Methods **response header, which lists **DELETE**. For example,

HTTP/1.1 204 No Content

Connection: keep-alive

Access-Control-Allow-Origin: https://foo.bar.org

Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE

Access-Control-Max-Age: 86400

The preflight response can be optionally cached for the requests created in the same URL using **Access-Control-Max-Age** header like in the above example.
