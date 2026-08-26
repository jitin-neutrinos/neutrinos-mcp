# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/redis-session-node>

The **Redis**** Session** node is used to configure how [sessions](/smart/project-concepts/session) should work in a server using the **Redis** database. You configure sessions globally so that the server knows how to handle session requests that come from multiple clients.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is part of the **Redis **node package. It is visible in the [Global nodes](/articles/server-services-designer-8/global-nodes) palette after downloading the Redis node package from Neutrinos Store and installing it on Neutrinos Studio. |
| --- | --- |

To manage a single session, that is to get, destroy, or update a session, use the [session](/articles/server-side-service-designer-publication/session-node) node.

### How to use

- Download the **Redis** node package from Neutrinos Store. See [how to download Redis node](/articles/server-services-designer-8/redis/a/h3_1062945736) to learn more.
- After the node package is installed on Neutrinos Studio, from the Global nodes palette, drag and drop the **Redis Session** node to the default [Global middleware sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) or the [route middleware sequence](/smart/project-concepts/middleware-sequence/a/h3__1478205622) and configure its properties.

### Associated Attributes

1. **Name: **A unique name for the node. This name will display on the canvas when you save the node.
2. **Function name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-services-designer-8/call-service-node) node.
3. **Proxy**: Trusts the reverse proxy while setting the secure cookie. If set to True, the **X-Forwarded-Proto header** will be used. The **X-Forwarded-Proto (XFP) header** is a de-facto standard header for identifying the protocol (HTTP or HTTPS) that a client used to connect to your proxy or load balancer. If set to False, all headers are ignored. The connection is considered secure only if there is a direct TLS/SSL connection.
4. **Resave**: If set to True, forces the session to be resaved to the session store, even if the session was never modified during the request.
5. **Rolling:** If set to True, forces the session identifier cookie to be set on every response.
6. Save Uninitialized (True): Forces a session that is uninitialized to be saved to the store. A session is uninitialized when it is new and not modified.
7. **Secret**: The secret key used to sign the session ID and encrypt the cookie. Choose string and enter the key, or choose env and enter the name of the environment property which holds the key.
8. **Unset**: Control the result of not setting the required session. Select the option from the drop-down list.
  - **Keep**: The session in the store will be kept, but modifications made during the request are ignored and not saved.
  - **Destroy**: The session will be destroyed (deleted) when the response ends.
9. **Store Type**: The type of storage in which the session information will be saved. By default, **Memory s****tore** is selected, which is a memory session store made for production. To configure a database store, see [Attributes for a new Redis configuration](/articles/server-services-designer-8/redis/a/h3_964573856).
10. **Cookies options**: By using Cookies, you can exchange information between the server and the browser to provide a way to customize a user session, and for servers to recognize the user between requests. Cookies are essentially used to store a session id. To set the Cookie options for this node, see [Configure cookie options](/articles/server-services-designer-8/redis-session-node/a/h3_1278606430) to set the cookie properties. To configure cookies for your application, see:
  - [Configure First-Party Cookies](/smart/project-sample-how-to-guide/configure-first-party-cookies)
  - [Configure Third-Party Cookies](/smart/project-sample-how-to-guide/configure-third-party-cookies)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | Cookies can only store up to 4KB of data.Cookies are private to the domain. A site can only read the cookies it sets. It cannot read cookies from other domains. |
| --- | --- |

### Configure Cookie Options

1. **Secure(True/False)**: Specify whether to set the cookie to be secure or not. If enabled, this attribute is set by the application server when sending a new cookie to the client. By default, the attribute is set to False. You can set this attribute to True to prevent cookies from being observed by unauthorized parties.
2. **Domain**: Specify the domain value for the cookie. Domain specifies allowed hosts to receive the cookie. If unspecified, it defaults to the host of the current document location, excluding subdomains. If the domain is specified, then its subdomains are also included. For example, if **neutrinos.co** is set as the domain, then cookies are included on subdomains such as **console.neutrinos.co** and **store.neutrinos.co**.
3. **Expires At**: Specify the date object to set the expiring date of the cookie. By default, there is no expiration set. For example, if you want the cookie to expire in 24 hours of its creation, specify **new Date(new Date().setDate(new Date().getDate() + 1))**.
4. **HTTP only (True/False)**: Informs the browser that this special cookie should only be accessed by the server. Any attempt to access the cookie from the client script is strictly forbidden. By default, this attribute is set to True.
5. **Max Age**: Specify a positive value indicating how long the cookie should live. A value of 0 means the cookie should expire immediately. A negative value results in no Max Age attribute in which case the cookie is removed when the browser is closed.
6. **Path**: Specify the path for the cookie. By default, this is set to `'**/**'`, which is the root path of the domain. The path attribute indicates a URL path that must exist in the requested URL to send the Cookie header. For example, if the path is set to** /docs**, then the following paths will match:
  - **/docs**
  - **/docs/Web/**
  - **/docs/Web/HTTP**
7. **SameSite: **Allows you to declare if your cookie should be restricted to a [first-party](/smart/project-sample-how-to-guide/configure-first-party-cookies) or same-site context. This property has the following options:
  - **True: **Sets the SameSite attribute to **Strict** for strict same site enforcement.
  - **False:** will not set the SameSite attribute.
  - **Lax (default):** Cookies are not sent on normal cross-site subrequests (for example to load images or frames into a third party site), but are sent when a user is navigating to the origin site (i.e. when following a link). This is the default cookie value if SameSite has not been explicitly specified.
  - **Strict:** Cookies will only be sent in a first-party context and not be sent along with requests initiated by third-party websites.
  - **None: **Cookies will be sent in all contexts, i.e in responses to both first-party and cross-origin requests. If SameSite is set to **None**, the cookie Secure attribute must also be set to **True** (or the cookie will be blocked).
