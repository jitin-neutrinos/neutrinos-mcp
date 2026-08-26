# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/odata-node>

OData (Open Data Protocol) is an ISO/IEC approved, OASIS standard that defines a set of best practices for building and consuming RESTful APIs. OData helps you focus on your business logic while building RESTful APIs without having to worry about the various approaches to define request and response headers, status codes, HTTP methods, URL conventions, media types, payload formats, query options, etc. OData also provides guidance for tracking changes, defining functions/actions for reusable procedures, and sending asynchronous/batch requests.

OData RESTful APIs are easy to consume. The OData metadata, a machine-readable description of the data model of the APIs, enables the creation of powerful generic client proxies and tools.

| ![](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.5.0.    You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (**ODATA node**) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **URL(Required)**: Enter the OData service URL. For example, https://services.odata.org/service1
4. **Method: **The type of method you want this node to perform. The methods can be **POST**, **GET**, **PATCH**, and **DELETE**.
5. **Data**: Enter the JSON object name which contains the data that should be passed to Odata Services. This field appears when you choose **POST** and **PATCH** as operations in the **Method** field.  For example, enter bh.datas in the data field and use the following code in the script node.
    Copy CodeJSONbh.datas= {
    "Emails" : [
    "Russell@example.com",
    "Russell@contoso.com",
    "newRussell@contoso.com"
    ]
   }
6. **Query**: Enter the query for the node should perform. For example, {$filter: `UserName eq 'Russell'`} or enter bh.query in this field and mention the query in the script node as below:
    Copy CodeMarkdownbh.query = {$filter: `UserName eq 'Russell'`}
7. **Search Param**: Used to search for data based on the parameters passed. For example, select string property and enter serviceRoot/People('russellwhyte'). You can also define a set of parameters that should be passed to the query in the script node and enter the bh object name in this field.
8. **Boundary Prefix**: Enter the boundary prefix for the request. Defaults to batch_.
9. **Changset Boundary Prefix**: Enter the changeset Boundary Prefix for the request. Defaults to changset_
10. **Endpoint**: Enter the URL of the request.
11. **Batch Headers**: Set of batch headers that you want to add for the node. Batch headers refer to the multiple operations performed with a single HTTP Request. For example, select bh.input and enter header.
12. **Use Changeset**: Set to true if you want to use the changeset.
13. **Use Relative URLs (Boolean)**: Set to true if you want to use the relative URLs.
14. **Credential**: The credentials you want to use. It indicates whether the user agent should send cookies from the other domain in the case of cross-origin requests.
15. **Fragment**: Enter the fragments for the service.
16. **Headers**: Set of headers that you want to add to the method. These headers accept pairs of names and their corresponding values as key-value pairs. Map this field to bh.local, bh, bh.input or string properties, and input the variable name.
17. **Mode**: The mode that you want to use for the method that you have selected. This is used to determine if cross-origin requests lead to valid responses, and which properties of the response are readable.
18. **Redirect**: The redirect mode to use.
19. **Referrer**: Specify the URL for the referrer. The referrer property of the Request interface is set by the user agent to be the referrer of the Request.
20. **Result Mapping**: Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.
