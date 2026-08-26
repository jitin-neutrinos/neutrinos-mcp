# Change Splash Screens and Icons

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/change-mobile-splash-screen-and-icons>

When you create an app, Neutrinos Studio creates default splash screens and icons of different sizes in the config.xml file. You can access them on the [config.xml editor](/smart/project-sample-how-to-guide/configure-dependencies) in your application.

#### Change Splash Screens and Icons

If you want to change the default splash screens and icons, perform the following:

1. Depending on the platform, Android or iOS, understand the dimensions of splash screens and icons that you should create. See [Cordova documentation](https://www.npmjs.com/package/cordova-plugin-splashscreen) to learn about the dimensions for each platform.
2. Create splash screens and icons. You can use tools such as [Ape Tools](https://apetools.webprofusion.com/#/) to create all the required icons and splash screens of different dimensions. These tools create an app bundle based on the platform that you select. After you download the bundle, you can view the icons and splash screens in the respective folders similar to that of the folders in the [Assets editor](/smart/project-sample-how-to-guide/add-assets). For example, this is the app bundle for Android that is downloaded from Ape Tools:
    ![App bundle from Ape Tools](/resources/Storage/how-to-articles-8/andriod_app_bundle.png)![folders in assets editor](/resources/Storage/how-to-articles-8/folders_assets_editor.png)
3. Navigate to the [Assets editor](/smart/project-sample-how-to-guide/add-assets) in your application and upload the splash screens and icons in the respective folders. For example, replace the **icon.png** in the **drawable-hdpi** folder with the **icon.png** in the **drawable-hdpi** folder of the app bundle.
    ![delete icon.png](/resources/Storage/how-to-articles-8/delete_icon.png)
    ![upload icon.png](/resources/Storage/how-to-articles-8/upload_icon.png)
4. Save and run the app.

#### Disable Splash Screens

If you want to disable the splash screen in your app, navigate to the config.xml editor, and add the following preference:

```javascript
<preference name="SplashScreenDelay" value="0"/>
```

#### Set Splash Screen Preferences

On the **Config.xml editor**, you can also add preferences to fade or delay the splash screen. See the [Cordova documentation](https://www.npmjs.com/package/cordova-plugin-splashscreen#preferences) to learn more.

#### Use Adaptive Icons

You can use adaptive icons on your mobile application to display a variety of shapes across different device models. For example, you can display an adaptive launcher icon in a circular shape on one OEM device, and display a squircle on another device.

See [Cordova documentation on Adaptive Icons](https://cordova.apache.org/docs/en/latest/config_ref/images.html#adaptive-icons) to learn how to add them in your application.
