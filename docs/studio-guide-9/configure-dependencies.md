# Update Device-Specific Configurations on Config.xml

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-dependencies>

The **Config.xml** file provides a number of default settings that allow you to control many aspects of an app's behavior. It is arranged based on the W3C's Packaged Web Apps (Widgets) specification and extended to specify core Cordova API features, plugins, and platform-specific settings.

To access this file, click the **Configure XML** option in the side menu of the [Studio Application page](/smart/project-concepts/studio-application-page).

![Config XML editor](/resources/Storage/studio-guide-9/xml.png)

Using this file, you can configure Cordova application resources for various types of devices such as mobile, tablets, and browsers. The common configuration settings that you perform are:

**Name: **The app's formal name, as it appears on the device's home screen and within app-store interfaces.
 Copy CodeXML<name>bhive-app</name>

**Description:** The metadata that may appear within app-store listings.
 Copy CodeXML<description> A sample app that responds to the deviceready event</description>

- **Author:** The contact information that may appear within the app-store listing.
- **Plugins:** Details about which plugin to restore for a hybrid app.
    Copy CodeXML<plugin name="cordova-plugin-device" spec="^1.1.0">
    <variable name="MY_VARIABLE" value="my_variable_value" />
   </plugin>

**Access:** The set of external domains that the app is allowed to communicate with. This default value allows the app to access any server.

 Copy CodeXML<access origin="*"></access>








 **Intent: **Controls which URLs the app can ask the system to open. By default, no external URLs are allowed.

 Copy CodeXML<allow-intent href="http://*/*" />

- **Application icon:** Application icons for various platforms such as Android and iOS.
    Copy CodeXML<icon src="res/IOS/icon.png" platform="IOS" width="57" height="57"
   density="mdpi" />

**Hooks:** Custom scripts that will be called by Cordova when certain events occur. Define your custom scripts here. For example, to run a custom script after a plugin is installed.

 Copy CodeXML<hook type="after_plugin_install" src="scripts/afterPluginInstall.js" />










 **Platform: **Configure preferences or elements that are specific to particular platforms. Apart from the preferences provided by default in the config.xml file, you can configure a range of other entries in this file that set preferences for your app on specific platforms. See [Cordova Documentation](https://cordova.apache.org/docs/en/latest/config_ref/#preference) to learn about the other preferences that you can set in your app.
 Copy CodeXML<platform name="android"><preference name="Fullscreen" value="true"
/></platform>







 **Splash screen:** Displays or hides a splash screen during the application launch. For example:


 Copy CodeXML <splash src="src/assets/iOS/Resources/splash/Default@2x~iphone~comany.png"/>


 For iOS devices, the splash screen should be chosen based on the dimensions. The default dimensions are listed below. However, there is no need to provide a splash screen image for each possible device, viewport, and orientation; iOS will choose the best image for the situation automatically.


 **iPhone:**





 **Scale **


 **Size and Filename**




 2x*


 1334 x 1334


Default@2x~iphone~anyany.png





 2x


 750 x 1334


Default@2x~iphone~comany.png





 2x


 1334 x 750


Default@2x~iphone~comcom.png





 3x*


 2208 x 2208


Default@3x~iphone~anyany.png





 3x


 2208 x 1242


Default@3x~iphone~anycom.png





 3x


 1242 x 2208


Default@3x~iphone~comany.png






 **iPad:**







 **Scale
 **


 **Size and Filename**










 2x*


 2732 x 2732


Default@2x~ipad~anyany.png





 2x


 1278 x 2732


Default@2x~ipad~comany.png








 For Andriod devices, the splash screen should be selected based on the density of the screen. The default densities are:









 **Density
 **


 **
 Dimensions**




 LDPI






 Portrait: 200x320


 Landscape: 320x200






 MDPI






 Portrait: 320x480


 Landscape: 480x320






 HDPI






 Portrait: 480x800


 Landscape: 800x480






 XHDPI






 Portrait: 720x1280


 Landscape: 1280x720






 XXHDPI






 Portrait: 960x1600


 Landscape: 1600x960






 XXXHDPI






 Portrait: 1280x1920


 Landscape: 1920x1280









 For more information about each configuration, see the [Cordova documentation](https://cordova.apache.org/docs/en/latest/config_ref/).
To view step-by-step instructions on how to change the default icons and splash screens, see [Change Mobile Splash Screen and Icons](/smart/project-how-to-articles/change-mobile-splash-screen-and-icons).
