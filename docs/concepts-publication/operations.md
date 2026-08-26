# Operations Type

<https://documentation.neutrinos.com/articles/#!concepts-publication/operations>

Neutrinos Data Model Editor allows you to seamlessly create HTTP endpoints for all the CRUD operations, which facilitates interaction with the database by communicating using REST APIs. Keeping in mind that you may need to inject custom validation (such as Authentication methods) into the HTTP endpoints to meet your application need, the data model editor provides you with the ability to configure middleware to be executed before the endpoint execution takes place and pre and post-execution flow to be executed during the database operation and bind them to your endpoint to alter the behavior of the HTTP request.

Click on [Entity Action](/articles/concepts-publication/entity) ![](/resources/Storage/concepts-publication/operations-2022-03-31.png)to add operations to an [entity](/articles/concepts-publication/entity).

### Operations Type

Neutrinos data model allows you to generate following type of [entity](/articles/concepts-publication/entity) operations.

| **Operation** | **Description** |
| --- | --- |
| Create | Creates a new attribute |
| Find-all | Returns all attributes of an entity |
| Find-by-id | Returns a specific attribute of an entity |
| Update-all | Updates all attributes of an entity |
| Update-by-id | updates a specific attribute of an entity |
| Delete-all | delete all attributes in of an entity |
| Delete-by-id | deletes a specific attribute of an entity |

### Operation Properties

You can find the description of the operation properties below.

| **Property** | **Description** |
| --- | --- |
| Operation Type | Indicates the type of the operation. This is a read-only property |
| Path | Refers to the path where the resource can be accessed. The path is auto-populated in the properties window**Default format:** ${basePath}/dm/Entity-Name/Operation-Type |
| [Middleware Sequence](/articles/concepts-publication/middleware-sequence) | You can choose a predefined middleware sequence to alter the behavior of the HTTP endpoint |
| Pre & Post Operation Flow/Operation Flow | Refers to the custom flows that can be interpolated into HTTP endpoints to execute certain flows during the operation. These flows are created using the [DM](/smart/project-server-side-service-designer/processor-node)[processor](/smart/project-server-side-service-designer/processor-node) node in DM nodesSimilarly while working with [Abstract](/articles/concepts-publication/abstract) data model you can define a** Service flow **using the [DM](/smart/project-server-side-service-designer/processor-node)[processor](/smart/project-server-side-service-designer/processor-node) node which gets executed during the operation |
