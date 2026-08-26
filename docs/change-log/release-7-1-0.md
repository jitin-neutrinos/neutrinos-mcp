# 7.1.0

<https://documentation.neutrinos.com/articles/#!change-log/release-7-1-0>

### 7.1.0

**Date: (2020-03-27) **

### Features

- Added** Chips** component as an advanced component in the layout section of the palette list.
- Added** Autocomplete** is an advanced component in the layout section of the palette list.
- Added** Email out** node in the server services designer.
- Added** Async block** node for both Client Services Designer and Server Services Designer.
- Added **Child Process,** and **AMQP **nodes to Server Services Designer.
- Added **Call Server API **node to Client Services Designer.
- **Analytics**:
  - Added analytics to save the file when the page is saved for mouse click and keyboard shortcut.
  - Added template name to the app metadata file.
  - Added timestamps for creating and modifying the app metadata file.
  - Added analytics for Migration, Deletion, Import and Export as .nos files.
  - Added analytics for dev mode startAnalyticsDev:link:all to package.json. Starts studio with the flag --analytics-dev
  - Added analytics for Code optimizations that are to use appObj wherever possible and removed the studio version check.
  - Added analytics for Kafka URL, start & call intervals and captureAnalytics in settings.json.
  - Added analytics features that are custom dependency install, store dependency install, environment save, CSD & SSD save, config.xml save.
  - Added analytics features to save Styles, data model, and clone capture.
  - Added migration and logic for adding createDate timestamp to appPages.json file.
  - Created file copies in **.neutrinos** on page save along with timestamps & UserID.
  - Added migration and logic for adding analyticsId and createdStudioVersion keys to appmetadata file,that is, **<appname>.json.**
  - Added timestamps for when the app metadata file is created & modified.

### Enhancements

- Added **host** field in Postgres node.
- Added **Post Login** and **Logout UI redirect URL** parameters.
- Added **error block** to import an app.
- Added an option to add an **Instance name** for the database configuration.
- Added hide marker attribute in the **Form** component.
- Added default workspace plugins in Plugins Manager.
- Enhanced the MongoDB node in the Server Services Designer.
- Enhanced the SQL Node in the Server Services Designer.

### Bug Fixes

Proper error message displayed for the wrong DB configuration. The studio version should be tracked during login.Entering a lengthy value in class property of any components will not give a remove icon when added. Selecting true in **Group Options** in the **Select** component is not allowing to set a complex field.**Back to login** link on a mac machine is not visible.Only the typed value is saved even after the autocomplete suggested value is selected in the **Log** node of the Server Service Designer.Typo of the word **Zoom** in the service designers.Async node **Done** button disabled when the called flow is deleted and entered.
Code generation does not happen for nodes other than the **Start** node when the service name is renamed.The **Save** button is disabled even after all the fields are given a value in the **XML** node.The npm run tsc command fails because of the wrong type definition.
Codegen fails for code with parameterized string.
Splash screen on mobile is supposed to be a Neutrinos screen.All selected flow in the Flows to be called get empty in the async node if any of the flow is deleted.Async node inserts empty inputs with the delete button.
