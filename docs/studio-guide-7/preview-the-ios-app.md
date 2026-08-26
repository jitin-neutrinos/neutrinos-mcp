# Step 1: Initialize the app

<https://documentation.neutrinos.com/articles/#!studio-guide-7/preview-the-ios-app>

Before deploying your iOS app, you can preview your app and perform end-to-end testing of the application functionality. To do that, perform the following steps:

### Step 1: Initialize the app

Initialize the application by clicking the **Initialize** option from the **Task** drop-down list. Click the play icon to run the task. The command on which the initialization happens is nmp install. This command installs **node_modules** for the app.

![Initialize](/resources/Storage/studio-guide-7/initialize_new.png)

You can see two tabs running the **Initialize** task in the terminal window.

- The first tab is labeled as **Initialize (Client)**. It initializes the app and the Client Services that you have created in the app.
- The second tab is labeled as** Initialize (Server)**. It initializes the server flows that you have created for the **Server **of the application.

### Step 2: Initialize Mobile

| ![Information](/resources/Storage/studio-guide-7/info.png) | Make sure you initialize the app before performing **Initialize iOS**. Else the mobile initialization will fail. |
| --- | --- |

Initialize the mobile application by clicking the **Initialize iOS **option from the **Task** drop-down list. Click the play icon to run the task. This task installs Cordova plugins and Cordova platforms for your app.

The command on which the initialization happens for iOS is npm run initialize-ios.

![Initialize mobile app](/resources/Storage/studio-guide-7/initialize%20mobile.png)

You can see the **Initialize** task in the terminal labeled as **Initialize iOS(Client)**. It initializes the application and Client Services that you have created in the app.

| ![Information](/resources/Storage/studio-guide-7/info.png) | The server does not get initialized for the mobile applications as it is a node app. |
| --- | --- |

### Step 3: Perform pod install

After you perform the **Initialize iOS** task in the terminal window, perform the following steps:

1. Change the directory to **<appname>/app/platform/ios**.**Copy CodeMarkdowncd <appname>/app/platform/ios**
2. Execute the** pod install** command. This command downloads and installs new pods for the iOS app. It also writes the version it has installed in the **Podfile.lock** file. Note that you will need **CocoaPods** installed to successfully run this command. Copy CodeMarkdownpod install
3. Navigate back to your app directory. Copy CodeMarkdowncd../..

### Step 4: Emulate your App (optional)

**Perform this step to open the iOS SImulator and test the app. If you want to build the app and test it in your device, navigate to Step 5.**

After you initialize your app, you can choose to emulate your app. An emulator/simulator is a software that creates a virtual machine version of a mobile device, such as an iOS phone or an iPhone. You use this software to run applications on the virtual mobile on your computer as though it was the actual mobile device.

Download the iOS emulator from [Xcode](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/iOS_Simulator_Guide/GettingStartedwithiOSSimulator/GettingStartedwithiOSSimulator.html).

The emulator lets you test an app and determine how well it performs on various types of mobile devices. It allows analysis of mobile content in real-time, locate errors in code, view rendering in an environment that simulates the mobile browser, and optimize the site for performance.

Click the **iOS Emulate** option from the **Task** drop-down list to build your mobile app and open the respective emulator.

An iOS emulator will open using which you can test your iOS application on your PC. This step does not create a** .ipa** file.

If you want to create the file, run this command in the terminal window. Update the --developmentTeam="<your_team_id>" option with your** team ID **before you execute this command.

```markdown
npm run build-mobile && cordova build ios --device --codeSignIdentity="iPhone Developer"   --developmentTeam="<your_team_id>" --buildFlag="-allowProvisioningUpdates"   --buildFlag="-UseModernBuildSystem=0"
```

If you want to build and test the **.ipa** file, make sure the following tasks are already performed:

- Should have an Apple Developer account.
- Should have registered the device in your Apple Developer account.
- Should have registered your** bundle_id** with capabilities in your Apple Developer account. Note that by default, push notification capabilities are enabled in Neutrinos apps.

### Step 5: Build your App

You can build your app on your local machine by choosing **iOS Build **option from the Task drop-down list.

Performing an** iOS build **compiles app resources and source code, and packages the app into an** IPA **file that you can test, deploy, and distribute. Transfer the **.ipa** file to your iPhone to perform end-to-end testing.

After completely testing your app, you can [deploy your app](/articles/studio-guide-7/deploying-an-application/a/GUID-070999B0-5864-47CF-AC68-E5569E12A698__GUID-98408369-771A-4220-9F0C-E96AB798CE41) from Neutrinos Studio. Note that deploying your app costs as the deployment process uses the Google Cloud Platform storage and resources. So make sure to build your app multiple times and test the app thoroughly on your local machine before performing the final deployment.
