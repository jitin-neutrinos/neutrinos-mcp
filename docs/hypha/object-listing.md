# Interface

<https://documentation.neutrinos.com/articles/#!hypha/object-listing>

The Object Listing is an interactive view that displays all objects associated with a specific project in a structured, tabular format. Each object in the listing represents a discrete data entity, such as a schema object.

This feature enables users to view and act upon multiple data objects efficiently within an interface.

The interface contains the following, as illustrated below:




 ![hypha-objects-landing-page](/resources/Storage/hypha/images/hypha-objects-landing-page.png)

## Interface

- The left navigation panel displays a list of objects associated with the selected project. The dropdown menu at the top shows the currently active project from the list of all available schemas on the platform. When a project is selected, the corresponding objects under that project are automatically populated in the navigation panel.
- The right-hand section of the page presents the selected object in a column-based layout, with each column representing a field.
- When an object is selected, the page displays the data rows(records) containing discrete values for each field defined within that object.
- You can use the filter option located at the top of the table to refine the displayed data. Additionally, you can refresh the table data by clicking the Refresh button located next to the Customize Table button at the top of the table.
    ![hypha-objects-landing-page-filter-option](/resources/Storage/hypha/images/hypha-objects-landing-page-filter-option.png)
- To add a new record to the selected object, click the Add [Object Name] button (for example, Add Lead) located at the top of the page.
    ![hypha-objects-landing-page-add-new-record-current-obj](/resources/Storage/hypha/images/hypha-objects-landing-page-add-new-record-current-obj.png)
- Additionally, you can set the number of rows (data records) displayed on the page, and navigate between pages using the pagination controls located at the bottom of the page.
    ![hypha-objects-landing-page-rows-navigation-options](/resources/Storage/hypha/images/hypha-objects-landing-page-rows-navigation-options.png)
- You can switch between projects using the drop-down menu that displays the current project name, located at the top-left corner of the page above the object list. Selecting a different project from the list loads the objects associated with the selected project.
    ![hypha-objects-landing-page-switch-project](/resources/Storage/hypha/images/hypha-objects-landing-page-switch-project.png)
- Object information is organized into tabs, with each tab displaying information relevant to a specific category. For example, in the illustrative screenshot above, the available tabs include Records, Tasks, My Leads, and others. Some tabs may be hidden by default. To view additional tabs, click the More button next to the last visible tab and select the required tab from the list.
    ![hypha-objects-landing-page-more-tabs-button](/resources/Storage/hypha/images/hypha-objects-landing-page-more-tabs-button.png)

## Object Task Relationship

In Hypha, an object–task relationship defines how a business object (the entity) is linked to one or more tasks (units of work or actions) that operate on or are triggered by that object. This relationship establishes context between entity and workflow, enabling the platform to manage processes in a structured, traceable, and state-driven manner.

### Objects and Tasks

An object represents a persistent business entity in the system, such as a Case, Claim, Policy, Customer, or Ticket. Objects store structured data, metadata, and lifecycle information, and act as the primary source for business operations.

A task represents an actionable unit of work associated with an object. Tasks can be:

- Human tasks (for example, review, approval, validation).
- System or automated tasks (for example, API calls, rule execution, notifications).

Tasks typically have attributes such as status, priority, owner, SLA, and due dates.

### Example Scenario

In the insurance claims domain:

- **Object**: Claim
- **Tasks**: Document Verification, Field Investigation, Approval

When a Claim object is created, the workflow engine generates tasks associated with that specific claim instance. Each task can access claim details (such as claim amount or policy type), update the object upon completion, and trigger subsequent tasks based on predefined rules.

The Tasks tab provides the interface for viewing object-related tasks. Task information is displayed in a tabular format with columns such as **Task ID**, **Lead ID** *(indicating the object record associated with the task)*, **Lead Name**, **Request Type**, **Description**, **Current Value**, **Requested Value**, **Priority**, and **Task Status** *(for example, In Review or Approved)*, as illustrated by the image below:




 ![hypha-objects-tasks-relationship](/resources/Storage/hypha/images/hypha-objects-tasks-relationship.png)

## Add Object Record

An object in Hypha represents a structured business entity (for example, Claim, Customer, Policy, or Case). Add Record is the fundamental operation used to insert a new row to the object, populated with values that conform to the object definition.

### Add Record

To add a new record to a specific object, follow these steps:

1. From the left navigation panel, navigate to the object to which you want to add a record.
    ![hypha-objects-new-record-landing-page](/resources/Storage/hypha/images/hypha-objects-new-record-landing-page.png)
2. On the Objects page, click the Add [Object] button located in the top-right corner of the page. In this illustration, the button is labeled Add Lead.
    ![hypha-objects-new-record-add-button](/resources/Storage/hypha/images/hypha-objects-new-record-add-button.png)
3. Entering values for all required fields of the object.
    ![hypha-objects-add-record-page](/resources/Storage/hypha/images/hypha-objects-add-record-page.png)
4. Click Save at the bottom of the page to add the record to the selected object successfully.
   ![hypha-objects-add-record-page-save-button](/resources/Storage/hypha/images/hypha-objects-add-record-page-save-button.png)
