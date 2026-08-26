# Use Neutrinos Authentication

<https://documentation.neutrinos.com/articles/#!studio-guide-8/configure-ids-with-neutrinos>

The Neutrinos authentication strategy authenticates users based on their username and password.

The user information is stored on the Neutrinos IDS database and the user management is performed from the Neutrinos Console by the Organisation Administrator.

If you want to authenticate your app users using the Neutrinos auth strategy, perform the following steps:

![Neutrinos IDS](/resources/Storage/studio-guide-8/neutrinos_ids.png)

1. In the Neutrinos Studio Application home page, click **Settings** and select **IDS**.
2. Configure [general IDS settings](/articles/studio-guide-8/configure-your-ids/a/h3_2144388477).
3. Select **Neutrinos** to enable Neutrinos Auth Strategy. There are no additional configurations required for this Strategy.
4. Select a client from the **Share Client info **drop-down with which you want to share the user information of the logged-in user. Make sure the client has IDS enabled to consume this information.
5. To give users access to the app, create **Teams** and onboard** U****sers **on Neutrinos Console. You should have the **organisation admins** privilege to perform this operation.

Neutrinos Auth Strategy authenticates users onboarded to Neutrinos Console by using their username and password. The user information is stored on the IDS Database to perform user management.

Once IDS is registered, the Server Services creates [IDS services](/smart/project-server-side-service-designer/ids-services) to handle user authentication and authorization by creating HTTP endpoints. If you have customized the IDS services and want to regenerate them on Server Services. Click the **Re-generate IDS Flows **button to get the original services.

After the duplicate flows are created, make sure you delete the customized IDS flows, else duplicated endpoints will result in unexpected behaviors.

Also, make sure that you configure the [Middleware sequences](/smart/project-server-side-service-designer/ids-services) by adding the required nodes if you deleted the original nodes.

After configuring IDS:

- Import and use the IDS module in your application. See [Using the IDS Module](/articles/studio-guide-8/use-ids).
- Create and manage **Teams** on Neutrinos Console to authorize users based on roles. See [Manage Teams](/articles/studio-guide-8/manage-teams).
