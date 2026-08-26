# Inbox Types

<https://documentation.neutrinos.com/articles/#!pulse-publication/inbox-config-editor-wf-cm>

This topic outlines the possible customizations that developers can implement in the Inbox using Workflow Studio. The first section explains how a Workbench user views the Inbox, while the later section covers the customizations.

The **Inbox** is a key feature in **Workbench **, helping users efficiently manage their daily tasks. As a Workflow Studio developer, you can design and customize inboxes to organize tasks based on user needs. The image below illustrates the basic layout of an inbox as seen by Workbench user:

![inbox-complete](/resources/Storage/pulse-publication/images/inbox-complete.png)

As a developer, you can customize the following:

- Add or remove columns to display relevant task details.
- Define filter criteria to control task visibility for Workbench users. By default, filters criteria pertaining to Case Instance and Task Instance are automatically added in the Workflow Studio. Based on the specific needs, these can be modified to add custom filter criteria.
- Enable or disable specific inbox types for users.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | The **Inbox** is scoped per project. Each project includes a **My** **Task Inbox**, **Team Inbox**, and **Groups Inbox **shared among all users. Additionally, an **Enquiry Inbox** can be enabled if needed. |
| --- | --- |

## Inbox Types

1. **My Task**: This type of Inbox is designed to display tasks specifically assigned to the logged-in Workbench user. It enables them to focus on their individual responsibilities, streamline task prioritization based on urgency or deadlines, and quickly access task details and related Case Information. The image below illustrates My Tasks inbox in Workbench:
    ![](/resources/Storage/pulse-publication/images/mytasks-inbox.png)
2. **Team Tasks**: This Inbox displays tasks assigned to the reportees of the logged-in Workbench user. The image below illustrates Team Tasks inbox in Workbench:
    ![](/resources/Storage/pulse-publication/images/teamtasks-inbox.png)
3. **Group Tasks**: Displays tasks assigned to a specific group of users but not yet allocated to any individual team member. The image below illustrates Group Tasks inbox in Workbench:
    ![](/resources/Storage/pulse-publication/images/grouptasks-inbox.png)
4. **Admin Inbox**: The Admin Inbox is similar to a standard user inbox but includes additional features that enable administrators to effectively manage and coordinate cases and tasks assigned to team members, as well as monitor their progress. The Admin can access three types of inboxes as discussed below:
  1. Tasks Inbox: This inbox type displays all the cases linked with the project. The image below illustrates Tasks inbox showcasing all the tasks for a particular project:
      ![tasks-inbox-fullscreen.png](/resources/Storage/pulse-publication/images/admin-tasks-inbox-fullscreen.png)
  2. Signal Inbox: If a deployed BPM process contains a single task and the Save Signal API is triggered before it, this list will display signals that are in a waiting state. The Alpha Admin can manually trigger this signal to approve the task, allowing the process to resume to the next step. The image below illustrates the Signal inbox in Admin UI Workbench.
      ![](/resources/Storage/pulse-publication/images/adminui-signal-inbox.png)
  3. Re-attempt Inbox: The Re-attempt Inbox in the Admin UI of Neutrinos Alpha Workbench is designed to manage failed or incomplete tasks. Based on business requirements, specific tasks can be configured to appear as 'Re-attempt.' This scenario enables an admin to restart the process from the exact node where it previously failed. The image below illustrates a Re-attempt inbox in Admin UI Workbench.
      ![](/resources/Storage/pulse-publication/images/adminui-re-attempt-inbox.png)

Regardless of the inbox type, the customization settings remain largely the same for all inboxes from a Workflow Studio developer's perspective. The following sections outline the customizations developers can make in **Workflow Studio**.

## Inbox Visibility

A developer can control the visibility of specific inbox types for users through **Workflow Studio**. For example, if a process requires all users to view tasks only from the **Group Tasks Inbox** and return to it after completing a task, other inboxes can be hidden. This is achieved by disabling the toggle for specific inbox types, ensuring they remain hidden from users. By default, this toggle is on, enabling the user to view and access it. The image below illustrates the toggle used to hide the Team Tasks inbox from Workbench user.

| ![Warning](/resources/Storage/pulse-publication/warning.png) | The 'My Tasks' inbox must always be enabled for the logged-in user to view their assigned tasks. |
| --- | --- |

![workflow-studio-config-disable-inbox](/resources/Storage/pulse-publication/images/workflow-studio-config-disable-inbox.png)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | If an inbox is disabled, any other inbox-related settings will not take effect, as the inbox is not accessible to the user. |
| --- | --- |

The image below shows that Team Tasks inbox is unavailable to Workbench users when the toggle is turned off:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-disable-inbox-workbench.png)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | For Inbox, you can add custom code trigger. For more information see, [Custom Code](/smart/project-alpha-platform/triggers/a/h2_1762374550). |
| --- | --- |

## Filter Criteria

Inbox filters in **Neutrinos Alpha Workbench **are customizable criteria used to sort and organize tasks. These filter criteria can be configured in. Some properties related to case instance and task instances are available as default filter criteria, applicable to all Inbox types. Additionally, developers can customize these filter criteria for Inboxes based on specific business requirements.

### Enable Filter

You can enable or disable the filter functionality in the Inbox by toggling the filter toggle available in each inbox. By default, the filter toggle is set to false (disabled).

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | When the filter is disabled, users will not be able to view the filter options in the Inbox. |
| --- | --- |

The below image illustrates the toggle to enable filtering functionality in the My Tasks Inbox.

![](/resources/Storage/pulse-publication/images/workflow-studio-config-enable-filter.png)

The GIF below, illustrates adding the filter criteria to Team Tasks inbox:




 ![](/resources/Storage/pulse-publication/images/workflow-studio-config-add-filter-gif.gif)




 To add filter criteria in Inbox, follow the steps below:

1. In the Config editor, navigate to Inbox editor > Choose the Inbox type, in which filter needs to be added. Ensure filter toggle is enabled.
2. Click **Add Filter Criteria** button > A new filter row is added.
3. Set the filter criteria as required. The values in each field can be as follows:
    **Field**
    **Description**
    Filter Name
    Type: The value can be either **String** or **Language**. If the value needs to be translated into multiple languages, select **Language** from the dropdown.
    Value textbox accepts the value displayed as the name of the filter.
    For example: Assignee
    Binding Value
    The binding value for each filter criteria can be either CO, Case Instance, Task Instance, or Signal Instance.
    CO
    A global variable, that contains the entire case data accessible across the application.
    Case Instance
    Accepts fields from the case instance, such as cid, piid, status, cdid, caseData.cdid, caseData.created_at, and caseData.updated_at.
    The caseData.created_at and caseData.updated_at fields are date fields, which require specifying a date range for filtering. You can also specify the date format as needed.
    Task Instance
    Accepts fields from the task instance, such as taskId, taskName, and taskStatus, along with select metadata fields, such as taskOwner and taskDescription and so on.
    The task instance also contains date fields for which you can specify the date format, similar to the case instance.
    Signal Instance
    Accepts fields from the signal instance (if the workflow includes a signal node), such as id, cid, piid, signalName, status, created_at and updated_at.
    The created_at and updated_at are date fields. You can also specify the date format as needed.
4. Click the **Save** button to save the created filter criteria. The filter will be visible in the **Inbox** for which it was created, for the **Workbench ** user.

The image below illustrates the filter criteria added to Team Tasks inbox in Workbench:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-enable-filter-workbench.png)

### Save Filter

**Save Filter** is an option that allows a **Workbench **user to save frequently used filter criteria. As a **Workflow Studio **developer, you can enable or disable this option using the **Save Filter** toggle. By default, this Save Filter toggle is enabled for all the type of inboxes. The image below illustrates the Save Filter toggle available for each inbox type:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-save-filter.png)

### Exact Mach

Filters are used to narrow down the list of cases based on specific criteria such as case ID, status, or other case attributes. An Exact Match filter ensures that the platform returns only those records whose field values exactly match the value specified in the filter condition, without allowing partial matches.

The Exact Match option can be enabled for filter criteria that support string-based matching, such as String fields and Multi Select values. To enable Exact Match for a specific filter, follow the steps below:

1. Navigate to the Config page from the left navigation panel to configure the settings.
    ![alpha-exact-match-filter-navigation](/resources/Storage/pulse-publication/images/alpha-exact-match-filter-navigation.png)
2. From the list of available configuration settings, click Inbox.
3. From the list of available inbox types, select the required inbox to view its configuration settings.
    ![alpha-exact-match-filter-navigation-inbox](/resources/Storage/pulse-publication/images/alpha-exact-match-filter-navigation-inbox.png)
4. In the Filter section, locate the filter criteria that use either the string (search) type or the dropdown (multi-select) type.
5. For the selected filter criteria, scroll to the right to locate the Exact Match checkbox. Enable this checkbox if the filter should require an exact match when applied by the user.
    ![alpha-exact-match-filter-exact-match-checkbox](/resources/Storage/pulse-publication/images/alpha-exact-match-filter-exact-match-checkbox.png)
6. Save the configuration settings to apply the Exact Match setting for the filter criteria.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | Note: When the Exact Match checkbox is enabled, it becomes the default criterion when a user applies this filter in the workbench. However, users can still enable or disable this option in the workbench as needed. |
| --- | --- |

### Delete Filter Criteria

You can remove a filter from an **Inbox** using the **Delete Filter** button available next to each filter criteria. Default filters in inboxes can also be removed. Once a filter is removed, the user will no longer be able to view it in the **Inbox** on **Workbench **. The GIF below illustrates how to delete a filter from the **Team Tasks Inbox**.

![](/resources/Storage/pulse-publication/images/workflow-studio-config-delete-filter.gif)

## Columns

Columns in the Inbox represent distinct data fields or attributes displayed for each task or item in the task list. Workbench users can customize the inbox view by selecting the columns they need. By default, the inbox table layout includes common columns that fetch data from both Case Instance and Task Instance. The GIF below illustrates how the user of Workbench interacts with the columns in Neutrinos Alpha Platform.

![](/resources/Storage/pulse-publication/images/columns-gif.gif)

As a developer, you can customize the columns in Inbox by modifying their order, hiding specific columns, enabling sorting, and selecting which columns appear for each inbox type. The GIF below illustrates how to add a column in Team Tasks inbox to view the assignee of tasks:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-add-column-gif.gif)

### Add Column

To add a column in any Inbox follow the steps below:

1. In the Config editor, navigate to Inbox editor > Choose the Inbox type, in which **Column** needs to be added.
2. Click the **Add Column** button > A new row to add a Column is added
3. Provide the details in the fields below:
    **Field**
    **Description**
    Column Label
    Type: The value can be either **String** or **Language**. If the value needs to be translated into multiple languages, select **Language** from the dropdown.
    Value textbox accepts the value displayed as the name of the Column.
    For example: Assignee
    Binding Value
    The binding value to column to fetch data can be either CO, Case Instance, Task Instance, or Signal Instance.
    CO
    A global variable, that contains values accessible across the application.
    Case Instance
    Accepts fields from the case instance, such as cid, piid, status, cdid, caseData.cdid, caseData.created_at, and caseData.updated_at.
    The caseData.created_at and caseData.updated_at fields are date fields. You can specify the date format as needed.
    Task Instance
    Accepts fields from the task instance, such as taskId, taskName, and taskStatus, along with select metadata fields, such as taskOwner and taskDescription and so on.
    The task instance also contains date fields for which you can specify the date format, similar to the case instance.
    Signal Instance
    Accepts fields from the signal instance (if the workflow includes a signal node), such as id, cid, piid, signalName, status, created_at and updated_at.
    The created_at and updated_at are date fields. You can specify the date format as needed.
    Hideable
    When this checkbox is enabled, the column is hidden by default from Workbench users. To make the column visible, users must click the **Columns** button and manually enable it.
    By default, this checkbox is unchecked. The column remains visible in the inbox table unless explicitly hidden.
    Sort
    The **Sort** checkbox, when enabled, allows Workbench users to sort data in the column. By default, this checkbox is disabled for all columns.
    **Note:** If the **Table Sort** toggle is disabled, users cannot sort data in a column, even if the **Sort** checkbox is enabled for a specific column.
    Action
    This setting allows you to remove a column from the inbox. Once removed, Workbench users will no longer see the column in the inbox.
4. Click the Save button to save the added column. The Column will be visible in the Inbox for which it was created, for the Workbench user.

The image below illustrates the column "Assignee" added to the Team Tasks inbox in Workbench:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-add-column-workbench.png)

### Column Selection

The **Column Selection** toggle allows Workbench users to choose which columns are visible in the inbox table. If you disable this toggle, users will not be able to select or customize the columns in their inbox table. When this toggle is disabled, all added columns are visible to users, regardless of whether they need them or not. By default, **Column Selection **toggle is enabled.

The image below illustrates the **Column Selection** toggle turned off for Team Tasks inbox:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-column-selection-toggle.png)

### Sort Table

Sorting allows a **Workbench **user to arrange the **Inbox** contents in ascending or descending order as needed . You can enable or disable the sorting functionality using the **Table Sort** toggle. By default, this toggle is enabled for all inboxes.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | The user can sort column content only if the **Table Sort** toggle is enabled. If this toggle is disabled, sorting will not be allowed, even if the column configuration permits it. |
| --- | --- |

The image below shows the Table Sort toggle enabled for Team Tasks inbox:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-table-sort.png)

### Set Rows

You can set the default number of rows visible in any inbox for a Workbench user. The specified number becomes the default row count. The GIF below shows how to set the default row count to 15 rows in the Team Tasks inbox.

![](/resources/Storage/pulse-publication/images/workflow-studio-config-set-number-of-row-gif.gif)

To set the default row count, follow the steps below:

1. In Config editor > Navigate to Inbox editor > Choose the type of Inbox
2. Set the **Number of Rows** to required value.
3. Click the **Save** button.

The image below shows the default number of rows displayed in Workbench for Team Tasks inbox:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-set-number-of-row-workbench.png)

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | Note that the default number of rows also depends on the default inbox list configured in Workbench. For example, if the default list is 'My Tasks' inbox with 5 rows set, the same number of rows will be shown by default in all other inbox types. |
| --- | --- |

## Dashboard in Inbox

The Dashboard is a UI component in the Workbench Inbox that displays a list of case statuses to users. You can customize it to show additional case-related information, hide it, or make it collapsible or static. By default, the Dashboard is enabled and collapsible. The image below shows how to enable the Dashboard and set the collapsible behavior:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-dashboard-behavior.png)

### Add Card in Dashboard

To add additional information to dashboard in inbox follow the steps below:

1. In the Config editor > Navigate to Inbox editor > Choose any Inbox type > Scroll to find Dashboard.
2. Enable the Dashboard toggle to view in the inbox. By default, it is enabled.
3. Click the **Add Card** button and set the following details:
    **Field**
    **Description**
    Label
    Type: The value can be either **String** or **Language**. If the value needs to be translated into multiple languages, select **Language** from the dropdown.
    Value textbox accepts the value displayed as the name of the Card in the Dashboard.
    For example: Pending
    Status
    Accepts the valid case status. For example, New Case, Pending, Completed.
    Icon
    Choose an appropriate icon for the card from the available icons in the dropdown list.
    Color
    Choose a color for the card's icon.
4. Click the **Save** button.

The GIF below shows how to add a card to the Dashboard to display cases with a **Pending** status in the Team Tasks inbox:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-dashboard-add-card-gif.gif)

The image below shows the Pending card added to the dashboard, along with the collapsible button in the Team Tasks inbox in Workbench:

![](/resources/Storage/pulse-publication/images/workflow-studio-config-dashboard-add-card-workbench.png)

## Download Case Summary

Download the summary for a **Global** page in a PDF format. You can configure this option to allow Workbench users to download the summary for a page from the **kebab** icon in the **Actions** column for each case. To configure download summary, follow the steps below:

1. In Config editor > Navigate to Inbox editor > Select the required inbox > Locate **Case Summary Download** toggle.
2. Enable the **Case Summary Download** toggle.
3. Choose the **Global Page** from the list of pages in the dropdown for which the summary should be downloaded.
4. Click the **Save** button.

The GIF below illustrates how to enable download summary of global page "New Cases" from Team Tasks inbox:

![workflow-studio-config-case-summary-download-gif](/resources/Storage/pulse-publication/images/workflow-studio-config-case-summary-download-gif.gif)

The GIF below illustrates how user can download case summary from Workbench:

![workflow-studio-case-summary-download-gif](/resources/Storage/pulse-publication/images/workflow-studio-case-summary-download-gif.gif)

## Enable Re-assign

From the Neutrinos Alpha Workbench, users, managers, admins, can manually assign tasks by specifying their names, provided the following settings are configured in Team or Group Tasks Inbox in Work Studio:

- **Enable Re-assign**: When this toggle is enabled, it allows tasks to be reassigned to other users. By default, it is disabled, preventing reassignment. You can enable the toggle to configure this feature.
- **Groups for Reassignment**: Select the user groups eligible for task reassignments. The reassignment checkbox appear for users belonging only to the specified groups. This ensures tasks are reassigned within the defined scope.
- **Manager Re-assign**: Enable this toggle to allow only managers to reassign tasks, restricting other users from re-assigning the task. By default, it is disabled, allowing any user to assign tasks.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | The Force Re-assignment toggle, when enabled, allows tasks to be assigned to users even if their bandwidth is set to 0. This is particularly useful for high-priority tasks that require immediate completion. |
| --- | --- |

The image below shows configurations enabled for re-assignment from Team Tasks inbox:

![workflow-studio-config-reassignment](/resources/Storage/pulse-publication/images/workflow-studio-config-reassignment.png)

## Enquiry Inbox

The Enquiry Inbox is an interface for managing and responding to enquiries effectively. It functions as a hub, allowing users to view, track, and act on queries or requests submitted by internal or external stakeholders. In addition to the above customizations, developers can configure specific pages to display when a case from the Enquiry Inbox is accessed. These pages may include global pages tailored to specific requirements. By default, these pages are read-only due to the enabled Read-Only toggle. The GIF below demonstrates the process of configuring a global page to open from the Enquiry Inbox when a case is selected in Workbench:

![workflow-studio-enquiry-inbox-global-page-gif](/resources/Storage/pulse-publication/images/workflow-studio-enquiry-inbox-global-page-gif.gif)

To configure a page to display upon selecting a case in the Enquiry Inbox, follow the steps below:

1. In Config editor > Navigate to Enquiry inbox editor > Select Pages.
2. From the available list of global pages in the dropdown, choose the page as per requirement.
3. The **Readonly** toggle is enabled by default. To allow users to edit, disable the toggle.
4. Click the **Save** button.
