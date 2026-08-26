# Creating Data Models

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-leave-management-system/designing-data-models>

A **Data Model** identifies the data, the data attributes, and the relationships or associations with other data. It enables you to:

- Understand how to design your database
- Structure and organize the data

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | Designing data models using Neutrinos Data Model editor will give you the advantage of using the Data Model API's directly from the **HTML **templates on events. This is possible because all the Data Model operations ( such as get(), put(), getId(), etc.) gets auto-generated during the page creation and are available within themselves. |
| --- | --- |

### Creating Data Models

1. To create a Data Model, click the **Add** button from the menu list and select **Data Model**. Data Model dialog box appears. ![Add data model](/resources/Storage/tutorial-create-a-leave-management-system/adddatamodel.png)
2. You can **add** a new data model or** Import** a data model.
3. To add a new data model, select New in the data model dialog box and configure the following:
  - **Data Model**: Name of the data model
  - **Description**: A short description of the data model
  - **Data Source**: Name to the database where the data resides.
  - ![Creating a new datamodel](/resources/Storage/tutorial-create-a-leave-management-system/datamodel3.png)
4. To import a data model, select Clone and configure the following:
  - **Select App**: Select an existing app in the workspace where the required data model resides.
  - **Select Data Model**: Select the name of the data model which is to be imported.
  - ![Importing a data model](/resources/Storage/tutorial-create-a-leave-management-system/datamodel4.png)

### Data Models for LMS

For the LMS app, you need to create the following data models:

- **Simple**: staff, leaves, leave request
- **complex**: employee

**Staff**

This data model captures information about the staff of the organization.

- department captures the department to which the employee/manager belongs to.
- employeeID captures a fictional ID of the employee/manager.
- managerName captures the manager name of the employee.
- groupList is the same as what was captured in the Neutrinos Console.

| **Name ** | **Type** | **IsArray** |
| --- | --- | --- |
| groupList | string | true |
| firstName | string | false |
| lastName | string | false |
| employeeID | string | false |
| username | string | false |
| displayName | string | false |
| department | string | false |
| managerName | string | false |

**Leaves**

This data model captures the leave information of an employee.

- **annualLeaves **captures the number of annual leaves applied
- **sickLeaves **captures the number of sick leaves applied
- **approvedLeaves ** captures the total number of leaves approved by the Manager

**Name**


 **Type**


 **IsArray**







 annualLeaves



 number


 false





 sickLeaves



 number


 false





 `approvedLeaves`



 number


 false






 **LeaveRequest**

This data model captures the leave requests. It has a mapping between the **Employee** and the **Manager** attributes**. **

- leaveType captures the type of leave (sick or annual) the employee is applying.
- fromDate and toDate capture the duration of the leave request.
- leaveStatus captures leave status*. *
- managerName to whom the leave is applied for approval.
- username of the user applying for leave.
- leaveReason to capture the reason for the leave request.

| **Name** | **Type ** | **IsArray** |
| --- | --- | --- |
| _id | string | false |
| leaveType | string | false |
| fromDate | Date | false |
| toDate | Date | false |
| duration | number | false |
| leaveStatus | string | false |
| userName | string | false |
| fullName | string | false |
| managerName | string | false |
| leaveReason | string | false |

**Employee**

The employee data model captures both the basic information of the employee as being the staff of the organization and the leave information.

| **Name** | **Type** | **IsArray** |
| --- | --- | --- |
| staff | MODEL(staff) | false |
| leaves | MODEL(leaves) | false |

| ![Information](/resources/Storage/tutorial-create-a-leave-management-system/info.png) | All the Data Models created above can be accessed in the code using the **dm** object. |
| --- | --- |
