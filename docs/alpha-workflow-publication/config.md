# Inbox

<https://documentation.neutrinos.com/articles/#!alpha-workflow-publication/config>

The Configuration Page in Workflow Studio empowers users to customize their Workflow Inbox according to specific needs and preferences.

The configuration page consists of five main sections:

1. **Inbox **- This section allows users to customize how their individual Inbox is organized and displayed, enabling adjustments to the appearance, sorting, and prioritization of tasks and notifications. It is designed to enhance the user's workflow efficiency by tailoring the interface to their specific preferences and operational needs.
2. **Admin Inbox **- The Admin Inbox section offers specialized settings for managing administrative tasks and notifications within the Workflow Studio. This configuration area is designed to streamline the workflow for users with administrative roles by providing options to customize how administrative activities are displayed and handled. The Admin Inbox customization enhances productivity by aligning the application interface with the unique demands of administrative tasks, allowing for better organization and quicker access to critical information.
3. **Enquiry Inbox** - The Enquiry Inbox section is dedicated to configuring the handling of enquiry-related tasks and messages within Workflow Studio. This section allows users to tailor how enquiries are organized, displayed, and managed, ensuring a streamlined process for addressing questions, requests, or feedback.
4. **Environment Variables** - Environment variables in Workflow Studio are essential for managing and configuring workflows. They provide a flexible, centralized, and secure way to handle dynamic configuration settings.
5. **Language** - This feature allows users to specify the language in which they want the workflow environment, including the inbox interface, notifications, and other textual elements, to be displayed. Workflow Studio supports multiple languages to accommodate users from diverse linguistic backgrounds. Users can select their preferred language from the available options to personalize their experience and improve usability.
6. **Holiday Calendar **- This feature allows users to define holidays and non-working days, and specify how these dates influence workflow scheduling and task assignments. By configuring the Holiday Calendar, users can ensure that tasks and deadlines are appropriately adjusted to account for holiday periods, avoiding conflicts and optimizing planning.
7. **Headers** - The Headers section allows users to configure and personalize the header elements of their Workflow Inbox. This configuration area provides options to modify how headers are displayed, including the customization of labels, sorting criteria, and organizational headers.

![](/resources/Storage/alpha-workflow-publication/config/configtab.png)

#### Inbox

In Workflow Studio's Inbox, there are three types of tasks: "My Tasks," "Group Tasks," and "Team Tasks." Here's what each category represents:

**My Tasks**: These are tasks specifically assigned to you as an individual user within the workflow system. "My Tasks" typically include assignments, deadlines, or actions that require your attention and completion. They're personalized to your role and responsibilities within the organization. You can view, manage, and complete these tasks directly from your inbox.**Group Tasks**: Group tasks are assignments or activities that are assigned to a specific group of users within the workflow system. Unlike individual tasks (which are assigned to a single user), group tasks are assigned to a designated team or department. Members of the group can collaborate on these tasks, view updates, and contribute to their completion collectively. Group tasks are useful for projects or workflows that require collaboration among multiple team members.**Team Tasks**: Team tasks are similar to group tasks but typically involve a broader team or department within the organization. These tasks are assigned to entire teams or departments rather than specific groups of users. Team tasks encourage collaboration and coordination among larger groups of employees who share common goals or responsibilities. They facilitate communication, alignment, and teamwork across different functional areas within the organization.The fields within the inbox section are described below:Field
Description
Filter Section
Filter Name - Serves as a label or identifier for each filter applied to the data in the inbox. It helps users understand and organize the filters they have added to narrow down their tasks or cases based on specific criteria.Binding Value - This column displays the field or attribute in the data that the filter will act upon. For example, a filter could be bound to fields like status, cid (case ID), or task status.Filter Type - Filter Type: This column specifies the type of filter being applied, such as String, Number, Date, etc.Action - Action: This column includes action icons, like a trash bin, allowing users to delete filters.Save Filter
Toggle button, use this toggle button to save the current filter settings for future use.
Table Sort
Toggle button use this for enabling or disabling sorting on the table.
Column Selection
Toggle button, indicating the availability of column selection functionality.
Number of Rows
Set the Dropdown menu to the required number(5,10.15 or 20), allowing the user to choose how many rows to display in the table.

##### Columns Configuration

| Field | Description |
| --- | --- |
| Column Label | Descriptive name for the column. |
| Binding Value | Represents the data source that populates the content of each column in the table. It determines what data will be displayed in each respective column. |
| Data Type | Specifies the type of data the column holds (Number, String, Date). |
| Hideable | Checkbox to determine if the column can be hidden. |
| Sort | Checkbox to enable or disable sorting for each column. |
| Action | Trash icon for deleting the column. |

#### Admin Inbox

This feature enables administrators to view, manage, and respond to various tasks, notifications, or requests related to the workflow processes configured within the system. This contains the following sections:

- [Tasks](/articles/alpha-workflow-publication/tasks)
- [Signals](/articles/alpha-workflow-publication/config/a/h5_634797929)

##### Tasks

They represent specific actions or work items that are part of a workflow process. These can include approvals, reviews, data entry tasks, document uploads, or any other action that requires human intervention or decision-making.

The fields within the Tasks section are described below:

| Field | Description |
| --- | --- |
| Tasks | A toggle switch to save the current task settings. |
| Filter | A toggle switch to save the current filter settings. |
| Filter Settings | The filter settings section has the following fields:Filter Name - Contains fields with names such as String and language"Binding Value - Represents the data source that populates the content of each column in the table. Filter Type - Options include "Range," "Multi Select," and "Date Range. For example, "CID" has a "Minimum" range, while "Case Status" and "Task Status" have multi-select options.Action - Trash icons to delete columns. |
| Save Filter | A toggle switch to save the current filter settings. |
| Table Sort | A toggle switch to enable sorting of table columns. |
| Column Selection | A toggle switch to enable column selection. |
| Number of Rows | A drop-down menu to select the number of rows displayed in the table. |
| Column Section | This section allows customization of table columns with the following components:Column label - Contains Text fields with labels like "CID," "Case Status," "Case Created At," "Task Status," and "Task Created At."Binding Value - Represents the data source that populates the content of each column in the table.Data Type - Options include "Number," "String," and "Date."Hideable - Checkboxes to make columns hideable.Sort - Checkboxes to enable sorting.Action - Trash icon to delete columns. |
| Dashboard | This section allows for the creation and management of dashboard cards:Collapsible: A toggle switch to enable collapsible cards.Add Card: A button to add new dashboard cards.Card List : Each card has multiple fields: - Label : Text fields with labels like "New cases" and "Other." - Status - Text fields with labels like "New cases" and "Other." - Icon - Drop-down menus to select icons. - Color: Option to chose Color selectors. - Action - Trash icons to delete cards. |

Signals

They are notifications or alerts generated by the workflow studio to inform administrators or users about specific events, conditions, or exceptions occurring within the workflow processes. Signals can indicate when tasks are overdue, when errors occur, when certain conditions are met, or when manual intervention is required.

| Field | Description |
| --- | --- |
| Signal | A toggle switch to save the current signal settings. |
| Filter | A toggle switch to save the current filter settings. |
| Filter Settings | The filter settings section has the following fields:Filter Name - Contains fields with names such as String and language".Binding Value - Represents the data source that populates the content of each column in the table.Filter Type - Options include "Range," "Multi Select," and "Date Range. For example, "CID" has a "Minimum" range, while "Case Status" and "Task Status" have multi-select options.Action - Trash icons to delete columns. |
| Save Filter | Toggle button, use this toggle button to save the current filter settings for future use. |
| Table Sort | Toggle button use this for enabling or disabling sorting on the table. |
| Column Selection | A toggle switch to enable column selection. |
| Number of Rows | Set the Dropdown menu to the required number(5,10.15 or 20), allowing the user to choose how many rows to display in the table. |
| Column Section | This section allows customization of table columns with the following components:Column Label - Contains Text fields with labels like "CID," "Case Status," "Case Created At," "Task Status," Binding Value - Represents the data source that populates the content of each column in the table.Data Type - Options include "Number," "String," and "Date."Hideable - Checkboxes to make columns hideable.Sort - Checkboxes to enable sorting.Action - Trash icon to delete columns. |
| Add Column | Click to add a column. |
| Dashboard | A toggle switch to enable dashboard. |
| Collapsible | This collapsible section contains the following components:Label - Text fields with labels like "New cases" and "Other."Status - Text fields with statuses like "New Case" and "other."Icon - Drop-down menus to select icons.Color - Option to chose Color selectors.Action - Trash icons to delete cards |
| Add Card | Click to add a card. |

#### Enquiry Inbox

#### 

In Workflow Studio's Enquiry Inbox, there are two sections: "Enquiry Task," and "Pages". Here's what each category represents:

- [Enquiry Tasks](/articles/alpha-workflow-publication/config/a/enqtask)
- [Pages](/articles/alpha-workflow-publication/config/a/pge)

**Enquiry Tasks **The fields within the Enquiry Tasks section are described below.Field
Description
Filter
Use the toggle button to save filter settings.
Filter Name
Serves as a label or identifier for each filter applied to the data in the inbox. It helps users understand and organize the filters they have added to narrow down their tasks or cases based on specific criteria.
Binding Value
This column displays the field or attribute in the data that the filter will act upon.
Filter Type
This column specifies the type of filter being applied, such as String, Number, Date, etc.
Action
This column includes action icons, like a trash bin, allowing users to delete filters.
Save Filter
Use this toggle button to save the current filter settings for future use.
Table Sort
Use this for enabling or disabling sorting on the table.
Column Selection
Indicates the availability of column selection functionality.
Number of Rows
Number of Rows Set the Dropdown menu to the required number(5,10.15 or 20), allowing the user to choose how many rows to display in the table.
Column Section
The following elements are there:Column Label - Descriptive name for the column.Binding Value - Represents the data source that populates the content of each column in the table. It determines what data will be displayed in each respective column.Data Type - Specifies the type of data the column holds (Number, String, Date).Hideable - Hideable Checkbox to determine if the column can be hidden.Sort - Checkbox to enable or disable sorting for each column.Action - Trash icon for deleting the column.Case Summary Download
Section to download case summary.**Pages **Fields available within the pages section are given below.Field
Description
Select Page
The select page drop-down list allows you to search and select a page.

#### Environment Variables

The environment variables section is used to add, modify, and remove environment variables as needed.

The following fields are available within the environment variables section:

Add Variable: By clicking the "+ Add Variable" button, users can add new environment variables, providing a key and possibly other details like value and description.Edit/Delete Variable: The vertical ellipsis icons (⋮) in the Action column suggest that users can perform actions on existing variables, such as editing or deleting them.![](/resources/Storage/alpha-workflow-publication/config/envvaa.png)

#### Language

Users can select their preferred language from a list of available options. Once selected, the user interface elements, such as menus, buttons, labels, and messages, are displayed in the chosen language, making it easier for users to navigate and interact with the system.

![](/resources/Storage/alpha-workflow-publication/config/languages.png)

![](/resources/Storage/alpha-workflow-publication/config/addlang.png)

The fields within the Language section are described below:

| Field | Description |
| --- | --- |
| Add Language | The Add Language option allows users to add new languages to the system. |
| Set Default Language | A dropdown menu at the top allows users to select a language from the available options. |
| Language Name | The name of the language. |
| Language Key | The key used to identify the language. |
| Direction | The text direction, such as Left-to-Right (LTR) or Right-to-Left (RTL). |
| Action | Options to edit or delete a language. |

#### Holiday Calendar

The Holiday Calendar application enables users to manage a list of holidays efficiently. Users can view and organize holiday details, including the date, repetition pattern, occasion, and action options for each entry.

The fields within holiday calendar are described below:

![](/resources/Storage/alpha-workflow-publication/config/holiday.png)

| Field | Description |
| --- | --- |
| Search Bar | Allows users to search for specific holidays within the calendar. |
| Date | Displays the holiday date. |
| Repeat | Shows the days or pattern on which the holiday repeats. |
| Occasion | Displays the holiday name. |
| Action | Contains icons for deleting holidays. |

**Add Holiday**

The "Add Holiday" screen allows you to define and manage your firm's holiday schedule or blackout days, significantly enhancing functionality and user experience in Workflow Manager. By predefining holidays, you can prevent scheduling conflicts, thereby improving scheduling accuracy and efficiency within the Workflow Manager.

![](/resources/Storage/alpha-workflow-publication/config/Addholiday.png)

Field
Description
From
A labeled date input field for the start date of the holiday. By default the current date is displayed. A calendar icon next to the field indicates that users can select a date from a date picker.
To
A labeled date input field for the end date of the holiday.Repeat
The repeat dropdown menu allows users to select the repetition pattern of the holiday. This could include options like daily, weekly, monthly, or specific days of the week.
Occasion
This is the field where users can describe the holiday. The description can be up to 255 characters long.Cancel
Click to cancel.
Add
Click to add the holiday.

**Headers**

The Headers section allows users to configure and personalize the header elements of their Workflow Inbox. This configuration area provides options to modify how headers are displayed, including the customization of labels, sorting criteria, and organizational headers.

![](/resources/Storage/alpha-workflow-publication/config/headerconfig.png)

The fields within the header section are described in the table given below.Field
Description
Label
This field is intended for entering the name or title of the header element that will appear in the Workflow Inbox.
URL
This field is for entering the web address that the header element will link to, providing a direct navigation option.
Select Groups
This dropdown allows the user to specify which user groups the header configuration will apply to.
Add Menu
This option suggests that the user can add additional header elements by clicking on it, facilitating the customization of multiple headers.
Toggle Switch
Use the toggle switch to enable or disable the current header configuration.
Plus icon
Use this icon to add a new header configuration to the menu.
