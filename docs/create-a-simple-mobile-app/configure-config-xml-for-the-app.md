# Update Config.xml

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/configure-config-xml-for-the-app>

When you create an app, a default configuration file named config.xml also gets created with the app. In this app, you will make use of the **Optical Character Recognition(OCR)**  and** Document Scanner** plugins to scan a PAN card and capture the information within that card.

Click **[Config XML](/smart/project-sample-how-to-guide/configure-dependencies) **on the menu list of the Studio Application page. Replace lines 90 to 120 with the following code to add the required plugins for this application.

```javascript
<plugin name="cordova-plugin-device" spec="2.0.2" />    <engine name="android" spec="7.1.4" />    <engine name="ios" spec="5.0.1" />    <plugin name="cordova-plugin-x-toast" spec="2.7.2" />    <plugin name="cordova-plugin-inappbrowser" spec="3.1.0" />    <plugin name="cordova-plugin-splashscreen" spec="5.0.2" />    <plugin name="cordova-plugin-whitelist" spec="1.3.3" />    <plugin name="cordova-plugin-geolocation" spec="4.0.1" />    <plugin name="cordova.plugins.diagnostic" spec="4.0.10" />    <config-file parent="NSBluetoothAlwaysUsageDescription" platform="ios" target="*-Info.plist">        <string>This app requires access to function properly</string>    </config-file>    <plugin name="cordova-plugin-mobile-ocr" spec="3.1.1" />    <plugin name="cordova-plugin-uniquedeviceid" spec="1.3.2" />    <plugin name="com.cordova.plugins.cookiemaster" spec="1.0.1" />
```

Thi add the required plugins for this application.
