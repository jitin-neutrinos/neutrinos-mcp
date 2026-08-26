# 7.2.0

<https://documentation.neutrinos.com/articles/#!change-log/release-7-2-0>

### 7.2.0

Date: 5th June 2020

### Features

Added option to **Upload folder** in the **Assets Editor** of Neutrinos Studio.

Added a preview field to Preview selected images in the **Create/Edit App** window while creating an app.

By default, open the last used app when you close and relaunch the Neutrinos Studio from the same app.

- Placed the Task Play button towards the right side of the task drop-down.
- All the apps created in Studio version 7.2.0 will be angular 9 apps. For every app created before 7.2.0, auto migration will upgrade the app to angular 9.

### Bug Fixes

Verify the resize of the attributes window after clicking the run task button.

Any editor Routes, Pages, etc. should only make a save call (file writes) when there are actual changes in the model.

Wrong error message in the Enter service name field if added you add a special character.

**Select language** in the Locales editor UI fix.

Custom Angular dependencies not added to the dependencies.module.ts file

If Dynamic Tab property set to true in tab component the **tabDataSource** and **tabLabels** properties are not displayed.

Lable field for the views in pages is not appearing.

Entering the duplicate value in the class of the attribute window of the page editor.

Middleware connection UI issue. In the middlewares workspace, the connection wire between the nodes is appearing.In the **Locales** editor of the Neutrinos Studio, when you select and deselect a language the Add button is not disabled.The attributes window of any node in the Server Services designer does not resize if the terminal window is open. **Add** and** Remove** dependencies should be disabled if none of the plugins are selected from the list in the plugins manager.Adding a plugin to the app with version 7.0.2 in 7.1.0 works and installs a plugin of version 7.0.2.
