# Create Application Alerts

<https://documentation.neutrinos.com/articles/#!trinity-publication/create-application-alerts>

To create alert(s) for application(s), follow the steps below:

1. In the left navigation pane, click Config to open the Alerts page. By default, the Application Alerts page is displayed, showing all alerts triggered for applications, as illustrated in the image below:
    ![trinity-alerts-application-landing-page](/resources/Storage/trinity-publication/images/trinity-alerts-application-landing-page.png)
2. Click the New Alert Config button at the top of the page to begin creating a new alert for the application.
    ![trinity-alerts-create-new-alert](/resources/Storage/trinity-publication/images/trinity-alerts-create-new-alert.png)
3. The Create Alert Configuration page opens, where you can configure the Alert Type, Application Type, and other related settings as described below:
    ![trinity-alerts-application-initial-step](/resources/Storage/trinity-publication/images/trinity-alerts-application-initial-step.png)
  1. Alert Type: Select the type of alert to configure. Alerts can be created for either Application or Storage, depending on the monitoring requirements.
  2. Application Type: Select the deployment method used for the application. Alerts can be created for applications deployed either through Trinity or via manual deployment. Choose Trinity if the application was deployed using Trinity; otherwise, select Others.
  3. If Application is selected as the alert type, you must specify the following details:
      ![Note](/resources/Storage/trinity-publication/project-trailproject/note.png)
      Note: If the application was deployed without using Trinity, the Version dropdown is replaced with Deployment Labels. These labels can be selected from the dropdown list, which supports multi-selection, and are used to identify the application on the cluster.
    1. Environment: Select the desired environment from the dropdown menu containing all available environments.
    2. Project: Select the desired project from the list of available projects within the environment selected.
    3. Application: Select the required application from the list of applications available within the selected project.
    4. Version: Choose the appropriate version corresponding to the selected application to ensure alerts are configured for the correct deployment instance.
4. Once the Alert Type, Application Type, Environment, Project, Application, and Version are selected, click the Next button at the bottom of the screen to proceed to the next step.
    ![trinity-alerts-application-next-button](/resources/Storage/trinity-publication/images/trinity-alerts-application-next-button.png)
5. On the next screen, configure the communication channel through which alerts will be delivered to users. You can choose from the following notification options:
    Both options can be enabled simultaneously.
    ![Note](/resources/Storage/trinity-publication/project-trailproject/note.png)
    Note: Configuring these notification options is optional. In the Post Action step of alert configuration, you can set up an API trigger to execute additional backend tasks based on your requirements.
    ![trinity-alerts-communication-channel-setup](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-setup.png)
    When the Receive Email on Failure option is enabled during communication channel setup, you must specify both the From and To email addresses.
    ![trinity-alerts-communication-channel-from-setup](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-from-setup.png)
  1. Receive an email on failure
  2. Receive a Teams channel notification on failure
  - The Fron dropdown lists all available email IDs that have been pre-configured on the platform.
  - You can search through the list of available email IDs or scroll to select one from the dropdown.
  - The To field requires a valid email ID to be entered manually. Note, multiple email id's can be entered in this field.
  - The Send Success Email checkbox is enabled by default. It triggers an alert when the application becomes live and operational.
  - If you prefer to receive alerts via Microsoft Teams, enable the Receive a Teams Channel Notification on Failure checkbox. You must provide a valid webhook URL associated with the desired Teams channel. To learn how to retrieve the webhook URL for a Teams channel, click the 'i' icon next to the checkbox.
      ![trinity-alerts-communication-channel-teams-webhook](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-teams-webhook.png)
6. In the next step, configure the alert conditions. This includes setting the following parameters:
  - Frequency - Specify how often the system should check (in minutes) for failures after the initial occurrence.
  - Maximum Failure Checks - The number of consecutive checks to verify if the application continues to fail. This counter resets once the application becomes live and operational.
  - Retry Interval - Specify the frequency interval at which the application should be checked to ensure it is functioning properly. For example, if a 6-hour interval is selected, the system will check the application’s status every 6 hours.
  - Application or Pod Status - Enabling this checkbox allows the system to check the application status and determine whether it is functioning as expected. This checkbox is enabled by default.
  - Liveness - Enable this checkbox to validate the response returned by the API endpoint. You can either validate the entire response or apply a custom validation to specific fields. This checkbox is enabled by default.
      ![trinity-alerts-communication-channel-config](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-config.png)
      When the Liveness checkbox is enabled, you must specify the following:
      ![trinity-alerts-communication-channel-liveness-check](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-liveness-check.png)
      Additionally, define the expected response type and the HTTP status codes that indicate a successful liveness check. The response can be in either JSON or string format:
      If the Custom Validation checkbox is enabled, you can define a custom function to evaluate specific fields in the response and verify whether the returned values meet the expected criteria.
      ![trinity-alerts-communication-channel-liveness-custom](/resources/Storage/trinity-publication/images/trinity-alerts-communication-channel-liveness-custom.png)
    - The request method type (e.g., GET, POST)
    - The API endpoint URL
    - Any required request body parameters
    - If the response is JSON, specify the expected JSON structure or fields that must be present.
    - If the response is a string, enter the exact string that should be matched to confirm liveness.
7. On the next page, the platform provides an option to trigger an API from an external application to perform backend tasks as needed. This option is useful when a communication channel (such as email or Microsoft Teams) has not been configured. You can choose to either:
  1. Configure a communication channel (such as email or Microsoft Teams) to send alerts
  2. Trigger an API to perform any backend tasks
  3. Or use both methods, depending on your requirements
8. To trigger an application's API to perform backend or other required tasks enable the , you must provide the request method (either GET or POST) and the API endpoint URL. Additionally, specify the necessary authorization details, including the token, client ID, and client secret, to authenticate and trigger the API successfully.
    ![trinity-alerts-configure-post-action](/resources/Storage/trinity-publication/images/trinity-alerts-configure-post-action.png)
9. After configuring the post-action API call as required, click the Next button at the bottom of the page to proceed.
    ![trinity-alerts-configure-post-action-next](/resources/Storage/trinity-publication/images/trinity-alerts-configure-post-action-next.png)
    ![Note](/resources/Storage/trinity-publication/project-trailproject/note.png)
    Note: The checkbox for performing additional actions when the application fails is disabled by default
10. The final step is to review all the configurations set for the application alert.
    ![trinity-alerts-final-review](/resources/Storage/trinity-publication/images/trinity-alerts-final-review.png)
    Once everything is verified, click the Create button at the bottom of the screen.
    ![trinity-alerts-application-final-create](/resources/Storage/trinity-publication/images/trinity-alerts-application-final-create.png)
