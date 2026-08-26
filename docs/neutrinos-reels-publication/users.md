# Interface

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/users>

Users are individuals who interact with the platform to perform tasks, initiate processes, and access system features. Each user account is uniquely identified and associated with attributes such as username, contact information, and authentication credentials.

Users are assigned roles and may also be grouped into organizational units (groups) to define their access levels and responsibilities. Based on these associations, users are granted permissions to perform actions such as viewing, creating, approving, or managing process-related activities.

This model ensures controlled and secure access to system functionality, with each user operating within defined access boundaries.

## Interface

![pulse-administration-user-page](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-user-page1.png)

Details of all users on the platform are presented in a tabular format:

- **Username**: Displays the name of the user name of the user
- **Email**: Displays the user’s email address provided during registration.
- **Roles**: Displays the roles associated with the user, as assigned during registration.
- **Status**: Displays the current status of the user, which can be Available, Inactive, or On Leave. A user is marked as Inactive when their status is disabled using the status toggle in task settings. When a user is on leave, the status is updated to On Leave. Deleting a user using the Delete option in the Actions column removes the corresponding row from the table.
- **Leave Until**: Displays the date and time until which the user is on leave.
- **Last Activity**: Displays the date and time when the user was last active on the platform.
- **Actions**: Displays a kebab menu. Clicking this menu allows you to edit user details or delete the user from the platform.

You can filter users based on role type, assigned groups, and status (such as available, active, inactive, or on leave). Use the pagination controls to adjust the number of rows displayed in the table and to navigate between pages.

## Add User

To add a user to the platform, follow the steps below:

1. From the left navigation panel, click Administration. By default, the Users page is displayed.
2. On the Users page, click Add. You can either create a new user or import an existing user.
    ![pulse-administration-users-add](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-add-a.png)
3. When you click New, a window opens where you can enter the user’s first name, last name, and email address to register the user. You can also enable user login with local credentials (username and password) by selecting the corresponding checkbox.
4. After entering the required details, click Next at the bottom of the page.
    ![pulse-administration-users-add-1](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-add-1.png)
5. On the next page, select one or more roles to assign to the user from the list of available roles. Use the search bar to quickly locate specific roles. For information on creating new roles, refer to the Roles topic. After selecting the required role(s), click Next at the bottom of the page.
    Selecting a role at this stage is optional. You can also assign roles later while editing the user.
    ![pulse-administration-users-add-choose-role](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-add-choose-role.png)
6. On the next page, select the group(s) to which the user should be assigned. You can assign the user to one or more groups. This step is optional and can be completed later while editing the user.
    Use the search bar to quickly locate specific groups. You can also use the Select All option at the top of the page to assign the user to all available groups at once.
    ![pulse-administration-users-add-choose-group](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-add-choose-group.png)
    After selecting the group(s), click Next to proceed to the next step in the user creation process.
7. The next step is to assign permissions to the user being created on the platform. You can enable or disable permissions by toggling the available effective permissions, such as Create, View, Edit, and Delete, across entities like roles, permissions, users, groups, projects, processes, rules, process instances, and workflows.
    If the user is not assigned to any role or group in the previous steps, you must override the default behavior to configure permissions. To do this, click Override at the top of the Permissions page, and then click Proceed in the confirmation dialog. This allows you to manually assign permissions to the user.
    ![pulse-administration-users-override-permissions](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-override-permissions.png)
    If the user is assigned to one or more roles or groups, the permissions are automatically derived based on those associations.
8. The next step is to assign a manager to the user. This step is optional, and you can choose to skip it during user creation. You can assign a manager later by editing the user. Use the search bar to quickly locate and select a user to assign as the manager. After adding a manager or choosing to skip this step, click Next to proceed.
    ![pulse-administration-users-choose-manager](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-choose-manager.png)
9. The next step is to assign subordinate users who report to the current user. You can select one or more users from the list of available users on the page. Use the search bar to quickly locate specific users. You can also use the Select All option at the top of the page to assign all available users as subordinates.
    ![pulse-administration-users-choose-subordinates](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-choose-subordinates.png)
    After selecting the subordinate users, click Next at the bottom of the page to proceed.
10. The next step is to select the relevant skills for the user. You can choose one or more skills from the available list by checking the corresponding boxes. Use the search bar to quickly locate specific skills. After selecting the required skills, click Next at the bottom of the page to proceed.
    To add a new skill, click Add or Search Skills at the bottom of the page and enter the skill name. If matching skills are available, select the appropriate option from the list. Otherwise, click Add next to the input field to create a new skill.
    ![pulse-administration-users-choose-skills](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-choose-skills.png)
11. The final step in user configuration is to define bandwidth and task settings. Specify the user’s available bandwidth, remaining bandwidth, and daily limit. Under Task Settings, use the toggles to control whether the user is eligible for task assignment. If the Status toggle is disabled, the user is marked as inactive. If the Task Distributor toggle is disabled, the system will not automatically assign tasks to this user. By default, the Status and the Task Distributor toggles are enabled. After all the fields have their respective values filled, click the Review and Save button at the bottom of the page.
    ![pulse-administration-users-choose-bandwidth-save](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-choose-bandwidth-save.png)
12. The final page allows you to review the configured permissions, roles, and groups associated with the user, along with the assigned skills. Click Create User to complete the process and create the user on the platform.
    ![pulse-administration-users-create-user-save](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-users-create-user-save.png)

## Edit User

To edit a user’s details, follow the steps below:

1. On the Users page, locate the user whose details need to be edited. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Edit.
    ![pulse-administration-edit-user-action-column](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-edit-user-action-column.png)
2. The subsequent screens in the edit workflow follow the same sequence as the user creation process. Navigate through each step to update the required details, such as permissions, roles, groups, skills, manager, subordinates, and bandwidth settings for task assignment.
    After making the necessary changes, review the updated information and save the settings to apply the updates.

## Delete User

To delete a user from the platform, follow the steps below:

1. On the Users page, locate the user to be deleted. In the corresponding row, go to the Actions column, click the kebab (three-dot) menu, and select Delete.
    ![pulse-administration-edit-user-action-column-delete](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-edit-user-action-column-delete.png)
2. A confirmation dialog is displayed, prompting you to confirm the deletion of the user. This action is irreversible and cannot be undone. Click Yes to confirm and delete the user from the platform.
   ![pulse-administration-edit-user-action-delete-confirmation](/resources/Storage/neutrinos-reels-publication/images/pulse-administration-edit-user-action-delete-confirmation.png)
