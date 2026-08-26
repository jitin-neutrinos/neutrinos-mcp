# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/http-out-node>

The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next middleware.

### How to Use

- Open the **Server Services** editor window.
- Open an existing service or click the** plus icon** to add a Server Service.
- In the Nodes Palette, drag and drop the **HTTP Out** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or an** HTTP In** node**.**

### Associated Attributes

- **Name****: **Unique name for the node. This name will be displayed as the node label on the canvas when you save the node.
- **Response Types**: A drop-down list displaying the types of responses that are returned to the client.
  - **JSON Object: **To send the HTTP response in JSON format.
  - **Binary buffer: **To send an HTTP response as a binary buffer. This is used when binary data is being returned. Binary data is typically images, audio or other multimedia objects.
  - **Stream**:  Stream is a datatype of the stream object that collects the data in the form of buffers. Choose Stream to send an HTTP response as a stream object. Refer [Stream](https://nodejs.org/docs/latest/api/stream.html) documentation to learn more.
  - **Plain Text: **To send the HTTP response in a simple plain text format.
  - **Next middleware: **To call the next middleware in the sequence if there are any. The Http code and response field disappears.
  - **Redirect**: To redirect to the specified URL. On selecting the redirect response type the HTTP code is set to 302 by default.
    - **Redirect URL**: Specify the URL to which the current request should be redirected. This field appears instead of the Response body only when you select the redirect response type.
- **Http code**: The status code of an Http response. HTTP response status codes indicate whether a specific HTTP request has been successfully completed. For example, **404** for** not found**, **302** for** found**, etc. Refer to this [link](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to see more status codes.
- **Response body**: The data that is to be sent to the client along with the HTTP response. The data can be mapped to an input or local property. Use the drop-down list to select the property type of the response body. If you want to map this field to bh.local, bh. , bh.input, variables or a** string**, enter the value. Select **as is** in the drop-down list to write the response body manually. This field is replaced with Redirect URL when you select Redirect as your response type
- **Headers**: Set the headers of the response. It allows the server to pass additional information with the response. These headers accept pairs of names and their corresponding values as key-value pairs. Click the **plus** icon to add multiple headers. If you want to map this field to bh.local, bh, bh.input or **string** properties, click the **Map** icon, select the property and input the variable name or select **as is **in the dropdown list and write it manually.
- **Cookies**: An **HTTP cookie** (web cookie, browser cookie) is a small piece of data that a server sends to the user's web browser. The browser may store it and send it back with the next request to the same server. Cookies are mainly used for Session management, Personalisation, and Tracking. Click the **plus icon** to add a cookie and click the edit icon to **Edit** the added cookie.![cookies](/resources/Storage/server-services-designer-8/httpoutcookies.png)

- **Name**: The name of the cookie.
- **Value**: Sets cookie value. The value parameter may be a string or object converted to JSON. You can map it to bh.input , bh, bh.local, **string** or **as in** properties. Select the property and enter the value.
- **Cookies option**: Select a cookie option from the drop-down list and enter the value for the option and click the plus icon. The cookie option gets added. You can also delete an option from the list.

You can map the cookies to bh.input, bh.local, bh, **string** or **as in** properties and enter the value. The cookie value should be in the format of:

```markdown
bh.local.cookietest = {testhttpreqc: { value: 'testhttpreqc', options: { maxAge: '10000' } },testhttpreqc1: {value: bh.input.cky,options: {expires: new Date(Date.now()+1),httpOnly: 'true',path: '/rev',secure: 'true',sameSite: 'strict',signed: 'abc'}}};
```

- Option include:
  - **Domain(String)**: The domain name for the cookie. By default, the domain name is the name of the app.
  - **Expiry date (Date)**: The expiry date of the cookie is set in GMT. If it is not specified or set to 0, it creates a session cookie.
  - **HTTP only (Boolean)**: Flags the cookie to be accessed only by the webserver.
  - **Maximum age(Number)**: Option used for setting the expiry time relative to the current time in milliseconds.
  - **Path(String)**: The path for the cookie. By default, the value of the path is set to** “/”**.
  - **Secure(Boolean)**: The cookie is marked to be used with HTTPS only.
  - **Signed(Boolean)**: Indicates if the cookie should be signed to know if the client has modified the cookies.
  - **Same Site(Boolean or String)**: The **SameSite** prevents the browser from sending the cookie along with cross-site requests.
