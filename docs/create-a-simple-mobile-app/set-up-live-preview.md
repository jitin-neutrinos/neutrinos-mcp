# Initialize the app

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/set-up-live-preview>

To initialize your app, perform the following:

1. On the Application page, on the top-center, you will see a drop-down list of tasks. Click the down arrow.
    ![Live view for LMS](/resources/Storage/create-a-simple-mobile-app/IL1.png)
2. Select the **Initialize** task from the list and click the **Run **button. The command on which the initialization happens is nmp install. This command installs **node_modules** for the app.
3. After the application is initialized, you need to initialize the application for mobile. To do so, click **Android Initialize **or **Ios Initialize** depending upon the mobile OS that you are creating the app for and **Run** the task. This task installs Cordova plugins and Cordova platforms for your app.

![initialization of LMS](/resources/Storage/create-a-simple-mobile-app/mobileinitialize.png)

| ![Information](/resources/Storage/create-a-simple-mobile-app/info.png) | Hovering over each of the tasks in the task list reveals a brief description of that task. Also, If you have a subscription to the platform, you can also Initialize and build this app as an iOS app. |
| --- | --- |

You![](http://docs1.neutrinos.co/DXR.axd?r=1_88-Qerdk) can track the progress of the task from the Terminal window.

| ![Warning](/resources/Storage/create-a-simple-mobile-app/warning.png) | Make sure that you are connected to the internet to run the **Initialize** task successfully. |
| --- | --- |
