# Step 1: Convert the App to a PWA

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/step1-convert-the-app-into-pwa>

PWA combines existing web technologies with modern browser features. They offer similar capabilities to iOS/Android/desktop apps. They are lighter on user devices' systems resources and are more efficient to manage as they can be installed directly from the browser and don't require app stores like native mobile apps.

After [creating the weather app](http://docs1.neutrinos.co/articles/psd-tutorial-publication), to convert the app to a PWA, perform these steps on Neutrinos Studio:

1. Open the weather app. The [Studio application page](/smart/project-concepts/studio-application-page) is displayed. Navigate to the **Settings** editor and select **PWA**.
2. Toggle **PWA** to **True**.
3. Click **Okay **to confirm the action. On click of **Okay**, the app is converted to a PWA. A default [application manifest](/smart/project-concepts/application-manifest) and [service worker](/smart/project-concepts/service-worker) are created, and necessary plugins are installed on the [Client Services Designer](/smart/project-concepts/client-services-designer).
4. Also, the PWA editor is auto-populated with default values. You can update them according to your requirement.
  1. **Name: **The name of the application that you entered during the app creation. This field cannot be updated.
  2. **Short Name: **The short name for your application.
  3. **Display: **How much of the browser UI should be displayed to the user.
  4. **Scope: **The navigation scope of this web app's application context.
  5. **Start URL: **The preferred URL that should be loaded when the user launches the web application.
  6. **Theme Color: **Theme color for the application. Enter the theme color to be** #1976d2. **
  7. **Background Color: Background color** for the application page to display. Enter the background color to be **#fafafa.**
  8. **Icons: **Image files that can serve as application icons for different contexts.

![PWA Settings](/resources/Storage/tutorial-create-a-pwa/PWA.png)

See [Convert to Progressive Web App(PWA)](/smart/project-sample-how-to-guide/convert-to-progressive-web-app) documentation to learn more about each of these fields. You can accept the default values in these fields, or update them as required.
