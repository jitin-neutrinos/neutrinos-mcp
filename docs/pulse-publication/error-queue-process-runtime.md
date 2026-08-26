# Interface

<https://documentation.neutrinos.com/articles/#!pulse-publication/error-queue-process-runtime>

The Error Queue page lists all errors encountered during process execution. These errors can occur for various reasons, such as invalid or mismatched input provided in a user task, SLA violations, or other runtime exceptions.

## Interface

![up-process-runtime-error-queue](/resources/Storage/pulse-publication/images/up-process-runtime-error-queue.png)

- Selection: Allows you to select one or more errors to retry or terminate the corresponding process instances.
- Process ID: Displays the unique ID of the process definition associated with the error.
- Process: Displays the name of the process associated with the error.
- Error: Displays the error message generated during process execution.
- Date and Time: Displays the date and time when the error occurred.
- Actions: Contains a kebab menu that provides an option to retry the execution of the process instance in which the error occurred.

Additionally, you can use the Search bar to search for a specific error or process. The Show by drop-down list allows you to specify the number of rows displayed in the table, while the pagination controls allow you to navigate between multiple pages of errors.

To know more about how to configure the error queue, refer [Error Queue](/articles/pulse-publication/error-queue) topic.
