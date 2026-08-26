# Default application dependencies

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/manage-app-dependencies>

Application dependencies are the libraries other than your project code that are required to create and run your application. Why are they important? There could be a variety of reasons. These reasons can include avoiding the pitfalls of poor application performance, reducing maintenance of an old version, etc.

### Default application dependencies

By default, when you create an application on Neutrinos Studio, a few dependencies are added to dependencies and devDependencies objects of the <application>/app/package.json file.

- The dependencies listed in the dependencies object are those that your project needs to be able to work in production.
- The dependencies listed in the devDependencies object are those that your project needs during development.

For each dependency, the package name and version is listed in the package.json file. When you initialize your app, Neutrinos Studio will download the dependencies that are listed in package.json that meet the semantic version requirements listed for each.

The default dependencies include:

```json
"dependencies": {        "@angular/animations": "10.2.4",        "@angular/cdk": "10.2.7",        "@angular/common": "10.2.4",        "@angular/compiler": "10.2.4",        "@angular/core": "10.2.4",        "@angular/flex-layout": "10.0.0-beta.32",        "@angular/forms": "10.2.4",        "@angular/material": "10.2.7",        "@angular/platform-browser": "10.2.4",        "@angular/platform-browser-dynamic": "10.2.4",        "@angular/router": "10.2.4",        "@swimlane/ngx-charts": "16.0.0",        "android-versions": "1.5.0",        "chart.js": "2.9.4",        "core-js": "3.8.1",        "d3": "6.3.1",        "firebase": "8.2.1",        "hammerjs": "2.0.8",        "localforage": "1.9.0",        "neutrinos-module": "0.0.60-beta.1",        "neutrinos-oauth-client": "1.2.4-beta.0",        "ng2-charts": "2.4.0",        "rxjs": "6.6.3",        "signature_pad": "3.0.0-beta.4",        "tslib": "2.0.0",        "zone.js": "0.11.3"    },    "devDependencies": {        "@angular-devkit/build-angular": "0.1002.1",        "@angular/cli": "10.2.1",        "@angular/compiler-cli": "10.2.4",        "@angular/language-service": "10.2.4",        "@types/jasmine": "3.5.0",        "@types/jasminewd2": "2.0.3",        "@types/node": "12.12.42",        "codelyzer": "5.1.2",        "jasmine-core": "3.5.0",        "jasmine-spec-reporter": "5.0.0",        "karma": "5.0.0",        "karma-chrome-launcher": "3.1.0",        "karma-cli": "2.0.0",        "karma-jasmine": "4.0.0",        "karma-jasmine-html-reporter": "1.5.0",        "karma-coverage-istanbul-reporter": "3.0.2",        "protractor": "7.0.0",        "sw-precache": "5.2.1",        "ts-node": "8.3.0",        "tslint": "6.1.0",        "typescript": "4.0.5",        "gulp": "4.0.2",        "gulp-cordova-create": "2.0.1",        "gulp-cordova-version": "0.3.0"    }
```

Angular dependencies are added to an app as Angular is a platform and framework for building applications.

npm dependencies are added for?

### Add a custom dependency

You can add custom dependencies of type npm and Angular to your application using the Plugin Manager on the Studio Application page. A custom dependency is added to serve a dedicated purpose in the application. For example, you can add a npm jquery dependency to

Perform the following steps:

1. Navigate to the Neutrinos Studio[Application page](/articles/concepts-publication/studio-application-page).
2. Click** Plugins **on the Action menu or press **Ctrl+Shift+P** to open the Plugins Manager.
3. Click the **Add Dependency** tab.
4. Select the type of dependency.
5. If you choose npm, enter a valid npm package name and the associated version. Click **Add Dependency**.
6. If you choose Angular, enter a valid Angular package name, version, and the Angular library to be added, and click the **+** icon.

### Manage custom dependencies

To edit or delete custom app dependencies added to your application, perform the following steps:

1. Click the** Custom Dependency** tab.
2. To edit a dependency, select the dependency. You will be navigated to the **Add Dependency **tab where you can make changes to the dependency.
3. To remove the dependency, select the dependency, and click **Remove Dependencies**.

![](/resources/Storage/app-builder-s-user-guide/1-4-import-from-neutrinos-store-img0006.png)

See

---

| **Learn More:** |
| --- |
| [Handle mismatch in app dependencies](/smart/project-how-to-articles/handle-mismatch-in-dependencies) |
