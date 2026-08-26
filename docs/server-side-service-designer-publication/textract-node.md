# How to use

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/textract-node>

**Textract node** is used to detect and analyze the text in documents and convert it into machine-readable text.

**Textract** is a complete AI-driven administration that separates printed text, and other information from archives that go past basic optical character acknowledgment (OCR) to recognize, comprehend, and extract information from structures and tables.

| ![Information](/resources/Storage/server-side-service-designer-publication/info.png) | This node is available from Neutrinos Studio Release 7.3.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node (Textract) and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select Textract Config:** The name of the configuration that connects to the AWS Textract Service APIs.
  - If you have an existing textract configuration, choose that config from the drop-down list.
  - If you want to create a new textract configuration, select **Add new config** from the drop-down list and click the **Map** icon to configure a new textract config. See [Attributes for a new Textract Config](/articles/server-side-service-designer-publication/textract-node/a/newtextractconfig) to know what are the properties to configure.
4. **Select Textract Operation: **Select the type of operation that is to be performed.
  - **Analyze Document: **Analyzes an input document for relationships between detected items.
  - **Detect Document:** Detects text in the input document. Textract can detect lines of text and the words that make up a line of text. The input document must be an image in JPEG or PNG format. DetectDocumentText returns the detected text in an array of Block objects.
  - **Start Document Analysis: **Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements. This operation can analyze text in documents that are in JPEG, PNG, and PDF format.
  - **Get Document Analysis: **Gets the results for **Start Document Analysis** operation that analyzes text in a document.
  - **Start Document Text Detection: **Starts the asynchronous detection of text in a document. Textract can detect lines of text and the words that make up a line of text. It can analyze text in documents that are in JPEG, PNG, and PDF format.
  - **Get Document Text Detection: **Gets the results for **Start Document Text Detection** operation that detects text in a document.
5. **Params Object: **Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads].
6. **Result:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.

### Attributes for a new Amazon Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name: **A display name for the Amazon config.
- **Endpoint: **The endpoint URI to send requests to. The default endpoint is built from the configured region and the syntax looks like this: https://{service}.{region}.amazonaws.com
- **Access Key Id (String): **The AWS access key ID.
- **Secret Access Key (String): T**he AWS secret access key.
- **Region (String): **The region to send service requests to.
- **Max Retries (Integer): **The maximum amount of retries allowed to attempt with a request.
- **Max Redirects (Integer):** The maximum amount of redirects allowed to follow with a request.
- **SSL Enabled (Boolean): **Whether to enable SSL for requests. **Secure Sockets Layer(SSL)** is a protocol for web browsers and servers that allows authentication, encryption, and decryption for the data sent over the Internet.
- **Compute Checksums (Boolean): **Wheather to compute checksums for payload bodies when the service accepts it.
- **Convert Response Types (Boolean): **Whether types are converted when parsing response data. Currently only supported for JSON-based services. Turning this off may improve performance on large response payloads. The default value is **True**.
- **Correct Clock Skew ****(Boolean)**: Whether to apply a clock skew correction and retry requests that fail because of a skewed client clock. The default value is **False**.
- **S3 Force Path Style (Boolean): **Whether to force path style URLs for S3 objects. The default value is **True**.
- **S3 Bucket Endpoint (Boolean):** Whether the provided endpoint addresses an individual bucket (false if it addresses the root API endpoint). Note that setting this configuration option requires an endpoint to be provided explicitly to the service constructor. The default value is **True**.
- **S3 Disable Body Signing ****(Boolean): **Whether S3 body signing should be disabled when using signature version v4. Body signing can only be disabled when using HTTPS. The default value is **True**.
- **S3 US East 1 Regional Endpoint (String): **When the region is set to 'us-east-1', whether to send s3 request to global endpoints or 'us-east-1' regional endpoints. This config is only applicable to the S3 client.
- **S3 Use Arn Region ****(Boolean): **Whether to override the request region with the region inferred from the requested resource's ARN. Only available for S3 buckets The default value is **True**.
- **API Version (String): **A String in YYYY-MM-DD format that represents the latest possible API version that can be used in all services (unless overridden by other API versions).
- **System Clock Offset (Number): **An offset value in milliseconds to apply to all signing times. Use this to compensate for clock skew when your system may be out of sync with the service time. Defaults to 0 milliseconds.
- **Signature Version (String): **The signature version to sign requests.The values can be: 'v2', 'v3', 'v4'.
- **Signature Cache (Boolean): **Whether the signature to sign requests is cached or not. Only applies to the signature version 'v4'. The default value is **True**.
- **Dynamo Db Crc (Boolean): **Whether to validate the CRC32 checksum of HTTP response bodies returned by DynamoDB. The default value is **True**.
- **Use Accelerate Endpoint (Boolean): **Whether to use the S3 Transfer Acceleration endpoint with the S3 service. The default value is **False**.
- **Client Side Monitoring (Boolean): **Whether to collect and publish this client's performance metrics of all its API requests. The default value is **True**.
- **Endpoint Discovery Enabled ****(Boolean): **Whether to call operations with endpoints given by service dynamically. The default value is **True**.
- **Endpoint Cache Size (Number): **The size of the global cache storing endpoints from endpoint discovery operations. Once the endpoint cache is created, updating this setting cannot change the existing cache size.
- **Host Prefix Enabled (Boolean): **Whether to marshal request parameters to the prefix of a hostname. The default value is **True**.
