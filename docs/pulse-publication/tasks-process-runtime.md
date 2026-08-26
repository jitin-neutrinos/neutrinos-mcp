# Interface

<https://documentation.neutrinos.com/articles/#!pulse-publication/tasks-process-runtime>

The Tasks submodule in the Process Runtime module lists all process instances that contain one or more user tasks.

## Interface

![up-process-runtime-tasks-table](/resources/Storage/pulse-publication/images/up-process-runtime-tasks-table.png)

- **ID**: Displays the process instance ID associated with the process instance under execution.
- **Task Name**: Displays the name of the user task node in the process instance.
- **Process Definition**: Displays the name of the process definition that contains the user task node.
- **Assignee**: Displays the name of the user currently assigned to complete the user task.
- **Created On**: Displays the date and time when the process instance was created.
- **Status**: Displays the current status of the corresponding user task.
- **Actions**: Contains a kebab menu that opens a context menu with an option to view the associated process definition.

Additionally, you can use the Search bar to search for a specific user task. The Show by drop-down list allows you to specify the number of rows displayed in the table, while the pagination controls allow you to navigate between multiple pages of user tasks.




 Further, you can use the Filter option to filter user tasks based on State, Assignee, Task ID, Process Definition, Created On, or Follow-up Date.

## Complete User Task

To complete the User task, follow the steps below:

1. In the Tasks submodule of the Process Runtime module, locate the required user task. You can use the Search bar to quickly find a specific user task. **Note**: You can work only on user tasks that are assigned to you. You can also reassign a task to another user. However, you cannot claim a task that is already assigned to another user.
2. Click the user task assigned to you to open the task details page. This page contains the following tabs:
  - Form: Displays the form associated with the user task, if available, and allows you to enter the required information to complete the task.
  - Details: Displays detailed information about the user task, including the Task Instance ID, Definition ID, Process Instance ID, Process Version, Process Name, Status, and other task-related details.
  - Diagram: Displays the process diagram
  - History: Displays the chronological sequence of events for the user task throughout its execution.
3. If the user task requires input for the process to continue, enter the required information in the fields provided in the Form section.
   ![up-process-runtime-tasks-user-task-complete](/resources/Storage/pulse-publication/images/up-process-runtime-tasks-user-task-complete.png)
4. After entering the required information, click Complete at the bottom of the page to complete the user task and allow the process instance to proceed to the next step.
   ![up-process-runtime-tasks-user-task-complete-button](/resources/Storage/pulse-publication/images/up-process-runtime-tasks-user-task-complete-button.png)
