# Client-Server Architecture

<https://documentation.neutrinos.com/articles/#!concepts-publication/client-server-architecture>

Client-server architecture is an architecture of a computer network in which many clients request and receive service from a centralized server (host computer). Client computers provide an interface to allow a computer user to request services of the server and to display the results the server returns. Servers wait for requests to arrive from clients and then respond to them.

A Client and a Server establishes a connection using an HTTP protocol. Once the connection is established, the Client sends an HTTP request to the server. After understanding the request, the server responds with appropriate data by sending back an HTTP response. For example:

![](/resources/Storage/concepts-publication/http_protocol.png)

Neutrinos provides you with a server using which you can design how the server should respond, and what information it should share with the HTTP requests that come from the client. You use [Server Services Designer](/articles/concepts-publication/server-services-designer) in Neutrinos Studio to do these configurations.

If you want to design the client requests that come to a server, you use the [Client Services Designer](/articles/concepts-publication/client-services-designer) in Neutrinos Studio.
