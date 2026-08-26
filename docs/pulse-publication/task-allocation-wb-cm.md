# Manual Task Distribution

<https://documentation.neutrinos.com/articles/#!pulse-publication/task-allocation-wb-cm>

Task distribution in the Neutrinos Alpha Platform is a process of assigning and managing tasks across users, teams, or groups. It ensures that tasks are allocated efficiently based on predefined workflows, user roles, and organizational requirements.
 Tasks can be assigned to a user in two ways

- **Manual**: A manager or an admin can assign tasks to a particular User.
- **Automated by Task Distributor**: The task distributor can automatically assign a task to a user based on either **Skill **of an User or using a **Round Robin** methods.

## Manual Task Distribution

From the Neutrinos Alpha Workbench, users can manually assign tasks to users by specifying their names, provided the following settings are configured in **Team **or **Group Tasks** Inbox in Workflow Studio:

- **Enable Re-assign**: When this toggle is enabled, tasks can be reassigned to other users. By default, it is disabled, preventing reassignment by other users.
- **Groups for Reassignment**: A group of users must be specified as eligible for task reassignment. The reassignment checkbox is available only to users within the specified group, ensuring that the task reassignment remains within the defined scope.
- **Manager Re-assignment (Optional)**: When this toggle enabled, only managers can assign tasks. By default, it is disabled, allowing any user to assign tasks.

### Reassigning Tasks in Team or Group Tasks Inbox

To reassign tasks in the Team or Group Tasks Inbox, follow these steps:

1. **Select Tasks**:
  - In the Workbench, navigate to Group Tasks inbox > Select the checkboxes for the tasks you wish to reassign.
  - Click the** Reassign **button.
      ![ASsign-task-1](/resources/Storage/pulse-publication/images/assign-task-step1.png)
2. **Assign to a User**:
  - On the **Reassign Tasks** page, click the **Assign **dropdown.
      ![assign-task-2](/resources/Storage/pulse-publication/images/assign-task-step2.png)
  - From the list of available users, search for or select the user ID of the intended assignee.
  - Click the **Confirm **button.
      ![assign-task-3](/resources/Storage/pulse-publication/images/assign-task-step3.png)
  - Verify that the selected user's ID is reflected in the **Assigned To** field.
  - Click the **Next **button to review the case details and the **New Assignee** field.
      ![assign-task-4](/resources/Storage/pulse-publication/images/assign-task-step5.png)
3. **Confirm Reassignment**:
  - Click the **Confirm** button.
  - Observe the **Reassignment Complete** page, confirming the successful assignment.
4. **Return to Inbox**: Click the **Back to Inbox** button to return to the **My Tasks** Inbox page.
    ![assign-task- confirm](/resources/Storage/pulse-publication/images/assign-task-step-confirmation.png)
    ![Note](/resources/Storage/pulse-publication/note.png)
    The new task assigned is added to the user and appears in their My Tasks inbox. Additionally, tasks may be assigned either individually or in bulk using **Bulk Assign** option available.

## Automated Task Distribution

The Task Distributor in the Neutrinos Alpha Workbench is designed to automatically assign tasks to users. This assignment is based on available User's bandwidth, Daily Limit, and / or the skills of logged-in users. This process operates on a timed interval to ensure tasks are distributed efficiently without overloading any user.

The components involved in Automated Task Distribution System are:

1. **Task Distribution System**: Core component responsible for initiating and managing the task distribution process.
2. **Admin Service**: Provides data on logged-in users.
3. **Config Service**: Handles configurations for task distribution.
4. **IDS Service**: Handles identity data for authentication and user information.

The flow diagram illustrates the process flow in automated task distribution:




 ![task distribution system flow](/resources/Storage/pulse-publication/images/task-distribution-system.jpg)

The Process flow of the Task distributor is as follows:

1. At specified intervals, the Task Configs are retrieved from the Config Service of the project.
2. The Admin Portal provides two lists for the task distributor: the list of configured user groups and the list of logged-in and active users.
3. The Task Distributor fetches all tasks in Ready state for groups. Further it checks the distribution criteria: Round Robin or Skill Based.
  1. Round Robin: The next user in the retrieved list of users is selected. For the selected user, their available bandwidth and daily limit are checked to determine if the task can be assigned. If the user is eligible, the task is assigned and accordingly the bandwidth and daily limits are adjusted for the user. Otherwise, the task remains unassigned, and the task distributor moves to the next available user in the list.
  2. Skill Based: The tasks are scored based on how well they match a current user's skill score and assigned to a user as follows:
    1. If an eligible task with a sufficient match score is available, it is assigned to the user, and the user's bandwidth is updated.
    2. If user is not eligible or the user's bandwidth/daily limit is insufficient, the system skips to the next user.

The process is repeated through all users in every user group until all tasks in the list are assigned or completed.
