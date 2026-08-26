# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/ebao>

[eBaoTech](https://www.ebaotech.com/) is a digital solution provider to the global insurance industry. It provides a containerized open API platform for general, life, and health insurance businesses covering the entire lifecycle of policies, and enables third parties to develop applications.

We have subscribed to the following EBAO APIs and are providing them as nodes on [Server Services Designer](/smart/project-concepts/server-services-designer):

- [Quotation](/articles/server-services-designer-8/quotation-node)
- [Issuance](/articles/server-services-designer-8/issuance-node)
- [Proposal v2](/articles/server-services-designer-8/proposal-v2-node)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.4.2.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Download the Plugin from Neutrinos Store. See [Download from Store](/articles/studio-guide-7/import-plugin).
- In the Nodes Palette, search for the installed node and drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### Ebao Configuration

Use these attributes to create a new connection to EbaoCloud to consume the APIs.

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name:** A display name for the MQTT configuration.
- **Token URL:** The URL from which you want to obtain the access token for authorization.
- **Token URL Version:** The version of the URL.
- **Username: **The username provided by eBaoCloud when you registered as an authorized vendor.
- **Password: **The password provided by eBaoCloud when you registered as an authorized vendor.
- **Base path:** The base path on which the API is served. The base path differs for each API.
- **Version:** The version of the API you want to consume.
- **X Ebao Tenant Id: **The unique id provided by eBaoCloud to identify the tenant.
