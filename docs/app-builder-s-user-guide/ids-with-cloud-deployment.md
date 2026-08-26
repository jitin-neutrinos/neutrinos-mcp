# IDS with Cloud Deployment

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/ids-with-cloud-deployment>

If your app is using the Neutrinos Identity Server (IDS) for authentication and if you want to deploy the app using the **1-click deploy** option, perform the following steps:

1. Deploy the app using the **1-click deploy** option.
2. Open to Neutrinos Console and navigate to the **Apps** page.
3. Locate your application card. Once the app is successfully deployed, click the **Web Link**. ![App web link](/resources/Storage/app-builder-s-user-guide/web_link.png)
4. Copy the web link and navigate back to Neutrinos Studio.
5. Open the IDS settings for your app and update the Login redirect URI with **<web_link>/api/login/cb**.
6. Update the Logout Redirect URI with **<web_link>/api/logout/cb**.![Login and logout redirect URIs](/resources/Storage/app-builder-s-user-guide/login_logout_redirect.png)
7. Save your app
8. Navigate back to the browser and refresh the deployed app. You will now see a login screen to authenticate your app users before they access the app.
