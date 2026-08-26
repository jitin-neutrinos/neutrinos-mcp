# Add User

<https://documentation.neutrinos.com/articles/#!pulse-publication/users-admin-cm>

In Neutrinos Alpha Workbench, the Users section within the Admin UI helps managing individual user accounts, access rights, and roles for the business process. This section provides administrators to control and monitor user activities, ensuring that the platform's security and operational efficiency are maintained. The image below illustrates the **Users **page in Admin UI.

![admin ui users page](/resources/Storage/pulse-publication/images/users-page-adminui.png)

The **Users page** presents user-related information in a tabular format, for each user:

1. **Username**: The username assigned to a user upon creation.
2. **Bandwidth**: The total number of tasks a user can perform.
3. **Remaining Bandwidth**: A system-calculated field that displays the remaining tasks after allocation, which cannot be edited by the Admin.
4. **Daily Limit**: The maximum number of tasks a user can complete in a single day, defined manually by the Admin.
5. **Remaining Daily Limit**: A system-calculated field that resets daily based on the Daily Limit. The recalculation requires overall available bandwidth to ensure the user receives the updated daily allocation upon completing their first task of the day.
6. **Groups**: The groups to which the user is assigned.
7. **Skills**: Displays the list of user's skills.
8. **Status**: Indicates whether the user is **Active** or **Inactive**.
9. **Actions**: Allows admins to edit and update user details.

## Add User

The flowchart below illustrates the process in User creation in the Neutrinos Alpha Platform.

![flowchart to create user](/resources/Storage/pulse-publication/images/createUser.jpg)

The Admin is responsible in adding both the User and creating relevant groups in the platform.

To add an **User** in the Workbench, follow these steps:

1. Click the **Add Users** button on the top-right corner of the Users Page > Select **Create** to open the user creation form.
2. In the **Create **page, provide **User** details
    Optionally, you can also add the following details for the users at the time of creating the user itself:
  1. **Username**: Enter the username to identify the user. Note that the username entered should exactly match an existing username in Identity Server. This is used to reference user metadata and manage groups in the Workbench.
  2. **Bandwidth**: Specify the total number of tasks the user can perform.
  3. **Daily Limit**: Set the maximum number of tasks the user can complete in a single day.
  4. **Status**: Use the toggle to indicate if the user is **Active**. By default, the toggle is disabled.
      ![Warning](/resources/Storage/pulse-publication/warning.png)
      If a user is disabled, they will be unable to log in to the Workbench. Any tasks assigned to the disabled user will remain with them and must be manually reassigned to other active users.
  5. **Task Distributor**: Use the toggle to enable or disable automatic task distribution for the user by **Task Distributor**. When disabled, tasks must be manually assigned to the user. By default, this toggle is turned off.
  1. **Add User To Groups**: Select a relevant group from the list of existing groups within the business process to add the user.
      ![Note](/resources/Storage/pulse-publication/note.png)
      To know more on Adding or Creating Groups through Admin UI, see [Groups](/articles/pulse-publication/groups-admin-cm/a/h2_1446455329) topic in Admin User Manual.
  2. **Add Skills To User**: Assign skills to the user to enable automatic task allocation by the task distributor system. When adding skills, the admin must specify the proficiency for each skill using a star rating system, where one star represents the lowest proficiency and five star represents the highest. Examples for skills include "Underwriting", "Operations", and others, depending on the needs of the business process. These skills help in For more information on how skills are used in automatic task allocation, see [Task Allocation](/articles/pulse-publication/task-allocation-wb-cm/a/h2_599310866), topic in Workbench User Manual.
      ![Note](/resources/Storage/pulse-publication/note.png)
      When adding skills, it is mandatory to include the corresponding proficiency level; otherwise, an error will occur.
  3. **Add Reportees**: If the user has managerial responsibilities, the admin can assign reportees to them, adding other users as subordinates. This establishes a logical organizational reporting structure and forms a team.

| ![Note](/resources/Storage/pulse-publication/note.png) | The steps outlined above assume that users are already part of the IDS. |
| --- | --- |

The image below illustrates creating or adding the User through the Admin UI:

![Add user - Admin UI - step](/resources/Storage/pulse-publication/images/users-page-adminui-step.png)

After the step one from the above image, the GIF below illustrates adding necessary details to create Users through Admin UI.




 ![Admin-ui- Add User - gif](/resources/Storage/pulse-publication/images/admin-ui-add-user-gif.gif)

| ![Note](/resources/Storage/pulse-publication/note.png) | Admins can search the User using the **Search** option in the **Users** page. |
| --- | --- |
