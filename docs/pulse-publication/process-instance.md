# Interface

<https://documentation.neutrinos.com/articles/#!pulse-publication/process-instance>

The Process Instances page displays a tabular list of all process instances along with their execution details. It includes instances in the Active, Aborted, Completed, Pending, and Suspended states.

## Interface

![up-process-runtime-process-instance-landing](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-landing.png)

- **ID**: Displays the unique Process Instance ID assigned to the process instance.
- **Name**: Displays the name of the process definition associated with the process instance.
- **Description**: Displays the description of the process definition associated with the process instance.
- **Version**: Displays the version of the process definition for which the process instance was created.
- **Last Updated**: Displays the date and time when the process instance was last updated.
- **Status**: Displays the current status of the process instance. The possible statuses are Active, Aborted, Completed, Pending, and Suspended.
- **Actions**: This column contains a kebab icon that opens a context menu with options to Signal or Abort the selected process instance.

Additionally, you can use the Search bar to search for a specific process instance. The Show by drop-down list allows you to specify the number of rows displayed in the table, while the pagination controls allow you to navigate between multiple pages of process instances.




 Additionally, the Filter option allows you to filter process instances by State, Name, Instance ID, Definition ID, Last Updated, and Start Timer, making it easier to locate specific process instances.

## Start Process

The Process Instances page also provides an alternative way to start a process instance. To start a process instance for a deployed process definition, follow these steps:

1. In the Process Runtime module, click the Process Instances submodule to open the list of process instances. Then, click Add in the upper-right corner of the page to start a new process instance.
    ![up-process-runtime-process-instance-add](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-add.png)
2. Next, select the required process definition from the Process Definition drop-down list, and then select the corresponding version from the Version drop-down list. If the selected process definition includes a form for capturing input values for process variables, the form is displayed in the Form section. Enter the required values in the available fields.
    ![up-process-runtime-process-instance-select-process-version](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-select-process-version.png)
3. After entering the required details, click Start at the bottom of the page to start the process instance for the selected process definition.
    ![up-process-runtime-process-instance-start](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-start.png)

## Process Instance Details

After a process instance is created, its details page is displayed. You can also open the details page for an existing process instance by selecting it from the Process Instances table.

The process details are organized into the following tabs:

1. Diagram: This tab displays the process diagram for the selected process instance as defined during the process design phase. A sample process diagram is shown below.
    ![up-process-runtime-process-instance-diagram](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-diagram.png)
    Additionally, when enabled, the Execution Count toggle in the upper-right corner of the tab displays the number of execution attempts for each node during process execution. By default, this toggle is disabled.
    ![up-process-runtime-process-instance-diagram-execution-count-enabled](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-diagram-execution-count-enabled.png)
2. Details: This tab displays the runtime details of the process instance, including the Instance ID, Definition ID, Status, Deployed Process Name, Definition Version, SLA Compliance (if configured), and other relevant information. The following image illustrates a sample Details tab for a process instance
   ![up-process-runtime-process-instance-details-tab](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-details-tab.png)
3. Documents: This tab displays the documents uploaded for the process instance, if any. The documents are presented in a tabular format with details such as the Document Name, Format, Size, Created Date and Time, and the available Actions. If no documents are uploaded, then this tab displays an empty table.
   ![up-process-runtime-process-instance-documents-tab](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-documents-tab.png)
4. Process Variables: This tab displays the process variables for the process instance. The variables are listed in a table that includes the Variable Name, Value, and Data Type. If no process variables are defined for the associated process definition, the table is empty.
   ![up-process-runtime-process-instance-process-variables-tab](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-process-variables-tab.png)
5. Logs: This tab displays detailed logs for the selected process instance. The logs are presented in a tabular format and include details such as the Time, Category, Node Type, Node Name, Log Details, Owner, and Status. The following image shows a sample Logs tab.
   ![up-process-runtime-process-instance-logs-tab](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-logs-tab.png)
    Additionally, you can expand an individual log entry by clicking the caret icon at the end of the corresponding row to view the raw metadata associated with that log entry.
   ![up-process-runtime-process-instance-logs-tab-raw-metadata](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-logs-tab-raw-metadata.png)
6. Timer: This tab displays the details of any timer nodes associated with the selected process instance. The information is presented in a tabular format and includes the Timer Name, Type, Schedule, Next Schedule (if applicable), Created At, and Status. If no timer nodes are associated with the process instance, the table is empty.
   ![up-process-runtime-process-instance-timer-tab](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-timer-tab.png)
