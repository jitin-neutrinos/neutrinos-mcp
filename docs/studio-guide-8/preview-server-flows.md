# Preview Server Flows

<https://documentation.neutrinos.com/articles/#!studio-guide-8/preview-server-flows>

Before deploying your application, you can preview the functionality of the server flows by using the **Live View** option from the Task drop-down list.

Perform the following steps:

1. **Initialize** the application by clicking the** Initialize **option from the **Task** drop-down list. Click the play icon to run the task. The command that executes during the initialization task is nmp install.
    ![Initialize app](/resources/Storage/studio-guide-8/project-how-to-articles/initialize_new.png)
    ![initialization of the server](/resources/Storage/studio-guide-8/project-how-to-articles/iniserver.png)
2. Once the initialization task is done, select **Live View** from the task drop-down list and run the task. The command that executes for the live view task is npm run start-dev.
    ![live view of the server](/resources/Storage/studio-guide-8/project-how-to-articles/liveserver.png)
3. After the dev server has started, you can call the HTTP Request from Client Services to hit the server's HTTP endpoint and perform server tasks.
