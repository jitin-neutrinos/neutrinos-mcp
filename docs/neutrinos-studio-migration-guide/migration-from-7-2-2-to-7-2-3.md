# Migration Steps

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-from-7-2-2-to-7-2-3>

### Migration Steps

Make sure you [Migrate the App](/articles/neutrinos-studio-migration-guide/migrate-your-application) to Studio version 8.1.0 and perform the following steps:

**Regenerate IDS flows**

When you [enable IDS](/smart/project-sample-how-to-guide/configure-your-ids) for your app, default [IDS server flows](/smart/project-server-side-service-designer/ids-services) get auto-generated in Server Services. These server flows have bugs in previous versions. To regenerate error-free IDS flows, perform the following steps:

1. Delete the existing IDS flows and nodes in the Server Services Designer. This includes:
  - **ids** and** idsutil** server services.![auto-generated ids flows](/resources/Storage/neutrinos-studio-migration-guide/ids_floes.png)
  - **IDSAuthorizedAPIs** middleware sequence![IDS middleware sequence](/resources/Storage/neutrinos-studio-migration-guide/ids_middleware.png)
  - **ide:hrefstart** node in the global middleware sequence![ids:href start node](/resources/Storage/neutrinos-studio-migration-guide/ids_href.png)
2. Navigate to settings and click **Regenerate IDS Flows** to regenerate the correct IDS flows.![regenerate IDS flows](/resources/Storage/neutrinos-studio-migration-guide/regenerate_flows.png)
3. Navigate to **tsconfig.json** file in the respective app folder on your local machine.
  - Search for **"lib"** property in the file.
  - Change "**es2016**" to "**es2018**" inside the lib property.![tsconfig](/resources/Storage/neutrinos-studio-migration-guide/2020-02-12_15h31_25.png)
  - Save the file.
4. Save the app.

---

**NGFORAGE_MOBILE_DRIVER Env Variable**

- After migrating the application from any version lower than 7.2.3, the **NGFORAGE_MOBILE_DRIVER **env variable defaults to ****INDEXED_DB**.**
- Make sure to change the database that you had used in the application earlier. To change the value
- The databases that are supported are **LOCAL_STORAGE, WEB_SQL, and INDEXED_DB **

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | IOS 14 does not support the WebSQL database. |
| --- | --- |
