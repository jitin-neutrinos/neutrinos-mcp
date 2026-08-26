# Operations Properties

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/operations-properties>

| Property | Description |
| --- | --- |
| Operation Type | Indicates the type of Operation. This is a read-only-property. |
| Path | Refers to the path where the resource can be accessed. The path is auto-populated in the properties windowDefault format:${basePath}/dm/Entity-Name/Operation-Type |
| Middleware Sequence | You can choose a predefined middleware sequence to alter the behavior of the HTTP endpoint. |
| Pre & Post Operation Flow/Operation Flow | Refers to the custom flows that can be interpolated into HTTP endpoints to execute certain flows during the operation. These flows are created using the DM processor node in DM nodes.Similarly while working with an Abstract data model you can define a Service flow using the DM processor node which gets executed during the operation. |
