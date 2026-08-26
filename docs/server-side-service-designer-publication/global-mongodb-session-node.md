# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/global-mongodb-session-node>

The **Mongo**** Session** node is used to configure how [sessions](/smart/project-concepts/session) should work in a server using the **MongoDB** database. You configure sessions globally so that the server knows how to handle session requests that come from multiple clients.

To manage a single session, that is to get, destroy, or update a session, you can use the [session](/articles/server-side-service-designer-publication/session-node) node.

### How to use

- Open the Server Services editor window.
- From the Global nodes palette, drag and drop the **Global MongoDB Session** node to the default [Global middleware sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) or the [route middleware sequence](/smart/project-concepts/middleware-sequence/a/h3__1478205622) and configure its properties.

### Associated Attributes

1. **Name: **A unique name for the node. This name will display on the canvas when you save the node.
2. **Function name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Proxy**: Trusts the reverse proxy while setting the secure cookie. If set to TRUE, the **X-Forwarded-Proto header** will be used. The **X-Forwarded-Proto (XFP) header** is a de-facto standard header for identifying the protocol (HTTP or HTTPS) that a client used to connect to your proxy or load balancer. If set to FALSE, all headers are ignored. The connection is considered secure only if there is a direct TLS/SSL connection.
4. **Resave**: Forces the session to be resaved to the session store, even if the session was never modified during the request.
5. **Rolling:** Forces the session identifier cookie to be set on every response.
6. **Save Uninitialized**: Forces a session that is uninitialized to be saved to the store. A session is uninitialized when it is new and not modified.
7. **Secret**: The secret key used to sign the session ID and encrypt the cookie. Choose string and enter the key, or choose env and enter the name of the environment property which holds the key.
8. **Unset**: Control the result of not setting the required session. Select the option from the drop-down list.
  - **Keep**: The session in the store will be kept, but modifications made during the request are ignored and not saved.
  - **Destroy**: The session will be destroyed (deleted) when the response ends.
9. **Store Type**: The type of storage in which the session information will be saved. By default, **Memory s****tore** is selected, which is a memory session store made for production. To configure a database store, see [Mongo Session node](/articles/server-side-service-designer-publication/global-mongodb-session-node/a/h3_2013103658).
10. **Auto Remove Session**:
  - **Native**: The session data is never destroyed.
  - **Destroy**: The data is destroyed as soon as the session is completed.
  - **Interval**: The session gets destroyed after a particular time interval.
11. **Cookies options**: By using Cookies, you can exchange information between the server and the browser to provide a way to customize a user session, and for servers to recognize the user between requests. Cookies are essentially used to store a session id. To set the Cookie options for this node, see [Configure cookie options](/articles/server-side-service-designer-publication/global-mongodb-session-node/a/h3_1278606430) to set the cookie properties. To configure cookies for your application, see:
  - [Configure First-Party Cookies](/smart/project-sample-how-to-guide/configure-first-party-cookies)
  - [Configure Third-Party Cookies](/smart/project-sample-how-to-guide/configure-third-party-cookies)

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | Cookies can only store up to 4KB of data.Cookies are private to the domain. A site can only read the cookies it sets. It cannot read cookies from other domains. |
| --- | --- |

### Configure Database Store

To configure a database store, perform the following:

1. The** Add new Database configuration** field allows you to configure the MongoDB database in which the session information is to be stored. You can select an existing database configuration from the drop-down list or click the **map icon** and add a new database configuration.
2. To add a new configuration, click the **Map** icon and enter the following:
  - **Connection Name**: The name of the database connection.
  - **Type**: The type of database you are configuring. This is a **read-only** field with **MongoDB **selected by default.
  - **URL**: The MongoDB connection URL used to connect to a MongoDB deployment. The standard MongoDB URL can have following format: mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database] .
  - **Optional > Options:** An optional query string in name-value pairs. From the drop-down list, select **str** and enter the name-value pair. For example, enter {"poolSize":7,"ssl":false}. Or, choose **env** and enter the environment property that contains the stringified JSON object. For the complete list of options, see [MongoDB documentation](https://mongodb.github.io/node-mongodb-native/3.4/api/MongoClient.html#.connect).

### Configure Cookie Options

1. **Secure(True/False)**: Specify whether to set the cookie to be secure or not. If enabled, this attribute is set by the application server when sending a new cookie to the client. By default, the attribute is set to FALSE. You can set this attribute to TRUE to prevent cookies from being observed by unauthorized parties.
2. **Domain**: Specify the domain value for the cookie. Domain specifies allowed hosts to receive the cookie. If unspecified, it defaults to the host of the current document location, excluding subdomains. If the domain is specified, then its subdomains are also included. For example, if **neutrinos.co** is set as the domain, then cookies are included on subdomains such as **console.neutrinos.co** and **store.neutrinos.co**.
3. **Expires At**: Specify the date object to set the expiring date of the cookie. By default, there is no expiration set. For example, if you want the cookie to expire in 24 hours of its creation, specify **new Date(new Date().setDate(new Date().getDate() + 1))**.
4. **Http only (True/False)**: Informs the browser that this special cookie should only be accessed by the server. Any attempt to access the cookie from the client script is strictly forbidden. By default, this attribute is set to True.
5. **Max Age**: Specify a positive value indicating how long the cookie should live. A value of 0 means the cookie should expire immediately. A negative value results in no **Max Age** attribute in which case the cookie is removed when the browser is closed.
6. **Path**: Specify the path for the cookie. By default, this is set to `'/'`, which is the root path of the domain. The path attribute indicates a URL path that must exist in the requested URL to send the Cookie header. For example, if the path is set to** /docs**, then the following paths will match:
  - **/docs**
  - **/docs/Web/**
  - **/docs/Web/HTTP**
7. **SameSite: **Allows you to declare if your cookie should be restricted to a [first-party](/smart/project-sample-how-to-guide/configure-first-party-cookies) or same-site context. This property has the following options:
  - **True: **Sets the SameSite attribute to **Strict** for strict same site enforcement.
  - **False:** will not set the SameSite attribute.
  - **Lax (default):** Cookies are not sent on normal cross-site subrequests (for example to load images or frames into a third party site), but are sent when a user is navigating to the origin site (i.e. when following a link). This is the default cookie value if SameSite has not been explicitly specified.
  - **Strict:** Cookies will only be sent in a first-party context and not be sent along with requests initiated by third-party websites.
  - **None: **Cookies will be sent in all contexts, i.e in response to both first-party and cross-origin requests. If SameSite is set to **None**, the cookie Secure attribute must also be set to **True** (or the cookie will be blocked).
