# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/http-request-node>

This is the default topic template.

The **HTTP Request **node is used to send or receive data from a remote server using HTTP requests. This node can also be used to make Rest API calls.

### Node Properties

- **Name:** A unique name for the node.
- **Function Name: **This is a read-only field. The function name is generated based on the name that you enter in the Name field. It is used to identify the node while debugging.
- **Method: **A drop-down list displaying the type of HTTP request. You can select the type of HTTP request or map the HTTP request method to a flow variable by clicking the **Map** icon. The methods include:
  - **GET: **Requests data from a specified resource. Requests using GET should only retrieve data.
  - **POST:** Submits data to the specified resource, often causing a change in state on the server.
  - **PUT:** Sends data to a server to create/update a resource.
  - **DELETE: **Deletes the specified resource.
  - **PATCH:** Applies partial modifications to a resource.
- **URL: **The location of the resource to which you are making an HTTP request. You can enter the URL directly or map the URL to a [page or flow variable](/articles/flow-designer-guide/properties-page-designer) by clicking the **Map** icon.
- **Return Type:** A drop-down list displaying the type of data the HTTP request returns. You can select the return type from the drop-down list or map the return type to a page or flow variable by clicking the **Map** icon. The return type drop-down includes:
  - **JSON:** To receive the HTTP response in JSON format. The response is a JavaScript object created by parsing the contents of received data as JSON.
  - **STRING:** To receive the HTTP response in a string format.
  - **BLOB:** To receive the HTTP response in the binary large object format. Blob represents a file-like object of immutable, raw data.
  - **ARRAYBUFFER:** To receive the HTTP response as an array buffer. ArrayBuffer represents a generic, fixed-length raw binary data buffer. You cannot directly manipulate the contents of an ArrayBuffer; instead, you create one of the typed array objects which represent the buffer in a specific format and use that to read and write the contents of the buffer.
- **Body: **The data that is to be sent to the server along with the HTTP request. Select the property type, and enter the variable name. Note that not every HTTP method has a request body. The GET method should not have a request body, whereas other methods such as POST, PUT, PATCH, and DELETE may or may not have a request body.
- **Result Mapping: **Maps the response received from the server to a page or flow variable. Select the property type, and enter the variable name.
- **Headers: **The headers of the HTTP request. These headers allow the client and the server to pass additional information with the request or the response. They accept pairs of names and their corresponding values as key-value pairs. You can enter the key and value directly or map the header to a page or flow variable by clicking the **Map** icon.
- **Query Parameters:** The query string parameters whose values are to be appended to the URL. This field accepts key-value pairs. For example, if the URL is https://localhost:4200/user and the parameter is id=5, then the entire URL will be https://localhost:4200/user?id=5. You can enter the key and value directly or map the header to a page or flow variable by clicking the **Map** icon.
- **Observe**: The observe value determines the return type, according to what you want to observe. The provided options are:
  - **None: **Returns null.
  - **Events: **An observed value of events returns an observable of the raw HttpEvent stream object, including progress events by default.
  - **Body: **An observed value of body returns an observable of response body object.
  - **Response: **An observed value of response returns an observable of the entire HttpResponse object.
- **Report Progress**: Determines whether this request should be made to expose progress events.
- **With Credentials**: Determines whether the HTTP request should be sent with outgoing credentials (cookies).
