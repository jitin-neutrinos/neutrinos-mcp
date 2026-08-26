# Purpose

<https://documentation.neutrinos.com/articles/#!pulse-publication/global-variables-wf-cm>

Global Variables are project-level configuration values that can be accessed across multiple platform capabilities, including Process Management, Case Management, Business Rules, and Integrations. They provide a centralized mechanism for storing values that need to be referenced consistently throughout the platform, eliminating the need to duplicate the same configuration across modules.

Global variables are scoped to both a project and a branch. This means that a global variable is available only within the project and branch in which it is created. However, within that scope, it can be accessed by all platform modules and capabilities.

## Purpose

Global variables are intended to:

- Centralize commonly used values.
- Eliminate hardcoded values within workflows and business rules.
- Ensure consistent behavior across modules and services.
- Simplify maintenance by allowing a value to be updated in one location.
- Support environment-specific configuration without modifying application logic.

## Interface

![up-global-variables-landing-page](/resources/Storage/pulse-publication/images/up-global-variables-landing-page.png)

- **Secret**: Contains a check box that indicates whether a global variable is treated as a secret. When enabled, the value of the corresponding variable is masked to prevent the actual value from being displayed. By default, the Secret check box is disabled for all variables.
- **Name**: Displays the name of the global variable
- **Type**: Displays the data type of the global variable. Supported data types include Numeric, String, Boolean, List, and JSON.
- **Value**: Displays the current value assigned to the global variable. The value is displayed only when the Secret check box for the corresponding variable is cleared. If the Secret check box is selected, the value is masked.
- **Used In**: Displays the platform components that reference the global variable.
- **Last Updated**: Displays the date and time when the global variable was last modified. The timestamp is updated whenever the variable's name or value is changed.
- **Added By**: Displays the name of the user who created the global variable on the platform.
- **Actions**: Provides the Copy and Delete options. Use Copy to create a duplicate of the selected global variable for modification, or Delete to remove the variable from the platform.

A Search bar is available to help you quickly locate a global variable. You can also use the available filters to narrow the list based on Type, Used In, Added By, or Last Updated.




 The Show By drop-down list allows you to control the number of rows displayed in the table. Use the pagination controls to navigate between multiple pages of variables.

## Add Global Variable

To add a global variable on the platform, follow the steps below:

1. On the landing page, click the required project to open it.
2. From within the project, click the branch drop-down list next to the project name at the top of the page, and then select the required branch.
3. After selecting the required branch, click the Variables module in the main left navigation pane.
4. The Global Variable Management page opens and displays all the global variables available for the selected project and branch. The variables are presented in a tabular format.
5. Before you can add or edit global variables, click the Lock icon on the top of the page to acquire the lock. By default, the Global Variable Management page is in a locked state.
    ![up-global-variables-landing-page-lock-icon](/resources/Storage/pulse-publication/images/up-global-variables-landing-page-lock-icon.png)
6. After acquiring the lock, click Add Value at the bottom of the page to add a new global variable. In the pop-up window, select the data type for the global variable.
7. A new row is added with the selected data type. Enter a name for the global variable and specify the value to be stored. Each global variable is defined as a key-value pair, where the variable name serves as the key and the assigned value serves as the value. If required, you can change the data type by selecting a different option from the Type drop-down list in the corresponding row. **Note**: You can check the secret check box, if the value for the variable needs to be masked.
8. After entering the required details, click the Save icon at the top of the page to save the global variable.
    ![up-global-variables-landing-page-lock-add-save](/resources/Storage/pulse-publication/images/up-global-variables-landing-page-lock-add-save.png)
9. After adding the global variable, click the Lock icon to release the lock on the Global Variable page.

## Delete Global Variable

To delete a variable from the platform, follow the steps below:

1. On the landing page, click the required project to open it.
2. From within the project, click the branch drop-down list next to the project name at the top of the page, and then select the required branch.
3. After selecting the required branch, click the Variables module in the main left navigation pane.
4. Click the Lock icon on the top of the page to acquire the lock.
5. Locate the global variable that you want to delete. If necessary, use the Search bar to quickly locate the variable.
6. In the Actions column for the corresponding global variable, click the Delete icon.
   ![up-global-variables-landing-page-lock-delete-icon](/resources/Storage/pulse-publication/images/up-global-variables-landing-page-lock-delete-icon.png)
7. In the confirmation dialog box, click Delete to confirm the operation.
   ![up-global-variables-landing-page-lock-delete-confirmation](/resources/Storage/pulse-publication/images/up-global-variables-landing-page-lock-delete-confirmation.png)
