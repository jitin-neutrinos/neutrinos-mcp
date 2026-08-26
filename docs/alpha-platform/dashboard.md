# Create Dashboard

<https://documentation.neutrinos.com/articles/#!alpha-platform/dashboard>

Dashboards provide critical insights into key performance metrics, enabling users to track task performance, identify bottlenecks, and ensure timely completion of critical business processes.

Insights, is a powerful business intelligence tool that offers capabilities for creating interactive dashboards. With visualization options including bar charts, line graphs, and pie charts, allow users to filter, organize, and display complex data in a user-friendly format. These intuitive visualizations are essential for helping teams gain actionable insights and improve overall operational efficiency.

## Create Dashboard

To create a dashboard follow the steps below:

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | These steps assume that the data source is already set up. |
| --- | --- |

1. In the Insights homepage, click the **New** button.
2. Choose one of the following options:
  1. **Question**: Create a new query using the visual editor.
  2. **SQL Query**: Write a custom SQL query.
  3. **Dashboard**: Build a dashboard to visualize multiple metrics.
  4. **Collection**: Organize related questions and dashboards.
  5. **Model**: Define reusable data models.
3. After selecting the query type and configuring data retrieval for the dashboard, choose a visualization type to represent the data effectively.
    ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png)
    If you choose **Dashboard** as the query type, note that it will not contain charts by default. You must create charts and add them to the dashboard for visualization.
4. Save the query by entering a name and description and selecting a collection location.
5. After adding a chart to the dashboard, resize or reposition it as needed. If necessary, add queries, then save the final dashboard.
6. Finally, publish the dashboard to be made accessible on the Alpha Platform.

## Publish Dashboard

To publish the dashboard, follow the steps below:

1. Add the below filters to the dashboard:
  1. **user_id**: Used to filter dashboard information for a specific user.
  2. **project_id**: Used to filter the dashboard information based on the project_id.
  3. **project_name**: Used to filter the dashboard information based on the project_name.
2. Save the dashboard after adding the filters.
3. After saving, click the **Sharing** button.
  1. Select the '**Embed in your application**' option.
  2. Click the '**Set up**' button and enable all the filters for editing.
  3. Click **Publish** to complete the process.

The GIF below illustrates the steps for publishing the dashboard:




 ![embed-dashboard](/resources/Storage/alpha-platform/images/embed_dashboard.gif)

## Add Dashboard

To add a dashboard in the Workflow Studio, follow the steps below:

1. Go to Config editor > Navigate to Dashboard editor > Ensure the Dashboard toggle is enabled. Enabling this option displays the dashboard category in the Main Menu of the Workbench. By default, this option is disabled, preventing users from viewing available dashboards even if they are added.
2. Click the Add button to create a new dashboard > Select the appropriate dashboard from the Dashboard Items dropdown.
3. From the **Assigned To** dropdown, select the user group that should have access to the dashboard.
4. Provide a name for the dashboard that aligns with the process specifications.
5. Use the Active toggle button to enable or disable the dashboard’s visibility on the Workbench. By default, new dashboards are set to Active.
6. Click the Save button.

The GIF below illustrates how to add a dashboard, and how it appears for a Workbench user:

![add-dashboard-workflowstudio](/resources/Storage/alpha-platform/images/add-dashboard-workflowstudio.gif)
