# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-from-5>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

Follow these migration steps if you are migrating your app from Neutrinos Studio 5.x to 6.0.0.

If you are migrating your app from previous releases of Neutrinos Studio, perform the migration steps mentioned in the below topics (based on the version from which you are upgrading) before you proceed with this topic.

- [Migrate to 4.0.2](/articles/neutrinos-studio-migration-guide/migrate-to-402)
- [Migrate to 3.3.1](/articles/neutrinos-studio-migration-guide/migrate-to-3)

---

### Migration Steps

If you choose to migrate your application to version 6.0.0, all the changes to your application's main.ts file will be lost. This is because your application's main.ts file will be replaced with the default main.ts file that comes with Neutrinos Studio 6.0.0 Angular seed app.

To fix this issue, perform these steps after migrating the app to 6.0:

- Open the `Ts` editor of each page and remove `this` variable from the `Get` method.

![migrate doc](/resources/Storage/neutrinos-studio-migration-guide/migrate2019-07-09_15h23_30.png)

- After migration, update all Cordova-plugins versions to the latest, in `config.xml`. Refer this for the latest Cordova plugin versions.

Copy CodeXML<plugin name="cordova-plugin-device" spec="~2.0.2"/>
 <engine name="android" spec="~7.1.4"/>
 <engine name="ios" spec="~4.5.4"/>
 <!-- <plugin name="cordova-plugin-local-notification" spec="~0.9.0-beta.2" /> -->
 <plugin name="cordova-plugin-x-toast" spec="~2.7.2"/>
 <plugin name="cordova-plugin-inappbrowser" spec="~3.0.0"/>
 <plugin name="cordova-plugin-splashscreen" spec="~5.0.2"/>
 <plugin name="cordova-plugin-whitelist" spec="1.3.3"/>
 <plugin name="phonegap-plugin-push" spec="2.2.3">
 <variable name="SENDER_ID" value="1:626566066881:android:aecfd1651b40f793"/>
 </plugin>
 <plugin name="cordova-plugin-camera" spec="~4.0.3">
 <variable name="CAMERA_USAGE_DESCRIPTION" value=""/>
 <variable name="PHOTOLIBRARY_USAGE_DESCRIPTION" value=""/>
 </plugin>
 <plugin name="cordova-plugin-file" spec="~6.0.1"/>
 <plugin name="cordova-plugin-geolocation" spec="~4.0.1"/>
 <plugin name="cordova.plugins.diagnostic" spec="~4.0.10"/>
 <plugin name="cordova-plugin-document-scanner" spec="2.0.1"/>
 <plugin name="phonegap-plugin-barcodescanner" spec="8.0.1"/>
 <plugin name="cordova-plugin-media-capture" spec="3.0.2"/>
 <plugin name="cordova-plugin-fingerprint-aio" spec="1.6.0"/>
 <plugin name="cordova-plugin-neutts" spec="1.0.0"/>
 <!-- <plugin name="cordova-plugin-mobile-ocr" spec="1.0.0" /> -->
 <plugin name="cordova-plugin-shake" spec="0.6.0"/>
 <plugin name="cordova-plugin-uniquedeviceid" spec="1.3.2"/>
</widget>

- In package.json file, add all the custom dependencies from the old app to the new app.
