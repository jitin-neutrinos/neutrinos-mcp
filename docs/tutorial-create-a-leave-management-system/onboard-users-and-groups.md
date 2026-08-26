# Adding Users

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/onboard-users-and-groups>

You onboard users and groups from [Neutrinos Console](https://console.neutrinos.co).

Any organization will have at least one organisation admins, and the user with organisation admins group access is granted permissions for managing users in his/her organization.

An organisation admins can also add custom groups to their respective organizations for managing user roles in the designed sample app.

For the LMS app, we are required to have a minimum of two users, one with the **Manager **group and the other with the **Employee **group. Employees will request leave from the respective managers of their department and the manager approves or rejects the leave request. Also, the manager being an employee can also apply for leave.

### Adding Users

To add a new user, click the **Add User** button in the **Users** section, fill the required information in the **Add User** form, and click the **Save User** icon to add the user.

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | You can select the **Teams** field to which the user belong after creating **Teams**. If the team already exists, you can select which team the user belongs to. |
| --- | --- |

For this tutorial, we are going to add two new test users to our organization. You can use the dummy data in the following tables as the user information.

### Manager

| Field name | Value |
| --- | --- |
| First Name | Michael |
| Last Name | Jordan |
| Organization Name | neutrinos |
| `Email` | m.jordan@{your organisation name}.co |
| Password | Pass1!5 |
| Teams | Manager |

### Employee

| Field name | Value |
| --- | --- |
| First Name | Jonathan |
| Last Name | Stones |
| Organization Name | neutrinos |
| `Email` | jonathan.st@{your organisation name}.co |
| Password | pass11! |
| Group | Employee |

After filling the required fields, click the ![](/resources/Storage/tutorial-create-a-leave-management-system/fundamentals-img0052.png) icon to save the user details. Once a new user is added successfully, you will see a snackbar with the message* "**The user is added to your organization.**"*

### Adding Teams

In the Neutrinos Console, navigate to the **Teams** section, and click the **Add** **team** icon ![](/resources/Storage/tutorial-create-a-leave-management-system/add_team.png) on the top-right section of the page. In the **Add team **dialog box, enter the **Team Display Name, Team Description, Add Users **for the team that you are creating from the drop-down list and click the **Save ![](/resources/Storage/tutorial-create-a-leave-management-system/fundamentals-img0052.png)** button to add the group to your organization.

For the LMS app, add the following groups:

- Employee
- Manager

![LMS onboard groups](/resources/Storage/tutorial-create-a-leave-management-system/TeamsLMS.png)

| ![Warning](/resources/Storage/tutorial-create-a-leave-management-system/warning.png) | It is important that you create at least one user with the Group **Manager** and another user with Group **Employee **for testing the LMS app. |
| --- | --- |
