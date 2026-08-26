# Deploy a UI Only app

<https://documentation.neutrinos.com/articles/#!studio-guide-9/deploy-web-app-external-source>

You can deploy the Web applications built on Neutrinos Studio to external sources such as PM2, IIS, and NGINX. Perform the following steps:

### Deploy a UI Only app

**Build the UI app**

To build a **UI Only **app, open the default terminal on Neutrinos Studio, navigate to the app folder, and run the following command:

```markdown
 cd app npm run build-web
```

![pwa build command](/resources/Storage/studio-guide-9/pwa%20build.png)

A dist folder is generated within the app folder containing all the build files.

**Deploy the app:**

- To deploy the app to the IIS server, see the [How to Host a Static Website using](https://newhelptech.wordpress.com/2018/06/20/step-by-step-how-to-host-a-static-website-using-iis-in-windows-server-2016/) blog. Make sure you select the /dist folder as the Physical path in Step7.
- To deploy the app to the Nginx server, see the [Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/). Copy the /dist folder and place it in the host path given in the NGINX config.

---

### Deploy an API Only app

**Build the API app:**

Open the default terminal on Neutrinos Studio, navigate to the server folder, and run the following command:

```markdown
 cd server npm run grunt
```

A build folder is generated within the server folder containing all the build files.

Deploy the app:

To deploy the app to the IIS or Nginx server, configure a reverse proxy on the respective server. Refer to these blogs to learn more:

- [Configuring reverse proxy on IIS](https://docs.microfocus.com/OMi/10.62/Content/OMi/AdminGuide/Hardening/RevProxy_IIS.htm)
- [Installing and Configuring Nginx](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- [Deployment process with PM2](https://codeburst.io/automate-your-deployment-process-with-pm2-b0fd7c256223)

---

### Deploy a Classic App

To deploy a classic app, follow the steps mentioned in [Deploy a UI Only app](/articles/studio-guide-9/deploy-web-app-external-source/a/h3_1938725575) and [Deploy an API Only app](/articles/studio-guide-9/deploy-web-app-external-source/a/h3__1156091723).
