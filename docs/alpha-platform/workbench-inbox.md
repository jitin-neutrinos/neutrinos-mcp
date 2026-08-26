# Types of Inbox

<https://documentation.neutrinos.com/articles/#!alpha-platform/workbench-inbox>

The Inbox is an essential tool to streamline daily workflows by organizing tasks in a manner that is most relevant to the user. It serves as the **primary interface** for task management, acting as a hub for all tasks assigned to you, your group, or your team.
 With a user-friendly interface, the **Inbox** is designed to facilitate ease of use, enabling users to efficiently manage and track tasks, enhance productivity. The **Inbox** consists of the following key features:

![](/resources/Storage/alpha-platform/images/inbox-complete.png)

1. **Inbox Table**: An interactive table that consolidates all active tasks, with each row corresponding to a specific task. You can filter the Inbox table based on the required criteria that helps to focus on required task.
2. **Inbox Lists**: This feature allows you to easily switch between different types of task inboxes, such as **My Tasks**, **Team Tasks**, and **Group Tasks**. Users can set a default list, which will load initially.
3. **Columns**: This feature allows users to select and view only the required information in the Inbox table, eliminating unnecessary clutter. The columns displayed in the Inbox can be customized based on specific needs to display relevant information tailored to each user.
4. **Filters**: The Inbox allows you to apply filters to retrieve filtered cases.

## Types of Inbox

The **Inbox** is categorized into multiple types to cater to different task management needs:

1. **My Tasks**: This type of Inbox is designed to display tasks specifically assigned to the logged-in user. It enables users to focus on their individual responsibilities, streamline task prioritization based on urgency or deadlines, and quickly access task details and related Case Information. The image below shows My Tasks Inbox assigned to a particular logged user.
    ![my tasks inbox](/resources/Storage/alpha-platform/images/mytasks-inbox.png)
    Alternatively, when you have additional bandwidth—for example, when you have fewer tasks or no tasks assigned in My Tasks—you can proactively pull tasks and work on them. For more details, refer to the [Pull Tasks](/articles/alpha-platform/pull-task) topic.
2. **Team Tasks**: It shows or displays tasks assigned to your reportees, providing managers a convenient way to assign or reassign tasks. The image below illustrates the Team Tasks Inbox, highlighting tasks assigned to team members.
    ![team tasks inbox](/resources/Storage/alpha-platform/images/teamtasks-inbox.png)
3. **Group Tasks**: Displays tasks assigned to a specific group of users but not yet allocated to any individual team member. Tasks in this inbox require reassignment to a specific user for further action. Reassignment can be performed in two ways:
    The image below shows Group Tasks Inbox assigned to specific group:
    ![group tasks inbox](/resources/Storage/alpha-platform/images/grouptasks-inbox.png)
  1. An admin can delegate a task from the group tasks.
  2. A user can claim a task from the group tasks and release it after completing the work. To know more, refer [Claim and Release Tasks](/articles/alpha-platform/claim-and-release-tasks) topic.

## Filters

Inbox filters in Neutrinos Alpha Workbench are customizable criteria used to sort and organize tasks. These filters help users view specific subsets of tasks based on parameters, such as case instance that contain task and case data.
 These filters provide the following uses:

1. **Enhanced Task Management**: Quickly identify tasks that require immediate attention, such as overdue or high-priority items.
2. **Custom Views**: Personalize task views to match user-specific needs, such as tasks within a task group or priority.
3. **Improved Efficiency**: Reduce time spent searching for tasks by directly accessing filtered lists tailored to your preferences.
4. **Workflow Optimization**: Gain insights into task progress by applying filters like status (e.g., "In Progress," "Completed").

To access filters in any inbox, click the **Filter** button in the respective inbox. The GIF below demonstrates some of the available filters and illustrates how to apply a sample filter to display cases with CID values between 12,000 and 13500:

![filter in Inbox](/resources/Storage/alpha-platform/images/filter-gif.gif)

| ![Note](/resources/Storage/alpha-platform/note.png) | The Filters can be customized based on the requirement in Workflow Studio. |
| --- | --- |

Further, users can save a filter by assigning it a name for faster access. To save a filter, follow the below steps:

1. In any Inbox, Click on **Filter**.
2. Create a Filter criteria > Click **Apply Filter**.
3. Click the **Save Filter** button > In the popup, set a **Filter Name**.
4. Click **OK**.
    The below GIF illustrates how to save a filter in Neutrinos Alpha Workbench.
    ![Save Filter Gif](/resources/Storage/alpha-platform/images/save-filter.gif)

Observe the Saved Lists section in the Inbox List contains filters that user saved. The image below illustrates a filter saved specifically for Group Tasks in the Saved Lists section.

![Saved Filter image](/resources/Storage/alpha-platform/images/savedfilter-inboxlist.png)

### Inbox URL Params

Previously, when filters were applied in the Inbox, refreshing or reloading the page would reset the filters and remove the applied criteria. With this enhancement, filter selections now persist across page refreshes and reloads.

Applied filters are also retained when you navigate from the Inbox to a case and then return—for example, by clicking the Home button from a case details page. This persistent behavior is supported across all Inbox types, including the [Admin Inbox](/articles/alpha-platform/admin-inbox).

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | The Inbox URL is now shareable. When another user accesses the shared URL, the Inbox opens with the same filters automatically applied, as the filter parameters are included as part of the URL. |
| --- | --- |

## Columns

Columns in the Inbox represent distinct data fields or attributes displayed for each task or item in the task list. They provide a structured and customizable view of task-related information, enabling users to quickly assess key details at a glance. For example, the columns can display essential details such as caseid, task name, priority, status, assigned user, and so on.

Click the **Columns** (![Columns icon](/resources/Storage/alpha-platform/images/columns-icon.png)) button in any inbox to check the available options under columns for the particular inbox. Users can personalize their Inbox by selecting the columns they wish to display and deselecting unnecessary columns to suit their preferences.

The GIF below demonstrates how to configure columns in the Inbox and include only the necessary columns:

![Columns selecting GIF](/resources/Storage/alpha-platform/images/columns-gif.gif)

## Dashboard in Inbox

The Dashboard is a user interface component in the Inbox of Neutrinos Alpha that displays a list of case statuses and allows users to add additional status information related to cases.

![Dashboard image](/resources/Storage/alpha-platform/images/dashboard-inbox.png)
