# Date: 23 July 2020

<https://documentation.neutrinos.com/articles/#!change-log/release-7-2-2>

### Date: 23 July 2020

**Release: 7.2.2**

### Enhancements:

- From this release, you can enable multi-tenant authentication option in Azure AD.
- Moved the **Add** Button for **Pages**, **Models**, **Legacy services **editors on top of their list.
- Creating a Page, Model, or a Legacy Service automatically opens the respective editors.
- Page List is alphabetically ordered.

### Bug Fixes

Monaco editor resizing issue.

Any service with a node (which has “Function Name“ field) that has the same name as that of a node (which also has “Function Name“ field) in a service that is alphabetically last will be shown as invalid.

The search results show an empty list if two or more words are added on the nodes palette on the services designer.

Upgrade studio icon instead of migrate app icon is shown if the app studio version is greater than the installed studio version.

An empty array for a child route is being saved in routes.json file after deleting the child route in the Routes editor.

Saving only middleware services does not generate the middleware sequence.

**~/.neutrinos/marketplace-components** does not always have compatible **@jatahworx/bhive-toolkits** package installed. After restoring the project when the migration fails, git history is erased because the **.git** folder is not recovered. For every environment in the app, the corresponding script is generated to run the server in both production and live view.The **Name** field of the **Session Node** is missing.The **S****ave** button is not disabled even if the form is invalid in the properties window of the **Async** node. Not able to save the **DBConfig** properties window because the **Save** button is disabled even if the properties window is valid.The **Save** button disabled even if all the required fields are filled in the **ADConfig** properties window. The **Save** button is enabled even if the user prefix is not entered in the properties window of the **ADConfig** node. The autocomplete **Group Options** is not working. The **panelClass** attribute of the **Select** component should suggest class names of the stylesheet. The **panelClass** attribute of the **Datepicker** component should suggest class names of the stylesheet.  Setting **Layout Direction **property value as **none** in Row and Column components does not work. Missing options like **space-around**, **space-between**, and **baseline** added to the **Perpendicular Direction **property of the Row and Column components.  Cannot bind a component class property to **Required** attribute in various **Form Control** components. Include **[****formControl]** attribute for **Datepicker** component because adding it goes to the wrong tag.

### Known Issue

- In mac machine, the plugin downloaded from the store does not get installed if the Neutrinos studio is not open

Dependencies UpgradeUpgraded dependencies related to typescript in the server app.typescript: 3.8.3@types/jsonwebtoken: 8.5.0
