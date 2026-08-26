# Use Active Directory Authentication Provider

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-ids-with-active-directory>

If you have an existing Active Directory and want to authenticate your app users and manage their permissions using it, perform the following steps:

![Active Directory IDS](/resources/Storage/studio-guide-9/Active%20Directoy_ids.png)

1. On the Neutrinos Studio Application home page, click **Settings** and select **IDS**.
2. Configure [general IDS settings](/articles/studio-guide-9/configure-your-ids/a/h3_2144388477).
3. Select **Active Directory** as your IDS provider. Additional fields to configure your Active Directory account appears.
4. Enter the **Active Directory URL** (LDAP URL) to configure the connection to the directory server. It is the URL where your Active Directory is hosted.
5. Enter the **Base DN**. Base DN is the section of the directory where the application will commence searching for users and groups. For example, if the domain name is **domain.neutrinos.org**, then the base DN can be **dc=domain,dc=neutrinos,dc=org**.
6. Enter the **Username Prefix** to be prepended to the username before the Active Directory bind is attempted. Usually, the prefix is the domain of your organization. For example, if **@test.neutrinos.io** is the [User Principal Name(UPN)](https://www.codetwo.com/kb/upn/#:~:targetText=In%20Windows%20Active%20Directory%2C%20a,domain%20name%20(UPN%20suffix).), then **@test** is the prefix.
7. Enter the **Username Postfix **to be appended to the username before the Active Directory bind is attempted. For example, if **@test.neutrinos.io** is the UPN, then** .io** is the postfix.
8. Enter the **Admin Username** and **Admin Password**. The administrator is responsible for managing the Active Directory and performs tasks such as creating and managing domains, preparing disaster recovery strategies, and handling user accounts. Click the **eye** icon to view or hide the password while entering a value for the **Admin Password** field.

Once IDS is registered, the Server Services creates [IDS services](/smart/project-server-side-service-designer/ids-services) to handle user authentication and authorization by creating HTTP endpoints. If you have customized the IDS services and want to regenerate them on Server Services. Click the **Re-generate IDS Flows **button to get the original services.

| ![Information](/resources/Storage/studio-guide-9/info.png) | After the duplicate flows are created, make sure you delete the customized IDS flows, else duplicated endpoints will result in unexpected behaviors.Also, make sure that you configure the [Middleware sequences](/smart/project-server-side-service-designer/ids-services) by adding the required nodes if you deleted the original nodes. |
| --- | --- |

After configuring IDS:

- Import and use the IDS module in your application. See [Using the IDS Module](/articles/studio-guide-9/use-ids).
- To give users access to the app, create **Teams** and onboard** U****sers **on Neutrinos Console. You should have the **organisation admins** privilege to perform this operation. See [User Management](/articles/studio-guide-9/perform-user-management).
