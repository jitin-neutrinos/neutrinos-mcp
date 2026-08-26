# Features:

<https://documentation.neutrinos.com/articles/#!change-log/release-9-00>

**9.0.0**

**Date: 2022-15-11**

### Features:

- Angular version upgraded to **13.x.x**
- Nodejs version upgraded to **16.x.x**
- User can access the added languages in the locales through `page.locales.languages`.
- User can add new locale entry to an already existing group.
- User cannot add duplicate key at the root level as well as with in the group.
- Migration for ConfigNodes (sql node) pool options.
- Dependencies upgraded.
- Updated **mongodb** version to **4.8.0** and **removeOne** and **removeMany** operations changed to **deleteOne** and **deleteMany**.
- Updated `.gitignore` to exclude `.angular/cache.`
- `bodyParser` is deprecated, and replaced with `express.json()` in `src/index.ts`.
- `url.parse` is deprecated, and replaced with `new url.URL()` in `src/index.ts`.
- Cordova 11 support and Upgraded platforms engines to the latest versions.
- Upgraded the Cordova plugins.
- Upgraded all the commented Cordova plugins.
- Option added to navigate to the start node from Async node’s attribute window.
- User can now add the multiple same flow calls in Async node’s attribute window.
- For `Signature Widget` component, added new events `(beginStroke)`, `(endStroke)`,`(beforeUpdateStroke)` and `(afterUpdateStroke)`, and removed `[onBegin]` and `[onEnd]` properties.

**Bug Fixes:**

- Title or name of Custom Dependency should not be editable.
- Imported SSD service should be draggable.
- Removing a custom dependency is not updating the Custom dependency list in plugin manager.
- Clearing off the value in the locales group and cannot add new value for the Key.
- Editing and saving import module chip adds a new chip instead of updating the same Custom Dependency.
- Editing already added entry value adds a new entry at the root in the design and the generated language.json files.
- Added `disableTooltipInteractivity:true` option to `tooltipDefaultOptions` so that it disables the ability for the user to interact with the tooltip element.
- Imports and functions removing after client service rename.
- Plugin Installation fails and removes the node packages from the studio.
- Studio launch from **8.3.0** to **9.0.0** fails.
- Throws error when uploading a file in a config node's "File Upload" field type.
- On store dependency not deleted from package.json on removing of that dependency.
- Editing and saving an already added dependency causes it to be removed from `dependencies` object in package.json
- Pie chart and line chart is not displaying in the end app.
- The non-english locales.json properties are saved as array of values.
- App card is removed even though delete fails.
- Added `trustServerCertificate: true` property in MSSQL Configuration.
- DDL is not getting generated when any of the ancestor directories have space(s) in their name.
- Added migration for server side `.npmrc` only from **8.3.0** to **9.0.0**.
- [Cordova][android] IDS login is not working, so added `AndroidInsecureFileModeEnabled` flag to `config.xml`. for Cordova-Android.
