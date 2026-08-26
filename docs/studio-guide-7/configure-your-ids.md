# General IDS Settings

<https://documentation.neutrinos.com/articles/#!studio-guide-7/configure-your-ids>

To authenticate and authorize your app users, you can have your app registered with the Identity Server. You can opt to use the default Neutrinos Auth Strategy or connect to OAuth providers such as Active Directory, Google, or Azure AD.

| ![Information](/resources/Storage/studio-guide-7/app-builder-s-user-guide/info.png) | If you have an on-premises or Private cloud IDS setup, then you should have a domain name with HTTPS to establish a secure connection. Public IPs cannot be configured with Azure Ad or Google accounts. |
| --- | --- |

### General IDS Settings

1. On the Neutrinos Studio Application home page, click **Settings** and select **IDS**.
2. Select **Skip Team Check **if you want to allow external users to login without checking for the team through the Active Directory OAuth strategy.
3. Select **Skip Consent **if you already have an active session with the IDS and want the app to skip showing u the IDS consent page.
    ![IDS consent page](/resources/Storage/studio-guide-7/ids%20consent%20page.png)
4. When you create an application on Neutrinos Studio, the application is registered as a client with [Neutrinos IDS](/smart/project-concepts/identity-server). IDS provides a client ID and a client secret which can be used to get an application access token to consume resources on IDS or with applications that use IDS. Select **Client credentials **if you want the application to authorize itself with IDS and get an access token. This token is valid for 60 minutes.
    **Usecase: **Consider that APP1 and APP2 are using IDS. If you want to consume the authorized APIs of App1 from App2, then App1 can get the access token from IDS using the access token API and App2 can verify this token with IDS before providing access to the resource or the API to App1.
5. Enter the **application display name** (the name of your app) which appears on the login, logout, and consent pages of your app.
6. The** IDS issuer URL** by default displays the identity server URL hosted by Neutrinos. If you have an IDS running in your environment, you can change the IDS issuer URL in the **settings.json** file. This file is present in the following folder or directory:
  - ***C:\Users\<user>***** \.neutrinos** in a Windows machine.
  - ***/home/<user>/.neutrinos*** in a Linux machine.
  - ***/Users/<user>/.neutrinos* ** in a MAC machine.
7. **Login Redirect URI**: A login redirect URI(Uniform Resource Identifier) is where the client is redirected after the authorization is successful. The login URI is required to obtain the token set and user information.
    By default, Neutrinos provides a URI where the Server-Side Services (SSD) is running locally in your machine. The SSD is the client of the IDS. You can also add additional Redirect URIs depending on where your SSD is running. To add a login redirect URI, click the **+** icon and provide the URI.
8. **Logout Redirect URI**: A logout redirects URI(Uniform Resource Identifier) is where the client is redirected after successfully logging out from the IDS. The logout URI is required to destroy or revoke the token set provided to a user. By default, Neutrinos provides a logout redirect URI. You can also add additional logout Redirect URIs by clicking the **+** icon.

### OAuth Providers

Configure IDS with the below OAuth providers and then use the [Neutrinos OAuth IDS Module](/articles/app-builder-s-user-guide/use-ids) in your application to call the server to authenticate and authorize users.

**Topics**

- [Use Neutrinos Authentication](/articles/studio-guide-7/configure-ids-with-neutrinos)
- [Use Active Directory Authentication provider](/articles/studio-guide-7/configure-ids-with-active-directory)
- [Use Google Authentication Provider](/articles/studio-guide-7/configure-ids-with-google)
- [Use Azure AD Authentication Provider](/articles/app-builder-s-user-guide/configure-ids-with-azure)

Once the IDS client is enabled, server flows are created in the [Server Services Designer](/articles/concepts-publication/server-services-designer) to host HTTP endpoints and handle operations such as user login and user logout. See [IDS Services](/smart/project-server-side-service-designer/ids-services) to learn about these Server flows.

Also, the organisation admins should perform [user management](/articles/app-builder-s-user-guide/perform-user-management)on [Neutrinos Console](/articles/concepts-publication/neutrinos-console) to provide application access to users.
