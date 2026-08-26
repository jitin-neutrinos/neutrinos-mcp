# Inbox

<https://documentation.neutrinos.com/articles/#!hypha/inbox>

Inbox is a work management interface that displays a consolidated list of actionable items—such as cases, tasks, or process instances - assigned to or accessible by a user based on role, ownership, and workflow state.

The Inbox displays work items in a tabular format, organized into separate tabs based on task categories. Each tab presents a specific set of cases or tasks assigned to a user or group. Within each tab, every row represents an individual case or task, and the columns display key metadata required to identify, prioritize, and take action on items efficiently.




 ![hypha-object-related-objects-inbox](/resources/Storage/hypha/images/hypha-object-related-objects-inbox.png)

- **Controls**:
  - **Filters**: The Filter button allows users to define filter criteria to narrow down inbox items based on attributes such as priority, status, submission type, or SLA.
  - **Task Selector**: The My Task dropdown enables users to switch between different task scopes, such as:
    - Tasks assigned to the current user
    - Tasks assigned to a group or queue
  - **Display Option**:
    - **Show by**: Controls the number of records displayed per page (for example, 5 rows).
    - **Pagination controls**: Allow navigation across multiple pages of inbox records, displaying the current range (for example, 1–15 of 40).
- **Key Columns**: The following columns are illustrated in the image above.:
  - Policy Number: Unique identifier for the business record or case associated with the task.
  - Priority: Indicates the urgency of the task (High, Medium, Low), typically derived from business rules.
  - Priority Score: A numerical representation of priority used for automated ranking and sorting.
  - Submission Type: Specifies the source or channel through which the record was submitted (for example, EPOS, ECOM, PAPER).
  - Status: Represents the current lifecycle state of the task (for example, New Case, Pending Received, Refer, Counter Offer Received).
  - Process SLA: Displays the overall SLA duration defined for completing the task within the process.
  - UW Process SLA: Indicates the underwriting-specific SLA applicable to the task.
  - UW Received Date: The date on which the task or record was received by underwriting.
