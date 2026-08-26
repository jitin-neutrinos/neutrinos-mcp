# Migrate from 7.0.2 to 7.1.0

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migrate-from-7-0-2-to-7-1-0>

| ![Information](/resources/Storage/neutrinos-studio-migration-guide/info.png) | Before following the below steps, please make sure you have already migrated the app to the latest version using Neutrinos Studio's auto migrate feature. |
| --- | --- |

**DB config nodes on Server Service Designer**

For any application you create using Neutrinos Studio version less than 7.1.0, in Server Services, the property type of the **DBConfig** node, whose type was selected to be **env** will be changed.

For Example, If the property type of the **Host** for an MSSql DBConfig was **env**, in version 7.1.0 it will become **String** on opening its attribute window.

This change is only in the UI which means the generated code is unaffected and your app will keep working as it was previously.

This change affects only if the properties are saved by clicking the **Done** button in its attribute window.

To fix this issue,

- Select **env** type manually for each property by opening the attribute window of the respective DBConfig and save it.
