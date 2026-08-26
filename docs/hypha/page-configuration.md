# Page Configuration

<https://documentation.neutrinos.com/articles/#!hypha/page-configuration>

Page configurations are fundamentally designed around the Business Object, which serves as the central structural and logical unit of the system. A Business Object defines the data schema, including its fields, data types, relationships, validation constraints, and access controls. Every UI page - whether it is a List Page or Form Page - is essentially a configured representation of this underlying object. The pages do not independently define data structures; instead, they consume and render the metadata defined at the Business Object level.

When a page is configured, it references the Business Object and selectively determines how its fields should be presented and interacted with. For example, a List Page chooses which object fields appear as columns and how sorting or filtering should be applied. A Form Page organizes the same fields into sections and maps them to input controls for record creation or modification. Although these pages differ in interaction patterns, they all rely on the same object schema, ensuring consistency in data handling, validation, and backend integration.

This relationship creates a clear separation between the data model and the presentation layer. The Business Object defines *what *data exists and how it behaves, while the page configuration defines *how *that data is displayed and interacted with in the UI. Because of this metadata-driven approach, changes at the object level - such as adding a new field or modifying validation rules - can be reflected across associated page layouts without requiring code-level modifications. At the same time, page-level configurations can control layout, visibility, and user interaction without altering the underlying schema.

A Business Object defines:

- Object Name
- Field Definitions
- Data Types
- Constraints
- Relationships with other objects
- RBAC configuration
- Business rules

Each page type represents a different interaction model for the same Business Object.

| **Page Type  ** | **  Purpose  ** | **  Relationship to Business Object** |
| --- | --- | --- |
| List Page | Displays multiple records | Uses selected object fields as columns |
| Form Page | Creates or edits records | Renders object fields as input controls |

To learn more about page configuration in Studio, refer to the [Pages](/smart/project-alpha-platform/pages) topic.
