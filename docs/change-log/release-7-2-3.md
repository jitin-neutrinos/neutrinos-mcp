# Release 7.2.3

<https://documentation.neutrinos.com/articles/#!change-log/release-7-2-3>

### Release 7.2.3

### Date: 11 October 2020

**Enhancements**

- Added default client env variable NGFORAGE_MOBILE_DRIVER which can take values `WEB_SQL`, `INDEXED_DB`, `LOCAL_STORAGE.`
- Neutrinos-module upgraded to version 0.0.59 to add the NGFORAGE_MOBILE_DRIVER environment property.
- Added a **Download File** option for the **HTTP Out** node of the Server Services Designer.
- Added search feature to search for particular **Pages**, **Services**, and **Models **in its respective lists. Search can be done by clicking the search icon or use the short cut **CTRL+F** when the list is open.
- The initial loading time of the services in the Services Designer is improved by 95%.
- Tooltip added to show the entire name of the services in the Services designer.
- Added click event property in the **Menu **component.
- The **required **field of the Form fields is set to **false **by default.
- Added validation for the package name when adding Custom Dependency in the Plugins Manager.

**Bug Fixes**

- Some nodes are not shown in list of selected nodes section of the Catch node.
- Error message not displayed when routes are invalid in the routes editor.
- The delete button not working in the Assets editor.
- The search function not working properly in the app list search.
- Creating an app with the same name as any existing app but with different casing fails and renames the existing app to the new name.
- The refresh button in the attributes window of views component tooltip is changed.
- HTML5 label issue:
  - When HTML5 is dragged and dropped, the component label still shown as HTML5 instead of the default value for the **Element type** attribute.
  - When the tag name is given manually(as opposed to selecting it from the dropdown), the given name is not updated as the component label. Instead, the label value is what was selected previously from the dropdown.
  - Tag names in the HTML component are not changed after selection.
- The routes editor does not get updated if a page that is used in any of the routes is deleted.
- Parsing of the **@Input** and **@Output** properties of the page for views is improved.
- The **headerclass **and **columnclass** properties are now autocomplete in the Table Column component to behave like a normal class property that shows suggestions for the classes defined in the styles editor.
- [Optional chaining](Tooltip added to show the entire name of the services in the Services designer.) (?.) and [nullish coalescing](Tooltip added to show the entire name of the services in the Services designer.) (??) operators throw invalid node errors.
- npm start script was not working for the server.
- Migration to update **neutrinos-oauth-client** module to version 1.2.2.
- Change IDS flow to destroy user sessions before the redirect.
- Change sameSite cookie option in GlobalSession in ids flow to lax.
- API was not getting executed using Swagger.
- Dependent npm packages are not getting installed when the component plugin is installed on the app.
- Deleted the file **manifest.json** and removed its reference from **index****.****html**.
- Fileout node with the streaming option enabled was not waiting for the file write operation to finish.
- No default config is selected for newly dragged and dropped node in the AMQP Producer node.
- Expression with spaces in the **optionValue** field generates the wrong template that breaks the app in the Select component.
- Signature widget component issues:
  - **Style **and **class **properties not getting generated in the page HTML.
  - **Mode **property options are invalid.
- Style and class attributes are not getting generated for the Error component.
- Removed the invalid attributes in the Menu component. (templateRef, direction, parentMenu and items)
- The typo of the Paginator button in the table component.
- The **buffer **option in the **Mode **attribute drop-down is removed for the progress spinner component.
- The **vertical** property of the **slider **component is not property bound.
- **hasBackDrop** property of **Sidenav ****Container **is not property bound.
- Progress spinner is not rendered with its default values.
- Cannot add appearance to the text area's mat-form-field.
- The button toggle component is invalid without a parent component.
- style and class attribute of the **Drop Column** component in the table component is not working.
- style and class attribute for the **Column **in the table component is invalid.
- Max record size attribute should be validated to accept only numbers in CSV node.
- Selected property in the Radio Group component could not be property bound.
- checked and value properties in the Radio button component could not be property bound.
- The code generation for the class property is invalid after migration in the Menu component.
- UI for the response body field breaks in some cases.
- No response is sent after converting a YML to a JSON file.
