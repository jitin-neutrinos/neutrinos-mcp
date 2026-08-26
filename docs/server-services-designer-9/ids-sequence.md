# Login API flow

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/ids-sequence>

The **ids service** contains all the flows that create HTTP endpoints to authenticate and authorize users of an application. HTTP Endpoints include:

- **/login** - prompts the user login page
- **/login/cb** - gets the access token, refresh token, and user information
- **/logout **- prompt the user logout page
- **/logout/cb **- destroys the user session
- **/user/info** - provides the logged-in user information to the client

Each HTTP endpoint is created using server flows. Learn about each flow in detail:

### Login API flow

![IDS Login Flow](/resources/Storage/server-services-designer-9/ids_login_api.png)

The Login API flow is used to create the** /login** HTTP endpoint. This flow validates if the IDS client is registered. Else, the server sends back an **HTTP 404 **status code indicating that the client is not registered.

### Login Callback API Flow

This flow is used to create the** /login/cb** HTTP endpoint. This is the callback URL that is called by IDS after the user is authenticated. The user session is created and the access token, refresh token, and the userInfo are created and maintained by Server Services for further requests. If an error occurs, the user is redirected back to the login page.

### Logout API Flow

![logout API flow](/resources/Storage/server-services-designer-9/logout_api_flow1.png)

This flow is used to create the** /logout** HTTP endpoint. If the session exists with IDS, the logout page is displayed to the user. If not, the response to this request will prompt the client to destroy the session details.

### Logout Callback API Flow

![logout callback api flow](/resources/Storage/server-services-designer-9/logout_callbacl_api_flow.png)

This flow is used to create the** /logout/cb** HTTP endpoint. It destroys the user session on both the client and server side.

### Middleware Flow to Add Href to bh

![Middleware flow to add HREF to bh](/resources/Storage/server-services-designer-9/href%20to%20bh%20flow.png)

This flow is used to append the origin (from where the request originated) to the bh. object to calculate the redirect URL that the IDS will callback.

### Redirect to Login Flow

![Redirect to login flow](/resources/Storage/server-services-designer-9/redirect_to_login.png)

This flow is used to handle exceptions during the login callback and redirects the user back to the login page.

### API Flow to Fetch User Information

![API to fetch user information](/resources/Storage/server-services-designer-9/api_fetch_userinfo.png)

This is the flow called by the [Neutrinos OAuth Client](/smart/project-sample-how-to-guide/use-ids) module to fetch user information.

### Middleware Flow to Check Authorized API

![Midleware flow to check authorized API](/resources/Storage/server-services-designer-9/authorized_api_flow.png)

This is a middleware flow used to validate the user session.

- If the session (access token, refresh token, and cookies) is valid, it allows the user to continue with the services. if the session is invalid, the middleware flow doesn't allow the user to access any service.
- If the access token is invalid, a new set of tokens is retrieved using the refresh token, and the session duration is extended.
- If the refresh token is invalid, or if the user has been revoked access by the organization administrator, then the session is destroyed and the request fails.
