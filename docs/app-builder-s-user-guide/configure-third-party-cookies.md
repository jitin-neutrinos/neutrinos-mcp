# Configure Third-Party Cookies

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/configure-third-party-cookies>

A cookie is associated with a domain. If this domain is different from the domain of the page you are on, the cookie is called a **third-party cookie**.

Third-party cookies are used for cross-site tracking, retargeting, and ad-serving.

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | The cookies set on the mobile app are always considered to be third-party cookies if the hostname is not given in the **config.xml** file. |
| --- | --- |

These cookies should be set over HTTPS (secure HTTP) protocol. If not, the app or the browser will reject the cookies.

To configure third-party cookies over HTTPS, perform the following:

1. Open the default [Global Middleware Sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) on [Server Services Designer](/smart/project-concepts/server-services-designer).
2. In the properties window of the [RDBMS session](/smart/project-server-side-service-designer/global-session-node) node or [Mongo Session](/smart/project-server-side-service-designer/global-mongodb-session-node) node (whichever session node you have chosen), configure the following properties:
  - Set Proxy to **true**.
  - Under Cookie Options:
    - set Secure to **true**.
    - Select **none** for sameSite
    - Do not set any value for maxAge. This is required if you don't want cookies to be persisted after the app closes.
3. In the properties window of the [CORS](/smart/project-server-side-service-designer/cors-node) node, configure the following properties:
  - For production environments, do not set any value for Origin. If you are working on a local environment, set Origin to **localhost:4200**.
  - Set Credentials to True.
4. Write an Angular interceptor (which can be used to modify or change the value of the HTTP request) and modify the request object to include withCredentials.Copy CodeJavaScriptreq = req.clone({ withCredentials: true });
