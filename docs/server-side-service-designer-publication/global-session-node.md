# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/global-session-node>

The** Global Session** or **RDBMS Session** node is used to configure how [sessions](/smart/project-concepts/session)should work in an RDBMS server. You configure sessions globally so that the server knows how to handle session requests that come from multiple clients. See [How sessions work](/smart/project-concepts/session) to learn more.

To manage a single session, that is to get, destroy, or update a session, you can use the [session](/articles/server-side-service-designer-publication/session-node) node.

### How to use

- Open the Server Services editor window.
- From the [Global nodes](/articles/server-side-service-designer-publication/global-nodes) palette, drag and drop the **RDBMS Session/Global Session** node to the default [Global middleware sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) or the [route middleware sequence](/smart/project-concepts/middleware-sequence/a/h3__1478205622) and configure its properties.

### Attributes Associated

- **Name: **A unique name for the node. This name will display on the canvas when you save the node.
- **Function Name****: **This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Proxy(True/ False)**: Trusts the reverse proxy while setting the secure cookie. If set to TRUE, the **X-Forwarded-Proto header** will be used. The **X-Forwarded-Proto (XFP) header** is a de-facto standard header for identifying the protocol (HTTP or HTTPS) that a client used to connect to your proxy or load balancer. If set to FALSE, all headers are ignored. The connection is considered secure only if there is a direct TLS/SSL connection.
- **Resave(True/False):** Forces the session to be resaved to the session store, even if the session was never modified during the request.
- **Rolling(True/False)**: Forces the session identifier cookie to be set on every response.
- **Save uninitialized(True/False)**: Forces a session that is uninitialized to be saved to the store. A session is uninitialized when it is new and not modified.
- **Secret**: The secret key used to sign the session ID and encrypt the cookie. Choose string and enter the key, or choose env and enter the name of the environment property which holds the key.
- **Unset**: Controls the result of not setting the required session. Select the option from the drop-down list.
  - **Keep**: The session in the store will be kept, but modifications made during the request are ignored and not saved.
  - **Destroy**: The session will be destroyed (deleted) when the response ends.
- **Store type**: The type of storage in which the session information will be saved. By default, **Memory s****tore** is selected. This is a memory store made for production. To configure a Database Store, see [RDBMS session node](/articles/server-side-service-designer-publication/global-session-node/a/h3_44321675).
- **Cookie options**: By using Cookies, you can exchange information between the server and the browser to provide a way to customize a user session, and for servers to recognize the user between requests. Cookies are essentially used to store a session id. To set the Cookie options for this node, see [Cookie options](/articles/server-side-service-designer-publication/global-session-node/a/h3_1003015590) to set the cookie properties. To configure cookies for your application, see:
  - [Configure First-Party Cookies](/smart/project-sample-how-to-guide/configure-first-party-cookies)
  - [Configure Third-Party Cookies](/smart/project-sample-how-to-guide/configure-third-party-cookies)

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | Cookies can only store up to 4KB of data.   Cookies are private to the domain. A site can only read the cookies it sets. It cannot read cookies from other domains. |
| --- | --- |

### Configure a Database Store

If you choose **Database Store** as your **Store type**, perform the following:

1. In the** Add new Database...** field, click the **Edit **button to configure the database in which the session information should be saved.
2. Choose an existing database from the drop-down list.
3. Enter the field values to add a new database configuration. The fields change based on the type of database you choose.
  - To configure the MSSQL database, see [MSSQL](/articles/server-side-service-designer-publication/configure-mssql-database) node documentation.
  - To configure the Oracle database, see [Oracle](/articles/server-side-service-designer-publication/configure-oracle-database) node documentation.
  - To configure the MYSQL database, see [MYSQL](/articles/server-side-service-designer-publication/configure-mysql-database) node documentation.
  - To configure the MariaDB database, see [MariaDB](/articles/server-side-service-designer-publication/configure-mariadb-database) node documentation.
  - To configure the PostgreSQL database, see [Postgres](/articles/server-side-service-designer-publication/configure-postgres-database) node documentation.

### Cookie Options

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
