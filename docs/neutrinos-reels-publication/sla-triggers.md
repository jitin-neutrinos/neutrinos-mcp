# Purpose

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/sla-triggers>

An SLA (Service Level Agreement) triggers defines a time-based condition that monitors and enforces deadlines within a process or a node (task). It ensures that critical business activities are completed within the defined timeframe, thereby maintaining compliance with business commitments or service-level policies.

SLA triggers can be configured at two levels: Process level and Node level. These triggers define when specific actions are executed in relation to the SLA timeline. SLA triggers can be initiated at the following points:

- Before the SLA expires
- At the time of SLA expiry
- After the SLA has expired

### Purpose

- To ensure the entire process completes within the agreed turnaround time (TAT).
- To ensure that each step of the process is completed promptly.
- To identify bottlenecks within a specific node, task, or process.

## Add SLA Triggers

The SLA triggers can be added at

- Process Level
- Node Level

### Process Level SLA

A Process-level SLA Trigger monitors the overall lifecycle of a process instance to ensure that it meets the defined service timelines. To add a Process-level SLA Trigger, follow the steps below:

1. Open an existing process or the process you have created on the platform.
2. In the Details section of the process, you can add new triggers. If any triggers are already configured, they will be displayed in this section.
    ![pulse-process-sla-triggers-1](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-1.png)
3. On the Add Trigger page, provide the following details:
    ![pulse-process-sla-triggers-2](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-2.png)
    For example, the image below shows the SLA Duration, SLA Type, and Priority fields with the values PT1H, Process Level, and High, respectively:
    ![pulse-process-sla-triggers-3](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-3.png)
  - SLA Duration: Specify the time period after which the SLA trigger expires. Provide the value in the ISO time format.
  - SLA Type: This field is prefilled with either Process level or Node level, indicating the level at which the SLA is being configured. This field is non-editable.
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      Note: A Process Level SLA trigger applies to the entire process, while a Node Level SLA trigger applies only to the specific node where it is configured.
  - Priority: Specifies the execution priority for the SLA triggers.
4. Click the Add Trigger button to add the trigger for the API calls and provide the below details.
  1. Set the SLA Timing. This can be configured to trigger before the SLA expires, at the time of SLA expiry, or after the SLA has expired. If Before SLA expiry or After SLA expiry is selected, specify the time offset relative to the SLA at which the API should be triggered. Provide this offset in ISO format.
  2. After setting the timing, click Configure in the Action section to define the trigger action.
      ![pulse-process-sla-triggers-action-configure](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-action-configure.png)
5. On the next screen, enter a name for the trigger and provide a brief description. Then, select the rule, workflow, or the rulegroup to be triggered from the Reels dropdown and choose the appropriate version. Use the search bar within the Rules dropdown to quickly locate a specific rule, rule group, or workflow.
    ![pulse-process-sla-triggers-action-configure-reels-options](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-action-configure-reels-options.png)
6. After selecting the appropriate rule, rule group, or workflow and its corresponding version, click Save at the bottom of the screen to persist the configuration.
    ![pulse-process-sla-triggers-action-configure-reels-options-save](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-action-configure-reels-options-save.png)
7. Finally, click Save on the Add Process SLA page to confirm and apply the SLA trigger configuration for the process.
    ![pulse-process-sla-triggers-action-configure-final-save](/resources/Storage/neutrinos-reels-publication/images/pulse-process-sla-triggers-action-configure-final-save.png)

### Node Level SLA

A node-level SLA defines the expected time constraints for completing a specific node in a process—such as a user task, approval step, or system activity. Unlike process-level SLAs (which track end-to-end completion), node-level SLAs focus on granular performance control, ensuring each step adheres to defined timelines.

1. Open an existing process or the process you have created on the platform.
2. Navigate to the node where you want to configure a node-level SLA. Open the node by double-clicking it. In the SLA Triggers tab, you can add new triggers. Any previously configured triggers are displayed in this section.
    ![pulse-sla-node-level-sla-access-gif](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-node-level-sla-access-gif.gif)
3. Click Add Trigger. On the Add Trigger page, provide the following details:
    ![pulse-sla-node-level-sla-options](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-node-level-sla-options.png)
    For example, the image below shows the SLA Duration, SLA Type, and Priority fields with the values PT1M, Node Level, and Medium, respectively:
    ![pulse-node-sla-triggers-basic](/resources/Storage/neutrinos-reels-publication/images/pulse-node-sla-triggers-basic.png)
  - SLA Duration: Specify the time period after which the SLA trigger expires. Provide the value in the ISO time format.
  - SLA Type: This field is prefilled with either Node level, indicating the level at which the SLA is being configured. This field is non-editable.
      ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
      Note: A Process Level SLA trigger applies to the entire process, while a Node Level SLA trigger applies only to the specific node where it is configured.
  - Priority: Specifies the execution priority for the SLA triggers.
4. Click the Add Trigger button to add the trigger and provide the below details.
  1. Set the SLA Timing. This can be configured to trigger before the SLA expires, at the time of SLA expiry, or after the SLA has expired. If the timing is set to either Before SLA expiry or After SLA expiry, you will be prompted to specify the time interval before or after the SLA at which the API should be triggered.
  2. After configuring the timing, specify whether the SLA should be triggered before or after the expiry by providing the time in ISO format. If the SLA is configured to trigger exactly at expiry, specifying a timing value is not required. Once the timing is defined, proceed to configure the action.
      ![pulse-node-sla-triggers-configure-action](/resources/Storage/neutrinos-reels-publication/images/pulse-node-sla-triggers-configure-action.png)
5. Click the Configure button in the Action section to set up the action to be executed on SLA expiry.
    ![pulse-node-sla-triggers-action-configure-button](/resources/Storage/neutrinos-reels-publication/images/pulse-node-sla-triggers-action-configure-button.png)
6. On the Configure page, enter a name for the trigger and provide a brief description. Then, select the required rule, rule group, or workflow from the available dropdown list. You can use the search bar to locate a specific component. Additionally, apply the filter options on the right side of the page to display only rules, rule groups, or workflows based on your requirement. After selecting the rule, rule group, or workflow, choose the appropriate version and click the Save button at the bottom of the page to save the trigger configuration.
    ![pulse-node-sla-triggers-action-configure-save-button](/resources/Storage/neutrinos-reels-publication/images/pulse-node-sla-triggers-action-configure-save-button.png)
7. Finally, on the SLA page, review all configurations to ensure they meet the requirements, and then click the Save button at the bottom of the page to apply the changes.
    ![pulse-node-sla-triggers-action-configure-final-save-button](/resources/Storage/neutrinos-reels-publication/images/pulse-node-sla-triggers-action-configure-final-save-button.png)

| ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png) | **Note**: You can configure multiple SLA triggers at both the process level and node level by clicking the Add Trigger button below the list of existing triggers. |
| --- | --- |

## Configure SLA Trigger

To configure an SLA trigger for either a process or a node, follow the steps below:

1. Navigate to the process or node for which the SLA needs to be configured.
  - Process-level SLA: Open the required process in the platform, navigate to the Details tab, and click the Add Trigger button to configure the SLA.
  - Node-level SLA: Open the process and locate the required node in the process designer. Double-click the node to open its details, navigate to the SLA Triggers tab, and begin the configuration.
2. Navigate to the Triggers section and click the Add Trigger button. Select the required SLA timing from the dropdown list. If Before SLA Expiry or After SLA Expiry is selected, specify the appropriate duration indicating how long before or after the SLA the trigger should be executed. Then, select the required rule, rule group, or workflow from the subsequent dropdown.
3. Create the required process variables under the Process Details page. These variables will be used to map the variables defined in the Rule, Rule Group, or Workflow selected in the next step.
    Navigate back to the Triggers section and select the required Rule, Rule Group, or Workflow along with the appropriate version. When prompted to map the required process variables to the selected component, choose the corresponding process variables and map them to the variables used in the Rule, Rule Group, or Workflow accordingly.
    In the illustration below, a process-level SLA is configured within a process. In this example, two process variables Age and Status have been created in the variable model.
    ![pulse-sla-illustration-process-variable](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-illustration-process-variable.png)
4. On the Triggers page, in this illustration, the process variables created in the previous step are mapped to the variables defined in the workflow.
    ![pulse-sla-illustration-variable-mapping](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-illustration-variable-mapping.png)
5. Click the Save button at the bottom of the page to save the SLA trigger configuration.
    ![pulse-sla-illustration-variable-mapping-save](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-illustration-variable-mapping-save.png)
6. Finally, on the Triggers page, you can view the configured SLA settings, including the SLA duration, trigger condition, action to be performed upon SLA expiry, and the name of the configured Rule, Rule Group, or Workflow. After verifying the configuration, click the Save button at the bottom of the page to complete the setup.
    ![pulse-sla-illustration-review-and-final-save](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-illustration-review-and-final-save.png)

In this illustration, the SLA trigger is configured to execute upon SLA expiry. If the user task is completed within the specified SLA duration, the task is completed successfully, and the SLA is neither triggered nor expired. However, if the user task is not completed within the defined duration, the SLA is triggered, and the SLA status changes to expired.




 In this example, the user task was not completed before the configured SLA duration. As a result, the SLA was triggered and subsequently marked as expired. This can be verified from the logs available for the process instance.




 To view the logs, navigate to Manage from the navigation bar and select the required process instance from the list of available process instances. Open the process instance and navigate to the Logs tab to view the execution logs. A sample log entry showing the SLA expiry is illustrated in the image below.



![pulse-sla-illustration-sla-trigger-expired](/resources/Storage/neutrinos-reels-publication/images/pulse-sla-illustration-sla-trigger-expired.png)
