# Status Codes

<https://documentation.neutrinos.com/articles/#!neutrinos-art-api-reference-guide/status-codes>

## Status Codes

When you call any of the Neutrinos Art REST endpoints, the Response header returns one of the standard HTTP status codes defined in the following table.

| HTTP Status Code | Description |
| --- | --- |
| 200 OK | The request was successfully completed. A 200 status is returned for a successful GET or POST method. |
| 202 Accepted | The request has been accepted for processing, but the processing has not been completed. The request may or may not eventually be acted upon, as it may be disallowed at the time processing actually takes place.The response contains a Location header of a job resource that the client should poll to determine when the job has finished. |
| 400 Bad Request | Deletes infoThe request could not be processed because it contains missing or invalid information (for example- a validation error on an input field, a missing required value, and so on). |
| 401 Unauthorized | The request is not authorized. The authentication credentials included with this request are missing or invalid. |
| 403 Forbidden | The user cannot be authenticated. The user does not have the authorization to perform this request. |
| 404 Not Found | The request specifies an endpoint that does not exist. |
| 405 Method Not Allowed | The HTTP verb specified in the request (DELETE, GET, POST, PUT) is not supported for the specified endpoint. |
| 406 Not Acceptable | The object identified by this request is not capable of generating a representation corresponding to one of the media types in the Accept header of the request. For example, the client's Accept header request XML be returned, but the endpoint can only return JSON. |
| 415 Not Acceptable | The client's ContentType header is not correct (for example, the client attempts to send the request in XML, but the endpoint can only accept JSON). |
| 500 Internal Server Error | The server encountered an unexpected condition that prevented it from fulfilling the request. |
| 503 Service Unavailable | The server is unable to handle the request due to temporary overloading or maintenance of the server. The Exadata Cloud Service REST web application is not currently running. |
