# Edit Cron Job

<https://documentation.neutrinos.com/articles/#!trinity-publication/create-cron-job>

Cron jobs can be created as a new job or an existing cron job can be imported. The steps below illustrate how to create a Cron job on Trinity:

1. Click Event from the left navigation panel to open the Events (Scheduled Events) page on the Trinity platform.
    ![trinity-events-navigation](/resources/Storage/trinity-publication/events/trinity-events-navigation.png)
2. Click the Create Event button located at the top-right corner of the page.
    ![trinity-events-create-button](/resources/Storage/trinity-publication/events/trinity-events-create-button.png)
3. Choose Add to create a new cron or select the Import option from the dropdown menu to import an existing one. In this example, Add is selected to create a new cron job.
    ![trinity-events-create-button-dropdown](/resources/Storage/trinity-publication/events/trinity-events-create-button-dropdown.png)
4. A Create Schedule page is displayed for creating a cron schedule. On this page, you need to provide the following details:
    ![trinity-events-create-schedule-cron-info](/resources/Storage/trinity-publication/events/trinity-events-create-schedule-cron-info.png)
  1. Schedule Name and Description, provide the name and description for the cron job. Note: The schedule name (cron job name) must follow the naming convention of using lowercase alphanumeric characters, with hyphens (-) used to separate words
  2. Execution Time and Recurrence Pattern can be configured with one of the following options:
    1. Replace with Previous Run: This setting replaces the existing cron job for the application with the newly created one.
    2. Allow Concurrent Runs: This setting retains both the existing and newly created cron jobs and allows them to execute concurrently for the specified application.
    3. Forbid Concurrent Runs: This setting retains both the existing and newly created cron jobs for the application; however, they are not permitted to execute simultaneously.
  3. Specify the Schedule Type either by entering a cron expression or using the UI to set the interval.
  4. Set the Time Frame (Time Zone) – an optional field. It is by default, Asia, Calcutta.
5. On the next page, provide the trigger details for the cron job. This includes selecting the trigger API, which can be either a third-party deployed API or an API deployed through Trinity, along with the environment, namespace, HTTP method (e.g., POST, GET), and the API endpoint
    Additionally, specify the required headers, body parameters (payload), and the authentication method applicable to the selected HTTP method
    Select the HTTP method. The base endpoint field is populated based on the selected environment, project, service, and version. Note: Append the base endpoint URL with the API-specific endpoint to successfully trigger the API. Failure to provide the API-specific endpoint may result in trigger failure.
    Once the details for the triggers are provided, click the Next button at the bottom of the page.
    ![trinity-events-cron-trigger-details](/resources/Storage/trinity-publication/events/trinity-events-cron-trigger-details.png)
6. On the next page, review all the details entered for creating the cron job. This page displays a summary of all the information provided during the configuration process.
    If any details need to be updated, use the Previous button at the bottom-left of the screen to navigate back and make the necessary changes before creating the cron job.
    Once reviewed, click the Create button to complete the process.
    ![trinity-events-final-create-button](/resources/Storage/trinity-publication/events/trinity-events-final-create-button.png)

# Edit Cron Job

An existing cron job can be edited to accommodate changes as per the requirements. To edit a cron job, follow the steps below:

1. Click Event from the left navigation panel to open the Events (Scheduled Events) page on the Trinity platform.
    ![trinity-events-navigation](/resources/Storage/trinity-publication/events/trinity-events-navigation.png)
2. From the list of available cron jobs on the platform, open the job you want to edit.
    ![trinity-events-open-cron-job](/resources/Storage/trinity-publication/events/trinity-events-open-cron-job.png)
3. The details page opens, displaying all information related to the selected cron job.
    ![trinity-events-cron-details-page](/resources/Storage/trinity-publication/events/trinity-events-cron-details-page.png)
4. In the details page, click the Edit option on the top right of the page.
    ![trinity-events-cron-edit](/resources/Storage/trinity-publication/events/trinity-events-cron-edit.png)
5. A page is displayed where you can edit and update the cron job according to your requirements.
6. After making the necessary updates to the cron job, click the Save button at the top of the page.
    ![trinity-events-edit-save-button](/resources/Storage/trinity-publication/events/trinity-events-edit-save-button.png)
