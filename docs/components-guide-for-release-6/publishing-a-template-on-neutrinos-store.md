# Publishing a Template on Neutrinos Store

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/publishing-a-template-on-neutrinos-store>

## Publishing a Template on Neutrinos Store

Templates are applications containing various UI or functional components. You use templates when creating an app to save time and reuse the existing functionality. For example, you import the [Neutrinos Login template](/articles/components-guide-for-release-6/neutrinos-login-templates) to use the [Neutrinos Identity Server (IDS)](/smart/project-sample-how-to-guide/learn-about-ids) and Neutrinos OAuth Strategy to authenticate your app users.

### Creating the app template

To create templates on Neutrinos Studio, perform the following steps:

1. [Download Neutrinos Studio](/smart/project-sample-how-to-guide/sign-in) and create an app with the functionality that you want to offer as a template.
2. Design the app with various UI and functional components.
3. Test the application for completeness by [previewing the app](/articles/project-sample-how-to-guide/live-preview-web-app).
4. If you have developed the app to be used as a mobile template, test the app functionality by [Previewing the Mobile App](/smart/project-sample-how-to-guide/live-view-the-mobile-app).
5. [Export the app](/smart/project-sample-how-to-guide/export-a-nos-file) as a .nos file and save it in a folder.
6. Add at least four screenshots of the template in the folder, along with an icon to represent your template on Neutrinos Store.
7. Add a word document named **Dependency**. List the value and purpose of the template, along with the template dependencies. This helps the Neutrinos team in testing the template's functionality. This document should answer questions relating to:
  1. **Value and purpose:**
    - What is the purpose of the template?
    - What features does it include?
    - What is the current problem(s) it will solve?
  2. **Dependencies:**
    - What platforms can the app be used in (iOS, Android, or Windows)?
    - Are there other credentials that are needed or already exist (analytics systems, or platforms)?
    - Does it need Apple, Google, or other developer accounts/credentials?
    - What are the APIs, services, servers, databases used in the template?
    - What operating system versions should support it?
8. Once all the assets are in place, zip the file and submit the .zip file to Neutrinos by raising a support ticket on [support@neutrinos.co](mailto:support@neutrinos.co). The Neutrinos team will review the template and upload the component(s) to the MarketPlace. The folder should have the following contents:
    ![template folder](/resources/Storage/components-guide-for-release-6/template_folder.png)
