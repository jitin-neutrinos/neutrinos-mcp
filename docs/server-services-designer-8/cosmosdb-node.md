# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/cosmosdb-node>

Azure Cosmos DB is Microsoft's globally distributed multi-model database service. You can use Azure Cosmos DB to quickly create and query key/value databases, document databases, and graph databases, all of which benefit from the global distribution and horizontal scale capabilities at the core of Azure Cosmos DB.

CosmosDB node package comprises of 2 nodes:

- [Item node](/articles/server-services-designer-8/item-node)
- [Container node](/articles/server-services-designer-8/container-node)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.7.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**CosmosDB node**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### CosmosDB Configuration

Use these attributes to create a new connection with a** CosmosDB Configuration.**

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name: **Name of the new configuration.
- **Disable Database**: Toggle this option to disable the configuration of a particular database connection. You can only disable the existing database configurations. This field does not appear when you are adding a new database configuration.
- **Endpoint: **Enter the URL of your cosmos DB database account.
- **Key: **Enter the key of your cosmos account.
- **Database ID: **Enter the database ID or name.
- **Create Database: **Toggle this field to create a new Database.
