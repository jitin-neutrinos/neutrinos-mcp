# Set Up Live Preview

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/set-up-live-preview>

To set up a live preview of your app on your local machine, perform the following steps:

1. In the Application page, on the top-center, you will see a drop-down list of tasks. Click the down arrow.

![Live view for LMS](/resources/Storage/tutorial-create-a-leave-management-system/liveviewLMS.png)

2. Select **Initialize** task from the list. Initializing determines certain aspects of how the system or program should function.

![initialization of LMS](/resources/Storage/tutorial-create-a-leave-management-system/initializeLMS.png)

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | Hovering over each of the tasks in the task list reveals a brief description of that task. |
| --- | --- |

3. Click on the **Run Task** button. The app gets initialized. You can track the progress of the task from the Terminal window.

![Run LMS](/resources/Storage/tutorial-create-a-leave-management-system/runLMS.png)

| ![Warning](/resources/Storage/tutorial-create-a-leave-management-system/warning.png) | Make sure that you are connected to the internet to run the **Initialize** task successfully. |
| --- | --- |

4. After the **Initialize** task is complete, click the **1-click Deploy** button to deploy the base app on Cloud. The app with the login pages (that are added by default as you chose the Neutrinos Login template during app creation) will be deployed.

![1-click deploy](/resources/Storage/tutorial-create-a-leave-management-system/1-click%20deploy.png)

5. After deploying the app, you can check the status of the build from the **Apps** section of [Neutrinos Console](https://console.neutrinos.co).

6. Once the app is deployed, click the **Web App Link** to launch the app.

![The Apps section in the Neutrinos Console](/resources/Storage/tutorial-create-a-leave-management-system/web_app_link.png)

7. To setup live preview of the app on your local machine:

1. copy the base URL of the launched app.

![The base URL of the launched app](/resources/Storage/tutorial-create-a-leave-management-system/baseURL.png)

2. Navigate back to Neutrinos Studio.

3. Click **Environments.** In the **Dev** environment, update **http://****localhost:3000** in the baseURL property to the URL of the launched app. Make sure that you are updating the HTTP protocol to HTTPS.

![Update the baseURL in Environments](/resources/Storage/tutorial-create-a-leave-management-system/env_baseurl.png)

4. Save the app.

5. Click the Task drop-down list, select **Live Preview** and click **Run**. This task builds your app on the local machine. You can access the build log from the Terminal window.

If the **Live View** task completes successfully, it will start the app server and your app will be launched at the address **localhost** and port number **4200**.

Any new changes saved in the studio will restart the app server and hence those changes will get reflected immediately in the app.
