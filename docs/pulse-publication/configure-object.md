# Configure Object

<https://documentation.neutrinos.com/articles/#!pulse-publication/configure-object>

The Object page in Pulse provides a comprehensive view of a selected object record. It displays all relevant information and metadata associated with that record, offering users a consolidated overview in a single screen. This page helps users understand the record’s field values, relationships between other objects and any operational configurations—such as events and associated pipelines defined within the environment.

When you select an object from the Object Manager page, the corresponding Object page opens and displays the configured details for that object. If the object has not yet been configured, you can configure it directly from this page. The Object page allows you to define and manage object settings, including Fields, Relationships, Page Layout, Events, and Pipelines.




 ![up-hypha-objects-fields-particular-object](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object.png)

- The left navigation pane provides access to the various configuration modules available for the selected object. The available configuration sections include:
  - **Fields**: Manage object fields.
  - **Relationships**: Define relationships with other objects.
  - **Page Layout**: Configure how fields are displayed within forms and pages.
  - **Event**: Configure event-based actions associated with the object.
  - **Pipeline**: Define business process stages or workflow pipelines for the object.
- The **Add** button, located in the upper-right corner of the page, allows users to create a new custom field for the selected object. When adding a field, users can typically configure properties such as: Field Label, description, name, data type, and group. After creation, the field becomes available for use within the object.
- The **Search** bar enables users to quickly locate a field within the selected object.
- The **Filter** option enables users to organize or narrow the displayed fields.
- The table displays all configured fields for the selected object. Each row represents an individual field.
  - **Field Label**: Displays the user-friendly name of the field as it appears throughout the application. For example, Account Name, First Name, and so on.
  - **Description**: Provides a brief explanation of the field's purpose. This helps understand the intended use of each field.
  - **Field Name**: Displays the system-defined or API name of the field. This identifier is commonly used for business rules, integrations (APIs), and so on. Unlike the field label, the field name is typically unique within the object.
  - **Group**: Displays the field group to which the field belongs. Field groups help organize related fields into logical categories, making large object definitions easier to manage.
  - **Modified By**: Displays the user who most recently modified the field. This includes both the User avatar and the User name.
  - **Data Type**: Displays the data type assigned to the field. For example, Text, Number, Date, etc.
  - **Action**: The Action column provides access to field-specific operations such as edit and delete, through a contextual menu.
- **Sorting**: Sortable columns display sorting indicators. Sorting allows fields to be arranged in ascending or descending order.
- **Pagination**: Displays pagination controls at the bottom-right of the page, allowing you to navigate through multiple pages when the selected object contains a large number of fields. Additionally, you can adjust the page size to enable you to view more or fewer records without navigating between different pages.

[Next Topic](/articles/pulse-publication/fields)

[Previous](/articles/pulse-publication/object-details)
