# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-to-402>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

Follow these migration steps if you are migrating your app from Neutrinos Studio 6.0.x to 6.1.0.

If you are migrating your app from previous releases of Neutrinos Studio, perform the migration steps mentioned in the below topics (based on the version from which you are upgrading) before you proceed with this topic.

- [Migrate to 3.3.1](/articles/neutrinos-studio-migration-guide/migrate-to-3)

---

### Migration Steps

#### Migrate from 4.0.1 to 4.0.2

Replace the existing **Progress spinner** component by dragging and dropping a new one in place of the old one and update the attribute values.

---

#### Migrate from 3.3.x to 4.0.1

If your app uses Neutrinos Art for authentication, upgrade the **neutrinos-module **to **0.0.34 **and run the following command:

Copy CodeJavaScriptcordova plugin add cordova-plugin-uniquedeviceid

---
