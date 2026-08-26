# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/ftp>

**SSH File Transfer Protocol (SFTP)** is a secure file transfer protocol. It runs over the **SSH protocol**. It supports the full security and authentication functionality of SSH. The **SSH **protocol (also referred to as Secure Shell) is a method for secure remote login from one computer to another. It gives a few elective alternatives to solid verification, and it ensures the correspondence's security and honesty with solid encryption.

**SFTP **also protects against password sniffing and man-in-the-middle attacks. It protects the integrity of the data using encryption and cryptographic hash functions and authenticates both the server and the user.

The following are the nodes under the SFTP category:

- [SFTP List](/articles/server-services-designer-8/sftp-list)
- [SFTP Get](/articles/server-services-designer-8/sftp-get)
- [SFTP Put](/articles/server-services-designer-8/sftp-put)
- [SFTP Command](/articles/server-services-designer-8/sftp-command)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select Plugins in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop the **SFTP List** node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### Attributes for a new SFTP Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: A name for the SFTP configuration.
- **Client ****Name (String)**: Enter the client name for the SFTP configuration.
- **Host (String)**: The host where the **SFTP** server is running.
- **Port(String)**: The port number that can be used to connect to the host where the SFTP server is running.
- **Force ****IPv4 (Boolean)**: Whether to connect only via IPv4 address.
- **Force ****IPv6 (Boolean)**: Whether to connect only via IPv6 address.
- **Username (String)**: The username to authenticate the connection to the SFTP server.
- **Auth_type**: Select the type of authentication you need for the SFTP configuration.
- **Password (String)**: The password for user authentication.
- **Ready ****Timeout (Number)**: Enter the time(in ms) to wait for the SSH handshake.
- **Enable ****Debug (Boolean)**: Whether the debugging should be enabled or not.
- **Strict ****Vendor (Boolean)**: Whether to perform a strict server vendor check or not.
- **Retries (Number)**: The number of times to retry connecting to the server.
- **Retry_factor (Number)**: The time factor used to calculate the time between the **Retries**.
- **Retry_min ****Timeout (Number)**: The minimum timeout between the retries/attempts.
