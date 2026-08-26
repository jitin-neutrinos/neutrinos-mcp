# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-from-6-1-0-to-6-2-0>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

Perform these steps if you are migrating your app from Neutrinos Studio 6.0.x to 6.1.0.

If you are migrating your app from previous releases of Neutrinos Studio, perform the migration steps mentioned in the below topics (based on the version from which you are upgrading) before you proceed with this topic.

- [Migrate from 6.0 to 6.1](/articles/neutrinos-studio-migration-guide/migration-steps-from-6-0-0-to-6-0-4)
- [Migrate from 5.x to 6.0.0](/articles/neutrinos-studio-migration-guide/migrate-from-5)
- [Migrate to 4.0.2](/articles/neutrinos-studio-migration-guide/migrate-to-402)
- [Migrate to 3.3.1](/articles/neutrinos-studio-migration-guide/migrate-to-3)

For example, If you are migrating your app from Neutrinos Studio version 5.0.4 to version 6.1.0, perform migration steps mentioned in [migrate from 5.x to 6.0.0](/articles/neutrinos-studio-migration-guide/migrate-from-5) and then perform the steps mentioned below.

---

### Migration Steps

There are no manual migration steps for this release of Neutrinos Studio. Click the ![](/resources/Storage/neutrinos-studio-migration-guide/migrate.png) icon to migrate your app to the latest version.

| ![Warning](/resources/Storage/neutrinos-studio-migration-guide/warning.png) | In the 6.2.0 version of Neutrinos Studio, the ***ngfor** attribute in the Select component is replaced with **datasource, optionView, and optionValue **attributes. If you have used the** *ngfor** attribute, on migration to 6.2.0, the attribute value gets converted and gets assigned to the new attributes.For example, if this was the values assigned- ***ngFor="let i of item; let k = index;"** then a new index **i** will be created and the following attributes will be assigned with these values on migration:datasource=itemoption = i |
| --- | --- |
