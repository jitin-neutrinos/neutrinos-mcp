# Deploy on Cloud

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/deploying-an-application>

### Deploy on Cloud

Neutrinos Studio allows you to deploy your apps on Cloud using the **1-Click Deploy** feature. If you choose this feature, the platform automatically generates deployment packages for different environments and devices. Also, you can deploy both web apps and mobile apps using a single code base, thus enabling better code efficiency and change management.

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | See [IDS with Cloud Deployment](/articles/app-builder-s-user-guide/ids-with-cloud-deployment) if you have enabled IDS services for your app. |
| --- | --- |

![1-Click deploy](/resources/Storage/app-builder-s-user-guide/cloud_deploy.png)

To deploy an app onto the cloud (without IDS configured):

Click the **1-Click Deploy** icon in the top-right corner of Neutrinos Studio.




 Select the deployment target for the build.




 Click **Deplo****y** to schedule the build for deployment.










 ![Information](/resources/Storage/app-builder-s-user-guide/info.png)


 The Deploy feature is enabled for users having access to Neutrinos Console. If you have access to Console and are not able to use the **1-Click Deploy **feature, contact your organization admin or reach out to [Neutrinos Support](mailto:support@neutrinos.co).









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
