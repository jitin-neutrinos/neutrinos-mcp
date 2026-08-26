# Interface

<https://documentation.neutrinos.com/articles/#!hypha/manage-relationships>

A relationship refers to the logical or semantic connection between data elements, entities, or objects across different data sources, domains, or systems.

Relationships define how records of one object reference depend on records of another object. The configuration ensures referential integrity, consistent data navigation, and controlled interaction across related entities.




 A relationship between two objects is typically defined by specifying a source object, a target object, and the relationship type. The relationship type determines cardinality, such as one-to-one, one-to-many, and governs how records are linked in the underlying data model.

In a one-to-many relationship, a parent object can be associated with multiple child object records. This is commonly implemented by introducing a reference field in the child object that stores the parent record's identifier. The system enforces referential integrity by validating that the referenced parent record exists. In a one-to-one relationship, a single record in one object corresponds to exactly one record in another object.

Relationships influence how data queries are executed. When retrieving a record, the system may perform join operations or secondary queries to fetch related data. Filtering and reporting capabilities can also leverage relationships to allow cross-object data exploration.

Additionally, relationships support cascading behaviors, such as preventing the deletion of a parent record when dependent child records exist, or optionally enabling cascade delete. These behaviors are configured to preserve data integrity and align with business rules.

## Interface

![hypha-object-relationship-landing-page](/resources/Storage/hypha/images/hypha-object-relationship-landing-page.png)

1. **Field Label**: Displays the user-friendly label of the field as shown in forms, pages, and record views. This label helps end users easily understand the purpose of the field.
2. **Field Name**: Displays the internal name of the field. This name is typically used in configurations, integrations, and programmatic references.
3. **Data Type**:Displays the data type that was configured when the field was created.
4. Action: Contains a kebab (three-dot) menu that provides access to actions, such as editing or deleting the relationship.

## Add Relationship

1. From the list of available objects in the table, select the object to which you want to add a new relationship.
2. On the Relationship page, all relationships currently associated with the object are listed. Click New at the top of the page to add a new relationship to the object.
    ![hypha-object-relationship-new-button](/resources/Storage/hypha/images/hypha-object-relationship-new-button.png)
3. The next step is to define the relationship type between the objects. The relationship can be configured as one-to-one or one-to-many. Select the appropriate option based on the intended data association between the objects.
    ![hypha-object-relationship-new-data-relationship](/resources/Storage/hypha/images/hypha-object-relationship-new-data-relationship.png)
4. After selecting the relationship type, click Next to proceed to the next step in the configuration process. To retain the current configuration without proceeding further, click Save. You can resume the configuration at a later time.
    ![hypha-object-relationship-new-relationship-next-save-button](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship-next-save-button.png)
5. In the next screen, associate the appropriate object with the current object. Select the required object from the drop-down list of available objects.
    ![hypha-object-relationship-new-relationship--related-object](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship--related-object.png)
6. After selecting the required object for association, click Next to continue with the configuration. To preserve the current progress without proceeding further, click Save and resume the configuration later.
    ![hypha-object-relationship-new-relationship--related-object-save-next](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship--related-object-save-next.png)
7. After selecting the associated object, select the specific field in that object to define the relationship. From the drop-down list, choose the appropriate field based on the required data association.
    ![hypha-object-relationship-new-relationship-related-object-field](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship-related-object-field.png)
8. After selecting the required field from the selected object for association, click Next to continue with the configuration. To preserve the current progress without proceeding further, click Save and resume the configuration later.
    ![hypha-object-relationship-new-relationship-related-object-field-save-next](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship-related-object-field-save-next.png)
9. On the subsequent screen, provide the required details to create the new field in the current object for establishing the association. Additionally, configure the deletion behavior for the field. You may choose to allow deletion, in which case the associated field will retain an empty value, or restrict deletion to prevent the field from being removed.
    ![hypha-object-relationship-new-relationship-related-object-fields](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship-related-object-fields.png)
10. After completing the relationship configuration and creating the necessary fields for the object association, click Save at the bottom of the screen to persist the configured relationship.
    ![hypha-object-relationship-new-relationship-related-object-save](/resources/Storage/hypha/images/hypha-object-relationship-new-relationship-related-object-save.png)

**Note**: If no relationships are configured for the selected object, the system displays an empty table with a message indicating that you can begin creating a new relationship.
