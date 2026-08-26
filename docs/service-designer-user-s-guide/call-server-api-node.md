# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/call-server-api-node>

The **Call Server API** node is used to send or receive data from a server API created in [Server Services Designer](/smart/project-concepts/server-services-designer).

| ![Information](/resources/Storage/service-designer-user-s-guide/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to Use

- Open the Services editor window.
- Click the **plus **icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop a **Call Server API **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow always starts with a **Start node**.

### Associated Attributes

- **Name:** Unique name for the node. This name will display on the canvas when you save the node.
- **Method**: A drop-down list used to filter the APIs. By default, the APIs of all the methods are listed. This field is only used to filter the APIs.
- **Service Name: **The server service you want to call. By default, all the APIs from all the services in the Server Services Designer are listed.
- **API: **The API in the server service that you want to call.
- **Path Parameters: **Path parameters to be appended to the URL. Path parameters are used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters. This field is displayed only if there are path parameters defined in the API you are calling. This field accepts pairs of names and their corresponding values as **key-value** pairs.
- **Return Type:** A drop-down list displaying the type of data the request should return. Select the return type from the drop-down list or if you want to map this field to a bh., bh.input, or bh.local variable, click the **Map** icon, select the property type, and input the variable name. The return type drop-down includes:
  - **JSON:** To receive the response in JSON format. The response is a JavaScript object created by parsing the contents of received data as JSON.
  - **STRING**: To receive the response in a string format.
  - **BLOB**: To receive the response in the binary large object format. Blob represents a file-like object of immutable, raw data.
  - **ARRAYBUFFER**: To receive the response as an array buffer. ArrayBuffer represents a generic, fixed-length raw binary data buffer. You cannot directly manipulate the contents of an ArrayBuffer. Instead, you create one of the typed array objects which represent the buffer in a specific format and use that to read and write the contents of the buffer.
- **![](/resources/Storage/service-designer-user-s-guide/cp_3.png)Body:** The name of the variable that contains the data that is to be sent to the API endpoint. The variable can be of bh., bh.input or bh.local property type. Use the drop-down list to select the property type. Note that not every method has a request body. The GET method should not have a request body, whereas other methods such as POST, PUT, PATCH, and DELETE may or may not have a request body.
- **Result Mapping: **Maps the response received from the API endpoint to the variable. The variable name can be of type bh., bh.input or bh.local. Use the drop-down list to select the property, and enter the variable name.
- **Headers: **This field is used to set the headers of the request. It allows the client and the server to pass additional information with the request or the response. These headers accept pairs of names and their corresponding values as **key-value** pairs. If you want to map this field to a bh., bh.input, or bh.local property type, click the **Map** icon, select the property, and enter the variable name.
- **Query Parameters: **Query string parameters to be appended to the URL. Query parameters are extensions of the URL that help define specific content or actions based on the data being passed. This field accepts **key-value** pairs. For example, if the URL is **https://localhost:8081/user** and the query parameter is **id=5**, then the entire URL will be **https://localhost:4200/user?id=5**. If you want to map this field to bh., bh.input, or bh.local property type, click the **Map** icon, select the property, and enter the variable name.
