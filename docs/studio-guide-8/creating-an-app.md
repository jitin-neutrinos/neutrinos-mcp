# Types of App

<https://documentation.neutrinos.com/articles/#!studio-guide-8/creating-an-app>

### Types of App

On the [Studio home page](/articles/concepts-publication/studio-home-page), you can create the following types of apps:

- **Classic App:** A classic app is a combination of **UI-only **app and **API-only** app. Choose this app type if you want to design the UI and the server APIs in a single app.
- **API-only app: **Choose this app type if you want to create server APIs that can be consumed by any client/application.
- **UI-only app:** Choose this app type to create everything that the user can see and interact with. This includes the user interface and the client services of the app.

### Best Practices

Follow these best practices while creating an app:

- While creating an app, make sure you provide a preview image and the app description. This helps identify your app easily on [Neutrinos Console](/smart/project-concepts/neutrinos-console).
- While creating your app, use the existing assets such as templates, plugins, and components from Neutrinos Store. This saves app development time. For example,
  - If you require user validation for the app, use the [Neutrinos-login-template](/smart/project-components-documentation-copy/neutrinos-login-templates).
  - If you have a requirement of displaying the data in excel sheets into HTML pages, use the [Excel Viewer](/smart/project-components-documentation-copy/excel-sheet) widget.
- Use the** Plugins** option on the top menu to [download existing app plugins](/articles/studio-guide-8/import-plugin) to your workspace. Plugins downloaded on the workspace can be applied to any app.

Naming ConventionsUse meaningful names within your apps. Stay away from using shortcuts, abbreviations, and acronyms. Also, use consistent naming conventions. For example, use **Leave Management System** as your app name instead of **LMS** as LMS also stands for Learning Management System.Use PascalCase.
Suffix foreign keys with "**Id"** for easy recognition. For example, **CustomerId**.

### Create an App

To create an app, click the respective **Create App** icon on the Studio Home page. The **Create New App** window opens up.

Enter the app details:

- **App Name:** Enter the name of the app that you want to create. The app name must have a minimum of 6 characters with no special characters except the hyphen (-).
- **Version:** The version of the app you are creating. By default, the value is 1.0.0.
- **Tenant:** The application tenant. Each customer organization is called a tenant. By default, the tenant is **n****eutrinos**.
- **Description**: Enter a brief description of your application.
- Upload a preview image of your app. Select an image from your local machine.
- This field is only visible when you are creating a **classic** app. In the **Templates **section, select the [app template](/smart/project-concepts/app-templates) to use in your app. You can either choose a **Blank **template or download an [existing template](https://store.neutrinos.co/web/catalog/templates) from Neutrinos Store by clicking the **+** icon.

### 

### Edit App Details

To edit an app, click **...** (the Edit button)  at the bottom right of the app and click **Edit Details**. The **Edit App Details page **opens up. After editing the app details, click **Save** to save the changes. Click **Cancel** to exit the window without saving the changes.

![edit app window](/resources/Storage/studio-guide-8/edit_app_details.png)

###
