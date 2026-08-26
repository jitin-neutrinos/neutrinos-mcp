# Add Fields

<https://documentation.neutrinos.com/articles/#!pulse-publication/fields>

The Fields page is used to create and manage the fields associated with a business object. Each field represents an attribute that stores data for the selected object. From this page, admins can add new fields, search existing fields, organize them into groups, and perform field-level management operations. The following image shows the Fields page for the Lead object with its configured fields.

![up-hypha-objects-fields-particular-object](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object.png)

## Add Fields

To add fields and configure an object, follow the steps below:

1. On the Objects page, click the object to which you want to add a field. The Fields page opens, displaying all the fields configured for the selected object. If no fields have been added or configured, an empty table is displayed. **Note**: The number displayed next to the Fields tab indicates the total number of fields configured for the selected object.
2. On the Fields page, click Add at the top of the page to create a new field for the selected object.
    ![up-hypha-objects-fields-particular-object-add-field](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object-add-field.png)
3. The next page allows you to select the data type for the new field. The selected data type determines the type of data that the field can store. In the following illustration, the Text data type is selected for the new field.
    ![up-hypha-objects-fields-particular-object-add-field-select-data-type](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object-add-field-select-data-type.png)
    After selecting the required data type, click Next at the bottom of the page.
4. On the next screen, select the field group assignment to assign the new field to a field group. A field group assignment determines which field group the new field belongs to within the object. Field groups logically organize related fields, making them easier to manage and display in the application.
    Next, provide the field details in the Add Field Details section. Specify the field API name, the field length (maximum number of characters), the field name to display in the user interface (UI), a brief description of the field, and the help text that will be displayed to users in the UI.
    ![up-hypha-objects-fields-particular-object-add-field-group-description](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object-add-field-group-description.png)
    After providing the required details on each page, click Done on the final page to add the new field to the selected object.

## Edit Fields

To edit the field(s) for a specific object, follow these steps:

1. On the Fields page, locate the row corresponding to the field to be edited. In the Actions column, click the kebab menu (⋮) and select Edit.
2. The Edit option allows you to modify field details, such as the field group to which the field belongs. You can change the field group assignment, update the field length by increasing or decreasing the maximum number of characters allowed, and modify the field name displayed in the user interface (UI). The Field (API name) is a read-only attribute and cannot be modified. It is displayed for reference and cannot be changed. The following image shows a sample Edit Field screen for an Account field.
   ![up-hypha-objects-fields-particular-object-edit-field](/resources/Storage/pulse-publication/images/up-hypha-objects-fields-particular-object-edit-field1.png)
    After updating the required field details, click Update at the bottom of the page to save the changes.

[Next Topic](/articles/pulse-publication/relationships)

[Previous](/articles/pulse-publication/configure-object)
