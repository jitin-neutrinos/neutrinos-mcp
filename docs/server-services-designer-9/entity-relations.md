# Relation Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/entity-relations>

Relationships refers to how certain entities are related. In a relational database, a large amount of data is often broken down into multiple blocks of data which are known as entities and they are further associated with related entities. In Neutrinos data model, a relationship is represented by a line or an arrow between two entities.

### Relation Properties

To view the relation properties window, click on the edit attribute button ![](/resources/Storage/server-services-designer-9/concepts-2022-03-31-8.png) of the respective attribute for which the relationship is established.

In Neutrinos studio relationships have the following properties:

**Name:** refers to the number of possible related attributes between two entities. Neutrinos data model has the following types of relationships.

| **Name** | **Description** |
| --- | --- |
| One to One | One attribute in X entity is related with one attribute in Y entity. |
| One to Many | One attribute in X entity is related with multiple attributes in Y entity. |
| Many to many | Multiple attributes in X entity is related with multiple attributes in Y entity. |

**Target Entity: **refers to the entity which is used as a target in the relationship.

**Referenced Column: **refers to the mapped attribute in the target entity.

**Eager: **If enabled, eager loading allows to efficiently load related data and related objects along with the base attribute being queried.

**Relationid**: If eager is set to false, a new field called RelationId is displayed. RelationId allows you to retrieve only the identifier (ID) of related entities instead of fetching the entire related entity object. The relationid should not be the referenced column name or current column name.

![](/resources/Storage/server-services-designer-9/entity-relations/Relationid.png)

**On Delete & On Update:** Indicates what should happen to the associated object when an object is deleted or Updated. The following options can be configured for each end of the association:

| **Value** | **Description** |
| --- | --- |
| Restrict | Restricts the user from deleting/updating the parent attribute. |
| Cascade | The child attribute is deleted or updated if the parent attribute is deleted/updated. |
| Set Null | The child attribute is set to NULL when the parent attribute is deleted/updated. |
| Default | The child attribute is set to its default value if the parent attribute is updated/deleted. |
| No Action | Does not affect the child attribute if the parent attribute is deleted or updated. |
