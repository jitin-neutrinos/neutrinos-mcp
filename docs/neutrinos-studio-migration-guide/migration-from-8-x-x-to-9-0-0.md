# Migration Steps

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-from-8-x-x-to-9-0-0>

### Migration Steps

Make sure you [Migrate the App](/articles/neutrinos-studio-migration-guide/migrate-your-application) to Studio version **9.0.0** and perform the following steps:

### Components

- Signature Widget
  - `signature_pad` dependency is Upgraded to `**4.0.7**`.
  - `[onBegin]` and `[onEnd]` properties are removed from the widget and `signature_pad` package.
  - Use `(beginStroke)` in place of `[onBegin].` <!-- BEFORE --><n-signature [onBegin]="functionName"></n-signature><!-- AFTER --><n-signature (beginStroke)="functionName($event)"></n-signature>
  - Use `(endStroke)` in place of `[onEnd]`. <!-- BEFORE --><n-signature [onEnd]="functionName2"></n-signature><!-- AFTER --><n-signature (endStroke)="functionName2($event)"></n-signature>
  - Added the following new events:-
    - `(beginStroke)` - Triggered before stroke begins.
    - `(endStroke)` - Triggered after stroke ends.
    - `(beforeUpdateStroke)` - Triggered before stroke update.
    - `(afterUpdateStroke)` - Triggered after stroke update.

### CORDOVA

- Cordova **11** support and Upgraded platforms engines to the latest versions.  Note: Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature.
  - Latest version of the platform engine for `**Android**` is `**10.1.2**`.
  - Latest version of the platform engine for `**iOS**` is `**6.2.0**`.
  - Follow the below steps to migrate the Cordova project:-
    1. Cordova 11 support Install Cordova 11
      - To uninstall the previous version of Cordova, use the following command in the terminal: `npm uninstall -g cordova`
      - To install Cordova 11, use the following command in the terminal: `npm install -g cordova@11.x.x`
    2. Clean and reset the project, unless you have never done `**Initialize** **Android**` or `**Initialize iOS**`. Even if another member in your team has done this step and you pulled his changes, you still have to follow these steps. This step accommodates for the new plugins added and the change to the beforeBuild.js script. There are two ways to do this. Do either one of the following steps. The first one might be easier but the second method is less prone to project corruptions.  (**OR**)  Note:
      - Delete `**node_modules**` folder, `**platforms**` folder, `**plugins**` folder and `**package-lock.json**`. Also remove any lines mentioning cordova plugins in the `**devDependencies**` and `**dependencies**` section of package.json. This last step is important as package.json has higher priority than config.xml when it comes to plugin and platform versions. After all this do `**initialize**` & `**mobile initialize**` again from Neutrinos Studio.
      - Delete `**platforms**` folder then run the following cli commands. After successfully running the below, make sure to remove any caret symbols added by cordova to these added plugins from both config.xml and package.json. This step is extremely important to prevent accidental version updates from breaking your entire app.
      - In Neutrinos Studio 9.0.0, cordova plugin cordova-plugin-uniquedeviceid is now replaced with cordova-plugin-uniquedeviceid-waymondo with version 1.3.3.
      - Update platforms using the following commands:
        1. Android Platform `cordova platform rm android && cordova platform add android@10.1.2`
        2. iOS Platform `cordova platform rm ios && cordova platform add ios@6.2.0`
- Upgraded the following Cordova plugins -
  1. `**cordova-plugin-device@2.1.0**`
  2. `**cordova-plugin-x-toast@2.7.3**`
  3. `**cordova-plugin-inappbrowser@5.0.0**`
  4. `**cordova-plugin-splashscreen@6.0.1**`
  5. `**cordova-plugin-camera@6.0.0**`
  6. `**cordova-plugin-file@7.0.0**`
  7. `**cordova-plugin-geolocation@4.1.0**`
  8. `**cordova.plugins.diagnostic@6.1.1**`
- Upgraded the commented Cordova plugins -

1. `**cordova-plugin-document-scanner@4.2.7**`
2. `**cordova-plugin-media-capture@4.0.0**`
3. `**cordova-plugin-fingerprint-aio@5.0.1**`
4. `**cordova-plugin-mobile-ocr@3.1.2**`

- Deprecated Plugins with replacement -
  1. `phonegap-plugin-barcodescanner` is deprecated so it is replaced with plugin `cordova-plugin-qr-barcode-scanner@4.2.7`
  2. `phonegap-plugin-push` is deprecated so now it is replaced with plugin `cordova-plugin-firebasex@14.2.1`

1. `cordova-plugin-whitelist` is deprecated. With the Allow List functionality now integrated into the core of Cordova Android (10.x and greater), this plugin is no longer required.

If you have used the above plugins in your project, you have to remove and add the latest versions. To do so, use the following commands:

- To remove a plugin, use: `cordova plugin rm <plugin_name>`
- To add a plugin, use: `cordova plugin add <plugin_name>@<version>`
- To check if all the plugins are installed use: `cordova plugins`

### Files that may effect during migration:

- .gitignore
- app/.npmrc
- server/.npmrc
- config.xml
- localesService.ts
- beforeBuilds.js
- main.ts
- style.scss
- import-module.ts
- n-localeResources.service.ts
- sd-page-common.service.ts
- firebaseInitForSericeWorker.ts
- initChartJS.ts
- index.ts
- CSVService.ts
- MongoPersistance.ts
