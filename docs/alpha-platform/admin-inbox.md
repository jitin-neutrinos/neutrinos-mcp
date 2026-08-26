# Types

<https://documentation.neutrinos.com/articles/#!alpha-platform/admin-inbox>

The Admin Inbox is similar to a standard user inbox but includes additional features that enable administrators to effectively manage and coordinate cases and tasks assigned to team members, as well as monitor their progress.

## Types

The Inbox in the Admin UI includes various types, each designed to serve specific capabilities, reflecting their usage and scope.

1. **Tasks**: This inbox type displays all the cases linked with the project. The image below illustrates **Tasks** inbox showcasing all the tasks for a particular project:
    ![admin-tasks-inbox](/resources/Storage/alpha-platform/images/admin-tasks-inbox-fullscreen.png)
2. **Signals**: In a deployed BPM diagram, when a process reaches a Signal Node, it pauses and waits for a specific signal to proceed. The **Signals** list displays all the signals received in the workflow, enabling administrators to identify which signals are valid for triggering. For instance, a process might pause at a Signal Node, say, waiting for an 'Approval Granted' signal. The Alpha Admin can manually trigger this signal to approve the task, allowing the process to resume to the next step. The image below illustrates the **Signal** inbox in Admin UI Workbench.
    ![admin-ui-signal-inbox](/resources/Storage/alpha-platform/images/adminui-signal-inbox.png)
    **Steps to Send Signal**: Follow the below steps to **Send Signal**(s):
    ![admin-ui-send-signal-gif](/resources/Storage/alpha-platform/images/adminui-send-signal-gif.gif)
    ![Note](/resources/Storage/alpha-platform/note.png)
    The Admin can send **Signals** either individually or in bulk.
  1. In the **Signal **inbox, select the signal(s) that needs to be sent.
  2. Click the **Send Signal** button.
  3. In the prompt screen, add the variable(s), if required, in JSON format as specified in the BPM workflow. Click the **Send Signal** button to send the signal and complete the process.
3. **Re-attempt Inbox**: The Re-attempt Inbox in the Admin UI of Neutrinos Alpha Workbench is designed to manage failed or incomplete tasks. Based on business requirements, specific tasks can be configured to appear as 'Re-attempt.' This scenario enables an admin to restart the process from the exact node where it previously failed. The image below illustrates a Re-attempt inbox in Admin UI Workbench.
    ![Admin-UI Re-attempt inbox](/resources/Storage/alpha-platform/images/adminui-re-attempt-inbox.png)
    **Steps to Re-attempt a task**: Follow the below steps to Re-attempt task(s):
    ![Re-attempt-process](/resources/Storage/alpha-platform/images/adminui-re-attempt-gif.gif)
    ![Note](/resources/Storage/alpha-platform/note.png)
    The Admin can **Re-attempt** tasks either individually or in bulk.
  1. In the **Re-attempt **inbox, select the task(s) which needs to be re-attempted.
  2. Click the **Re-attempt** button
  3. In the prompt screen, click the **Re-attempt** button to complete the Re-attempt process.
