# Application Alerts

<https://documentation.neutrinos.com/articles/#!trinity-publication/application-alerts>

Alerts are configured to notify users when an application experiences downtime or fails to function as expected. These alerts can be set up to send email notifications or trigger APIs of other applications, allowing users to perform backend tasks as needed. This helps minimize disruptions and facilitates timely troubleshooting to restore the application.

The Application Alerts page loads by default when you click on Alerts. It features three dropdown menus at the top that allow you to filter alerts by Environment, Project, or Application. A Date Filter is available, enabling you to filter alerts within a specific date range—ranging from Today to the Last 90 Days. You can also set a custom date range if needed.

Pagination controls at the top of the page let you define how many rows are displayed. By default, 10 rows are shown, but this can be changed to 20 or 30 according to your preference. You can navigate through multiple pages using these controls to view all configured alerts.




 ![trinity-alerts-page-details](/resources/Storage/trinity-publication/images/trinity-alerts-page-details.png)

Further, the page also displays a list of alerts sent from the platform. The information is presented in a table format, with each row representing the details of alerts:

- **Project/ Namespace**: Displays the project or namespace associated with the application for which the alert is created.
- **Environment**: Displays the environment where the application is deployed
- **Application**: Displays the application name associated with the alert.
- **Type**: Displays the deployment type of the application—either Trinity or manual deployment.
- **Failed Time**: Displays the timestamp of the most recent failed attempt to send the alert.
- **Notified**: Displays the status of the most recent attempt to send the alert.

The dropdown at the end of each row expands to display detailed information about a specific alert. This includes:

- The application status
- The error message thrown
- The failure message, if any
- The number of retry attempts made to send the alert
- The total number of pods and the number of running pods
- The request type associated with the alert
- The response type configured for the alert
- The response status codes expected
- The success email address configured during alert setup
- The retry interval is defined during configuration
- Any custom validations set up during alert configuration.

| ![Note](/resources/Storage/trinity-publication/project-trailproject/note.png) | Note: The above image displays a list of alerts because some alerts have already been created in the platform. If no alerts exist, this list will appear empty. |
| --- | --- |

The image below illustrates the Events page when no events have been created on the platform.



![trinity-alerts-no-alerts-available](/resources/Storage/trinity-publication/images/trinity-alerts-no-alerts-available.png)
