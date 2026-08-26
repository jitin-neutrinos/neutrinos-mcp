# Initialize and Preview the App

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/initialize-and-preview-the-app>

After creating the app, perform the following steps to initialize and preview the app.

1. On the [Application page](/smart/project-concepts/studio-application-page), on the top-center, a drop-down list of tasks can be found. Click the down arrow.
   ![Live view for LMS](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/IL1.png)
2. Select **Initialize** task from the list. Initializing determines certain aspects of how the system or program should function.
   ![initialization of LMS](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/IL2.png)
    ![Information](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/info.png)
    Hovering over each of the tasks in the task list reveals a brief description of that task.
3. Click on the **Run Task** button. The app gets initialized.
   ![Run LMS](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/IL3.png)
    ![Warning](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/warning.png)
    Make sure that you are connected to the internet to run the **Initialize** task successfully.
4. After the **Initialize** task is complete, select the **Live View** task from the list.
   ![live view of LMS](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/IL4.png)
5. Click on the **Run Task** button. This task builds your app on the local machine. You can access the build log from the Terminal window.
6. If the **Live View** task completes successfully, it will start the app server and your app will be launched in the default browser. You can see the app running at the address **localhost** and port number** 4200**. Any new changes saved in the studio will restart the app server and hence those changes will get reflected immediately in the app.
7. Once the app is launched, enter a city name for which you want to view the weather data. For example, Tokyo. The app should display the weather data similar to this:

![Live view of weather app](/resources/Storage/psd-tutorial-publication/project-tutorial-weather-app/weather_app_deployed.png)
