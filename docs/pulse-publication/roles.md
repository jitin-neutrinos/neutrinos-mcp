# Purpose

<https://documentation.neutrinos.com/articles/#!pulse-publication/roles>

Roles define a set of permissions and responsibilities assigned to users. They act as an abstraction layer between users and system capabilities, enabling controlled access to platform features such as process design, execution, monitoring, and administration.

### Purpose

Roles are used to:

1. Control access to platform features and components
2. Standardize permissions across multiple users
3. Simplify user management by assigning roles instead of individual permissions
4. Enforce security policies

## Interface

The available roles on the platform are displayed in a tabular format, as shown in the illustration below:




 ![pulse-administration-roles-landing-page](/resources/Storage/pulse-publication/images/pulse-administration-roles-landing-page.png)

- **Role Name**: Displays the unique name of the role on the platform (for example, test-role).
- **Modules**: Lists the platform components the role has access to. These are displayed as tags (e.g., roles, permissions, users, groups, projects, user-tasks, processes).
- **Permissions**: Shows the total number of permissions configured for the role (e.g., 72, 8). These permissions define the actions the role can perform across modules.
- **Users**: Indicates how many users are currently assigned to the role (e.g., 4, 3).
- **Last Updated**: Displays the timestamp of the most recent modification made to the role.
- **Actions**: Provides a context menu (kebab icon) for performing operations such as editing, or deleting the role.

Use the search bar to quickly locate specific roles available on the platform. Use the Show By dropdown to control the number of rows displayed, and the navigation controls at the top of the page to move between pages.

## Add Role

This section provides a step-by-step guide to creating a new role on the platform and associating it with relevant groups or users.

1. From the left navigation panel, navigate to Administration. Within the Administration page, click the Roles tab.
    ![pulse-administration-roles-landing-page-1](/resources/Storage/pulse-publication/images/pulse-administration-roles-landing-page-1.png)
2. Click Add at the top of the page.
    ![pulse-administration-roles-add-button](/resources/Storage/pulse-publication/images/pulse-administration-roles-add-button.png)
3. The first step is to provide the basic details for the role, including the Role Name and a brief Description. After entering these details, click Next at the bottom of the page to proceed. Optionally, you can clone an existing role to use as a baseline for the new role. This helps streamline the setup process and reduces repetitive configuration efforts.
    ![pulse-administration-roles-add-new-role-basic-details](/resources/Storage/pulse-publication/images/pulse-administration-roles-add-new-role-basic-details.png)
4. On the next page, select the permissions to associate with the role. By default, no permissions are assigned unless the role is created by cloning an existing role. Permissions can be configured by enabling the toggle switch at the module level to grant all associated permissions, or by expanding a module and selecting individual permissions as needed. In the example below, the role Test is granted all permissions for the Roles, Permissions, Users, and Groups modules by enabling the module-level toggle switches. For the Process and Rules modules, only specific permissions are assigned by selecting them individually.
    ![pulse-administration-roles-add-new-set-permissions](/resources/Storage/pulse-publication/images/pulse-administration-roles-add-new-set-permissions.png)
5. The next step is to associate users with the role. Use the search bar to locate specific users, then select one or more users to assign to the role. This step is optional, and you may choose to skip adding users. After making the required selections, click Next at the bottom of the page to proceed.
    ![pulse-administration-roles-add-new-associate-users](/resources/Storage/pulse-publication/images/pulse-administration-roles-add-new-associate-users.png)
6. The final step is to associate the role with one or more projects. Once associated, the role becomes available within the selected projects. You can select a single project or multiple projects for association. The role can then be assigned to groups or users within each project. After selecting the required projects, click Next at the bottom of the page to proceed.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    **Note**: If no project is selected, the role is applied by default and made available across all projects.
    ![pulse-administration-roles-add-new-associate-projects](/resources/Storage/pulse-publication/images/pulse-administration-roles-add-new-associate-projects.png)
7. The next page displays a summary of all configured settings for the role. Review the details, and click Create Role at the bottom of the page to complete the role creation process.
    ![pulse-administration-role-add-new-group-configure-create-role](/resources/Storage/pulse-publication/images/pulse-administration-role-add-new-group-configure-create-role.png)

## Edit Role

To edit roles available on the platform, follow the steps below:

1. On the Roles page, locate the role whose details need to be edited. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Edit.
    ![pulse-administration-role-edit-role](/resources/Storage/pulse-publication/images/pulse-administration-role-edit-role.png)
2. The subsequent screens in the edit workflow follow the same sequence as the role creation process. Navigate through each step to update the required details, such as permissions, users, and projects.
    After making the necessary changes, review the updated information and click Save Changes to apply the updates.

## Delete Role

To delete a role from the platform, follow the steps below:

1. On the Roles page, locate the role to be deleted. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Delete.
    ![pulse-administration-role-delete-role](/resources/Storage/pulse-publication/images/pulse-administration-role-delete-role.png)
2. A confirmation dialog is displayed, prompting you to confirm the deletion of the role. This action is irreversible and cannot be undone. Click Yes to confirm and delete the group from the platform.
    ![pulse-administration-role-delete-group-confirm](/resources/Storage/pulse-publication/images/pulse-administration-role-delete-group-confirm.png)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | **Note**: A role cannot be deleted if it is currently associated with one or more users. |
| --- | --- |
