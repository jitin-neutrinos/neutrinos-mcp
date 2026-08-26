# Human Tasks and Task States

<https://documentation.neutrinos.com/articles/#!pulse-publication/case-assignments-and-task-states-wb-cm>

In the Neutrinos Alpha Workbench, Case assignment and Task States play an important role in efficiently managing business processes.

Cases can be assigned to a user by an Admin, Manager, or Task Distributor. Alternatively, users can self-assign cases from the **Group Tasks** inbox using the **Case** **Checkout** feature. Case Checkout refers to the process of temporarily assigning a case to a user when they access or interact with it. Once the user clicks back or closes the case, it is checked back into the **Group Tasks** inbox, making it available for further processing or for other users to claim. This ensures streamlined task ownership, accountability, and seamless transitions within automated workflows.

| ![Note](/resources/Storage/pulse-publication/note.png) | If the user closes the browser while the case is open, the case becomes locked under the user's name and remains in their "My Tasks" inbox. Also, Case **Checkout **is applicable only for **Group Tasks**. For cases in My Tasks and Team Tasks inboxes, the cases are already assigned to specific users. |
| --- | --- |

The GIF below demonstrates the process of case checkout, where a case is assigned to a user from the Group Tasks inbox upon interaction. The case is then reflected in the user's My Tasks inbox.

![Case Checkout Gif](/resources/Storage/pulse-publication/images/case-check-out-gif.gif)

For more information on Task Allocation, see [Task Allocation](/articles/pulse-publication/task-allocation-wb-cm) topic.

The GIF below illustrates the case check-in process. When a user navigates back or closes a case that was previously assigned to them through the checkout process, the case is returned to the **Group Tasks** inbox, making it available for reassignment.

![Case check in GIF](/resources/Storage/pulse-publication/images/case-check-in-gif.gif)

## Human Tasks and Task States

**Human Tasks** in the Neutrinos Alpha Platform represent activities that require human intervention within a business process. These tasks are essential for workflows where automated actions alone cannot address certain requirements, such as decision-making, approvals, data validation.

Human tasks in business processes are represented and defined using BPMN 2.0 standards. They are seamlessly integrated into process flows requiring human intervention and play an important role in advancing a case to its completion. Each case instance created within the process contains these human tasks as part of its workflow.

A Human Task instance is referenced from the Workbench and retrieves the associated pages. These pages provide access to Case Data, Process Information, User Session Information, and third-party integrations. Both the Case and Process are marked as in-progress while a Human Task is active. Task variables are used to capture output values from completed tasks.

The input and output task variables of human tasks influence decision-making within the business process, ensuring workflow progression.

## Task Pages

Data to or from the task variables can be provided through forms configured by developers at design time. These forms are retrieved in the workbench when a user accesses a task and are referred to as **Task Pages**. A Task Page displays information from data sources like Case Data that contain relevant data about Case Instance, Integration Layer that are accessed through APIs, DMS that contain documents and associated metadata, CMS that holds content and the Rëels Master Data. Additionally, Task Pages can leverage components available in the **Marketplace** to enhance functionality and user experience. These components enable further customization and integration capabilities, supporting dynamic and interactive task execution.

The below image illustrates a sample Task Page created to display user related information.

![Sample Task Page](/resources/Storage/pulse-publication/images/sample-task-page.png)

For more information on Task Pages, see [Layouts, Categories and Forms](/articles/pulse-publication/layouts-categories-and-forms-wb-cm) topic.

## Task States

Task States represent various states that a Human Task can go through in its lifecycle from its initiation to its completion. The image below is a flowchart that highlights possible states through which a Human Task goes through its lifetime.

![Task States Flowchart](/resources/Storage/pulse-publication/images/taskstates.jpg)

When a task is **Created**, it automatically transitions to the **Ready** state. Upon assignment to a specific group, the task's state changes from **Ready** to **Reserved**. If a user checks out the task, it enters the **In Progress** state. Conversely, when the user checks in the task, it reverts to the **Reserved** state. After the task is successfully completed, it transitions to the **Completed** state. However, if an exception occurs preventing completion, the task moves to the **Failed** state.

## Decision Making

Decision-making for tasks is a key function of task execution within business processes. Tasks are designed to facilitate efficient decision-making by providing the necessary context to the users. These decisions are enabled and executed based on the type of task and the associated business process workflow logic.

In Neutrinos Alpha, decisions for Human Tasks are made manually by users interacting with the task. The **Task Page** serves as the user interface, providing task-specific information, enabling data evaluation, and supporting decision-making actions.

These decisions are influenced by task variables passed to the business process, which can be mapped to process variables as task outputs, enabling dynamic manipulation of the business process control flow.

By combining automated decisions with user-driven actions, the data-driven decision-making ensures tasks progresses efficiently and align with the organization's business processes and objectives.
