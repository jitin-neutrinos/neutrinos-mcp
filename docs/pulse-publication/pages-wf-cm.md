# Layouts

<https://documentation.neutrinos.com/articles/#!pulse-publication/pages-wf-cm>

A Page can be designed to display information from data sources like Case Data that contain relevant data about Case Instance, Integration Layer that are accessed through APIs, DMS that contain documents and associated metadata, CMS that holds content and the Rëels Master Data. To design pages use the components available in the Workflow Studio. You can also leverage additional components from Neutrinos Marketplace.

## Layouts

Define the structure for the Layout to display or gather information from an end user. The layout can include the following components:

1. **Panels**: To organize and group related controls. It acts as a top-level widget for creating the base-layout.
2. **Columns**: Inside each Panel component, columns can organize the panel into horizontal spaces with either three, two, or one column. Within each column, you can arrange widgets in a horizontally stacked manner.

## Form Controls

Form controls are the interactive components through which users interact with the application. Following are the components that are available in Workflow Studio.

1. **Input Fields**: For capturing user inputs required to complete the task.
2. **Buttons**: To trigger specific actions, such as submit, make an API call, or refresh data etc. and so on.
3. **Document Viewer**: To view the documents present in the case.
4. **Dropdowns**: To provide selectable options for predefined choices.
5. **Checkbox Buttons**: For enabling or disabling specific boolean( true, / false ) values or mapped (bound) data. Data can be part of alpha.co or alpha.local.
6. **Radio Buttons**: To provide selectable options.
7. **Tables**: Provides a structured way to organize information or data, typically in rows and columns, enabling users to store, retrieve, and manipulate data efficiently.

The image below illustrates a sample design of a form layout that gathers basic information about a person:

![workflow-studio-sample-layout-options-image](/resources/Storage/pulse-publication/images/workflow-studio-layout-options.png)

## Page Settings

Page settings can be triggered using three events: On Init, Before Init, and On Change. Each of these have different behavior that impacts the page settings.

1. **On Init**: Executes logic when the page is initialized. This is often used to set up the page's state or fetch required data.
    Key uses:
  1. Initialize Variables: Initialize or set default values to attributes or objects used by the page.
  2. Fetch Data: Make API calls to retrieve data to populate page elements, such as dropdowns or tables.
2. **Before Init**: Executes logic before the page's UI is rendered. Especially useful in hiding or showing sections based data fetched for other APIs.
    Key uses:
  1. Pre-Fetch Data: Gather critical data needed before the page is rendered, ensuring a seamless user experience.
  2. Dynamic Routing: Redirect the user to another page if certain conditions are not met (e.g., lack of permissions or prerequisites).
  3. Modify Configurations: Adjust alpha.co and/or alpha.local settings before the page is displayed.
  4. Conditional Initialization: Decide whether the page should proceed with initialization based on certain conditions.
3. **On Change**: Executes logic when a specific field, variable, or component value is updated. This is useful for creating dynamic, interactive pages.
    Key uses:
  1. Field Validations: Validate the input of a field when its value changes.
  2. Dynamic Updates: Update other fields, components, or UI elements based on the changed value. For example, updating a table or chart when a dropdown selection changes.
  3. API Calls: Trigger backend service calls based on the new value.
  4. Conditional Logic: Enable or disable components dynamically based on the updated value.
  5. Event Triggering: Initiate workflows or events based on the value change (e.g., saving form progress or triggering notifications).
