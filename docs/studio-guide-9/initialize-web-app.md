# Initialize the App

<https://documentation.neutrinos.com/articles/#!studio-guide-9/initialize-web-app>

The Initialization process installs the required **node_modules** for your application.

Select the **Initialize** option from the **Task** drop-down list and click the **play** icon to initialize the web application. The command on which the initialization happens is npm install.

![Initialize app](/resources/Storage/studio-guide-9/initialize_new.png)

Based on the type of app you created, respective services will get initialized. For example, if you are initializing a **classic** app, both the **Client** and **Server **services get initialized.

![Client and server services initalizing](/resources/Storage/studio-guide-9/init_cli_server.png)

If you are initializing a **UI Only** app, only client services get initialized. If you are initializing an **API Only** app, then the server services are initialized.
