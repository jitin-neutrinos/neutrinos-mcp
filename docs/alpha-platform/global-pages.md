# Dashboards

<https://documentation.neutrinos.com/articles/#!alpha-platform/global-pages>

Global pages are reusable layouts or components designed for use across multiple tasks within a project. They enhance consistency and efficiency by providing shared functionality and reusable page components. By reducing redundancy, global pages streamline development and ensure a uniform user experience.

Key benefits of global pages can be listed as follows:

1. **Reusability**: Create a page once and use it across multiple tasks.
2. **Consistency**: Maintain a standardized UI pattern across different tasks.
3. **Maintainability**: Update a global page once, and the changes are automatically reflected across all tasks that use it.

For more information on creating Global Pages, see Layouting topic in Workflow Studio Manual.

## Dashboards

Dashboards provide insights into key performance metrics, enabling users to track task performance, identify bottlenecks, and ensure timely completion of critical tasks.

The GIF below demonstrates how a dashboard appears in the Workbench:

![Add dashboard to workbench GIF](/resources/Storage/alpha-platform/images/add-dashboard-workbench.gif)

## Form Submits

Form submissions in the Neutrinos Alpha Platform is a fundamental feature that allows for efficient data collection and processing. This involves capturing user-entered data from form fields and handling it for operations, including storing the data in databases, triggering specific workflows, or integrating with external APIs.

When a user fills out a form and submits it, the data undergoes validation either on the client side (browser) or the server side. Client-side validation focuses on field format checks, such as ensuring email fields contain valid addresses, numeric fields accept only numbers and mandatory fields like "Name" and "Age" and so on are completed. While client-side validation enhances user experience by providing instant feedback and prompting corrections before submission, server-side validation ensures data integrity and security, by verifying the submitted data on the server.

The key benefits of form submission:

1. **Data Validation**: The platform ensures that all submitted data conforms to rules, improving the accuracy and reliability of the collected information. Workbench supports both client-side and server-side validation.
2. **Event Triggering**: Workbench leverages form submissions to automate workflows and initiate various actions. For example, submitting a form can trigger record updates in connected databases, or call APIs to communicate with external services.
3. **Integration and Processing**: Submitted data in the application can be seamlessly stored in database or external systems via API calls. This ensures that data is accessible for future use, such as generating reports or performing analytics. Neutrinos Alpha’s flexible architecture supports interaction with multiple systems, facilitating smooth data transfer across platforms.

The image below demonstrates a sample form submit upon a case approval

![Form submission sample](/resources/Storage/alpha-platform/images/formsubmit-sample.png)
