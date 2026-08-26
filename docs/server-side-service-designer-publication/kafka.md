# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/kafka>

Kafka is a messaging system that safely moves data between systems. Depending on how each component is configured, it can act as a transport for real-time event tracking or as a replicated distributed database. Although it is commonly referred to as a queue, it is more accurate to say that it is something in between a queue and a database, with attributes and tradeoffs from both types of systems.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Attributes for a new Kafka Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

1. **Name**: The name of the config.
2. **Disable Kafka:** Toggle this option to disable the configuration of a particular database connection. You can only disable the existing database configurations. This field does not appear when you are adding a new database configuration.
3. **Client Id:** Enter the client id of your Kafka account.
4. **Brokers:** The list of brokers that you want to send the messages. A Broker is a Kafka server that runs in a Kafka Cluster.
5. **Connection Timeout: **Specify the time by which the Kafka server should respond to the connection request. Enter the time in **milliseconds**(ms). If a client connection does not receive a response from the server after the specified seconds, the request will be timed out and the client will immediately receive a Connection timed out error message. The default value of the Connection Timeout is **10000**.
6. **Request Timeout**: Specify the time by which the Kafka server should respond to the request. Request Timeout message is a status code with a message that is returned to the client when a request to the server takes longer than the server’s allocated timeout window. The default value of the Request timeout is **15000**.
7. **SSL:** Whether to enable SSL for requests. Secure Sockets Layer(SSL) is a protocol for web browsers and servers that allows authentication, encryption, and decryption for the data sent over the Internet.
8. **Reject Unauthorized: **If not false a server automatically rejects clients with invalid certificates.
9. **CA:** Optionally override the trusted CA certificates. The value can be a string or Buffer, or an Array of strings and/or Buffers.
10. **Key: **Enter the key of your Kafka account.
11. **Cert**: Cert chains in PEM format. One cert chain should be provided per private key.
12. **SASL: **Toggle this to enable the SASL to authenticate clients. When the toggle is set to true, configure the following:
  - **Mechanism**: The name of the SASL mechanism.
  - **Username**: Enter the username of the SASL Authentication.
  - **Password**: Enter the password-authenticated with the username.
  - **Authorized ****Identity**: The authorized id of the SASL.
  - **Access ****KeyId**: The authority key id of the SASL.
  - **Secret ****Access ****Key**: The secret key is used to sign the session ID and encrypt the cookie. Choose string and enter the key, or choose env and enter the name of the environment property which holds the key.
  - **Session ****Token**: An array of partition assignment protocols ordered by preference.
13. **Retry**: Whether to retry the configured connection.
