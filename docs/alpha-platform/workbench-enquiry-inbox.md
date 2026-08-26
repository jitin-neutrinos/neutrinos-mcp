# Enquiry Inbox Filters

<https://documentation.neutrinos.com/articles/#!alpha-platform/workbench-enquiry-inbox>

The **Enquiry Inbox** is an interface for managing and responding to enquiries effectively. It functions as a hub, allowing users to view, track, and act on queries or requests submitted by internal or external stakeholders.

The Enquiry Inbox enables to handle a wide range of enquiries with emphasis on versatility, enabling users to address ad-hoc or dynamic enquiries, which is why the Enquiry Inbox is not task-specific.

| ![Note](/resources/Storage/alpha-platform/note.png) | By default, the Enquiry inbox does not fetch or show any information. |
| --- | --- |

## Enquiry Inbox Filters

Since the **Enquiry Inbox** is not task-specific, filters play a crucial role in retrieving the required information efficiently. The Enquiry Inbox supports a variety of filters to help users refine and locate enquiries based on specific criteria. These filters include, but are not limited to:

- **Text Search**: Perform a text-based search for case or task-related information, including attributes such as caseStatus, taskName, taskStatus, taskDescription, taskSubject, taskOwner, Enumerable List and others.
- **Date Range**: Perform a date range-based search on case or task-related attributes, such as caseCreatedAt, caseLastUpdatedAt, taskCreatedOn, and others.
- **Number Range**: Perform numeric-based search on case or task-related attributes such as cid, taskId, piid, and others.

| ![Note](/resources/Storage/alpha-platform/note.png) | The default structure that can be mapped and searched are Case Instance and Task Instance. |
| --- | --- |

The following is a list of core case and task properties that can be used for filter operations in the Enquiry Inbox:

| **Attributes** | **Description** |
| --- | --- |
| **  Core Case Properties  ** |  |
| cid | **Case Instance ID**: A unique numeric identifier for the case, used to distinguish it from other instances.    For example: 9569 |
| piid | **Process Instance ID**: A numeric identifier that references the associated process instance.    For example: 2384 |
| case_last_updated_at | **Last Case Update Timestamp**: The timestamp of the most recent update to the case, represented in ISO 8601 datetime format.    Format: YYYY-MM-DDTHH:mm:ss.sssZ.    For example: "2024-12-10T07:59:03.591Z" |
| status | **Current Case Status**: Indicates the present status of the case.    For example: "New Case" |
| cdid | **Case Data ID**: A numeric identifier referencing the associated case data.    For example: 237 |
| Case Data Object | **Nested Case Data**: Contains detailed information about the case and is structured under the **caseData **attribute.     **cidid**: A numeric identifier referencing the parent case ID.    **data**: A flexible JSON object containing case-specific data.    **created_at**: The timestamp indicating when the case was created, represented in ISO 8601 format.    **updated_at**: The timestamp of the last modification made to the case, represented in ISO 8601 format. |
| **  Core Task Properties  ** |  |
| taskId | A unique numeric identifier for the task. |
| taskName | The name of the task, represented as a string value. |
| taskStatus | Indicates the present status of the task.    For example: "RESERVED" |
| currentProcessInstanceId | A numeric field that references the current process instance. |
| parentProcessInstanceId | A numeric field that references the parent process instance. |
| Task Metadata | Nested under metadata, contains additional task information:     **containerId**: The container identifier associated with the task, represented as a string value.    **taskSubject**: The subject line of the task, represented as a string value.    **taskDescription**:A detailed description of the task, represented as a string value.    **taskOwner**: The email address of the task owner, represented as a string value.    **createdOn**: The timestamp when the task was created, represented in ISO 8601 format.    **potOwners**: The potential owners of the task, represented as a string value.    **taskDelegatedTime**: The timestamp when the task was delegated, represented in ISO 8601 format.    **groups**: An array of group objects, each containing priority levels. |

| ![Note](/resources/Storage/alpha-platform/note.png) | The queries applied use an AND operation, meaning that all conditions must be true for the filter to return results. For example, if the filter is applied with status="New Case" and priority = "High", the results will only show cases that meet both conditions simultaneously. |
| --- | --- |

The GIF below demonstrates the process of applying filters in the Enquiry Inbox to retrieve information. In this example, filters are applied to locate cases with **CID**s ranging from 9500 to 10000 **AND **a **Case Status** of “New”.

![Enquiry inbox applying filter](/resources/Storage/alpha-platform/images/enquiryinbox-filter.gif)

In addition to the above mentioned filters, you can apply a **text search** filter to retrieve information related to cases or task using either full or partial text matches. For instance, you can search for cases based on the assignee's name. The image below demonstrates how to search for cases assigned to a specific individual using a full-text search.

![Full text search - Enquiry inbox](/resources/Storage/alpha-platform/images/full-text-search-enquiry.png)

To perform a partial text search, use the mod (%) operator along with the desired text as the search criteria. The image below demonstrates how to search for a case using a partial text search.

![Partial text search - Enquiry Inbox](/resources/Storage/alpha-platform/images/partial-text-search-enquiry.png)

| ![Note](/resources/Storage/alpha-platform/note.png) | The **text search** filter is an additional filter option that can be added in Workflow Studio, in the similar way how other filters are added. |
| --- | --- |

The mod (%) operator in filter can be used to perform partial text search in ways as detailed below:

| **Pattern** | **Description** |
| --- | --- |
| %value% | To represent a pattern where there can be any number of characters before and after a specified value,    For example: %name% |
| val%ue% | To represent a pattern that starts with a specific value, followed by any number of characters before and after the search pattern.    For example: nam%e% |
| %val%ue | To represent a pattern that ends with a specific value, with any number of characters before or after the search pattern.  For example: %nam%e |

| ![Note](/resources/Storage/alpha-platform/note.png) | Partial search functionality supports only string data types and does not accommodate numeric partial searches. |
| --- | --- |
