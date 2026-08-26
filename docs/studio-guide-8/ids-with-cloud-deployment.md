# IDS with Cloud Deployment

<https://documentation.neutrinos.com/articles/#!studio-guide-8/ids-with-cloud-deployment>

If your app is using the Neutrinos Identity Server (IDS) for authentication and if you want to deploy the app using the **1-click deploy** option, perform the following steps:

1. Enable the 1-click deploy feature on Studio and restart Studio. See [Enable 1-click deploy](/articles/studio-guide-8/deploying-an-application-on-cloud/a/h3_1151222537) to learn how.
2. Deploy the app using the **1-click deploy** option.
3. Open to Neutrinos Console and navigate to the **Apps** page.
4. Locate your application card. Once the app is successfully deployed, click the **Web Link**. ![App web link](/resources/Storage/studio-guide-8/web_link.png)
5. Copy the web link and navigate back to Neutrinos Studio.
6. Open the IDS settings for your app and update the Login redirect URI with **<web_link>/api/login/cb**.
7. Update the Logout Redirect URI with **<web_link>/api/logout/cb**.![Login and logout redirect URIs](/resources/Storage/studio-guide-8/login_logout_redirect.png)
8. Save your app
9. Navigate back to the browser and refresh the deployed app. You will now see a login screen to authenticate your app users before they access the app.
