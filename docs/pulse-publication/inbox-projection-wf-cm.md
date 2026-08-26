# Use Case

<https://documentation.neutrinos.com/articles/#!pulse-publication/inbox-projection-wf-cm>

In versions earlier than 25.12-24.0.0.0-current (current channel, Trinity Asset Version 1.0.6) and 25.12.12.0.0-lts (LTS channel), the Inbox retrieved the complete case data. This behavior introduced significant data retrieval overhead and could negatively impact platform performance.

To optimize platform performance, the Inbox Projection feature is introduced to minimize the load on the platform during data retrieval. With this feature, only the required keys needed for display in the Inbox are fetched based on the configured inbox columns. Any additional keys required for processing or use in custom code can be **explicitly **configured in the inbox trigger.

## Use Case

To illustrate the Inbox Projection feature, consider a scenario where a row in the inbox needs to be highlighted for cases that have been assigned but have not received any action for a particular CustomerType. In this example, assume that the configured columns display only CaseID, CaseStatus, TaskStatus, and CustomerName. This means that only these keys are directly accessible from the custom code.

As part of optimization, only the data (keys) corresponding to the configured columns are sent to the inbox. However, in this scenario, the CustomerType key is also required to determine whether any action has been taken for a specific type of customer. Since the CustomerType key is not part of the configured columns, it is not directly accessible from the custom code

## Add Additional Keys

To handle such situations, the CustomerType field can be explicitly specified in the inbox trigger under the custom code section. This ensures that the required key is fetched from the case data and made available to the custom logic for processing.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | All case and task instances are directly accessible from the custom code. However, if a key or field is of type CO, it must be **explicitly **specified as part of the Inbox Projection to make it accessible within the custom code. |
| --- | --- |

### Example

In the example below, a CO field named “email”, which is not mapped in the inbox, is used in the custom code. This field is explicitly mapped as part of the inbox projection so that it can be accessed in the custom code. The field is then displayed in the alert when the user clicks on the group tasks.



![alpha-inbox-projection](/resources/Storage/pulse-publication/images/alpha-inbox-projection.gif)
