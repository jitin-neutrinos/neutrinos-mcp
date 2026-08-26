# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/http-request-node>

The **HTTP Request** node is used to send or receive data from one server to another through HTTP requests.

### How to Use

- Open the **Server Services** editor window.
- Open an existing server service or click the** Add a Server Service** button to add a new service.
- In the Nodes Palette, drag and drop the **HTTP Request** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **HTTP In** node or a **Start node**.

### Associated Attributes

- **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
- **Method: **The HTTP method that you want to execute. The method specifies what the client would like the server to do with the specified resource. HTTP methods include:
  - **GET**- Requests data from the specified Uniform Resource Identifier(URI). Where a URI is a string of characters that unambiguously identifies a particular resource.
  - **DELETE**- Deletes a resource at the specified URI.
  - **POST**- Creates a new resource at the specified URI.
  - **PUT**- Updates a resource at a specified URI.
  - **PATCH** - Makes partial changes to the existing resource at the specified URI.
  - If you want to map this field to the bh. or bh.local property, click the **Map** icon and select the property, and specify the variable that contains the HTTP method. To learn about Server-side Service properties, or to create them, see [Properties in Server Services](/articles/server-services-designer-9/properties-in-server-services).
- **URL: **The URL of the server on which you want to perform HTTP operations. Select String in the drop-down list and enter the URL. If you want to map this field to a bh.input, env, or bh.local property, click the **Map** icon, select the property, and enter the variable that contains the URL. If you choose env, enter the environment property which contains the value. Make sure that the environment property is added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before calling this property here.
- **Return Type:** From the drop-down list, select the type of data that the HTTP request should return. Data types include:
  - **JSON: **To receive the HTTP response in JSON format. The response is a JavaScript object created by parsing the contents of received data as JSON.
  - **String: **To receive the HTTP response in string format.
  - **Array Buffer: **To receive the HTTP response as an array buffer.
- **Body: **Additional content that can be sent to the server to process the current request. Map this field to the bh., or bh.local property by clicking the **Map **icon, selecting the property, and inserting the variable name which contains the body of the HTTP Request.
- **Result Mapping:** The bh. or bh.local property to which you want to pass the result of the HTTP Request. The variable that you map should be of an object. For example, if you specify bh.local.result in this field, then that local property **result** will hold the response of the HTTP Request. The response can contain the following properties:

- statusCode
- headers
- responseUrl
- redirectList
- responseCookies
- requestDuration

- **Headers: **The HTTP headers of the request. Headers are used to pass additional information about the request to the server. For example, this is a sample HTTP Header: Copy CodeHTMLContent-Type : application/json
   connection : keep-aliveEnter the key and value you want to set as the HTTP Header. Click the** Add** icon to add more key-value pairs. Or, click the **Map** icon to map the key-value to the bh. or bh.local property. The variable that you map should be of an object. For example, bh.local.headers = {"content-Type" : "application/json", "connection" : "keep-alive"}. ![](/resources/Storage/server-services-designer-9/http_req2.png)
- **Query Parameters: **Enter a defined set of parameters to be attached to the end of a URL. These are extensions of the URL that are used to help define specific content or actions based on the data being passed or received. For example, if the URL is http://example.com/path?name=Branch&products=[Journeys,Email,Universal%20Ads], then** name=Branch&products=[Journeys,Email,Universal%20Ads] **is the query parameter that is appended to the URL to retrieve or post specific content.
    Enter the key and value you want to set as the query parameter. Click the** Add** icon to add one or more key-value pairs. Or, click the **Map** icon to map the key-value to the bh. or bh.local property, and enter the variable name. The variable that you map should be of an object. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads]}.
- **Request timeout:** Enter the time in milliseconds. If set to a positive number, this paramter override the globally set httpRequestTimeout parameter.
   ![](/resources/Storage/server-services-designer-9/http_req2.png)
- **Append body as query string parameters: **Toggle this field to True if you want to use the body of the HTTP request as the query string parameter. This field appears only if you choose the Get method.
- **Use Authentication:** Toggle this button to True if you want to authenticate your HTTP request. You will see a drop-down list providing three different authentication strategies. You can choose an authentication method from the drop-down list, or click the **Map** icon to map a bh. or bh.local. property which contains the authentication method that you want to use. Accepted authentication methods are:
  - **Basic authentication: **This is a simple authentication in which you provide authentication details (a user ID and password) to the server. The authentication information is passed to the server in an Authorization header. If you choose this authentication strategy, you can enter the username and password by selecting str from the drop-down list or enter the environment properties which holds the username and password values by selecting env from the drop-down list.
  - **Digest Authentication: **This is a method of authentication in which a request from a potential user is received by a network server and then sent to a domain controller. The domain controller sends a special key, called a digest session key, to the server that received the original request. If you choose this authentication strategy, you can enter the username and password by selecting str from the drop-down list or enter the environment properties which holds the username and password values by selecting env from the drop-down list.
  - **Bearer Authentication: **The bearer token is a cryptic string, usually generated by the server in response to a login request. In this authentication method, the client must send this token in the Authorization header when making requests to the resources on the server. If you choose this authentication strategy, you can enter the username and password by selecting str from the drop-down list or enter the environment properties which holds the username and password values by selecting env from the drop-down list.
- **Enable Secure (SSL/TLS) connection:** Toggle this field value to True if you want to configure a TLS or SSL certificate for the HTTP request. You will see a drop-down list with the SSL /TLS certificates that you would have created previously. Select a certificate to secure your connection.
    ![](/resources/Storage/server-services-designer-9/enable_ssl.png)
- Or, click the **Edit** icon to open the **Add new TLS config node** editor. Using this editor, you can add a new certificate. If you have already selected a certificate from the drop-down list, then you can use this editor to update the existing certificate.
  - **Name:** Enter a name for the TLS/SSL certificate.
      ![TLS config properties](/resources/Storage/server-services-designer-9/new_tls_cert.png)
  - **Server Name:** Enter the server name.
  - **Verify server certificate:** This toggle button is enabled by default. It verifies the server certificate with the server for authenticity.
  - **Certificate:** Upload the SSL/TLS certificate.
  - **Private key:** Upload the file containing the private key using which the server can decrypt the message.
  - **passphrase:** Enter the secret encryption/decryption key that is used to protect the file containing the private key.
  - **CA Certificate:** Upload the digital certificate issued by a certificate authority (CA).
  - After entering the details, click ![](/resources/Storage/server-services-designer-9/correct.png) to save the certificate. After the certificate is uploaded, the HTTP request encrypts and decrypts user page requests as well as the pages that are returned by the Web server.
- **[Use Proxy](/articles/server-services-designer-9/http-request-node/a/useproxy): **Toggle this field to True if you want to use a proxy server for the HTTP request. When an HTTP client has a request, the cache of the proxy server is checked before the request goes to the regular server. You will see a drop-down list of proxy configurations that you would have created previously. Select a proxy configuration.
    ![](/resources/Storage/server-services-designer-9/use_proxy.png)
- Or, click the **Edit** icon to open the **HTTP Proxy Properties** editor. Using this editor, you can add a new proxy configuration. If you have already selected a certificate from the drop-down list, then you can use this editor to update the existing configuration.
  - **Name: **Enter the name of the proxy configuration ![HTTP proxy properties](/resources/Storage/server-services-designer-9/new_proxy_server.png)
  - **URL:** Enter the URL of the proxy server.
  - **Use proxy authentication:** Toggle this button to True if you want to enable authentication of your proxy server.
  - **username: **The username to authenticate the proxy user. Proxy authentication is required to block requests for content from unauthenticated users. Choose str from the drop-down list to enter a string value for the username, or choose env to enter the environment property that has the username value.
  - **password: **The password associated with the username to authenticate the proxy user. Choose str from the drop-down list to enter the password directly, or choose env to enter the environment property that has the password stored in it.
  - **Ignore List: **This is a proxy exception list that is used to tell the browser to access the URL, Host, or IP directly and to not forward the request to the proxy server. Use the **Add** icon to add one or more keys. Once the keys are added, you can use the** Delete** icon to delete the key from the list.
- **Follow Redirect:** If enabled, it is used by the response server to tell the request server to go to another URL to find the requested content. The response server will append the server location and the status-code **301**in the response it sends back to the request server. The request server will then use this data to communicate with the other server which contains the required content.
- **Reject Unauthorized: **If set to false, allows requests to be made to HTTPS sites that use self-signed certificates. Toggle this field value to True if you do not want to allow the usage of self-signed certificates while making HTTP requests.
- **Use Query String: **If enabled, the HTTP request uses the querystring module to stringify and parse query strings. That is, it serializes the array as foo=bar&foo=baz instead of the default foo[0]=bar&foo[1]=baz. See [Node.js documentation](https://nodejs.org/api/querystring.html) to learn more.

- **Cookies:** A cookie is a small piece of data that a server sends to the user's web browser. It is used to tell if two requests came from the same browser, keeping a user logged in. Click the **Add** icon to add a new cookie, or click the **Map** icon to map the cookie value to a bh.local, bh.input, or to give the values as is.
- If you click the** Add** icon, you will see the following fields in the attributes window:
  - **Name:** Enter a name for the cookie
  - **Value:** Enter the cookie value to be associated with the cookie name. You can select as is from the left drop-down list and enter the value, or select bh.local or bh.input from the drop-down list to map the property to a variable that contains the cookie value.
  - **Cookies Option:** This drop-down list provides the following cookie options for which you can set values. Enter the value and click the Add icon to add the value to the list.
    - **Domain name:** Specify a subdomain for your cookie. For example, a domain name can be **mysite.com**.
        ![](/resources/Storage/server-services-designer-9/cookies_example.png)
    - **Expiry date: **Enter the expiry date of the cookie in UTC format. For example, the expiry date can be **Mon, 09 Dec 2019 17:04:05 UTC**. If you don’t set the expiration date, the cookie will expire when the browser is closed.
    - **Http only:** Enter True to make the cookies inaccessible via the document.cookie API, so they are only editable by the server. Else, enter False.
    - **Maximum age:** Use this field instead of the **Expiry date** field to mention how long the cookie can live. For example, if you want the cookie to expire after 60 minutes, enter** 3600** as the value of the **Maximum age** parameter. **Note that Internet Explorer does not support this parameter.**
    - **Path:** Specifies a document location for the cookie. The cookie is sent to the server only if the path matches the current document location or a parent. For example, if you set the path to **/dashboard**, then cookies are sent on **/dashboard**, **/dashboard/today,** and other sub-URLs of **/dashboard/**, but not on **/posts**.
    - **Secure: **Enter True to make sure the cookie can only be transmitted securely over HTTPS, and it will not be sent over unencrypted HTTP connections
    - **Signed: ** Set to True to make the cookies unreadable in the frontend, but transparently encoded/decoded on the server-side. Else, set to False.
    - **Same site:** Set to True to tell the servers that a cookie is not sent on cross-site requests, but only on resources that have the cookie domain as the origin.
  - If you click the **Map** icon, you can select as is from the left drop-down list and enter the value, or select bh.local or bh.input from the drop-down list to map the property to a variable that contains the cookie value.
