# Enable Navigation Guard

<https://documentation.neutrinos.com/articles/#!alpha-platform/app-config>

The App Config feature allows developers to alert workbench users from navigating between pages without saving changes and enables administrators to assign owned tasks to other users using the 'Enable Navigation Guard' and 'Add User Groups' features, respectively.

## Enable Navigation Guard

When a workbench user attempts to navigate to another page without saving their changes, you can alert them about the unsaved changes. Enable the toggle to activate the Navigation Guard, which displays an alert message if the user tries to leave a page without saving. By default, this feature is disabled, that is no alert message is shown. To enable the navigation guard, follow the steps below:

1. Click the **Config **editor > Navigate to **App Config**.
2. Enable the toggle button next to Enable Navigation Guard.
3. Click the **Save** button.

The GIF below illustrates an alert message shown to a workbench user when the Enable Navigation Guard toggle is enabled:

![enable-navigation-guard](/resources/Storage/alpha-platform/images/workflow-studio-config-enable-navigation-guard.gif)

## Add User Groups

When an Alpha Admin reassigns owned tasks (tasks already assigned to a user), you can restrict the list of users available for reassignment. A developer can define specific user groups to which an admin can assign tasks by selecting them through the 'Add User Groups' option. To restrict the list of users available for reassignment, follow these steps:

1. Click the **Config** editor > Navigate to **App Config**.
2. From the **dropdown checklist**, select the user groups that the admin should see while reassigning tasks.
3. Click the **Save** button.

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | If no user groups are specified, or if Default group is selected, all users are visible for reassignment. |
| --- | --- |

The GIF below demonstrates how to assign users from the 'Medium' group for an admin to reassign owned tasks:

![add-user-group](/resources/Storage/alpha-platform/images/workflow-studio-config-app-config-add-user-group.gif)

The image below displays the admin UI with a list of users who belong exclusively to the 'Medium' group when reassigning tasks:

![admin-add-user-group](/resources/Storage/alpha-platform/images/workflow-studio-config-admin-add-user-group.png)
