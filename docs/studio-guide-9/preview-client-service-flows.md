# Preview Client Service Flows

<https://documentation.neutrinos.com/articles/#!studio-guide-9/preview-client-service-flows>

After creating client services for your application, you can preview and see how the services perform their functions before deploying the application by using the **Live View** option in the **Task** drop-down list. Perform the following:

1. **Import** the client services that you have created to an application page and **Inject** the services in the constructor of the page. See [Import client services](/articles/studio-guide-9/import-client-services-to-the-page-ui) to learn more.
2. After importing the services, initialize your application by clicking the **Initialize** option in the **Task** drop-down list. Click the play icon to run the task. The command that runs during the initialization task is npm install.
    ![initialize](/resources/Storage/studio-guide-9/project-how-to-articles/initialize.png)
    ![Initialize the client](/resources/Storage/studio-guide-9/project-how-to-articles/clientini.png)
3. After the app is initialized, select **Live view** from the Task drop-down list and run the task. The command that executes the live view task is ng serve --open .
    ![Live view of client services](/resources/Storage/studio-guide-9/project-how-to-articles/clientlive.png)

The preview of the application is rendered on the browser. A **Client Service** gets triggered by clicking any action button on the application page. If the client service encounters an HTTP request, the flow of the service is transferred to the **Server Service **flow. The server flow gets executed and sends the HTTP response back to the client.
