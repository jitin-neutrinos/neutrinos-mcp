# Purpose

<https://documentation.neutrinos.com/articles/#!pulse-publication/groups>

Groups are logical collections of users organized based on shared characteristics such as department, role, or responsibility. Groups simplify user management and enable efficient access control, task assignment, and collaboration across the platform.

### Purpose

Groups are primarily used to:

- Organize users into meaningful categories (e.g., Operations, Finance, Support)
- Simplify access control by assigning permissions at the group level instead of individually
- Enable role-based operations where users within a group perform similar tasks
- Facilitate task assignment by allowing tasks to be assigned to a group rather than specific users

## Interface

The available groups on the platform, which are used to organize users into logical categories, are displayed in a tabular format, as shown in the image below:




 ![pulse-administration-groups-landing-page](/resources/Storage/pulse-publication/images/pulse-administration-groups-landing-page.png)

- **Group Name**: Displays the name of the configured group on the platform.
- **Roles**: Shows the roles assigned to the group. Roles define the functional responsibilities or access levels of users within the group.
- **Permissions**: Indicates the number of permissions associated with the group. These permissions govern access to features, processes, or system actions.
- **Users**: Displays the number of users assigned to the group.
- **Last Updated**: Shows the timestamp of the most recent update made to the group configuration.
- **Actions**: Provides a context menu (kebab icon) for performing operations such as editing, or deleting the group.

Use the search bar to quickly locate specific groups available on the platform. You can also filter groups based on roles to view relevant results. Use the Show By dropdown to control the number of rows displayed, and the navigation controls at the top of the page to move between pages.

## Add Group

To add a group to the platform, follow the steps below:

1. From the left navigation panel, navigate to Administration. Within the Administration page, click the Groups tab.
    ![pulse-administration-groups-landing-page-1](/resources/Storage/pulse-publication/images/pulse-administration-groups-landing-page-1.png)
2. Click Add at the top of the page.
    ![pulse-administration-groups-add-new-group-add-button](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-add-button.png)
3. The first step is to provide basic details for the group, such as the group name and a description. After entering these details, click Next at the bottom of the page to proceed.
    ![pulse-administration-groups-add-new-group-basic-details](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-basic-details.png)
4. On the next page, select the roles to associate with the group. By default, when this group is selected, users assigned to the chosen roles are included in the group. This step is optional, and you can proceed without selecting any roles. Use the search bar to quickly locate specific roles. You can select one or more roles for the group. After selecting the roles, or choosing to skip this step, click Next to proceed.
    ![pulse-administration-groups-add-new-group-configure-roles](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-configure-roles.png)
5. The next step is to associate users with the group. You can use the search bar to locate specific users and select one or more users to include in the group. This step is optional, and you can choose to skip adding users. After making the required selections, click Next at the bottom of the page to proceed.
    ![pulse-administration-groups-add-new-group-configure-users](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-configure-users.png)
6. The final step is to assign permissions to the group. These permissions are applied to all users and roles associated with the group. Permissions can include Create, View, Edit, and Delete for platform modules such as roles, permissions, users, groups, rules, workflows, process instances, case definitions, case instances, user tasks, CMS, custom code, and more. To enable a set of permissions, use the toggle switch for the required module. In the illustration below, the example group is configured with all permissions enabled for rules, permissions, users, and groups using the toggle option.
    ![pulse-administration-groups-add-new-group-configure-permission-toggle](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-configure-permission-toggle.png)
    You can also customize permissions for a specific modules by expanding it and selecting the required permission set. In the illustration below, the example group is configured with only View permission for rules, and Start and View permissions for process instances.
    ![pulse-administration-groups-add-new-group-configure-permission-toggle-customise](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-configure-permission-toggle-customise.png)
7. The next page displays all the configured settings for the group. Review the configurations, and click Create Group at the bottom of the page to complete the group creation process.
    ![pulse-administration-groups-add-new-group-configure-create-group](/resources/Storage/pulse-publication/images/pulse-administration-groups-add-new-group-configure-create-group.png)

## Edit Group

To edit a group on the platform, follow the steps below:

1. On the Groups page, locate the group whose details need to be edited. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Edit.
    ![pulse-administration-groups-edit-group](/resources/Storage/pulse-publication/images/pulse-administration-groups-edit-group.png)
2. The subsequent screens in the edit workflow follow the same sequence as the group creation process. Navigate through each step to update the required details, such as roles, users, and permissions settings for task assignment.
    After making the necessary changes, review the updated information and save the settings to apply the updates.

## Delete Group

To delete a user from the platform, follow the steps below:

1. On the Groups page, locate the user to be deleted. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Delete.
    ![pulse-administration-groups-delete-group](/resources/Storage/pulse-publication/images/pulse-administration-groups-delete-group.png)
2. A confirmation dialog is displayed, prompting you to confirm the deletion of the group. This action is irreversible and cannot be undone. Click Yes to confirm and delete the group from the platform.
    ![pulse-administration-groups-delete-group-confirm](/resources/Storage/pulse-publication/images/pulse-administration-groups-delete-group-confirm.png)
