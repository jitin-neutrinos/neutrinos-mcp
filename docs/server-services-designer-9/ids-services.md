# IDS Services

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/ids-services>

When you enable [IDS](/smart/project-concepts/identity-server) on the client, two new services are added to the [Server Services Designer](/smart/project-concepts/server-services-designer). They are:

- The [ids service](/articles/server-side-service-designer-publication/ids-sequence). It contains all the flows which create HTTP endpoints.
- The [idsutil service](/articles/server-side-service-designer-publication/ids-utility-sequence). It contains all the utility flows that facilitate the flows in the **ids **service.

![IDS services](/resources/Storage/server-services-designer-9/ids_services.png)

If you customize the IDS services and if you want to regenerate the default flows on Server Services, click the **Re-generate IDS Flows **button in the Neutrinos Studio **Settings** editor.
