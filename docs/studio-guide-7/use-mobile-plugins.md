# View Existing Plugins

<https://documentation.neutrinos.com/articles/#!studio-guide-7/use-mobile-plugins>

A **Mobile Plugin** is an add-on code that provides JavaScript interface to native components. They allow your app to use native device capabilities beyond what is available to pure web apps.

On Neutrinos Studio, you can perform the following operations with respect to Mobile Plugins:

1. View the existing plugins
2. View platforms
3. Adding plugins
4. Removing plugins

Initialize your application and your mobile platform(Android initialize or ios initialize) before you perform the above operations.

### View Existing Plugins

You can view the existing plugins that already exist in your application. To do so, perform the following:

1. After you initialize your app for mobile, open the default or any terminal on the Neutrinos Studio and enter cordova plugins .
2. After you enter the command, you can view all the plugins and their versions that are installed in the application.

### View Platforms

1. Enter cordova platforms command on the terminal and you can view the platforms.

If you would have initialized android, the platform will be android and the version. If you have initialized ios. then the platform will be ios and the version of the platform.

![platform cordova](/resources/Storage/studio-guide-7/platforms.png)

### Add Plugins

You can add plugins in three ways, they are:

1. Using npm
2. Using GitHub
3. Using local machine downloads Cordova plugin add <path where plugin.xml exist in local machine> Note: give the relative path to keep the plugin within the project

#### Using npm

You can add any non-existing plugins that you want to use for your application. To add a plugin, use the following code:

Copy CodeCodecordova plugin add <plugin-name>@<plugin-version>

/* For example: cordova plugin add cordova-plugin-neushake@1.0.0 */

#### Using GitHub

You can add non-existing plugins for your application using the GitHub links for a particular plugin. To do so, use the following code in the terminal:

```code
cordova plugin add <plugin link from github> /* For example: cordova plugin add https://github.com/NeutrinosPlatform/cordova-plugin-neushake.git */
```

To get the link of the plugin, perform the following steps:

1. In GitHub, search for the plugin you want to add.
2. Open the plugin and click clone and download.
3. Copy the link.

#### Using local machine

You can add plugins to your app by downloading the plugin to your local machine and mentioning the path of the downloaded plugin.

```code
cordova plugin add <path where plugin.xml file exist>/* For example: cordova plugin add C:\Users\neutrinos\Downloads\cordova-plugin-neushake-master */
```

### Remove Plugins

You can remove any existing plugins that you don't need for your application. To do so, use the following command in the terminal:

```code
cordova plugin rm <plugin name>/* For example: cordova plugin rm cordova-plugin-neushake  */
```

Removing a plugin remains the same no matter how it was added.

---

| **Learn More:** |
| --- |
| [Mobile Security Best Practices](/smart/project-best-practices/mobile-security-best-practices) |
