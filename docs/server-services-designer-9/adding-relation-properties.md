# Adding Relation Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/adding-relation-properties>

After adding attributes, the relation properties need to be established between tables. This section will provide more information on adding relation properties and the interlinked fields in each table.

For more information on how to add a relation property, refer to the [Relationship](/articles/server-services-designer-9/entity-relations) section within this document.

The table given below provides information about relation properties and the linked fields in each table.

| **Table Name** | **Source Attribute** | **Target Attribute** | **Relation Type** |
| --- | --- | --- | --- |
| Agent | Policy | Agent(Policy Table) | Many to Many |
| Policy | Claims | Policy_id(claim table) | One to Many |
| Transaction | customer_id | Transaction_data(customer table) | Many to One |
| Customer | contacts | Customer_data(customer contact details table) | One to One |

![](/resources/Storage/server-services-designer-9/relational.png)
