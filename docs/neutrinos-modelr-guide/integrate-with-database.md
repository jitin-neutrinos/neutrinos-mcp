# Integrating with Databases

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/integrate-with-database>

## Integrating with Databases

Modelr provides a large number of widgets to link to both SQL databases such as MSSQL, MySQL, Oracle Database, and NoSQL databases such as MongoDB, Cassandra, etc. To integrate with a database, you should install the respective node to read and write to that database, and then configure the node to include the database properties.

**SQL Database: **

To install and configure a SQL database such as **M****icrosoft SQL (****MSSQL)**, perform the following steps:

1. In the Modelr home page, click ![](https://ci4.googleusercontent.com/proxy/jyu4iYEdJaVg_LsbjuXbzYOs_68i-jwyq8obxrYATESXNFdHxwdCxQhwUW9S4uPJ8JODpMUn8EtltrqSDb4uG0h4B4lk26T_QjRQYw6D84ppQORUBt3GxIHP9h_vwg=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/menu.png) and select **Manage palette**.
2. Click the **Install** tab and enter **MSSQL**. A number of nodes associated with MSSQL get displayed. Read the node description to understand the purpose of the node.
3. Install the node-red-contrib-mssql node.![Install a node using Manage palette](https://ci5.googleusercontent.com/proxy/nagfYC_lOjks-5Ce_pXRjb3aoAOmh8CTwCCPeFoe219EolT_Ub-F_faieQyok3F_dvIwUmGh_MY1MxLpQ49rP3OKz8yHz5brRbKIgNuqz3crc7LmtfG50jNJG_0sqZo=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/mssql.png)
4. Modelr shows a pop-up screen asking you to go through the documentation to check for dependencies. This node has no dependencies. Therefore, click **Install**.
5. The MSSQL node gets installed.
6. Search for the node using the **Search** bar. Drag and drop the node to the flow editor.
7. Design the flow. For example:![A flow created using the MSSQL node](https://ci3.googleusercontent.com/proxy/NhiJk7TUaDphZbj72NbH_knQDhRSdZscSUh6QkyCBAyOK0fdOX7X_HxBdJ_N4hJECEwB3e523BoLUhB1cj6mK3KGcs5Y2UoOzi2iMqRvHVbRblcym4xbnufPpcq7vLmaCU5aWQ=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/mssql_flow.png)
8. Double-click the node to configure the database.
9. Click the **edit **icon next to the **Connection** field to add a new MSSQL connection:![Edit properties of MSSQL node](https://ci4.googleusercontent.com/proxy/yCet3A5m84JJ6t3O4jNWRJMvxvXIZS5kZshjPTXt2jczDBYJro_Lka0stwuClHZugCbiKvdaJyHfxLMxUxS6UEPnmgXWB15qDKVO7eQ0Jn1OUURySoKPqmeJnaI3FNIQ_oOm=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/add_mssql.png)
10. Enter the configuration details to connect to the database and click **Add**.![Configure the MSSQL database](https://ci3.googleusercontent.com/proxy/DJ3NZwlf0WPCHfeDUhd2-hH-cX0A4hdVDxSej2qqZqQAmxba2wv2yQjqNFyIjETt1Eu0BnyXUBgkm2udkQe0r__9K9pDNLv8xaqtF1m_DfqqOBea7mD0HgT1lV36egSJHKO-BQ=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/mssql_conf.png)
11. In the **Edit MSSQL node** window, enter the query that you want the node to execute and click **Done**. For example: ![Edit MSSQL node](https://ci4.googleusercontent.com/proxy/gdM4fx3xxmzhT3Gtg3UUYvyfxOusKv96RN0oumRiWJxtiSkaMjprqBj9XTIpX8NwCe1CBXnzFuCXNjrDDXB6rDDDhy0dytajEI1HrCJtQrBdDz_I17orM-TyYB-WSFUDTqjj8g=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/edit_mssql.png)
12. In the Edit MongoDB in node configuration window, enter the configuration details to connect to the database and click **Add**

When the app is deployed, and the Neutrinos Modelr flow is called, The app connects to the configured MSSQL database and fetched the details of the DEPARTMENT table.

**NoSQL Database:**

To install and configure a NoSQL database such as MongoDB:

1. Perform steps 1 to 9 mentioned above. In place of the MSSQL node, use the **node-red-contrib-mongodb** node.
2. Enter the configuration details to connect to the NoSQL database and click **Add**. You can find the connection string in the **Compose**console of the MongoDB Viewer by clicking on your database name and clicking the **Admin** tab.![Creating a MongoDB connection](https://ci5.googleusercontent.com/proxy/9DqFoQnY9m8hfatMuDdQsWkxc7g5e6NmR0qRVRyr_xqpFuMyzzjMDUoetQRibMzM8icuyjyU9Pg7lzsk_Z0FERxzy-IGxm8e0sd9haL0xchoMudlvzvxcf9zwPBMW9DMJQgmeV3IoA=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/mongodb_conf1.png)
3. In the **Edit mongodb in node** configuration window, enter the **collection** name and select the **operation** that you want the node to perform. Click **Done**. For example:
   ![Query MongoDB](https://ci4.googleusercontent.com/proxy/Kc5TkVTgzD1esFuzxtD4lR-J_UnvAeK02qRYupU6wAZxL8cQISifx--xtZLqk3htCjPcTBvdKmc1XtViyVG9UfKDbRXpwLsk4JFvm7RwVUMj3WwXuxK2n6AMHhBV82bm8PAZEfzrFj9PYgHnFg=s0-d-e1-ft#http://docs1.neutrinos.co/resources/Storage/neutrinos-modelr-guide/mongodb_node_config.png)

When the app is deployed, and the Neutrinos Modelr flow is called, The app connects to the configured MongoDB database and retrieves the data from the collection. See [Power Prototyping with MongoDB](https://www.compose.com/articles/power-prototyping-with-mongodb-and-node-red-2/) for more details.
