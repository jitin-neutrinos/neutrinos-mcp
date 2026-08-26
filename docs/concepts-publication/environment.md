# Environment Properties

<https://documentation.neutrinos.com/articles/#!concepts-publication/environment>

An environment is a system or a server where an application is hosted.

### Environment Properties

Environment properties define the environment for an application (client) or a server or both the application and the server.

- Select the **Client** checkbox to set the environment properties for the front-end application.
- Select the **Server** checkbox to set the environment properties for the server.
- Select both **Client **and **Server** checkboxes to set the environment properties for the application and the server.

![Client or Server in environments](/resources/Storage/concepts-publication/project-sample-how-to-guide/env_client_server.png)

The following environment properties are available by default on Neutrinos Studio:

- **production:** The flag to enable or disable the production mode of the app.
- **ssdURL: **The Url where [server services](/articles/concepts-publication/services/a/h3_1880384879) are running. It defaults to **localhost:8081**.
- **tenantName: **The organization of the user.
- **appName:** The name of the application.
- **namespace:** The namespace to be used for the app.
- **googleMapKey:** The API key for google maps. It is a unique identifier that is used to authenticate requests associated with your project for usage and billing purposes.
- **useDefaultExceptionUI:** The flag to show snack bar messages when HTTP requests fail.
- **isIDSEnabled:** The flag which indicates if the [Identity Server](/articles/concepts-publication/identity-server) is enabled for an application.
- **SSD_BASE_PATH:** The base path where [Server Service APIs](/articles/concepts-publication/services/a/h3_1880384879)are mounted.
- **SSD_DEFAULT_PORT: **The port where the [Server Services Designer](/articles/concepts-publication/server-services-designer) is running.
- **webAppMountPoin****t:** The path which serves the angular app.
- **CLOCK_TOLERANCE: **The time difference (in seconds) that can be tolerated between the IDS server and the SSD. After the time difference elapses, the user will not be authenticated to access the app.
- **NGFORAGE_MOBILE_DRIVER**: The type of storage that is used by mobiles to store data. Values that are accepted are:
  - LOCAL_STORAGE - A lightweight way to store data in browsers. The usage is capped at 5MB in many browsers.
  - WEB_SQL - A web page used for storing or managing the data in the database. The API is supported by Google Chrome, Opera, and Android browsers.
  - INDEXED_DB**(default)** - A way to store a large amount of structured data on the client and use indexes for efficient retrieval.
