# HTTP Endpoints

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/http>

## HTTP Endpoints

These recipes address problems specific to **HTTP endpoints **and shows by example how they can be solved using the capabilities of Modelr .

[Create an HTTP Endpoint](/articles/neutrinos-modelr-guide/http/a/h1__111561868)


 [Handle query parameters passed to an HTTP endpoint](/articles/neutrinos-modelr-guide/http/a/handleparameterstohttpend)




 [Handle URL parameters in an HTTP endpoint](/articles/neutrinos-modelr-guide/http/a/handleurlparametersinhttpend)




 [Access HTTP request headers](/articles/neutrinos-modelr-guide/http/a/h1_591035913)




 [Include data captured in another flow](/articles/neutrinos-modelr-guide/http/a/handleurlparametersinhttpend)




 [Serve JSON content](/articles/neutrinos-modelr-guide/http/a/servejsoncontent)




 [Serve a local file](/articles/neutrinos-modelr-guide/http/a/h1_1114966349)




 [Post data to a flow](/articles/neutrinos-modelr-guide/http/a/h1__1079123274)




 [Work with cookies](/articles/neutrinos-modelr-guide/http/a/h1__1671693824)

---

### 

# Create an HTTP Endpoint

### Problem

You want to create an HTTP endpoint that responds to GET requests with some static content, such as an HTML page or CSS stylesheet.

#### Solution

Use the `**HTTP In**` node to listen for requests, a `Template` node to include the static content, and an `**HTTP Response**` node to reply to the request.

#### Example

![](https://cookbook.nodered.org/images/http/create-an-http-endpoint.png)

```html
[~]$ curl http://localhost:1880/hello <html>  <head>  </head>  <body>    <h1>      Hello World!    </h1>  </body></html>
```

### Discussion

The `**HTTP In**` and `**HTTP Response**` pair of nodes are the starting point for all HTTP endpoints you create.

Any flow that starts with an `**HTTP In**` node must have a path to an `**HTTP Response**` node otherwise requests will eventually timeout.

The `**HTTP Response**` node uses the `payload` property of messages it receives as the body of the response. Other properties can be used to further customize the response - they are covered in other recipes.

The `**Template**` node provides a convenient way to embed a body of content into a flow. It may be desirable to maintain such static content outside of the flow.

---

# Handle query parameters passed to an HTTP endpoint

### Problem

You want to access the query parameters passed to an HTTP endpoint, such as:

```html
http://example.com/hello-query?name=Nick
```

### Solution

Use the `msg.req.query` property of the message sent by the `**HTTP In**` node to access the parameters.

#### Example

![](https://cookbook.nodered.org/images/http/handle-query-parameters.png)

```html
[~]$ curl http://localhost:1880/hello-query?name=Nick <html>  <head>  </head>  <body>    <h1>      Hello Nick!    </h1>  </body></html>
```

### Discussion

The `msg.req.query` property is an object of key/value pairs for each query parameter.

In the above example, a request to `/hello-query?name=Nick&colour=blue` results in the property containing:

```html
{ "name": "Nick", "colour": "blue" } 
```

If there are multiple query parameters with the same name, they will be provided as an array. For example, `/hello-query?colour=blue&colour=red:`

`Copy CodeHTML{ "colour": ["blue","red"] }


 `

---

# Handle URL parameters in an HTTP endpoint

### Problem

You want to create a single HTTP endpoint that can handle requests where parts of the path are set per-request.

For example, a single endpoint that can handle requests to both:Copy CodeHTMLhttp://example.com/hello-param/Nick http://example.com/hello-param/Dave

### Solution

Use named path parameters in your `**HTTP In** node’s ``URL property and then access the specific value provided in a request using the ``msg.req.params property of the message.`

#### Flow

![](https://cookbook.nodered.org/images/http/handle-url-parameters.png)

#### Example

```html
[~]$ curl http://localhost:1880/hello-param/Nick <html>  <head>  </head>  <body>    <h1>      Hello Nick!    </h1>  </body></html>
```

### Discussion

Named path parameters in the `URL` property can be used to identify parts of the path that can vary between requests.

The `msg.req.params` property is an object of key/value pairs for each path parameter.

In the above example, the node is configured with a URL of `/hello-params/:name`, so a request to `/hello-param/Nick` results in the `msg.req.params` property containing:

```html
{ "name": "Nick" }
```

---

# Access HTTP request headers

### Problem

You want to access the HTTP headers sent in a request.

### Solution

Use the `msg.req.headers` property of the message sent by the `**HTTP In**` node to access the headers.

#### Example

![](https://cookbook.nodered.org/images/http/access-http-request-headers.png)

```html
[~]$ curl http://localhost:1880/hello-headers <html>  <head>  </head>  <body>    <h1>      User agent: curl&#x2F;7.49.1    </h1>  </body></html>
```

### Discussion

The `msg.req.headers` property is an object of key/value pairs for each request header. The header names are all lower-cased regardless of how they appear in the request.

---

# Include data captured in another flow

### Problem

You want to respond to an HTTP request using data captured by another flow.

### Solution

Store data using `flow context` so that it can be retrieved within the HTTP flow.

#### Example

![](https://cookbook.nodered.org/images/http/include-data-from-another-flow.png)

```html
[~]$ curl http://localhost:1880/hello-data <html>  <head>  </head>  <body>    <h1>      Time: 1480201022517    </h1>  </body></html>
```

### Discussion

There are many different ways data can be stored and retrieved within a flow. For example, using an external database.

Node-RED provides the `flow context` as a simple key/value store that is accessible to all nodes on the same tab.

The example above stores a timestamp generated by an `**Inject**` node into `flow context` using a `**Change **`node. The flow that handles the HTTP request then uses another `**Change**` node to retrieve the value attaching it to the message which is then passed to a `**Template**` node to generate the response.

---

# Serve JSON content

### Problem

You want to respond to an HTTP request with JSON data.

### Solution

Set the `content-type` of the response to `application/json` using the `msg.headers` object.

#### Example

![](https://cookbook.nodered.org/images/http/serve-json-content.png)

Copy CodeHTML[~]$ curl -i http://localhost:1880/hello-json HTTP/1.1 200 OK X-Powered-By: Express Access-Control-Allow-Origin: * Content-Type: application/json; charset=utf-8 Content-Length: 20 ETag: W/"14-jgfjeX8FTECC4q5nXp6n5g" Date: Sat, 26 Nov 2016 23:07:50 GMT Connection: keep-alive { "Hello": "World" }

### Discussion

The HTTP headers returned in the response can be set using the `msg.headers` property. It should be an object of key/value pairs for each header.

To return well-formed JSON, the `Content-Type` header should be set to `application/json `so the receiver knows to handle it as JSON data.

---

# Serve a local file

### Problem

You want to create an HTTP endpoint that responds to GET requests with content from a local file, such an png image.

### Solution

Use the `**File In**` node to load the required content and set the `Content-Type` to the appropriate value for the file type being returned.

#### Example

![](https://cookbook.nodered.org/images/http/serve-a-local-file.png)

```html
[~]$ curl  http://localhost:1880/hello-file > file.png 
```

### Discussion

When loading a non-text file such as an image, the `**File In**` node must be configured to return a `Buffer` object.

So that the receiver knows how to handle the file, the `Content-Type` header must be set to the appropriate mime type. The example above, which returns a `.png` file sets the `Content-Type` header to `image/png`.

---

# Post data to a flow

### Problem

You want to post data to a flow.

### Solution

##### For raw data:

Use the `**HTTP In**` node to listen for POST requests that have their `Content-Type` set to `text/plain` and access the posted data as `msg.payload`.

#### Example

![](https://cookbook.nodered.org/images/http/post-raw-data-to-a-flow.png)

```html
[~]$ curl -X POST -d 'Nick' -H "Content-type: text/plain" http://localhost:1880/hello-raw <html>  <head>  </head>  <body>    <h1>      Hello Nick!    </h1>  </body></html>
```

### Discussion

When the `**HTTP In**` node receives a request with the `Content-Type` header set to `text/plain` it makes the body of the available as `msg.payload`:

`var name = msg.payload;`

##### For Form data:

Use the `**HTTP In**` node to listen for POST requests that have their `Content-Type` set to `application/x-www-form-urlencoded` and access the form data as properties of `msg.payload`.

#### Example

![](https://cookbook.nodered.org/images/http/post-form-data-to-a-flow.png)

```html
[~]$ curl -X POST -d "name=Nick" http://localhost:1880/hello-form <html>  <head>  </head>  <body>    <h1>      Hello Nick!    </h1>  </body></html>
```

### Discussion

HTML Forms can be used to send data from the browser back to a server. If configured to `POST` the data, the browser will encode the data held in the `<form>` using a `content-type` of `application/x-www-form-urlencoded`.

For example, when a form that looks like this is submitted:

```html
<form action="http://localhost:1880/hello-form" method="post">  <input name="name" value="Nick">   <button>Say hello</button> </form>
```

it results in the request:

```html
POST / HTTP/1.1 Host: localhost:1880 Content-Type: application/x-www-form-urlencoded Content-Length: 9  name=Nick 
```

When the `**HTTP In**` node receives such a request, it parses the body of the request and makes the form data available under `msg.payload`:

```html
var name = msg.payload.name;
```

##### For JSON data:

Use the `**HTTP In**` node to listen for POST requests that have their `Content-Type` set to `application/json` and access the parsed JSON as properties of `msg.payload`.

##### Example

![](https://cookbook.nodered.org/images/http/post-form-data-to-a-flow.png)

```html
[~]$ curl -X POST -d '{"name":"Nick"}' -H "Content-type: application/json" http://localhost:1880/hello-form <html>  <head>  </head>  <body>    <h1>      Hello Nick!    </h1>  </body></html>
```

### Discussion

When the `HTTP In` node receives a request with the `Content-Type` header set to `application/json` it parses the body of the request and makes the data available under `msg.payload`:

```html
var name = msg.payload.
```

---

### Work with cookies

### Problem

You want to create an HTTP flow that uses cookies.

### Solution

The messages sent by the `**HTTP In**` node include the `msg.req.cookies` property that lists the cookies set on the current request.

The `**HTTP Response**` node will use the `msg.cookies` property in order to set or clear cookies.

#### Example

![](https://cookbook.nodered.org/images/http/work-with-cookies.png)

This example provides three HTTP endpoints:

- `/hello-cookie` returns a page that lists the cookies currently set
- `/hello-cookie/add` adds a new cookie and redirects back to `/hello-cookie`
- `/hello-cookie/clear` clears all cookies created by the example and redirects back to `/hello-cookie`

### Discussion

The `msg.req.cookies` property is an object of key/value pairs containing the cookies set on the current request.

```html
var mySessionId = msg.req.cookies['sessionId']; 
```

In order to set a cookie in the response, the `msg.cookies` property should be set to a similar key/value object.

The value can be either a string to set the value of the cookie with default options, or it can be an object of options.

The following example sets two cookies - one called `name` with a value of `Nick`, the other called `session` with a value of `1234` and an expiry set to 15 minutes.

```html
msg.cookies = {     name: 'nick',     session: {         value: '1234',         maxAge: 900000     } } 
```

The valid options include:

- `domain` - (String) domain name for the cookie
- `expires` - (Date) expiry date in GMT. If not specified or set to 0, creates a session cookie
- `maxAge` - (String) expiry date as relative to the current time in milliseconds
- `path` - (String) path for the cookie. Defaults to /
- `value` - (String) the value to use for the cookie

To delete a cookie, set its value to null.
