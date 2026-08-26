# Migration Steps

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-from-7-x-x-to-7-6-0>

### Migration Steps

Make sure you [Migrate the App](/articles/neutrinos-studio-migration-guide/migrate-your-application) to Studio version 7.6.0 and perform the following steps:

**Install Cordova 10**

To uninstall the previous version of Cordova, use the following command:

```markdown
npm uninstall -g cordova
```

To install Cordova 10, use:

```markdown
npm install -g cordova@10.x.x
```

---

**Update Platforms**

If you have initialized an application for mobile whether be it android or Ios, you have to remove the platform and add the latest platforms.

To remove an Ios platform from a project, use:

```markdown
cordova platform rm ios
```

To add the latest ios platform, use:

```markdown
cordova platform add ios@6.1.1
```

To remove the android platform from a project, use:

```markdown
cordova platform rm android
```

To add the latest android platform, use:

```markdown
cordova platform add android@9.0.0
```

---

** Update Plugins**

The following are the plugins that are updated to the latest version:

| **Plugin name** | **Latest version** |
| --- | --- |
| cordova-plugin-inappbrowser | 4.0.0 |
| cordova plugin-splashscreen | 6.0.0 |

If you have used the above plugins in your project, you have to remove and add the latest versions. To do so, use the following commands:

To remove a plugin, use:

```markdown
cordova plugin rm <plugin_name>
```

To add a plugin, use:

```markdown
cordova plugin add <plugin_name>@<version>
```

---

**Added Plugins**

The following plugins were added and supported from Neutrinos Studio Release 7.6.0:

| **Plugin name** | **Version** |
| --- | --- |
| @ahovakimyan/cordova-plugin-wkwebviewxhrfix | 1.0.0 |
| cordova-plugin-neucookies | 1.0.0 |

Once you reinitialize your application, confirm that the above plugins are added. If not, you should add the plugins manually using the following commands.

To add **@ahovakimyan/cordova-plugin-wkwebviewxhrfix** plugin, use:

```markdown
cordova plugin add @ahovakimyan/cordova-plugin-wkwebviewxhrfix@1.0.0
```

To add **cordova-plugin-neucookies** plugin, use:

```markdown
cordova plugin add cordova-plugin-neucookies@1.0.0
```

---

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | To check if all the plugins are installed, use cordova plugins command and make sure that the correct versions of the plugins are installed. |
| --- | --- |
