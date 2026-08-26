# Locales Group

<https://documentation.neutrinos.com/articles/#!studio-guide-8/version-8-1-0>

Here is a list of new features and enhancements introduced in Neutrinos Studio version 8.0.1:

### Locales Group

Locales group allows you to group together multiple locales keywords and bind them to the pages by either interpolating the key path in a component or binding the locales group keys with the page flow to render a multilingual UI.

See [Locales Group](/articles/studio-guide-8/apply-internationalization/a/h3__319744391) documentation to learn more.

### Enhancements

- Added ability to toggle full screen view for the code editor in the `Script' node's attribute window.
- Upgraded angular and electron dependency of Studio to 12 and 13 respectively.
- server/src/utils/ndefault-session/Session/SessionStore.ts is migrated to the latest version.
- Stepper global option is added at component level.
- A tree view of the list of users is added in the start node's attributes window.
- Added ability to navigate to the user of a start node (link Call Service, Async nodes) from the start node and vice versa.
- New nodes under `Navigation' section for page's Flow editor to get the navigation data of that page such as route query parameters, path parameters, route data etc.
- Shortcut key Ctrl+0 is added to switch between the UI and the Flow editors of an active page.
- Removed fxHide property from default list of properties for Row and Column components in UI Editor for pages .
- Upgraded the generated UI app's Angular and Cordova dependencies to 12.x and 10 respectively.
- Export/Import feature is added to the pages' flow editor. This enables the users to import a flow and export the JSON file other applications.
- Added [ngZone](/smart/project-service-designer-user-s-guide/zone-node) node for executing tasks outside or inside the angular zone. For example, use Operation Type: Run Outside Angular to run the task outside the angular zone.
- Added ability to navigate to the view's page from a page in which the view is being used.

### Bug Fixes

To learn about bug fixes, see [Release 8.1.0](/smart/project-change-log/release-8-0-1)
