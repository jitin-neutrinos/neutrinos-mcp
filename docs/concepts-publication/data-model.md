# Data Model

<https://documentation.neutrinos.com/articles/#!concepts-publication/data-model>

Data modeling is the process of diagramming data flows. It is the first step in defining the structure of the available data. Data models comprises of datasets, which can be arranged in hierarchical structures of parent and child datasets. Each child dataset represents a subset of the dataset covered by its parent dataset. This model is used to define the characteristics of the data formats, structures, and database handling operations to efficiently support the data flow requirements.

**Benefits of Data Model:**

- **Reduced Costs** - Using Data Models as the nucleus for building applications results in lower project costs and error detection in early stages.
- **Higher Quality** - Data Models generate more questions, leading to higher integrity and defining business rules more accurately. Its visual nature facilitates communication and collaboration between stakeholders and subject matter experts.
- **Managed Risk** - Helps in understanding and mitigating any foreseen risk associated with it in the development phase.
- **Minimal Error rate** - Data models contain in-built queries that can reduce discrepancies and syntax errors.
- **Faster application Development** - Data models provide Drag-and-drop functionality and an intuitive visual UI to developers, increasing the productivity and faster application development.

**Terminologies**

The following table provides information about the terminologies used in Data Modelling.

| **Terminology** | **Description** |
| --- | --- |
| Entity | An Entity is a table within a data model. Each table has multiple columns and are interlinked with other tables in a data model. |
| Attribute | An attribute represents the column of a table. |
| Relationship | Describes how entities are inter-connected. |
| Reference Table | Used to resolve the many-to-many relationships among the entities into one-to-many and many-to-one relationships through a reference table. |
| Database Logical Design | Describes the database within a data model. |
| Logical Design | Here we create all the keys, tables, rules, constraints, etc. |
| Database Physical Design | Describes the file organization, internal database storage design and indexing techniques. |
| Physical Model | Describes the physical depiction of the database. |
| Schema | Detailed description of the database. |
| Logical Schema | Theoretical description of a database. |

Using Neutrinos studio you can design two types of data Model:

1. [Database Model](/articles/concepts-publication/database-model)
2. [Abstract Model](/articles/concepts-publication/abstract)
