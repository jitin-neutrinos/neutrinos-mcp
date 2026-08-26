# Prerequisites

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-from-7-0-0-to-7-0-2>

### Prerequisites

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

### Migration Steps

#### IDS Flows

When you [enable IDS](/smart/project-sample-how-to-guide/configure-your-ids) for your app, default [IDS server flows](/smart/project-server-side-service-designer/ids-services) get auto-generated in Server Services. These server flows have bugs in version 7.0.0 and 7.0.1. To regenerate error-free IDS flows, perform the following steps:

1. Delete the existing IDS flows and nodes in the Server Services Designer. This includes:
  - **ids** and** idsutil** server services.
      ![auto-generated ids flows](/resources/Storage/neutrinos-studio-migration-guide/ids_floes.png)
  - **IDSAuthorizedAPIs** middleware sequence
      ![IDS middleware sequence](/resources/Storage/neutrinos-studio-migration-guide/ids_middleware.png)
  - **ide:hrefstart** node in the global middleware sequence
      ![ids:href start node](/resources/Storage/neutrinos-studio-migration-guide/ids_href.png)
2. Navigate to settings and click **Regenerate IDS Flows** to regenerate the correct IDS flows.
    ![regenerate IDS flows](/resources/Storage/neutrinos-studio-migration-guide/regenerate_flows.png)
3. Navigate to **tsconfig.json** file in the respective app folder on your local machine.
  - Search for **"lib"** property in the file.
  - Change "**es2016**" to "**es2018**" inside the lib property.
      ![tsconfig](/resources/Storage/neutrinos-studio-migration-guide/2020-02-12_15h31_25.png)
  - Save the file.
4. Save the app.
