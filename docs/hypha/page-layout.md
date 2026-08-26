# List Page

<https://documentation.neutrinos.com/articles/#!hypha/page-layout>

The Page Layout determines how objects are presented within the platform interface.




 The following layout types are available:

- **List Page**: Provides a tabular view of all objects available on the platform.
- **Form Page**: Displays the detailed information for a specific object.

## List Page

A List Page is a page layout used to display a collection of records for a specific object (entity). It provides users with a consolidated, tabular view of data and enables actions such as viewing, filtering, sorting, creating, and editing records.




 The List Page typically serves as the entry point for interacting with object-level data. It presents data in a tabular (grid) format and serves as the primary interface for:

- Viewing records
- Searching and filtering data
- Performing row-level and bulk operations
- Navigating to detailed record pages
- Creating new records

The image below illustrates a sample List page view for the Lead object:




 ![hypha-studio-page-layout-list-page](/resources/Storage/hypha/images/hypha-studio-page-layout-list-page.png)

## Form Page

A Form Page is a structured layout used to create, view, or update a single record of a configured object (entity). It provides a field-driven interface that enables users to input, edit, validate, and submit data. The Form Page is typically used in:

- Record creation workflows
- Record modification (Edit mode)
- Record viewing (Read-only mode)
- Task-driven data capture scenarios

The Form Page is designed to:

- Capture data through UI controls
- Enforce validation rules
- Support workflow-driven interactions
- Enforce field-level and object-level permissions

A form can be structured using layout components to create single-column or multi-column arrangements, as well as collapsible sections for improved organization and usability. The layout can incorporate various input and action components, including Text Area, Date Picker, Dropdown, Radio Button, Checkbox, and Button controls. Each component provides configurable properties such as:

- Label customization
- Placeholder text configuration
- Read-only settings
- Mandatory field configuration
- Validation rules

In addition to visual and behavioral configurations, triggers can be defined at the component level. These triggers enable the execution of specific events, such as:

- Invoking APIs
- Generating notifications
- Executing business rules
- Updating dependent fields dynamically

The image below illustrates a sample Form page view:

![hypha-studio-page-layout-form-page](/resources/Storage/hypha/images/hypha-studio-page-layout-form-page.png)
