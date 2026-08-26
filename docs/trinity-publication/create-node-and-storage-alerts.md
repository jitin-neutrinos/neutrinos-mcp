# Create Node and Storage Alerts

<https://documentation.neutrinos.com/articles/#!trinity-publication/create-node-and-storage-alerts>

This section highlights the steps that differ when creating storage alerts compared to application alerts. To create an alert for storages, follow the steps below:

1. In the left navigation pane, click Config to open the Alerts page under Nodes or Elastic Storage. By default, the Application Alerts page is displayed, showing all alerts triggered for applications, as illustrated in the image below:
    ![trinity-alerts-nodes-info-displayed-config-page](/resources/Storage/trinity-publication/images/trinity-alerts-nodes-info-displayed-config-page.png)
2. Click the New Alert Config button at the top of the page to begin creating a new alert for the nodes or elastic storage.
    ![trinity-alerts-nodes-create-button](/resources/Storage/trinity-publication/images/trinity-alerts-nodes-create-button.png)
3. Select the type of storage for which the alert needs to be created. You can choose either Node Storage or Elastic Storage, or both.
    ![trinity-alerts-node-storage-type-storage](/resources/Storage/trinity-publication/images/trinity-alerts-node-storage-type-storage.png)
4. Select the environment(s) for which the storage alert should be created. Note: All available environments are listed in the dropdown menu. You can select multiple environments by using the checkboxes next to each item.
    ![trinity-alerts-nodes-select-environment](/resources/Storage/trinity-publication/images/trinity-alerts-nodes-select-environment.png)
    Once the type of storage and the environment is selected, click the next button at the bottom of the screen.
    ![trinity-alerts-storage-next-button](/resources/Storage/trinity-publication/images/trinity-alerts-storage-next-button.png)
5. Configure the communication channel by specifying the From and To email IDs, or by setting the webhook URL for the Teams channel to notify users about the storage alert. This process is like the one illustrated for configuring Application Alerts. To learn more about setting up communication channels, refer to the steps outlined under Application Alerts.
6. In the next step, configure the alert conditions. This includes setting the following parameters:
    ![trinity-alerts-storage-percentage](/resources/Storage/trinity-publication/images/trinity-alerts-storage-percentage.png)
  1. Frequency: Specify how often the system should check (in minutes) for failures after the initial occurrence.
  2. Maximum Failure Checks: The number of consecutive checks to verify if the application continues to fail. This counter resets once the application becomes live and operational.
  3. Retry Interval: Specify the frequency interval at which the application should be checked to ensure it is functioning properly. For example, if a 6-hour interval is selected, the system will check the application’s status every 6 hours.
  4. Percentage: Set the threshold percentage of storage usage that triggers the alert.
  5. Additionally, you can enable the Send Daily Percentage Updates checkbox to send daily storage usage updates to users.
7. Once the alert configuration is complete, click Next to proceed to the Post Action step—only if a communication channel has not been configured. This step allows users to trigger an API in another application to perform required backend tasks. To learn more about setting up API triggers using post actions, refer to steps 7 and 8 in the Application Alerts section
8. Finally, review the configured settings and click the Create button to complete the setup.
