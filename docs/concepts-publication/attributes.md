# Types

<https://documentation.neutrinos.com/articles/#!concepts-publication/attributes>

Attributes are elements that describe and/or identify the entity. For example, a Customer entity typically has attributes for the name of the customer, an e-mail address, and other personal information. If we compare with databases, the attribute is a column in an [entity](/articles/concepts-publication/entity).

Each entity will by default consist a primary key id attribute.

To add an attribute:

1. Create an [entity](/articles/concepts-publication/entity).
2. Click on ![](/resources/Storage/concepts-publication/concepts-2022-03-31-7.png).
3. Define attribute type and properties.

### Types

Attributes in Neutrino studio can be of the following type:

| **Type** | **Description** |
| --- | --- |
| number | A whole number. The range of this type is –2,147,483,648 to 2,147,483,647. |
| string | A text containing letters, spaces, numbers and other characters. This type can be set to unlimited or limited it with the number of necessary symbols. |
| date | Date in following format YYYY-MM-DD |
| time | Time in following format hh:mm:ss[.nnnnnnn] |
| date time | A point in time that consists of a date and a time component, accurate up to milliseconds. |
| Boolean | Refers to the boolean data type which accepts the value as True or False. |
| Complex Type | Refers to a foreign key when the [relationship](/articles/concepts-publication/entity-relations) is established. |

### Attribute Properties

In studio you can define general and advance properties of an attribute. Click on edit attribute button ![](/resources/Storage/concepts-publication/concepts-2022-03-31-8.png) corresponding to an attribute to view the attribute properties window.

**Note: **If a relationship is defined for an attribute, the relation properties window will be displayed when the edit attribute button ![](/resources/Storage/concepts-publication/concepts-2022-03-31-8.png) is clicked.

**General Properties**

The general properties description is provided in the following table:

| **Property** | **Description** |
| --- | --- |
| Name | Defines the name of an attribute. |
| Type | Displays the attribute type. |
| Required Toggle Button | Indicates required properties. |
| Max Length | Defines the maximum length of the attribute value. |
| Minimum Length | Defines the minimum length of the attribute value. |
| Pattern | A regular expression in which the input's value must match the specified pattern for the value to pass validation. |
| Default | Refers to the default value of an attribute.**Note:** This property is only available for Date-time and Boolean datatype. |
| Select-Date | When you choose date-time as the datatype, this property provides a sub category to select date, date-time or time as the datatype. |

**Advance Properties**

Data model enables you to define the following advance properties based on the datatype you have chosen for the attribute.

| Property | Description | Value |
| --- | --- | --- |
| Database Datatype | Refers to the datatype of the attribute in the database table.**Note:** Data types can have different names in different database. For datatypes having identical names, the size and other details may vary. For more information refer to specific database documentation. |  |
| Precision | Refers to the number of digits within a number. Note: This property is not available for String datatype. |  |
| Scale | Refers the number of digits to the right of the decimal point in a number**.****Note:** This property is not available for String datatype. |  |
| Table Column Name | Refers to the name of the attribute in the database table.**Note:** This property specifically change the name of the attribute in the database. This change does not effect the name of the attribute in Studio. | Allows only Alphabets, numbers and Underscore as value. |
| Primary | Enables you to set an attribute as Primary key. |  |
