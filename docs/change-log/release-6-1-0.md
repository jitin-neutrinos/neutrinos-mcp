# 6.1.0

<https://documentation.neutrinos.com/articles/#!change-log/release-6-1-0>

## 6.1.0

#### Date: (2019-08-26)

#### Required Upgrades

#### The following upgrades are required to support Neutrinos Studio version 6.1.0:

- The **Angular **version has to be updated from 7.2.3 to 8.2.0.
- The **node.js** version has to be updated to versions between 10.9.x and 12.x.x.
- The Angular material** Flex layout** has to be upgraded from version 7.0.0-beta.19 to 8.0.0-beta.26.

If you face any breaking changes after upgrading to the latest version, follow the workarounds and migration steps mentioned in the [Migration Guide](/articles/neutrinos-studio-migration-guide/migration-steps-from-6-0-0-to-6-0-4).

#### Features

A **Value** property is added to the **Button Toggle Group** component to reverse map/bind values.Removed rxjs-compat and updated rxjs to version 6.x.x. See [Migrate from 6.0.0 to 6.1.0](/smart/project-migration-guide/migration-steps-from-6-0-0-to-6-0-4) for more information.The following files in the app are now replaced with the respective ones in the default generated app:package.jsonn-dataSorce.service.tsn-localeResources.service.tsn-map.component.ts,polyfills.tsimport-modules.tsThe Gulp task is created to create a **www **directory (if it does not exist) before Cordova prepare.In the Table component, an index variable is provided to columns.

**Bug Fixes**

The **Delete **and **Minimize** buttons are not hidden on copy-paste.The workspace title is updated after a UI service is renamed.After deleting a page, a pop-up warning message is displayed in the **Routes** editor indicating that the page does not exist.In the Plugins Manager:the template list is refreshed to show the downloaded template after adding a template from the Neutrinos Store.the search filter is cleared after a search is performed on the templates list.If you do not select a template and click the **Remove **button, a snack bar message is displayed.The **About Neutrinos **link is updated to [http://neutrinos.co](http://neutrinos.co).The copy-paste feature will not create a component with the same ID.The clear search for the palette list is working.cyclic dependency on a view will throw an error message.In UI services, the **Switch** node's else condition is working.If you are doing a mobile build of your app, Neutrinos automatically creates the **www** folder in your directory.

**Known Issues**MediaObserver.asObservable() emits 2 events each time the media changes. See [https://github.com/angular/flex-layout/issues/1041](https://github.com/angular/flex-layout/issues/1041) for more details.
MediaObserver.asObservable()emits wrong events on breakpoints. See [https://github.com/angular/flex-layout/issues/1059](https://github.com/angular/flex-layout/issues/1059) for more details.
Changes are not applied on window resize. That is, on resizing the window, directives such as- fxLayout.lt-md, ngStyle.gt-xs, fxFlexOrder, etc. are not applied. See [https://github.com/angular/flex-layout/issues/947](https://github.com/angular/flex-layout/issues/947) to learn more.
Custom dependencies added using the Neutrinos Studio cannot be updated.**Workaround: **Delete the custom dependency from the Plugins Manager and add it again. See [Import Dependencies from Neutrinos Store](/smart/project-app-builder-guide-for-release-6/copying-existing-templates-widgets-and-more) for more information.![Delete custom dependency](/resources/Storage/change-log/del_custom.png)
