# Layouts

<https://documentation.neutrinos.com/articles/#!alpha-platform/layouts-categories-and-forms>

Layouts in the Neutrinos Alpha Workbench define the structure for displaying or gathering information and interacting with a specific task. They are highly customizable and allow users to design task pages tailored to the needs of the workflow.

## Layouts

Define the structure for the Layout to display or gather information from an end user. The layout can include the following components:

1. **Panels**: To organize and group related controls. It acts as a top-level widget for creating the base-layout.
2. **Columns**: Inside each Panel component, columns can organize the panel into horizontal spaces.

## Form Controls

Form controls are the interactive components through which users interact with the application. Following are the components that are available in Workflow Studio.

1. **Input Fields**: For capturing user inputs required to complete the task.
2. **Buttons**: To trigger specific actions, such as submit, make an API call, or refresh data etc. and so on.
3. **Document Viewer**: To view the documents present in the case.
4. **Dropdowns**: To provide selectable options for predefined choices.
5. **Checkbox Buttons**: For enabling or disabling specific boolean( true, / false ) values or mapped (bound) data. Data can be part of alpha.co or alpha.local.
6. **Radio Buttons**: To provide selectable options.
7. **Tables**: Provides a structured way to organize information or data, typically in rows and columns, enabling users to store, retrieve, and manipulate data efficiently.

This flexibility ensures that task pages can be configured to meet diverse operational requirements, improving user interaction and task efficiency. By providing a structured and purpose-driven interface, layouts enhance clarity and usability, enabling seamless task execution.

Panels function as top-level widgets for creating the base layout. Each panel contains sections organized into horizontal spaces with either three, two, or one column. Within each column, widgets are arranged in a horizontally stacked manner. These sections can include various render components such as Buttons, Input Fields, Dropdowns, Date Pickers, Checkboxes, Radio Buttons, Tables, and many more. The components in the layout can be customized to validate and ensure they contain the appropriate data based on your business requirements.

The image below illustrates one, two, and three column vertical section layout in a task page.

![Layout-sample-image](/resources/Storage/alpha-platform/images/categories-layout-sample.png)

## Categories

In the Workbench, when a user interacts with a case by clicking on it, they can view various tasks associated with the case in the left-side panel of the page. These task pages are based on the requirements of the business process workflow. Further, you can categorize these pages according to specific requirements and apply conditions to control which task pages are displayed.

You can either add new pages to an existing category or create a new category when a new task page is being created for tasks within the business process.

The image below illustrates a sample of categories that includes Application Overview, Documents, and Decision. It can vary according to your application, depending on your requirements.

![Categories sample image](/resources/Storage/alpha-platform/images/categories-fullpage.png)

Under each category showcased in the sample image above, multiple task pages are displayed. These pages are organized according to business logic.

| ![Note](/resources/Storage/alpha-platform/note.png) | The Pages that are available on the Home page of the Workbench are referred as Main Pages. See [Navigate Links](/articles/alpha-platform/navigate-links) Links topic for more information. |
| --- | --- |

## Validation

**Input** controls provides support for data validation of the user input. It can be as simple as making a field mandatory, or setting a minimum or maximum length while a user enters input into the field. The components in Workbench accommodates these validations in them to enhance the experience.

- The **Checkbox** component allows you to mandate a user to check an option using the **Mandatory** toggle.
- The **Input Field** component provides a wide range of validation options:
  - Setting a **Minimum** and **Maximum** property value allows users to enter a numeric value within the specified range in the Input Field.
  - You can set the **MinLength** and **MaxLength** properties to require users to enter a minimum and maximum number of characters in the Input Field.
  - The input field can also have a **Regex Pattern** specified to ensure the input matches the required pattern based on the application needs.
  - You can make an Input Field read-only by enabling the **Read Only** toggle.
  - You can make the Input Field component mandatory by enabling the **Mandatory** toggle.

The image below illustrates the use of **MinLength** and **Regex** validations applied to Input components. These validations ensure accurate data entry and display appropriate error messages to the user when the input does not meet the required criteria.

![MinLength and Regex applied](/resources/Storage/alpha-platform/images/minlength-regex.png)

## Placeholder and Hint Text

A placeholder displays text within a control when no value is selected or entered, and it disappears as soon as a value is input. Placeholders are applicable to components such as Input Fields and Dropdowns. In contrast, hint text is displayed beneath a component to guide the user in entering the correct value format. Unlike placeholders, hint text is always visible, regardless of whether a value has been entered in the component. The image below provides a sample section of a form, illustrating the use of Placeholder and Hint Text, along with a field marked as Mandatory.

![Placeholder and hint text image](/resources/Storage/alpha-platform/images/placeholder-hint-text.png)

## Forms

Form is an interactive user interface component to capture, display, and manage data within workflows. Forms act as the primary medium for user input, enabling interaction with the system by facilitating the submission, modification, or review of information. It is collection of the Layout and Category of controls that make the complete Form. The below image illustrates a sample form that contains render components.

![Sample Form image](/resources/Storage/alpha-platform/images/sample-form-fullscreen.png)
