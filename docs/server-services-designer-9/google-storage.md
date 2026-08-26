# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/google-storage>

**Google Cloud Storage** allows worldwide storage and retrieval of any amount of data at any time. You can use Google Cloud Storage for a range of scenarios including serving website content, storing data for archival and disaster recovery, or distributing large data objects to users via direct download.

This node comprises:

- [Google Storage Object node](/articles/server-services-designer-9/google-storage-object-node)
- [Google Storage Bucket node](/articles/server-services-designer-9/google-storage-bucket-node)

| ![](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select Plugins in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download. (In this case, search for** Google ****Storage)**
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop the **Google Storage Object** node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### Attributes for a new Storage Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: The name of the config.
- **Key Filename: **Upload a file that contains the key of the Google Storage Account
- **Project ID(String)**: Enter the project ID to authenticate your storage account. You can fetch the project id from the storage key file JSON.
