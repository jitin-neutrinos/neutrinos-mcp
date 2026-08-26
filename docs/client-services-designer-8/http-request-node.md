# How to Use

<https://documentation.neutrinos.com/articles/#!client-services-designer-8/http-request-node>

The **HTTP Request** node is used to send or receive data from the remote server using HTTP requests. This node can also be used to make Rest API calls.

### How to Use

- Open the Services editor window.
- Click the **plus **icon to add a new service or open an existing service in the service list.
- In the Nodes Palette, drag and drop an **Http Request **node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow always starts with a **Start node**.
- After the flow is created, import the service to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** Unique name for the node. This name will display on the canvas when you save the node.
- **Method**: A drop-down list displaying the type of HTTP request. Select the type of HTTP request or if you want to map the HTTP request method to a bh.input, or bh.local variable, click the **Map** icon, select the property, and enter the variable name. The methods include:
  - **GET:** The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.
  - **POST**: The POST method submits an entity to the specified resource, often causing a change in state on the server.
  - **PUT**: The PUT method replaces all current representations of the target resource with the request payload.
  - **DELETE**: The DELETE method deletes the specified resource.
  - **PATCH**: The PATCH method applies partial modifications to a resource.
- **URL: **The location of the resource to which you are making an HTTP request. Enter the URL manually or if you want to map this field to a bh.input, or bh.local variable, click the **Map** icon, select the property, and input the variable name.
- **Return Type:** A drop-down list displaying the type of data the HTTP request returns. Select the return type from the drop-down list or if you want to map this field to a bh.input, or bh.local variable, click the **Map** icon, select the property, and input the variable name. The return type drop-down includes:
  - **JSON:** To receive the HTTP response in JSON format. The response is a JavaScript object created by parsing the contents of received data as JSON.
  - **STRING**: To receive the HTTP response in a string format.
  - **BLOB**: To receive the HTTP response in the binary large object format. Blob represents a file-like object of immutable, raw data.
  - **ARRAYBUFFER**: To receive the HTTP response as an array buffer. ArrayBuffer represents a generic, fixed-length raw binary data buffer. You cannot directly manipulate the contents of an ArrayBuffer; instead, you create one of the typed array objects which represent the buffer in a specific format and use that to read and write the contents of the buffer.
- **Body:** The name of the variable that contains the data that is to be sent to the server along with the HTTP request. The variable can be an input or local property. Use the drop-down list to select the property type. Note that not every HTTP method has a request body. The GET method should not have a request body, whereas other methods such as POST, PUT, PATCH, and DELETE may or may not have a request body.
- **Result Mapping: **Maps the response received from the server to the variable. The variable name can be of type  input or local. Use the drop-down list to select the property, and enter the variable name.
- **Headers: ** HTTP headers set the headers of the HTTP request. It allows the client and the server to pass additional information with the request or the response. These headers accept pairs of names and their corresponding values as **key-value** pairs. If you want to map this field to a bh.input, or bh.local variable, click the **Map** icon, select the property, and enter the variable name.
- **Query Parameters: **Query string parameters whose values are appended to the URL. This field accepts **key-value** pairs. For example, if the URL is **https://localhost:4200/user** and the parameter is **id=5**, then the entire URL will be **https://localhost:4200/user?id=5**. If you want to map this field to a bh.input, or bh.local variable, click the **Map** icon, select the property, and enter the variable name.
- **Observe**: The observe value determines the return type, according to what you want to observe. The provided options are:
  - **None: **Returns null.
  - **Events: **An observed value of events returns an observable of the raw HttpEvent stream object, including progress events by default.
  - **Body: **An observed value of body returns an observable of response body object.
  - **Response: **An observed value of response returns an observable of the entire HttpResponse object.
- **Report Progress**: Determines whether this request should be made to expose progress events.
- **With Credentials**: Determines whether the HTTP request should be sent with outgoing credentials (cookies).
