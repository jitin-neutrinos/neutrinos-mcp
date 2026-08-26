# 8.1.0

<https://documentation.neutrinos.com/articles/#!change-log/release-8-0-1>

### 8.1.0

**Date: (12/03/2021)**

### Features

- [Locales Groups](/smart/project-sample-how-to-guide/apply-internationalization) feature is been introduced to internationalize the app UI which enables the users to,

1. Copy a locales key path by using the copy path icon.
2. Add multiple keys together to create a locales group and populate multiple values into one key.
3. Delete the locales group and delete any specific key from a locales group.
4. Interpolate the group key that consists of multiple keys with a component or bind them in a page flow to render a multilingual UI.

### Enhancements

- Added ability to toggle full screen view for the code editor in the `Script' node's attribute window.
- Upgraded angular and electron dependency of Studio to 12 and 13 respectively.
- server/src/utils/ndefault-session/Session/SessionStore.ts is migrated to the latest version.
- Stepper global option is added at component level.
- A tree view of the list of users is added in the start node's attributes window.
- Added ability to navigate to the user of a start node (link Call Service, Async nodes) from the start node and vice versa.
- New nodes under `Navigation' section for page's Flow editor to get the navigation data of that page such as route query parameters, path parameters, route data etc.
- Shortcut key Ctrl+0 is added to switch between the UI and the Flow editors of an active page.
- Removed fxHide property from default list of properties for Row and Column components in UI Editor for pages.
- Upgraded the generated UI app's Angular and Cordova dependencies to 12.x and 10 respectively.
- Export/Import feature is added to the pages' flow editor. This enables the users to import a flow and export the JSON file other applications.
- Added [ngZone](/smart/project-service-designer-user-s-guide/zone-node)node for executing tasks outside or inside the angular zone. For example, use Operation Type: Run Outside Angular to run the task outside the angular zone.
- Added ability to navigate to the view's page from a page in which the view is being used.

### Bug Fixes

- When changes are made to any page or service when explorer is in search mode stops showing the dirty indicator on that tree item.
- On MAC, plugins are not getting downloaded from the store when no instance of studio is open.
- **SSD/CSD** Multiple import dialogs were being opened when the shortcut key for import is used.
- **Dark Mode **- We have resolved the following bugs when the studio is run in the Dark Mode:

1. snack bar color should be in dark.
2. Manage plugin window font color should be consistent.
3. Menu options for services and Settings from the menu pane should have border (UI).

- Unable to import an exported middleware flow when the client editor is open.
- Call server API node - Call server node attribute window is breaking.
- Button CSS issue on flowpicker window.
- Event binding set in custom property is throwing error for html component.
- Not able to add class if the class attribute window autocomplete drop-down is in display in UI editor's component attribute window.
- Fixed an issue where the user was not being able to create a page with the same name as a deleted page.
- **CSD/SSD -** Close application window without save crashes after removing switch node with the added conditions.
- Toggle button for page editor's palette gets disabled when switched from other editors like Routes.
- **Callservice / Async node **- Changing the client service name is not updating its import path where it is being used.
- Script discards old changes after switching between different components.
- Fixed an issue where the explorer tree item name was sometimes showing as 'undefined'.
- Changes are not being detected if the services are saved and the attribute window values are edited.
- **Node SDK** - Fixed an issue where typedInput's "nullable" option was not working correctly .
- Compilation errors are displayed when service with the name log is created.
- Config XML editor disappears after switching from another editor.
- Even bind-able properties were showing multiple times in come scenarios when switching between flow picker and text UI in page's component attribute window.
- Fixed an issue where the import path for the flow being used was not updating when a call service is copied/moved from one page to another page at different levels in explorer hierarchy.

- Documentation link of Proxy setting is missing in Http request node.
- Fixed an issue where the import path for the flow being used was not updating when a call service is copied/moved from one page to another page at different levels in explorer hierarchy.
- **CallService **- Calling a page start node and mapping output generates wrong code and breaks the end app.
- Docs link for on-online and on-offline are incorrect.
- Doc link for Views is incorrect.
- **Soap Node** - The WSDLUrl property throws error while live view if the value for the server env option is empty.
- UI issue on switch node after adding three conditions.
- Call service node not getting refreshed when changes made to the used start flow.
- Add select options value field should not be mandatory for the **Select** component.
- **HTTP Request** - env type option for the Node attributes.
- **Table flow generation** - We have resolved the following bugs in the Table flow generation:

1. Data source should be assigned onInit.
2. **Paginator** and **Sort** is not working.

- displayDefaultIndicatorType is not added to the global options for stepper component.
- Doughnut chart's label field is prefilled with value "100".
- Generating the flow for the paginator component adds the flowpicker for the (page) property.

- [Node][Cron] **bh.local** is not available for Cron node.
- Not able to migrate **api** and **ui** only app.
- Any app created between 7.1.0 and 7.5.0 cannot be migrated to the 8.0.1 version.
- **SwitchNode** - Loose equality operators were not working.
- Getting error when trying to display the SSD app in **Live View**.
- **Locales** - cannot access locales keys using page.locales.keys.<key_name> if trying to access them in OnInit node.
- npm run tsc throws error for IDS flows.
- Imports are getting removed randomly for the generated page.component.ts.
