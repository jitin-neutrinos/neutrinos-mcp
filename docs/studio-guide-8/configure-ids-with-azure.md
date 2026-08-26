# Add Users and Groups

<https://documentation.neutrinos.com/articles/#!studio-guide-8/configure-ids-with-azure>

If you have an existing Azure Active Directory account using which want to authenticate your app users and manage their permissions, perform the following steps:

1. On the Neutrinos Studio Application home page, click **Settings** and select **IDS**.
2. Configure [general IDS settings](/articles/studio-guide-8/configure-your-ids/a/h3_2144388477).
3. Select **Azure AD** as your IDS provider. Additional fields to configure your account appears.
4. Enter the **Client ID**,** Client Secret**, and** Tenant ID**. These values are used by Azure AD to provide an access token. To obtain the Client ID and Client Secret:
  1. Navigate to [https://portal.azure.com/](https://portal.azure.com/) page
  2. On the home page, open the** App Registration** page. You can also use the search bar and search for the page.
  3. On the **App Registration** page, Click **New Registration**.
  4. Enter the OAuth Client ID in the **Name** field.
  5. Choose who can access the application. This is based on your app requirement.
  6. Provide the **Redirect URI**. This is the URL where your IDS is running. Suffix the URI with **/auth-provider/return**. For example, if the URL is **http://localhost** , redirect URI will be **http://localhost/auth-provider/return**.
      ![Azure - Register App](/resources/Storage/studio-guide-8/azure_register_app.png)
  7. Click** Register**.
  8. After you register your application, you will see the **client ID** and **Tenant ID** from the **Overview** page.
  9. Navigate to the **Certificate and Secrets** page to create the Client Secret.
  10. Click **Create New Secret**.
    1. In the **Add Client Secret** window, add your app description, choose the expiry, and click Add.
    2. The Client secret value gets displayed for you.
        ![Azure Client secret](/resources/Storage/studio-guide-8/azure_client_secret.png)
5. Enter the **Response mode**. This determines how Azure AD returns the result parameters. By default, the response mode is set to **query**. You cannot use any other Response Mode.
6. Enter **S****copes**. This defines what information the client application wants Azure AD to return. By default, scopes is set to **openid profile email address phone offline_access **. You cannot delete the default scopes. But you can add more scopes depending on what your client application requires.
7. Enter the **P****rompt **value. This specifies whether the authorization server prompts the user for reauthentication and consent. If no value is specified and the user has not previously authorized access, then the user is shown a consent screen. The prompt value can be:
  - **none: **Where the authorization server does not display any authentication or user consent screens; it will return an error if the user is not already authenticated and has not pre-configured consent for the requested scopes. You can use this option to check for existing authentication and/or consent.
  - **select_account: **Where the authorization server prompts the user to select a user account. This allows a user (who has multiple accounts at the authorization server) to select amongst the multiple accounts that they may have current sessions for.
  - **consent:** Where the authorization server prompts the user for consent before returning any information to the client.
8. You can also enable the **Multi-Tenant** option. Multi-tenancy means that a single instance of the software and its supporting infrastructure serves multiple customers. Each customer shares the software application and also shares a single database.

### Add Users and Groups

Once you setup Azure Ad on Neutrinos Studio, you should add users and groups to provide access to the app. Perform the following steps:

- Navigate back to [https://portal.azure.com/](https://portal.azure.com/).
- Goto **Home** > **Enterprise applications** to perform user management for your application.
- Open the registered app that you created in **Step 7**.
- In the left navigation menu, click **Users and Groups**.
- On the **Users and Groups** page, click **Add user**.
    ![Azure - Add User](/resources/Storage/studio-guide-8/azure_add_user.png)

- To add users to the app, select Users and Groups. To add a user, see [Add Users on Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory). To add a group, see [Add Groups in Azure AD](https://docs.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-groups-create-azure-portal).
    ![Azure - Add User](/resources/Storage/studio-guide-8/azure_add_user1.png)

Once IDS is registered, the Server Services creates [IDS services](/smart/project-server-side-service-designer/ids-services) to handle user authentication and authorization by creating HTTP endpoints. If you have customized the IDS services and want to regenerate them on Server Services. Click the **Re-generate IDS Flows **button to get the original services.



 ![Information](/resources/Storage/studio-guide-8/info.png)

 After the duplicate flows are created, make sure you delete the customized IDS flows, else duplicated endpoints will result in unexpected behaviors.Also, make sure that you configure the [Middleware sequences](/smart/project-server-side-service-designer/ids-services) by adding the required nodes if you deleted the original nodes.



After configuring IDS:Import and use the IDS module in your application. See [Using the IDS Module](/articles/studio-guide-8/use-ids).Create and manage **Teams** on Neutrinos Console to authorize users based on roles. See [Manage Teams](/articles/studio-guide-8/manage-teams).
