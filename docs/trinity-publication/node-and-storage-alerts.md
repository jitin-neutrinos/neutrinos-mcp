# Node and Storage Alerts

<https://documentation.neutrinos.com/articles/#!trinity-publication/node-and-storage-alerts>

Similar to application alerts, storage alerts notify users about issues related to storage systems. These can include node storage or Elastic storage. The process of creating storage alerts is largely similar to that of application alerts, with a few key differences.




 ![trinity-alerts-nodes-info-displayed-config-page](/resources/Storage/trinity-publication/images/trinity-alerts-nodes-info-displayed-config-page.png)

This page, similar to the Application Alerts page, displays information about the alerts configured for nodes. The details are presented in a tabular format and include the following information:

- Environments: Displays the environment associated with the Node or Elastic Storage alert.
- Percentage: Displays the storage utilization percentage threshold at which the alert is triggered.
- Maximum failure checks: Displays the number of consecutive failure checks performed before triggering the alert.
- Created By: Displays the user ID of the person who created the alert.

The dropdown arrow at the end of each row allows users to expand the alert and view additional details, including:

- Whether daily usage percentage updates are enabled
- The frequency of checks performed on the storage
- Retry interval
- Created By
- Created date and time
- Last updated date and time
- Email configuration settings (if configured), including the From and To email ID, and whether a success email should be sent when the storage issue is resolved.
