# Filter-by

<https://documentation.neutrinos.com/articles/#!concepts-publication/filter-by>

In Data Model Nodes, a Filter-by is a set of comparisons that must be true for a data item to be returned. These comparisons are typically between field names and their associated values.

The Filter clause typically extends the SQL query by an additional where clause.

**Operators **

The filter by/where conditions allows you to perform a database operations with AND & OR operators. You can find the descriptions and the value format for these operators below.

| **Name** | **Description** | **Value** |
| --- | --- | --- |
| AND | The AND operator displays a record if all the conditions separated by AND are TRUE | should be declared as a collection object separated by a ',',Example: To run the following querySELECT * FROM "user"WHERE "firstName" = 'Timber' AND "lastName" = 'Saw' Specify {firstName: "Timber", lastName: "Saw"} |
| OR | The OR operator displays a record if any of the conditions separated by OR is TRUE. | OR operator should be declared as an Array of objects where each objects are separated by a ','Example: To run the following querySELECT * FROM "user" WHERE ("firstName" = 'Timber' AND "lastName" = 'Saw') OR ("firstName" = 'Stan' AND "lastName" = 'Lee')Specify [ { firstName: "Timber", lastName: "Saw" }, { firstName: "Stan", lastName: "Lee" } ] |

**How to use**

Neutrinos data model nodes ([Find](/smart/project-server-side-service-designer/find-node), [Remove](/smart/project-server-side-service-designer/delete-node), [Update](/smart/project-server-side-service-designer/update-node))properties allows you to define the filter by attribute:

You can map this field to the below properties.

| **Property Name** | **Description** |
| --- | --- |
| bh. | If you map the filter by field to bh. property, define the filter condition by declaring a variable using script, start or processor node and then select the variable as the value. |
| bh.input/bh.local | If you map the filter by field to bh.input/bh.local properties, define an input/local variable in the start node and select the variable as the value |
| as is | If you map the field to as is property, define the filter condition in the text field associated with the filter by attribute. |

See [Properties](/articles/server-services-designer-8/properties-in-server-services) to learn more about these variables/flow objects.
