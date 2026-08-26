# How Server Services Work

<https://documentation.neutrinos.com/articles/#!studio-guide-8/how-server-services-work>

Server services provide various functionalities such as sharing data and resources among multiple clients, performing computation for a client, etc.

You use the Server Services Designer(SSD) to create HTTP endpoints ( by using the [HTTP In](/articles/server-side-service-designer-publication/http-in) and [HTTP out](/articles/server-side-service-designer-publication/http-out-node) nodes). This endpoint, when hit by the client, performs the required functionality and sends the response back to the client. For example, here is an HTTP flow to handle user login. The client requests the server to authenticate the user by calling the **/login** endpoint. The server checks the user credentials based on the username and password. If valid, it redirects the user to the home screen of the application. If invalid, it sends the **client not registered** error to the client.

All HTTP requests that are received by the server goes through [Middleware Sequences](/smart/project-concepts/middleware-sequence). The [Global Middleware Sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) is responsible for handling all client requests and sending a valid response back to the clients. A [Route Middleware Sequence](/smart/project-concepts/middleware-sequence/a/h3__1478205622) is responsible for making changes to a particular client request.

Using the Server Service Designer, you can alter the Global Middleware Sequence and add additional functionalities or perform configurations of the HTTP requests. For example, you can add the Global Session node to the Global Middleware Sequence to configure session management for all the client requests. See [Global Session](/articles/server-side-service-designer-publication/global-session-node) node to learn more. You can also create your own middleware sequence and add it to the Global Middleware Sequence to alter its flow. See [Middleware Start](/articles/server-side-service-designer-publication/middleware-start-node) to learn more.

Any changes made to the Global Middleware Sequence applies to all HTTP requests that hit the server. If you want to alter a specific HTTP request, you use the Route Middleware Sequence and configure it the way you want to handle that HTTP request.

To pass data within the flow, or from one flow to another, the Server Services Designer provides you with a bh. object and its properties.
