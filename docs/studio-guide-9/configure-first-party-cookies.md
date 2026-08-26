# Configure First-Party Cookies

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-first-party-cookies>

A cookie is associated with a domain. If this domain is the same as the domain of the page you are on, the cookie is called a **first-party cookie**. These cookies allow website owners to collect analytics data, remember language settings, and perform other useful functions that provide a good user experience.

To configure first-party cookies, perform the following:

Open the default [Global Middleware Sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) on [Server Services Designer](/smart/project-concepts/server-services-designer).In the properties window of the [RDBMS session](/smart/project-server-side-service-designer/global-session-node) node or [Mongo Session](/smart/project-server-side-service-designer/global-mongodb-session-node) node (whichever session node you have chosen), configure the following properties:Set Proxy and Secure to **false**.Set sameSite to **lax**. This sets the cookies only for the origin that is requesting them.In the [CORS](/smart/project-server-side-service-designer/cors-node) node, set Credentials to **false**.
