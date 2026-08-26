# Purpose

<https://documentation.neutrinos.com/articles/#!pulse-publication/timer>

A Timer Node is a workflow element within a process definition that introduces time-based behavior into a business process. It instructs the Process Runtime to suspend or delay process execution until a specified temporal condition is met.

When a process instance reaches a Timer Node during execution, the Process Runtime creates a corresponding timer instance and registers it with the Timer service. Once the configured trigger condition is satisfied, the timer is activated and the process resumes execution along the defined workflow path.

## Purpose

A Timer Node allows a process to:

- Pause execution for a specified duration
- Wait until a specific date and time
- Schedule future process activities

## Interface

![up-process-runtime-process-instance-timer-submodule](/resources/Storage/pulse-publication/images/up-process-runtime-process-instance-timer-submodule.png)

- **Name**: Displays the name of the timer used in the process instance.
- **Version**: Displays the version of the process instance.
- **Periodic**: Displays the duration for which the timer remains active during the execution of the process instance.
- **Deployment**: Displays the deployment type of the process definition. The deployment type can be Default for manually deployed processes or automatic for processes deployed through a Timer Start node.
- **Status**: Displays the current status of the timer associated with the process instance.
- **Last Updated**: Displays the date and time when the timer was last updated.
- **Actions**: This column contains a kebab icon that opens a context menu with options to Edit the timer, Pause the timer, or View the associated process.
