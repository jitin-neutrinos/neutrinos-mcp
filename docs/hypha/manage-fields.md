# View Fields

<https://documentation.neutrinos.com/articles/#!hypha/manage-fields>

Fields are part of an object’s definition. A field definition specifies the data type and the associated metadata that control the validation and behaviour of the object.

## View Fields

To view all fields associated with a specific object, navigate to the Object Manager page and select the required object. Each row represents a field and its associated metadata. The table includes the following columns:




 ![hypha-studio-object-fields-landing](/resources/Storage/hypha/images/hypha-studio-object-fields-landing.png)

### Interface

1. **Field Label**: Displays the user-friendly label of the field as shown in forms, pages, and record views. This label helps end users easily understand the purpose of the field.
2. **Description**: Provides a brief description of the field. This helps clarify the intent, usage, or business context of the field.
3. **Field Name**: Displays the internal name of the field. This name is typically used in configurations, integrations, and programmatic references.
4. **Group**: Indicates the group or category to which the field belongs. Grouping helps organize related fields logically within the object.
5. **Modified By**: Shows the user who last modified the field configuration.
6. **Action**: Contains a kebab (three-dot) menu that provides access to field-level actions, such as editing or deleting the field.

## Add Field

To add one or more fields to a specific object, follow these steps:

1. From the list of available objects, select the object to which you want to add a new field.
2. On the Fields page, all fields currently associated with the object are listed. Click Add at the top of the page to add a new field to the object.
    ![hypha-studio-object-fields-add-field-button](/resources/Storage/hypha/images/hypha-studio-object-fields-add-field-button.png)
3. The first step is to define the data type for the field value. Select a data type from the available list. You can also use the search bar on the page to locate a specific data type quickly.
    ![hypha-studio-object-fields-new-field-datatype](/resources/Storage/hypha/images/hypha-studio-object-fields-new-field-datatype.png)
4. The next screen displays several properties that you can configure for the field.
    ![hypha-studio-object-fields-new-field-details](/resources/Storage/hypha/images/hypha-studio-object-fields-new-field-details.png)
  - **Field Group Assignments**: Field Group acts as a metadata container that associates a field with a specific functional or business context.
  - **Field Label**: The user-friendly name of the field, typically displayed in forms, page layouts, and record views.
  - **Length**: Specifies the maximum allowed length of the field value. This property is typically applicable to text-based fields.
  - **Field Name**: The technical identifier for the field, used internally by the platform, APIs, integrations, and queries.
  - **Descriptions**: A detailed description of the field’s purpose and usage, serving as inline documentation for administrators and developers.
  - **Help Text**: Short instructional text displayed to end users during data entry, guiding them on the expected value and format.
5. After entering values for all field properties, click Save at the bottom of the page.
    ![hypha-studio-object-fields-new-field-details-save-button](/resources/Storage/hypha/images/hypha-studio-object-fields-new-field-details-save-button.png)

## Edit Fields

To edit the details of a field associated with an object, follow these steps:

1. From the left navigation panel, select Objects.
2. From the list of available objects in the table, select the object that contains the field you want to edit. In the row for the required field, click the kebab icon in the Action column and select Edit.
3. On the Fields page, the previously configured property values for the field are prepopulated. Update the required values and click Save. You can also change the group association to which the field belongs, if needed.
    ![hypha-studio-object-fields-add-field-button](/resources/Storage/hypha/images/hypha-studio-object-fields-add-field-button.png)

**Note**: The Edit option allows you to modify specific field properties, such as field constraints, allowed characters, minimum and maximum length, and the field index. However, changing the field name is not permitted.

## Delete Fields

To delete a field associated with an object, follow these steps:

1. From the left navigation panel, select Objects.
2. From the list of available objects in the table, select the object that contains the field you want to delete. In the row for the required field, click the kebab icon in the Action column and select Delete.
3. In the pop-up screen, click Remove to delete the field from the associated object permanently.
    **Note**: If a field is associated with more than one object or is part of a field group, deleting it is not supported. Doing so may cause exceptions in the project and disrupt system functionality.
    ![hypha-studio-object-fields-new-field-details-delete-error](/resources/Storage/hypha/images/hypha-studio-object-fields-new-field-details-delete-error.png)

**Note**: When a delete operation is performed on a field, the field is soft deleted. Once deleted, the field is no longer available for use on the platform.
