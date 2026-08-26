# Pull Task

<https://documentation.neutrinos.com/articles/#!pulse-publication/pull-task-wb-cm>

Tasks are typically assigned to a user either by the Task Allocator or by an Admin. The Pull Task feature allows users to manually pull tasks into My Tasks based on their available bandwidth. This enables users to proactively take up work when they have fewer tasks than usual or no tasks currently assigned.

To pull tasks, follow these steps:

1. In the workbench, go to the Inbox page, click the **Tasks** dropdown and select **My Tasks** to view the list of My Tasks.
    ![alpha-pull-tasks-navigate-my-tasks](/resources/Storage/pulse-publication/images/alpha-pull-tasks-navigate-my-tasks.png)
2. Scroll to the bottom of the page. At the end of the page, locate the option to pull tasks. Select the number of tasks you want to pull based on your need or requirement. You can choose to pull 1, 3, 5, 8, or a custom number of tasks. The total number of available tasks for the day is displayed at the bottom of the screen. Note: If your daily bandwidth is exhausted, you will not be able to pull additional tasks.
    ![alpha-pull-tasks-options](/resources/Storage/pulse-publication/images/alpha-pull-tasks-options.png)
    When a user selects a specific number of tasks to pull, the platform uses a fire-and-forget mechanism. This allows the user to continue navigating to other pages while the system allocates the requested tasks in the background. Because the pull operation runs entirely in the background, the user can continue with other work without any interruption.
    Tasks are pulled in real time, and the UI is updated continuously as each task is processed, indicating whether the pull operation was successful or failed. The average latency is *x* seconds, depending on the number of tasks pulled or requested.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    The most commonly pulled task counts are 3 or 5.
3. Once you select the number of tasks to pull, they will appear in your **My Tasks** list. For example, the GIF below demonstrates pulling a single task from the pool of available tasks in the Group Tasks list.
    ![alpha-pull-tasks-options-1-task](/resources/Storage/pulse-publication/images/alpha-pull-tasks-options-1-task.gif)
    The tasks pulled by a user can be affected by allocation priority. The priorities are as follows:
    For example, suppose a task with ID 1000 is pulled through the pull operation, but the same task is simultaneously (or at any later point) assigned to another user by an Admin. In that case, the task will no longer appear in *My Tasks* for the user who initially attempted to pull it. In summary, Admin Assignment has the highest priority and overrides any other type of task allocation.
  1. Admin Assignment: 1 (Highest)
  2. Pull Task Operation: 2
  3. Task Distributor: 3 (Lowest)
