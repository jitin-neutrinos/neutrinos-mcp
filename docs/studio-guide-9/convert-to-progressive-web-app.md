# Convert to Progressive Web App(PWA)

<https://documentation.neutrinos.com/articles/#!studio-guide-9/convert-to-progressive-web-app>

| ![Information](/resources/Storage/studio-guide-9/info.png) | To convert your app to PWA, you need Neutrinos Studio 7.7.0 or later. |
| --- | --- |

You can convert any app to a [Progressive Web App(PWA)](/smart/project-concepts/progressive-web-app) by enabling the **PWA** toggle button in the **Settings** editor. Once enabled, the Studio will create a default [service worker](/smart/project-concepts/service-worker) and an [application manifest](/smart/project-concepts/application-manifest) file.

To convert your application to PWA, perform the following steps:

1. Click **Settings** on the [Studio Application page](/smart/project-concepts/studio-application-page), and select **PWA**.
    ![Selecting PWA](/resources/Storage/studio-guide-9/pwa1.png)
2. Toggle **PWA** to true.
    ![Enable PWA](/resources/Storage/studio-guide-9/pwa2.png)
3. **Note that once you convert your app to a PWA, you cannot convert it back to a standard app using this editor.** Click **Okay** to confirm your action.
    ![confirmation pop-up](/resources/Storage/studio-guide-9/pwa_popup.png)
4. Update the following properties of your application manifest in the PWA editor to suit your company's brand guidelines:
  - **Name: **The name of the application that you entered during the app creation. This field cannot be edited.
  - **Short Name: **The short name for your application.
  - **Display: ** The display mode changes how much of the browser UI is shown to the user. Select a display mode from the drop-down list:
    - **standalone: **The application will look and feel like a standalone application. This can include the application having a different window, its own icon in the application launcher, etc.
    - **fullscreen:** All of the available display area is used and no user agent chrome (the visible aspect of a browser aside from the webpages such as toolbars, menu bar, tabs) is shown.
    - **minimal-ui: **The application will look and feel like a standalone application, but will have a minimal set of UI elements for controlling navigation. The elements will vary by browser.
    - **browser: **The application opens in a conventional browser tab or new window, depending on the browser and platform. This is the default.
  - **Scope: **The navigation scope of this web app's application context. It restricts what web pages can be viewed while the manifest is applied. If the user navigates outside the scope, it reverts to a normal web page inside a browser tab or window. For example, if we are setting the scope of the service worker to **/app/**, then the service worker will control requests from pages like **/app/**, **/app/lower/** and** /app/lower/lower**, but not from pages like **/app** or** /**, which are higher.
  - **Start URL: **The start URL of the web application, that is, the preferred URL that should be loaded when the user launches the web application.
  - **Theme Color: **The default theme color for the application. Use the color picker to select a color.
  - **Background Color: **A placeholder background color for the application page to display before its stylesheet is loaded. Use the color picker to select a color.
  - **Icons: **Image files that can serve as application icons for different contexts. For example, they can be used to represent the web application amongst a list of other applications. Click the** +** icon and upload icons of different dimensions.
