# Use Google Authentication Provider

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-ids-with-google>

If you have an existing Google Cloud account using which want to authenticate your app users and manage their permissions, perform the following steps:

![Google IDS](/resources/Storage/studio-guide-9/google_ids.png)

1. On the Neutrinos Studio Application home page, click **Settings** and select **IDS**.
2. Configure [general IDS settings](/articles/studio-guide-9/configure-your-ids/a/h3_2144388477).
3. Select **Google** as your IDS provider. Additional fields to configure your account appears.
4. Enter the **Client ID** and **Client Secret**. These values are provided by Google for IDS to connect with Google. To obtain the Client ID and Client Secret:
  1. Open the [Google API Console Credentials](https://console.developers.google.com/apis/credentials) page.
  2. Click **Select a project**, then** NEW PROJECT**, and enter a name for the project, and optionally edit the provided Project ID. Click **Create**.
  3. On the Credentials page, select **Create credentials**, then OAuth client ID.
  4. You may be prompted to set a product name on the Consent screen. If so, click the **Configure consent **screen, and supply the requested information. Make sure that you add **neutrinos.co** or the domain where your IDS is running as the authorized domain. Click **Save** to return to the Credentials screen.
      ![Google Consent Screen](/resources/Storage/studio-guide-9/Google%20Consent%20screen.png)
  5. In the **Credentials** screen, select **Web Application** for the Application type.
    1. Enter the name of your OAuth Client ID.
    2. In the **Authorized JavaScript origins** field, enter the URL where the IDS is running. For example, the URL can be **http://localhost**.
    3. In the **Authorized redirect URIs** field, enter the URL where your IDS is running, or suffix the URI with **/auth-provider/return**. For example, the URL can be **http://localhost **or **http://localhost/auth-provider/return**.
    4. Click **Save**.
        ![Google Credentials Screen](/resources/Storage/studio-guide-9/google_credentials.png)
  6. On the page that appears after saving the credentials, copy the** client ID **and **client secret **to your clipboard, or download the JSON file.
5. Navigate back to the IDS Settings on Neutrinos Studio. Enter the **Response Type**. This is the type of response that the Google OAuth provider sends back to the IDS. By default, the response type is set to **code** which is exchanged between IDS and Google to get the token set. You cannot use any other Response Type.
6. Enter the **Response mode**. This determines how Google returns the result parameters. By default, the response mode is set to **query**. You cannot use any other Response Mode.
7. Enter **S****copes**. This defines what information the client application wants Google to return. By default, scopes is set to **openid https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email**. You cannot delete the default scopes. But you can add more scopes depending on what your client application requires.
8. Enter the **P****rompt **value. This specifies whether the authorization server prompts the user for reauthentication and consent. If no value is specified and the user has not previously authorized access, then the user is shown a consent screen. The prompt value can be:

Once IDS is registered, the Server Services creates [IDS services](/smart/project-server-side-service-designer/ids-services) to handle user authentication and authorization by creating HTTP endpoints. If you have customized the IDS services and want to regenerate them on Server Services. Click the **Re-generate IDS Flows **button to get the original services.

 ![Information](/resources/Storage/studio-guide-9/info.png)After the duplicate flows are created, make sure you delete the customized IDS flows, else duplicated endpoints will result in unexpected behaviors.Also, make sure that you configure the [Middleware sequences](/smart/project-server-side-service-designer/ids-services) by adding the required nodes if you deleted the original nodes.

After configuring IDS:Import and use the IDS module in your application. See [Using the IDS Module](/articles/studio-guide-9/use-ids).Create and manage **Teams** on Neutrinos Console to authorize users based on roles. See [Manage Teams](/articles/studio-guide-9/manage-teams).
