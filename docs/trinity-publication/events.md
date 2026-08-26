# Navigate within Events

<https://documentation.neutrinos.com/articles/#!trinity-publication/events>

Events - Cron Job Management - job is a scheduled task that runs automatically at predefined intervals. In Trinity, cron jobs are configured for applications deployed on clusters. These applications can be either deployed through Trinity or be third-party applications deployed independently.

They are typically used to automate tasks, trigger workflows or API calls at specific times, and perform routine operations without manual intervention. The Events page lists all the available Cron jobs (if available) in a tabular form as shown in the image below:




 ![trinity-events-landing-page](/resources/Storage/trinity-publication/events/trinity-events-landing-page.png)

1. **Name**: Displays the name of the cron job as specified during its creation.
2. **Environment**: Displays the name of the environment for which the cron job was created.
3. **Time Zone**: Displays the name of the time zone in which the application is deployed. This is selected during cron job creation.
4. **Namespace**: Displays the namespace of the cluster from the selected environment to which the cron job is assigned.
5. **Expression**: Displays the cron expression or interval configured during cron job creation.
6. **Created At**: Displays the timestamp when the cron job was created.
7. **Updated At**: Displays the timestamp of the most recent update made to the cron job.
8. **Action**: Use the options in this column to either export or delete the cron job.

| ![Note](/resources/Storage/trinity-publication/project-trailproject/note.png) | Note: The above image displays a list of events because some events have already been created in the platform. If no events exist, this list will appear empty. |
| --- | --- |

The image below illustrates the Events page when no events have been created on the platform.

Additionally, you can search for a specific cron job using the search bar. You can also control the number of cron jobs displayed by using the Show By option. If there are multiple cron jobs on the platform, use the pagination controls at the top of the page to navigate through the list.

# Navigate within Events

On the Events page, navigate to any created event and click it to open its details. By default, the event details page displays all the information provided during the creation of the associated cron job.

1. The left navigation panel includes two sections: Details and Logs
  1. Details: Displays information about the cron job and is opened by default.
  2. Logs: Shows the execution logs associated with the cron job.

# Logs

A cron job can fail at two levels. The Logs page maintains these as listed below:

1. Triggers: API Endpoint Level failure occured due to issues with the API endpoint itself or incorrect configuration of the endpoint in the cron job. Related logs are available under the Triggers tab.
    ![trinity-events-api-endpoint-status](/resources/Storage/trinity-publication/events/trinity-events-api-endpoint-status1.png)
2. Cron: Cluster Level failures occurred are issues with the cluster to which the cron job is assigned. The execution status—whether successful or failed—at the cluster level is displayed under the Cron tab.
    ![trinity-events-cluster-status](/resources/Storage/trinity-publication/events/trinity-events-cluster-status.png)
