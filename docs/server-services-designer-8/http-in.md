# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/http-in>

The **HTTP In** node is used to create an HTTP endpoint that responds to the requests. That is, it provides an HTTP end-point for creating web services.

The request properties from the client are stored in the following bh.input properties:

```javascript
bh.input.params = web.req.params;bh.input.query = web.req.query;bh.input.body = web.req.body;bh.input.files = web.req.files;bh.input.cookies = web.req.cookies;bh.input.headers = web.req.headers;bh.input.hostname = web.req.hostname;bh.input.method = web.req.method;bh.input.path = web.req.path;bh.input.signedCookies = web.req.signedCookies;
```

### How to Use

- Open the **Server Services** editor window.
- Open an existing service or click the** plus icon** and add a Server Service.
- In the Nodes Palette, drag and drop the **HTTP In** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start n****ode** or an **HTTP In** node.

### Associated Attributes

1. **Name****: **Unique name for the node. This name will display on the canvas when you save the node.
2. **Method:** It specifies what the client would like the server to do with the specified resource. Select a method from the drop-down list. HTTP methods include:
  - **GET**- Requests data from the specified Uniform Resource Identifier(URI). Where a URI is a string of characters that unambiguously identifies a particular resource.
  - **DELETE**- Deletes a resource at the specified URI.
  - **POST**- Creates a new resource at the specified URI.
  - **PUT**- Updates a resource at a specified URI.
  - **PATCH** - Makes partial changes to the existing resource at the specified URI.
3. **Path:** The URI path on which you want to perform the HTTP operations. For example, if the path is /file-upload/:jdf then the complete path will be localhost:8081/api/file-upload/:jdf
4. **Middleware Sequence:** The middleware sequence that you want to use for this **HTTP In** node. It has a dropdown where you can select the middleware sequence that is configured in the middlewares section of the services. The middleware sequences are denoted with the sequence id's or by their names in the list. See Configuring middleware to know more.
5. **File Upload:** Configure the fields in this section to accept the file uploads. To do so, toggle "**A****ccept File Upload?**" to true. These fields appear only when you set the file upload to true:

- **Destination**: Defines where the file should be saved after uploading. Choose **File Path** or **Memory**. The drop-down options change based on your selection:![File upload in http](/resources/Storage/server-services-designer-8/file_upload.png)
  - **File path**: The uploaded file is saved in the system. Configure the path in the **Upload Path **field.

6**. Documentation: **Configure the fields in this section to generate a swagger document that can be found in path **/api-docs**.

- **Summary: **The summary of the API endpoint.![Documentation of http in](/resources/Storage/server-services-designer-8/Httpin_doc.png)
- **Description**: The description of the API.
- **Select Parameter Type**: Configure this section to generate documentation for the parameters expected by the API.
  - **Name**: The name of the parameter.
  - **Description**: The description of the parameter.
  - **Select parameter Type**: Select the type of parameter from the dropdown list:
    - **Query**: Query string parameters whose values are appended to the URL. For example, if the URL is **https://localhost:4200/user?id=5 **then the query parameter is **id.**
    - **Path**: Path parameters are the variable parts of a URL path. They are typically used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters, each starting with a colon (:). For example, in /users/:id, :id is the path parameter.
    - **Body**: Body parameters is the request body expected by the API.
  - **Required**: Toggle this field to indicate that the parameter is mandatory or not. Click the **+ Add** button to add the documentation.
- **Responses**: Configure the fields in this to generate documentation for the responses sent by the API.
- **Consumes**: The list of content types accepted for the request body. Click the** + Add **button to add the value.
  - **Content-type**: Content type for the body of the request. For example, **text/html**.
- **Produces**: The list of content types for the response. Click the **+ Add **button to add the value.
  - **Content-type**: Content type for the response content. For example,** multipart/form-data**

After deploying the app, all the swagger documentation that you create using the** HTTP In **node can be accessed by clicking the **swagger documentation** link next to Server Services.

![Swagger documentation link](/resources/Storage/server-services-designer-8/swagger1.png)

A sample swagger doc looks like:

![The generated swagger document](/resources/Storage/server-services-designer-8/swaggerdoc.jpeg)
