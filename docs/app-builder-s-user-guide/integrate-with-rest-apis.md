# Consuming REST APIs

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/integrate-with-rest-apis>

You can seamlessly consume and expose REST APIs in your app by using the HTTP nodes on the Server Services Designer without having to write any code.

You can also perform exception handling to debug and troubleshoot any exceptions that occur when these services are executed.

### Consuming REST APIs

To consume a REST API, you use the [HTTP Request](/smart/project-service-designer-user-s-guide/http-request-node) node in the Server Services Designer. Using the HTTP Request node, you specify:

- The** HTTP method** (such as GET, PUT, etc.) that you want to execute.
- The **service endpoint URL** or the** base URL **where the API is running
- The **response format** in which the HTTP request is expected to return the data
- and the **result mapping object **which should hold the response of the HTTP Request.

![HTTP request node](/resources/Storage/app-builder-s-user-guide/http_req.png)

Additionally, depending on the REST API that you are connecting to, you may also be required to specify the **security and authentication requirements, body,** and the** query parameters** (if any).

For example, to connect to the OpenWeatherMap API ( a free weather API from OpenWeatherMap) and call weather data for a city, the API needs the city name and the API key as the query parameter:

Therefore, the query parameter in the HTTP Request node is constructed like this:

Security and authentication requirements that you can configure in the HTTP Request are:

See [Attributes in HTTP Request node](/smart/project-server-side-service-designer/http-request-node/a/h3__2110286098) to learn more.

### Exposing REST APIs

With Neutrinos, developers can expose any part of the application logic as an API. This is achieved by using the [HTTP In](/smart/project-server-side-service-designer/http-in) node in Server Services Designer.

When you deploy an application, all the API end-points that you have created in Server Services Designer are created, and the service is ready to be used. There no need for extra configurations or deployments.

For example, in this screenshot, we are creating an API endpoint createUser using the HTTP In node:

When exposing REST APIs, you can also create the documentation of the API using the same node. Neutrinos automatically generates the swagger documentation according to the Open API spec and makes it available under ${host}/api-docs.

For example, here is an example of documentation section inside the [HTTP In](/smart/project-server-side-service-designer/http-in) node:

When deployed, the swagger doc will look like this:

![createuser APi swagger doc](/resources/Storage/app-builder-s-user-guide/createuser_swagger.png)

To troubleshoot REST APIs, see [Troubleshoot Service Flows](/articles/app-builder-s-user-guide/troubleshoot-service-flows).

###
