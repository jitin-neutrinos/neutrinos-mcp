# Enable 1-Click Deploy

<https://documentation.neutrinos.com/articles/#!studio-guide-9/deploying-an-application-on-cloud>

Neutrinos Studio allows you to deploy your apps on the Google Cloud Platform using the **1-Click Deploy** feature. If you choose this feature, the platform automatically generates deployment packages for different environments and devices. Also, you can deploy both web apps and mobile apps using a single code base, thus enabling better code efficiency and change management.

#### Enable 1-Click Deploy

The** 1-Click Deploy** feature is disabled by default on Neutrinos Studio. To use this feature, open the settings.json file in the $Home/.neutrinos folder of your home directory and add the following property at the root of the JSON object in that file. If the property already exists, set its value to true. After saving the changes, restart Neutrinos Studio to view the 1-Click deploy icon.

```javascript
"enableOCD":true
```

![1-Click deploy](/resources/Storage/studio-guide-9/cloud_deploy.png)

#### Deploy the App

| ![Information](/resources/Storage/studio-guide-9/info.png) | See [IDS with Cloud Deployment](/articles/studio-guide-9/ids-with-cloud-deployment) if you have enabled IDS services for your app. |
| --- | --- |

To deploy an app onto the cloud (without IDS configured):

Click the **1-Click Deploy** icon in the top-right corner of Neutrinos Studio.




 Select the deployment target for the build.




 Click **Deplo****y** to schedule the build for deployment.









 **Check the Status of your Build**

 To check the status of your deployment, login to Neutrinos Console, and navigate to the **Apps** section and select your app card to view the build status. The app deployment will take a few minutes as the deployment process involves multiple steps. You can view individual steps status and completion duration using the app build details section.


 Build Steps


 Build steps indicate the build step progress along with individual step duration. Following are the possible build steps:










 **Status**


 **Description**






 **Scheduled**


 An app is scheduled for build and deployment.





 **Processing**



 The scheduled app build or current step is in progress.




 **Success**


 Individual build steps are completed successfully.







 **Failed**


 The app build status changes to **failed** when the individual build step has failed.















 Use the **Refresh** icon at bottom of each panel to refresh the build timeline. To download the build logs, click the **Download Log File **icon.


 If your app gets built successfully, the build status will be updated to Success. If your build fails, the build status will be updated to Failed. In such a case, you can download the build logs and check for app errors.







 Redeploy your App

 If your build fails or if you face connectivity issues during deployment, use the **Re-deploy** option on the app card to reschedule the build. If you make changes to the app in Neutrinos Studio, use the **1-Click Deploy** option again to redeploy app changes onto the Cloud. You can schedule only one active build for a given app at a time.

View the Deployed AppWhen your build is completed successfully, click the **Web Link **icon to launch your app.If you had selected an Android build, click **Download the .apk file** icon to download the android build of your app.If you had selected an iOS build, click **Download the .ipa file** icon to download the iOS build of your app.
