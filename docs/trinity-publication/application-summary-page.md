# Application Summary Page

<https://documentation.neutrinos.com/articles/#!trinity-publication/application-summary-page>

The application (app) level Summary page displays important information about installed apps in a single window. It provides users with in-depth insights into overall application performance and enables them to accurately isolate the root-cause of any application-level slowdown. The overall app summary tab presents details related to endpoints and errors. The Request analysis tab provides count of API errors based on the types (Example: 4XX,5XX).

![](/resources/Storage/trinity-publication/application-summary-page/appsummary.png)

The fields within the Request analysis section are described in the below table.

| Field | Description |
| --- | --- |
| Requests | Total requests received. |
| Errors | Total errors response. |
| 2XX | Indicates that the client's request was successfully received, understood, and accepted by the server. Example:200 OK: The request was successful, and the server returns the requested content. 201 Created: The request was successful, and a new resource was created as a result. |
| 4XX | Indicates that there was an error on the client's side. It typically occurs when the client's request is invalid. Example:400 Bad Request: The server cannot understand the client's request due to malformed syntax. 404 Not Found: The requested resource could not be found on the server. |
| 5XX | Indicates that there was an error on the server while fulfilling the client's request. It typically occurs when the server encounters an unexpected condition or fails to process the request. Example:500 Internal Server Error: An unexpected error occurred on the server that prevents it from fulfilling the request. 503 Service Unavailable: The server is temporarily unable to handle the request due to maintenance or overload. |
| 3XX | Indicates that the client needs to take additional action to fulfill the request. Typically involves redirecting the client to a different location or resource. Example: 301 Moved Permanently: The requested resource has been permanently moved to a new URL.302 Found: The requested resource can be found under a different URL. |
