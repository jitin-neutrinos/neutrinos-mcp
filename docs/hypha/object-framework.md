# Key Components of Object Framework

<https://documentation.neutrinos.com/articles/#!hypha/object-framework>

An object framework provides a blueprint to model real-world data assets (like datasets, files, tables, APIs, policies, etc.) as objects with properties, relationships, and behaviours. This enables consistent data representation, access, and governance across hybrid and multi-cloud architectures.




 **Note**: Objects are created with a tenant-wide scope, meaning any schema within the organization can access them.

# Key Components of Object Framework

| **  Component   ** | **  Description** |
| --- | --- |
| Data Objects | Represent structured/unstructured data entities (e.g., tables, blobs, documents). |
| Metadata Objects | Define technical, business, and operational metadata (schemas, lineage, tags, etc.). |
| Policy Objects | Enforce data access, retention, and compliance rules (e.g., RBAC, GDPR policies).Service Objects |
| Service Objects | Abstract reusable data services (e.g., transformation, cataloging, masking). |
| Relationship Mapping | Define how objects relate (e.g., a dataset linked to a policy or transformation pipeline). |

## Purpose

1. Unified Abstraction: Decouples data representation from physical storage or sources.
2. Reusability: Objects can be reused across pipelines, catalogs, or workflows.
3. Extensibility: New object types or behaviors can be added without disrupting existing systems.
