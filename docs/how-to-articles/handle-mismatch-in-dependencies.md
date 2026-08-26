# Web Apps

<https://documentation.neutrinos.com/articles/#!how-to-articles/handle-mismatch-in-dependencies>

Oh no, I Messed Up! This is a common scenario that a developer would face while creating apps with dependencies. But worry not, here are a few ways to get out of the mess.

### Web Apps

If you have messed up your project dependencies while deploying your web app and want to start over, perform the following steps:

1. Navigate to the <app_name>/app folder in your workspace.
2. Delete the node_modules folder and the package-lock.json file.
3. Navigate to Neutrinos Studio, install the project dependencies, and initialize your app.
    ![Initialize app](/resources/Storage/how-to-articles/initialize.png)

### Mobile Apps

If you want to remove or add a single [plugin](/smart/project-concepts/plugin), execute the respective command and then rebuild (Run the respective Andriod or iOS build) and run/emulate the app.



 Copy CodeMarkdown//To remove a plugin
cordova plugin remove <cordova-plugin-name>

//To add a plugin
cordova plugin add <cordova-plugin-name>

There can be a few plugins that are platform dependent. In such cases, if you only want to remove a single platform, navigate to your app directory, execute the following code, and then rebuild and run the app.



 Copy CodeMarkdowncordova platform remove android | ios



 If you have messed up your project dependencies while building your mobile app and want to start over, perform the following tasks:




 Navigate to the <app_name>/app folder in your workspace.


 Delete the node_modules, package-lock.json, platforms, and plugins folders.



 Navigate back to Neutrinos Studio and re-install your app dependencies.




 Run the** Initialize** task.


 ![Initialize app](/resources/Storage/how-to-articles/initialize.png)







 Run the **Initialize Mobile **task.




 ![Initialize app](/resources/Storage/how-to-articles/initialize.png)







 (optional) To install CocoaPods dependencies for iOS apps, change directory to platform/ios and install all CocoaPods dependencies and then change the directory back to the app.Copy CodeMarkdowncd platform/ios && pod install.

cd ../../



 (optional) The iOS build might require you to add the following build flags. You can remove them if not necessary.Copy CodeMarkdownnpm run build-mobile && cordova build ios
 --device
 --codeSignIdentity="iPhone Developer"
 --developmentTeam="your-team-id"
 --buildFlag="-allowProvisioningUpdates"
 --buildFlag="-UseModernBuildSystem=0"
 --provisioningProfile="your-app's-provisioning-profile-if-required"

![Information](/resources/Storage/how-to-articles/info.png)




 Changes made in the **config.xml **file will reflect after doing a build, you don't have to remove and re-add platforms.


 Make sure to always commit your code so that you can revert changes that you made to your code.
