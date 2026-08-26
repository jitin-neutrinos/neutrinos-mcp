# Neutrinos Login Template

<https://documentation.neutrinos.com/articles/#!components-guide-8/neutrinos-login-templates>

## Neutrinos Login Template

### Overview

The Neutrinos Login Template is a pre-built login template that you can use while creating your app. This template uses [Neutrinos Identity Server (IDS)](/articles/concepts-publication/identity-server) and is configured with the Neutrinos oAuth Strategy by default to authenticate your app users. You can retain Neutrinos OAuth strategy or edit the IDS Settings to opt for the following auth strategies:

- [Google](/smart/project-sample-how-to-guide/configure-ids-with-google)
- [Active Directory](/smart/project-sample-how-to-guide/configure-ids-with-active-directory)
- [Azure](/smart/project-sample-how-to-guide/configure-ids-with-azure)

![Information](/resources/Storage/components-guide-8/info.png)


 This template is available for you to use from Neutrinos Studio release 7.1.0.

### How to use

1. Open Neutrinos Studio. In the Studio home page, click the **Create App **icon to create a new app. Fill in the required fields.
2. If the neutrinos Login template is not already listed under **Templates**, click the **plus** icon next to the **Templates**. You will be navigated to the **Neutrinos Store**.
    ![Create pPp dialog box](/resources/Storage/components-guide-8/create_1.png)
3. Search for **Neutrinos Login template** and download it.
    ![Login template on Neutrinos Store](/resources/Storage/components-guide-8/ids_store.png)
4. Navigate back to the **Neutrinos Studio** and select **Neutrinos Login Template** under the **Templates** section and click **Create** button. The app gets created.
    ![neutrinos Login template on Create app page](/resources/Storage/components-guide-8/create_2.png)
5. Open the newly created app. Click **Setting**s on the editor pane and enter the **Application display name **under the **IDS **section.
    ![App display name](/resources/Storage/components-guide-8/app_name.png)
6. The Neutrinos OAuth strategy is selected by default. If required, select a different auth strategy, and enter the required details. See [Configure IDS](/smart/project-sample-how-to-guide/configure-your-ids) for more information.
    ![Information](/resources/Storage/components-guide-8/info.png)
    You can select more than one OAuth strategy to authenticate your app users. But you cannot select **Neutrinos **and** Active Directory **auth strategies at once.
7. Click **Save**. After you configure the IDS setting and save your configuration, [IDS flows](/smart/project-server-side-service-designer/ids-services) will be generated in the Server Services Designer to handle login, logout, and session details of the user.
8. Navigate to Server Services Designer and confirm that the flows are created. If not, you might have to validate your IDS settings and click **Regenerate IDS Flows **button.
9. Run the** Initialize** task from the **Task **drop-down menu.
    ![initialize task](/resources/Storage/components-guide-8/init.png)
10. After the app is initialized, run the **Live View** task from the Task drop-down menu.
11. The live view of the app opens in your browser.

### Description

When you import the Neutrinos Login Template to your app, the following settings are pre-configured:

**Environments Editor**

In the Environments editor, the** isIDSEnabled** property is set to** True**. This property indicates that the IDS is configured for this app. This indication is required for the client module to enable the request to start authentication.

**Server Services Designer (SSD)**

The SSD flows are auto-generated to host HTTP endpoints or APIs for the application to authorize and authenticate its users. See [IDS Services](/smart/project-server-side-service-designer/ids-services) for more detail. If the SSD flows are not generated, or if you have customized the SSD flows and want to regenerate the default flows, click the **Regenerate IDS Flows **button in the IDS Settings editor.

**Home page**

The** Home **page is created as part of the template and the oAuth module is imported to this page. Navigate to the TS editor of the page.

You see the **neutrinos-oauth-client** module imported to this page. Once this module is imported to the page, you can call all the [Neutrinos OAuth methods and properties](/smart/project-sample-how-to-guide/use-ids/a/h3_1350895405) to perform any customized Auth operations.

**Routes**

Navigate to the** Routes **editor. You will see that the** NeutrinosAuthGuardService** is enabled on the Home page. This service checks if the user has logged in, If not, it calls the IDS** login()** method to log the user in and create the user session.

Watch this video to learn how to configure Neutrinos IDS using the login template.
