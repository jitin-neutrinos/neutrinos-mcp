# Features

<https://documentation.neutrinos.com/articles/#!change-log/release-7-9-0>

### Features

- New icons are provided on Client Services Designer and Server Services Designer to [Export and Import](/smart/project-sample-how-to-guide/import-and-export-services) respective services.

### Enhancements

- The search functionality of the [HTML 5 component](/smart/project-components-documentation-copy/html) is enhanced.
- (imageDataChange) and (imageDataUrl) properties are added to the Signature widget.
- The Use Query String property is added to the **HTTP Request** node on Server Services Designer.

### Bug Fixes

- Cannot open studio on mac due to the npm version mismatch issue.
- Can save a key without value in the locales editor.
- SVG-type images are not being previewed in the assets editor.
- Drag and not dropping a component into the Wysiwyg editor stops showing all the component top-right icons.
- The watch value should be boolean in the Process Manager2 settings.
- All the string literals are not replaced by constants.
- Node name using the Edit Label feature will show string in quotes.
- Collapsing a Card greater than a content child component messes up the UI of the page.
- The .bh objects are shown in the wrong place while editing the node's properties window.
- Blank apps list throws an error.
- Import and Export flows:
  - Cannot export a flow with HTTP request node.
  - Importing middlewares to a new service is creating a blank service.
  - Should throw an error when random value is added in the import.
  - Cannot import a flow with plugin builder node.
  - Change detection on service is not reflected if changes are made after importing flows.
  - Imported middleware flows are not rendered in the middleware's service.
  - The node should show invalid if any invalid property is in the node after importing.
- Locales editor - A typo in the Snack bar.
- Error while live viewing due to the wrong type in **initChartJS.ts** file.
- Comment behavior on child components differs on reopening the page.
- Session node name display should be proper.
- The **[collection name]** and** [imageFilter]** attributes should be deleted from the **Image** component.

### Known Issue

After upgrading Neutrinos Studio to the latest version, if you try to install a node from Neutrinos Store, you encounter an error stating that you are running an old version of Neutrinos Studio. This is because the marketplaceUrl property is not updated to the latest version. **Workaround:**Open the /.neutrinos/settings.json file in your local machine.Update the studio version in the marketplaceUrl property to the installed version of Neutrinos Studio -  https://store.neutrinos.co/api/**<INSTALLED_VERSION_OF_STUDIO>** . For example, for the studio version 7.9.0, the URL would be **https://store.neutrinos.co/api/7.9.0**. Save the file and restart **Neutrinos Studio**.For all the 7.X versions of Neutrinos Studio, if you have **node js** version 14 and above installed in your machine and you have used the **Postgres SQL** database in your app, the database connection will not be established. **Workaround:**Navigate to the **package.json** file inside the **Server** folder of your app.Update the **pg**** version** to 8.7.1 in the **dependencies** section of the **package.json** file.Run the **I****ntialize** task again from the Studio
