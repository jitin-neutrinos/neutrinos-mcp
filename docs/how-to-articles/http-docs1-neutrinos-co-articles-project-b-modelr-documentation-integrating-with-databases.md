# How to Integrate your App with a Database?

<https://documentation.neutrinos.com/articles/#!how-to-articles/http-docs1-neutrinos-co-articles-project-b-modelr-documentation-integrating-with-databases>

## How to Integrate your App with a Database?

---

| ![Information](/resources/Storage/how-to-articles/info.png) | Neutrinos Modelr is deprecated from Neutrinos Platform version 7 and further releases. This article is applicable only till Version 6 of the platform. |
| --- | --- |

You can Integrate your app with a database with the help of Neutrinos Modelr. Modelr provides a large number of widgets to link to databases such as MSSQL, MySQL, Oracle Database, MongoDB, etc.

To integrate your app with a database, you have to install a respective database node to read and write to the database. The nodes are further configured to include the database properties.

Now consider a case to install and configure a Microsoft SQL(MSSQL) node.

You perform the following steps:

**Step 1**: Launch the Neutrinos Modelr homepage from the Neutrinos Studio. Click the action button ![](/resources/Storage/how-to-articles/project-b-modelr-documentation/menu.png) on the top right and select **manage palette**.

**Step 2**: Click the **Install** tab and search for the **MSSQL node** using the search bar. A number of nodes associated with **MSSQL** are displayed with the node description. Read the description and understand the purpose of the node.

**Step 3**: In this case, Install the node-red-contrib-mssql node.

![MSSQL node](/resources/Storage/how-to-articles/project-b-modelr-documentation/MSSQL%20node.png)

**Step 4**: The modelr shows a pop-up window asking you to go through the documentation of this node and understand any dependencies of the node. The node-red-contrib-mssql node has no dependencies. Therefore, click **Install** on the pop-up screen and the node gets installed.

**Step 5**: Search for the installed node using the search bar on the top-left of the modelr homepage. Drag and Drop the installed node to the flow editor.

**Step 6**: Create a Modelr Flow. For example,

![The modelr flow](/resources/Storage/how-to-articles/project-b-modelr-documentation/modelrflow.png)

**Step 7**: Double click on the **MSSQL** node and configure the properties of this node. Enter the Query that the MSSQL node should execute. To insert data into the database, enter an** insert **query and to fetch data from the database you enter a **select** query. Click the edit icon ![](/resources/Storage/how-to-articles/project-b-modelr-documentation/fundamentals-img0008.png) next to the connection field and enter the configuration details to connect the database. Click **Done.**

![insert query for the node](/resources/Storage/how-to-articles/2019-09-19_10h46_24.png) ![node query information](/resources/Storage/how-to-articles/project-b-modelr-documentation/nodequery.png) ![configuration of the node](/resources/Storage/how-to-articles/project-b-modelr-documentation/nodeconfig.png)

**Step 8**: Once the nodes are configured and the flow is ready, deploy the modelr flow by clicking the deploy button ![](/resources/Storage/how-to-articles/project-b-modelr-documentation/deploy.png) on the top-right of the modelr homepage. If you have inserted, deleted or updated data, navigate to the Mongo DB GUI to see the changes. For example,

![Mongo DB](/resources/Storage/how-to-articles/mongoDB.png)

**Step 9**: After deploying the flow, the flow can be called from the app by creating a flow in UI service and making an **HTTP request** using an HTTP Request node..

![UI service flow to call a modelr flow](/resources/Storage/how-to-articles/project-b-modelr-documentation/uiserviceflow.png) ![url for the HTTP node](/resources/Storage/how-to-articles/project-b-modelr-documentation/httpurl.png)

**Step 10: **After the flow in UI services is ready, call the flow by inserting an **import** and an **inject** statement in the **TS** editor of the page.

![inject and import statement](/resources/Storage/how-to-articles/importinject.png)

The App connects to the configured **MSSQl** Database and fetches the required data from the database.

Similarly, you can configure other databases such as Mongo DB, Oracle, etc.
