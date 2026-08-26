# Constraints

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/constraints>

Constraints are rules enforced on the data columns of an entity. These are used to limit the type of data that can enter a table. This ensures the accuracy and reliability of the data. The neutrinos data model(database) contains the following constraints:

- **Check Constraint**: ensures that all the values in a column satisfy the specified conditions. For example, we can limit the value range for an attribute. To create a check constraint for an entity:
  - Click on the ![](/resources/Storage/server-services-designer-9/constraints-2023-04-27.png) corresponding to an entity.
  - Select Check.
  - Click on Add new in the check constraint window to add a check constraint.

![](/resources/Storage/server-services-designer-9/Checkconstraint.png)

- **Unique Constraint** : ensures that all values in a column or a group of columns are different. For example, you can add multiple columns together to be defined as unique.

To create an unique constraint:

- Click on the ![](/resources/Storage/server-services-designer-9/constraints-2023-04-27-1.png) corresponding to an entity.

- Select unique.

- Click on Add new in the Unique constraint window.

- **Index** - It is created to group multiple columns together to improve performance while retrieving the data.
- **Users** - Displays the service flows which are using the entity for database operations.t topic template.
