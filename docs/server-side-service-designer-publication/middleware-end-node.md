# How to Use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/middleware-end-node>

The **Middleware End node **indicates the end of the middleware flow. It is used to send responses back to requests received from a** Middleware start node** or past the control to the next middleware.

### How to Use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** Add a Server Service** button to add a new service.
- In the Nodes Palette, drag and drop the **Middleware End** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or an **HTTP In** node.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Response Types**: A drop-down list displaying the types of data the HTTP response returns. If you want to map this field to a bh.input, or bh.local variable, click the **Map button**, select the property, and input the variable name. See [properties](/articles/server-side-service-designer-publication/properties-in-server-services) to learn more.
  - **Binary buffer: **To send an HTTP response as a binary buffer. This is used when binary data is moved in the file system.
  - **Stream: **Choose Stream to send an HTTP response as a stream object. Refer [Stream](https://nodejs.org/docs/latest/api/stream.html) documentation to learn more.
  - **JSON Object: **To receive the HTTP response in JSON format. The response is a **JavaScript object** that is created by parsing the contents of received data as **JSON**.
  - **Plain Text: **To receive the HTTP response in a simple plain text format.
  - **Next middleware: **To call the next middleware in the sequence if there are any.
- **Http code**: The status code of an Http response. HTTP response status codes indicate whether a specific HTTP request has been successfully completed. For example, **404** for **not found**, **302** for **found**, etc.
- **Response body**: The name of the variable that contains the data that is to be sent to the server along with the HTTP request. The variable can be an input or local property. Use the drop-down list to select the property type of the response body. If you want to map this field to bh.local, bh variable, click the **Map** icon, select the property, and enter the variable name. Select **as is** in the drop-down list to write the response body manually.
- **Headers**: HTTP headers sets the HTTP headers of the response. It allows the client and the server to pass additional information with the response. These headers accept pairs of names and their corresponding values as key-value pairs. If you want to map this field to bh.local, bh variables, click the Map icon, select the property and enter the variable name or select **as is **in the dropdown list and write it manually. Click the plus icon to add multiple headers.
- **Cookies**: An **HTTP cookie** (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with the next request to the same server. Click on the plus icon to **add** a cookie and click the edit icon to **Edit** the added cookie.![cookies](/resources/Storage/server-side-service-designer-publication/httpoutcookies.png)

- **Name**: The name of the cookie.
- **Value**: Sets cookie `name` to `value`. The `value` parameter may be a string or object converted to JSON. You can map it to bh.input or bh.local properties. Select the property and enter the value.
- **Cookies option**: Select a cookie option from the drop-down list and enter the value for the option and click the plus icon. The cookie option gets added. You can also delete an option from the list. Option include:
  - **Domain**: The domain name for the cookie. By default, the domain name is the name of the app.
  - **Expiry date**: The expiry date of the cookie is set in GMT. If it is not specified or set to 0, it creates a session cookie.
  - **HTTP only**: The flags of the cookie can be accessed only by the webserver.
  - **Maximum age**: The convenient option used for setting the expiry time relative to the current time in milliseconds.
  - **Path**: The path for the cookie. By default, the value of the path is set to** “/”**.
  - **Secure**: The cookie is marked to be used with HTTPS only.
  - **Signed**: Indicates if the cookie should be signed.
  - **Same Site**: SameSite prevents the browser from sending the cookie along with cross-site requests.
