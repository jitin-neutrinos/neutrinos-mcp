# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/call-server-api-node>

This is the default topic template.

The **Call Server API **node is used to send or receive data from a server API created in [Server Services Designer](/smart/project-concepts/server-services-designer).

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Service Name:** The server service that you want to call.
- **API: **The API in the server service that you want to call.
- **Path Parameters:** Path parameters to be appended to the URL. Path parameters are used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters. This field is displayed only if there are path parameters defined in the API you are calling. This field accepts pairs of names and their corresponding values as key-value pairs.
- **Return Type:** A drop-down list displaying the type of data the request should return. You can select the return type from the drop-down list or map the return type to a page or flow variable by clicking the **Map** icon. The return type drop-down includes:
  - **JSON:** To receive the response in JSON format. The response is a JavaScript object created by parsing the contents of received data as JSON.
  - **STRING:** To receive the response in a string format.
  - **BLOB:** To receive the response in the binary large object format. Blob represents a file-like object of immutable, raw data.
  - **ARRAYBUFFER:** To receive the response as an array buffer. ArrayBuffer represents a generic, fixed-length raw binary data buffer. You cannot directly manipulate the contents of an ArrayBuffer; instead, you create one of the typed array objects which represent the buffer in a specific format and use that to read and write the contents of the buffer.
- **Body:** The [flow variable](/articles/flow-designer-guide/properties-page-designer) that contains the data that is to be sent to the API endpoint. Note that not every method has a request body. The GET method should not have a request body, whereas other methods such as POST, PUT, PATCH, and DELETE may or may not have a request body.
- **Result Mapping:** Maps the response received from the API endpoint to the flow variable.
- **Headers:** The headers of the request. These headers allow the client and the server to pass additional information with the request or the response. They accept pairs of names and their corresponding values as key-value pairs. If you want to map this field to a page or flow variable, click the **Map** icon.
- **Query Parameters: **Query string parameters to be appended to the URL. Query parameters are extensions of the URL that help define specific content or actions based on the data being passed. This field accepts key-value pairs. For example, if the URL is https://localhost:4200/user and the parameter is id=5, then the entire URL will be https://localhost:4200/user?id=5. You can enter the key and value directly or map the header to a page or flow variable by clicking the **Map** icon.
