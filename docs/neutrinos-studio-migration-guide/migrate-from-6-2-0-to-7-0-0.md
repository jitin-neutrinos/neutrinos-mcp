# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-from-6-2-0-to-7-0-0>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

Perform these steps if you are migrating your app from Neutrinos Studio 6.2 to 7.0

If you are migrating your app from previous releases of Neutrinos Studio, perform the migration steps mentioned in the below topics (based on the version from which you are upgrading) before you proceed with this topic.

- [Migrate from 6.1 to 6.2](/articles/neutrinos-studio-migration-guide/migrate-from-6-1-0-to-6-2-0)
- [Migrate from 6.0 to 6.1](/articles/neutrinos-studio-migration-guide/migration-steps-from-6-0-0-to-6-0-4)
- [Migrate from 5.x to 6.0.0](/articles/neutrinos-studio-migration-guide/migrate-from-5)
- [Migrate to 4.0.2](/articles/neutrinos-studio-migration-guide/migrate-to-402)
- [Migrate to 3.3.1](/articles/neutrinos-studio-migration-guide/migrate-to-3)

For example, If you are migrating your app from Neutrinos Studio version 6.1 to version 7.0, perform migration steps mentioned in [migrate from 6.1 to 6.2](/articles/neutrinos-studio-migration-guide/migrate-from-6-1-0-to-6-2-0) and then perform the steps mentioned below.

---

### Migration Steps

#### Installing Cordova 9

To install and use Cordova 9 to build your mobile app, see the [Cordova documentation for Release 9](https://cordova.apache.org/announcements/2019/03/22/cordova-cli-release-9.0.0.html). As part of this installation, note that you should remove any 3rd party plugins

 which are failing with the requireCordovaModule error, and update them

 to the versions which work with Cordova 9.

To remove a Cordova plugin, use:

Copy CodeMarkdowncordova plugin rm <plugin-name>

To add a Cordova plugin, use:

Copy CodeMarkdowncordova plugin add <plugin-name>

#### Support for Cordova 9 on Neutrinos Studio

If you have an existing mobile app that you are building on Neutrinos Studio, and want to use Cordova 9 to build the app. Follow the step below

**Step 1**: You should clean and reset the project. This is required to accommodate the new plugins added and the changes made to the beforeBuild.js script.

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | These steps are to be performed if you or your team have initialized the mobile app by running the **Cordova Prepare** command using the CLI or the **Initialize Mobile** task using the Neutrinos Studio Task drop-down list. |
| --- | --- |

There are 2 ways to clean and reset your project.

**Option 1:**

- Delete the following from your application's folder. Your application files are stored under your application name in your Studio workspace.
  - **platforms **folder
  - **node_modules** folder
  - **plugins** folder
  - **package-lock.json** file
- Remove any lines mentioning about the Cordova plugins in the devDependencies and dependencies section of the **package.json** file. This is an important step as the **package.json** file has a higher priority than the **config.xml** file for plugin and platform versions.
    ![Package.json file](/resources/Storage/neutrinos-studio-migration-guide/package_json.png)
- Run the** Initialize** task from the Task drop-down list.
    ![Initialize task](/resources/Storage/neutrinos-studio-migration-guide/initialize.png)
- Run the **Initialize Mobile **task from the Task drop-down list.

**Option 2:**

- Delete the **platforms **sub-folder from your application's folder. You can locate the folder under your application name in your Studio workspace.
- Open a command prompt and run the following commands. Copy CodeMarkdown//Adding a Cordova plugin
   cordova plugin add com.cordova.plugins.cookiemaster@1.0.1
   //Upgrading Cordova plugins to version supportd by Cordova 9
   cordova plugin rm cordova-plugin-inappbrowser && cordova plugin add cordova-plugin-inappbrowser
   cordova plugin rm cordova-plugin-fingerprint-aio && cordova plugin add cordova-plugin-fingerprint-aio@2.0.0
   cordova plugin rm cordova-cordova-plugin-shake && cordova plugin add cordova-plugin-neushake@1.0.0

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | In the **config.xml** and **package.json** files, remove any caret symbols ( ^ ) added by Cordova to the plugins. This is an important step and should be performed to prevent accidental version updates from breaking your entire app. |
| --- | --- |
