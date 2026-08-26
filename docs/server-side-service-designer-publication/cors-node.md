# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/cors-node>

The **CORS** node is used to enable [Cross-origin resource sharing](/smart/project-concepts/cross-origin-resource-sharing). It is used to configure how the Cross-Origin Resource Sharing should work in the sever. You can only add the **CORS** node to the [Global](/smart/project-concepts/middleware-sequence/a/h3_1547994352)[Middleware Sequence](/smart/project-concepts/middleware-sequence/a/h3_1547994352) or [Route Middleware Sequences](/smart/project-concepts/middleware-sequence/a/h3__1478205622). It cannot be used with customized service flows that you create in the Server Services Designer.

### How to use

- Open the Server Services editor window.
- From the** Global **Palette, drag and drop the **CORS** node to the **Global or Route Middleware Sequences **and configure its properties.

### Associated Attributes

### 

1. **Origin: **Configure the web content's origin. It is defined by the scheme (protocol), host (domain), and port of the URL used to access it. Two objects have the same origin only when the scheme, host, and port match. Configuring the **Origin** property affects whether the Access-Control-Allow-Origin header is generated.
    **Examples: **Same originhttp://example.com/app1/index.html
   http://example.com/app2/index.html
   The URLs are of the same origin because of the same scheme (HTTP) and host (example.com).
   Different originhttp://example.com
   http://www.example.com
   http://myapp.example.com
   The URLs are of different origin because of different hosts.
   If the **toggle** button is unchecked for the Origin filed, then all requests are rejected/not allowed. If the toggle button is enabled, then all requests will be allowed. Click the **Edit **icon next to the origin field and perform the following:
  - If you set the** Origin** to a **string**, then you enter a specific origin. For example, if you set the string value to **http://example.com**, then only requests from **http://example.com** will be allowed to access resources using CORS.
  - If you set the **O****rigin** to a **regular expression** pattern, then the expression will be used to test the request origin. If it's a match, the request origin will be reflected. For example, the pattern** example\.com$ **will reflect any request that is coming from an origin ending with **example.com**. Note that only JavaScript regular expressions are supported here.
  - If you set the Origin to to env, enter the environment property that holds the value of the web content's origin, or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.
2. **Methods: **If you select methods in this field, the options request from the browser will receive the response header **Access-Control-Allow-Methods** with the listed HTTP methods. This header is used to decide whether the app or the consumer of API is allowed to make an actual request with the particular HTTP method to the **resource/endpoint** of the server. Allowed HTTP methods include:
  - **GET:** Requests a representation of the specified resource.
  - **POST:** Submits an entity to the specified resource.
  - **PUT: **Replaces all current representations of the target resource with the request payload.
  - **DELETE:** Deletes the specified resource.
  - **PATCH: **Applies partial modifications to a resource.
  - **OPTIONS: **Describes the communication options for the target resource.
3. **Allowed headers: **If you configure this field, the options request from the browser will receive the response header **Access-Control-Allow-Headers** with the listed HTTP headers. This header is used by the browser to decide whether the App or the consumer of API is allowed to make an actual request with the particular HTTP Header to the** resource/endpoint** of the server Configures the **Access-Control-Allow-Headers CORS header**. Enter the header and click the **Add** icon to add the header.
4. **Exposed headers:** Configures the **Access-Control-Expose-Headers CORS header**. This header is used to expose the headers that have been mentioned in it. By default 6 response headers are already exposed which are known as CORS-safe listed response headers. They are: ![cors1](/resources/Storage/server-side-service-designer-publication/CORS1.png)
    Enter a header other than the default headers and click the **Add** icon to add the header. You can add more than one header. If not added, no custom headers are exposed.
  - Cache-Control
  - Content-Language
  - Content-Type
  - Expires
  - Last-Modified
  - Pragma.
5. **Credentials:** Configures the **Access-Control-Allow-Credentials CORS header**. This header Indicates whether or not the response to the request can be exposed when the C**redentials** field is enabled. Enable the **toggle** button to pass the header. Else, this field is omitted.
6. **Max Age: **Configures the **Access-Control-Max-Age CORS header**. This header indicates how long the results of a [preflight request](/articles/server-side-service-designer-publication/cors-node/a/h3__1918120618) can be cached. Enter an integer value to pass to the header. Else, this field is omitted.
7. **Preflight Continue: **Toggle this button to consider the same preflight request check result for the next CORS request.
8. **Options success status:** Provide a status code to use for successful **OPTIONS** requests. This field accepts only an integer value. For example, 200.
