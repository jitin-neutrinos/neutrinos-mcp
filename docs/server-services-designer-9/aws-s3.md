# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/aws-s3>

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides easy-to-use management features so you can organize your data and configure finely-tuned access controls to meet your specific business, organizational, and compliance requirements. Amazon S3 is designed for durability, and stores data for millions of applications for companies all around the world.

AWS S3 comprises the following nodes:

- [S3 Bucket](/articles/server-services-designer-9/s3-bucket)
- [S3 Upload](/articles/server-services-designer-9/s3-upload)
- [S3 Object](/articles/server-services-designer-9/s3-object)
- [S3 Multiport Upload](/articles/server-services-designer-9/s3-multiport-upload)

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select Plugins in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop the **S3 Upload** node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### Attributes for a new AWS Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name: **A display name for the textract config.
- **Endpoint: **The endpoint URI to send requests to. The default endpoint is built from the configured region and the syntax looks like this: https://{service}.{region}.amazonaws.com
- **Access Key Id (String): **The AWS access key ID.
- **Secret Access Key (String): T**he AWS secret access key.
- **Region (String): **The region to send service requests to.
- **Use Dualstack(Boolean)**: Enables IPv6/IPv4 dual-stack endpoint.
- **Max Retries (Integer): **The maximum amount of retries allowed to attempt with a request.
- **Max Redirects (Integer):** The maximum amount of redirects allowed to follow with a request.
- **SSL Enabled (Boolean): **Whether to enable SSL for requests. **Secure Sockets Layer(SSL)** is a protocol for web browsers and servers that allows authentication, encryption, and decryption for the data sent over the Internet.
- **Compute Checksums (Boolean): **Whether to compute checksums for payload bodies when the service accepts it.
- **Convert Response Types (Boolean): **Whether types are converted when parsing response data. Currently only supported for JSON based services. Turning this off may improve performance on large response payloads. The default value is **True**.
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
