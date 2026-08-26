# Activity

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/logs>

The Reels Platform provides logging capabilities to track activities, audits, and executions.

- **Activity** Logging tracks user logins and logouts.
- **Audit** records the creation and updates of Rules, Rule Groups, Workflows, and Master Data.
- **Rules Execution** tracks the execution of Rules, Rule Groups, and Workflows.

## Activity

Displays user login and logout activity on the Reels Platform. This section includes details such as Execution Timestamp, User, Action Type, Status, and Duration (min.).




 ![logs-activity-tab](/resources/Storage/neutrinos-reels-publication/images/logs-activity-tab.png)

- **Execution Timestamp**: Contains the timestamp of the user's login or logout event.
- **User**: Contains the user ID of the user who logged in or logged out.
- **Action Type**: Indicates whether the event was a login or logout.
- **Status**: Indicates whether the login or logout event was successful.
- **Duration**: Indicates the duration for which the user remained logged in.

Use the search bar in this tab to find activities.




 ![logs-activity-tab-searchbar](/resources/Storage/neutrinos-reels-publication/images/logs-activity-tab-searchbar.png)

Additionally, you can filter the displayed information using the filter option available in this tab. The filter allows you to refine records by date and time, with a selectable date range from the current day to one year and a time duration ranging from 15 minutes to 24 hours.




 ![logs-activity-tab-filter](/resources/Storage/neutrinos-reels-publication/images/logs-activity-tab-filter.png)

## Audit

Displays details related to the creation and updates of Rules, Rule Groups, or Workflows. This section includes information such as Execution Timestamp, Rule ID or Workflow ID, User, Action Type, Release Notes, Status, and Rule Type.




 ![logs-audit-tab](/resources/Storage/neutrinos-reels-publication/images/logs-audit-tab.png)

- **Execution Timestamp**: Contains the timestamp of the creation or update of a Rule, Rule Group, Workflow, or Master Data.
- **Rule ID/ Workflow ID**: Specifies the ID of the executed Rule or Workflow.
- **User**: Contains the user ID of the person who executed the Rule or Workflow.
- **Action Type**: Specifies whether the event was the creation or update of a Rule or Workflow.
- **Release Notes**: Contains the release notes provided when the Rule or Workflow was published.
- **Status**: Contains the execution status of the Rule or Workflow, indicating whether it was successful or not.
- **Rule Type**: Specifies the type of Rule that was created or updated.

Use the search bar in this tab to find specific information in the audit.




 ![logs-audit-tab-searchbar](/resources/Storage/neutrinos-reels-publication/images/logs-audit-tab-searchbar.png)

Additionally, you can filter the displayed information using the filter option available in this tab. The filter allows you to refine records by date and time, with a selectable date range from the current day to one year and a time duration ranging from 15 minutes to 24 hours.




 ![logs-audit-tab-filter](/resources/Storage/neutrinos-reels-publication/images/logs-audit-tab-filter.png)

## Rules Execution

This section displays details related to the execution of Rules, Rule Groups, or Workflows. It includes information such as the Execution Timestamp, Name, Rule or Workflow ID, Deployment ID, Release Notes, Type, Status, User/Token, Input Parameters, and Output Result.




 ![logs-rules-execution-tab](/resources/Storage/neutrinos-reels-publication/images/logs-rules-execution-tab1.png)

- **Execution Timestamp**: Contains the timestamp of the execution of a Rule, Rule Group, Workflow, or Master Data.
- **Name**: Specifies the name of a Rule, Rule Group, Workflow, or Master Data entity that is executed.
- **Rule ID/ Workflow ID**: Specifies the ID of the executed Rule or Workflow.
- **Deployment ID**: Specifies the deployment ID for the Rule, Rule Group, Workflow, or Master Data.
- **Release Notes**: Contains the release notes from the most recent publication of the Rule, Rule Group, Workflow, or Master Data.
- **Type**: Specifies the type of the executed rule.
- **Status**: Contains the execution status of the Rule or Workflow, indicating whether it was successful or not.
- **User/Token**: Contains the user ID or the token of the person who executed the Rule or Workflow.
- **Input Parameters**: Lists the input parameters provided to the Rule during execution.
- **Output Result**: Contains the output result of the executed rule or workflow.
- **Error Message**: Displays error messages that occurred during the execution of the Rule or Workflow.
- **Execution Duration**: Displays the time taken for the Rule or Workflow to execute.
- **Version**: Displays the version of the executed Rule or Workflow.

Use the search bar in this tab to find specific information in the Rules Execution tab.




 ![logs-rules-execution-searchbar](/resources/Storage/neutrinos-reels-publication/images/logs-rules-execution-searchbar1.png)

Additionally, you can filter the displayed information using the filter option available in this tab. The filter allows you to refine records by date and time, with a selectable date range from the current day to one year and a time duration ranging from 15 minutes to 24 hours.




 ![logs-rule-execution-filter](/resources/Storage/neutrinos-reels-publication/images/logs-rule-execution-filter.png)

[Next Topic](/articles/neutrinos-reels-publication/content-repository)

[Previous Topic](/articles/neutrinos-reels-publication/assets-api)
