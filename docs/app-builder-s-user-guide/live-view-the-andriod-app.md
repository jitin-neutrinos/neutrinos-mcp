# Step 1: Initialize the app

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/live-view-the-andriod-app>

Before deploying your app, you can preview your mobile app and perform end-to-end testing of your application functionality. to do that, perform the following steps:

### Step 1: Initialize the app

Initialize the application by clicking the **Initialize** option from the **Task** drop-down list. Click the play icon to run the task. The command on which the initialization happens is nmp install. This command installs **node_modules** for the app.

![Initialize](/resources/Storage/app-builder-s-user-guide/initialize_new.png)

You can see two tabs running the **Initialize** task in the terminal window.

- The first tab is labeled as **Initialize (Client)**. It initializes the app and the Client Services that you have created in the app.
- The second tab is labeled as** Initialize (Server)**. It initializes the server flows that you have created for the **Server **of the application.

### Step 2: Initialize the app for Android

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | Make sure you initialize the app before performing **Initialize Android**. Else the mobile initialization will fail. |
| --- | --- |

Initialize the mobile application by clicking the **Initialize Android **option from the **Task** drop-down list depending upon the mobile OS that you are creating the app for. Click the play icon to run the task. This task installs Cordova plugins and Cordova platforms for your app.

The command on which the initialization happens for android is npm run initialize-android.

![Initialize mobile app](/resources/Storage/app-builder-s-user-guide/initialize%20mobile.png)

You can see the **Initialize** task in the terminal labeled as **Initialize Android(Client)**. It initializes the application and Client Services that you have created in the app.

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | The server does not get initialized for the mobile applications as it is a node app. |
| --- | --- |

### Step 3: Emulate your App (optional)

**Perform this step to open the mobile emulator and test the app in the emulator. If you want to build the app and test it in your device, navigate to Step 5.**

After you initialize your mobile, you can choose to emulate your app. An emulator is a software that creates a virtual machine version of a mobile device, such as an Android phone or an iPhone. You use this software to run applications on the virtual mobile on your computer as though it was the actual mobile device.

Download and install the Android emulator from [Android Studio](https://developer.android.com/studio/run/emulator) or the iOS emulator from [Xcode](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/iOS_Simulator_Guide/GettingStartedwithiOSSimulator/GettingStartedwithiOSSimulator.html).

Click the **Android Emulate **from the Task drop-down list to build your mobile app and open the respective emulator.

The android app gets built and opens the Android emulator in Neutrinos Studio. You can access the build file (.apk file) from the location highlighted in the image below. You can use this emulator as a target platform to run and test your **Android** applications on your PC.

### Step 4: Build your App

You can build your app on your local machine by choosing the **Android Build **option from the Task drop-down list.

Performing an** Android build** compiles app resources and source code, and packages the app into an** APK** file that you can test, deploy, and distribute. Transfer the** .apk** file to your Android phone to perform end-to-end testing.

After completely testing your app, you can [deploy your app](/articles/app-builder-s-user-guide/deploying-an-application/a/GUID-070999B0-5864-47CF-AC68-E5569E12A698__GUID-98408369-771A-4220-9F0C-E96AB798CE41) from Neutrinos Studio. Note that deploying your app costs as the deployment process uses the Google Cloud Platform storage and resources. So make sure to build your app multiple times and test the app thoroughly on your local machine before performing the final deployment.
