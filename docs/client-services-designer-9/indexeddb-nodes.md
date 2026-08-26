# How to use

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/indexeddb-nodes>

IndexedDB is a database that is built into a user's browser. You can use this database to persistently store data.

- It stores almost any kind of value by keys, multiple key types.
- It supports transactions for reliability.
- It supports key range queries and indexes.
- It can store much bigger volumes of data than [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

Because IndexedDB lets you create web applications with rich query abilities regardless of network availability, your applications can work both online and offline.

It comprises the following nodes:

- [Connect](/articles/client-services-designer-9/connect-node)
- [Transaction](/articles/client-services-designer-9/transaction-node)
- [Cursor](/articles/client-services-designer-9/cursor-node)
- [Insert](/articles/client-services-designer-9/insert-node)
- [Upsert](/articles/client-services-designer-9/upsert-node)
- [Get](/articles/client-services-designer-9/get-node)
- [Remove](/articles/client-services-designer-9/remove-node)

To work with IndexedDB, you should open a connection to your database, and then perform operations on the data.

| ![Information](/resources/Storage/client-services-designer-9/info.png) | These nodes are available from Neutrinos Studio version 7.7.0. Get familiar with the [IndexDB concepts](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Basic_Concepts_Behind_IndexedDB#gloss_transaction) before you work with them. |
| --- | --- |

### How to use

- Open the **Client Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Client Service.
- Select** Plugins** in the menu and navigate to the [Neutrinos Store](https://store.neutrinos.co/web/catalog/featured).
- Search for the node.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

###
