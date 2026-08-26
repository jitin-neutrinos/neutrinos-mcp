# IDS Services

<https://documentation.neutrinos.com/articles/#!concepts-publication/ids-services>

**IDS Services **are flows that are generated when you register the Identity Server client for your application using the [IDS Settings editor](/articles/app-builder-s-user-guide/configure-your-ids).

See[About IDS](/articles/concepts-publication/identity-server) to learn more.

**IDS Services** host HTTP endpoints or APIs for the application to authorize and authenticate its users.

Each application (or client) uses the [IDS OAuth Client module](/articles/app-builder-s-user-guide/use-ids) to call the HTTP endpoints from the application. When the endpoint is called in the server, the server interacts with the IDS and executes the **ids** and **idsutil** server flows in the [Server Services Designer](/articles/concepts-publication/server-services-designer) to perform operations such as login, logout, renew access token, etc.

Apart from executing the server flows for the endpoints, SSD also maintains and manages user session details. By default, the session is stored in memory. You can use the [Global Session](/articles/server-side-service-designer-publication/global-session-node) node to persist the session in the database.

A user session gets created after the user is authenticated. A session contains a refresh token and cookies. A refresh token is valid for 14 days and cookies are valid for 15 days.

Once the user is authenticated, an access token is also created by the server and this is valid for 60 minutes. After the access token expires, a new set of a token (which contains refresh token and access token) is retrieved by using the refresh token. The session is extended each time the new token is generated.

| ![Information](/resources/Storage/concepts-publication/project-server-side-service-designer/info.png) | If your application does not want the server to persist the session, then navigate to the [Global Session](/articles/server-side-service-designer-publication/global-session-node) node and remove the default** Max Age** property value. If you want the server to persist the session for less than 14 days, then change the default **Max Age** property value to less than 15 days. Any value greater than 15 is not valid. |
| --- | --- |

Once IDS is enabled, the Global Sequence is updated with three nodes, CORS, a custom Middleware, and a global session.

- The **custom middleware flow - ids:hrefstart **appends the origin (from where the request originated) to the bh. object.
- The **Global Session** node is used to configure the session and cookies.
- The** CORS **node allows requests coming from **localhost:4200** by default. You can update this URL based on your origin.

The IDS also generates a route middleware sequence that can be used to protect other APIs that you might create which requires the user to be authorized.

If Server Services and the UI are running on the same domain, adding the CORS node in the [Global Middleware Sequence](/articles/concepts-publication/middleware-sequence/a/h3_1547994352) is not required. If they are running on different domains, make sure that the **Credentials** and** Origin** properties are configured.

| ![Information](/resources/Storage/concepts-publication/project-server-side-service-designer/info.png) | IDS services don't work on Safari if the Server Services and UI are running on different domains. See [Enable cross-site cookie in Safari](https://www.whatismybrowser.com/guides/how-to-enable-cookies/safari) for a workaround. |
| --- | --- |
