# Purpose

<https://documentation.neutrinos.com/articles/#!pulse-publication/process-runtime>

A process instance is the runtime execution of a deployed process definition. It represents a single execution of a business process initiated to fulfill a specific business request or transaction. Each process instance maintains its own execution state, business data, task assignments, audit history, and interactions with other platform services throughout its lifecycle.

While the process definition describes what should happen, the process instance records what is happening for a particular business transaction.

## Purpose

A process instance provides the runtime context required to:

- Execute workflow logic
- Store process-specific data
- Coordinate human and automated activities
- Invoke business rules
- Maintain execution history
- Track progress
- Handle exceptions
- Integrate with external systems
- Support auditing and reporting

## Characteristics

1. Instance Metadata: Each process instance contains runtime metadata, including the Process Instance ID, Process Name, Process Version, and current Status.
2. Process Variables: Each process instance maintains its own set of runtime variables. These variables are local to the instance, updated throughout process execution, used in rules and conditions, and passed to services as required.
3. Integration with Case Management: A process instance can create or update a case, participate in an existing case, or be launched by a case.

## Interface

![up-process-runtime-landing-page](/resources/Storage/pulse-publication/images/up-process-runtime-landing-page1.png)

The Process Runtime module consists of the following submodules: Process Definitions, Process Instances, Timers, Tasks, Migration, Error Queue, and Logs.

- Process Definitions: Lists all process definitions that have been created using the Process Designer and deployed to the platform.
- Process Instances: Displays all process instances that have started execution and are in the Active, Aborted, Completed, Pending, or Suspended state. You can also start a new process instance from this submodule.
- Timers: Lists all processes configured with a Timer Start node that automatically initiates process execution when the configured timer elapses.
- Tasks: Lists all process instances that include one or more user tasks in their execution flow.
- Migration: Enables you to configure the migration of process instances from one process version to another. The migration configuration includes mapping the source process to the target process version, along with the mapping of process variables, nodes, and other runtime elements required for a successful migration.
- Error Queue: This submodule displays errors encountered during process execution that caused process instances to be aborted or suspended. From this submodule, you can export error reports and retry one or more failed process instances.
- Logs: This submodule displays transaction details related to process execution. It is organized into two tabs: Archival/Retention and Audits. The Archival/Retention tab provides information about process archival and retention, while the Audits tab displays the audit logs for process execution.
