# Add Relationship

<https://documentation.neutrinos.com/articles/#!pulse-publication/relationships>

A relationship is a logical association between one object and another object within the same tenant or organization.

## Add Relationship

To add a relationship to an object, follow these steps:

1. On the Objects page, click the object to which you want to add a new relationship.
2. In the Fields page, click Relationships in the left navigation pane. If no relationships are added, an empty table is displayed as illustrated in the image below:
    ![up-hypha-objects-relationships-empty-table](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-empty-table1.png)
    If the object already has relationships with other objects on the platform, the associated fields are listed in the table. **Note**: The Relationships tab displays the number of fields in the selected object that have relationships with other objects.
    ![up-hypha-objects-relationships-existing-relationships-table](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-existing-relationships-table.png)
  - **Field Label**: Displays the label assigned to the field when it was created.
  - **Field Name**: Displays the name of the field specified during field creation.
  - **Data Type**: Displays the relationship type of the field (for example, One-to-One or One-to-Many) with the related object.
  - **Related Object**: Displays the object to which the field is related.
  - **Action**: Displays the kebab menu for each relationship. Click the kebab menu to edit or delete an existing relationship.
3. Click Add in the upper-right corner of the Relationships page to create a new relationship.
    ![up-hypha-objects-relationships-add-new](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-add-new.png)
4. The next step is to select the relationship type that defines how the selected objects are associated with each other. The platform supports the following relationship types:
    After selecting the relationship type, choose the target object from the drop-down list to establish the relationship.
    ![up-hypha-objects-relationships-add-new-type-and-object](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-add-new-type-and-object.png)
  - One-to-One
  - One-to-Many
  - Many-to-Many
  - Heirarchical
5. On the next screen, provide the details of the field that will be associated with the selected object. The system retrieves all fields from the related object and creates the association with the current object. **Note: **This field is added to the object as part of the relationship. It is an optional field that extends the object's existing schema properties and is not part of the object's original schema.
    Enter the following details for the new field:
    Then, specify the deletion behavior to define what happens when the referenced lookup record is deleted.
    ![up-hypha-objects-relationships-add-new-field-object](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-add-new-field-object.png)
  - Field Label
  - Field Name
  - Description
  - Help Text
6. Click Next to create and save the relationship.

## Edit Relationship

To edit an existing relationship between objects, follow the steps below:

1. On the Objects page, click the object whose relationship you want to edit.
2. On the Fields page, click Relationships in the left navigation pane to open the Relationships page.
3. In the Relationships table, locate the relationship to update.
4. In the Actions column, click the kebab menu, and then select Edit to open the Edit Relationship page.
5. On the Edit Relationship page, update the field label, field name, description, help text, and deletion behavior for the associated field.
    ![up-hypha-objects-relationships-edit-new-field-object](/resources/Storage/pulse-publication/images/up-hypha-objects-relationships-edit-new-field-object.png)
    **Note**: The relationship type (for example, One-to-One, One-to-Many, Many-to-Many, or Hierarchical) and the associated field selected when the relationship is created cannot be changed.

[Next Topic](/articles/pulse-publication/events)

[Previous](/articles/pulse-publication/fields)
