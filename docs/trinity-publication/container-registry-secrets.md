# Container Registry Secrets

<https://documentation.neutrinos.com/articles/#!trinity-publication/container-registry-secrets>

Container registry secrets function as keys that unlock access to your private collection of container images. These secrets consist of credentials, typically including a username and password or a token, which authenticate and permit access to a specific container registry. This mechanism guarantees that only authorized users can pull and push images to and from the registry, ensuring the security of your valuable containers.

![](/resources/Storage/trinity-publication/container-registry-secrets/continue.jpg)

The icons present within the Container registry secrets screen are described in the below table

| Icon | Description |
| --- | --- |
| ![](/resources/Storage/trinity-publication/container-registry-secrets/refresh.png) | Click to refresh the container registry secret details. |
| ![](/resources/Storage/trinity-publication/container-registry-secrets/delete.png) | Hovering over the container registry secret name will display the delete icon. Clicking on this icon will delete the container registry secret. |
| ![](/resources/Storage/trinity-publication/container-registry-secrets/editicon.png) | Hovering over the container registry secret name will display the edit icon. Clicking on this icon will delete the container registry secret. |
| ![](/resources/Storage/trinity-publication/container-registry-secrets/view.jpg) | Click to view the password. |

To Create a Container Registry Secret:

1. Navigate to All Projects > Select a Project.
2. Click on Container registry secrets > New Registry Secret.
   ![](/resources/Storage/trinity-publication/secrets/CRS.png)
3. This displays the Create container registry secret pop-up window.
   ![](/resources/Storage/trinity-publication/secrets/CreateCrs.png)
4. Enter the following details:
   - Enter a display name
   - Enter the Registry URL
   - Select a Username and Password.
5. Selecting the checkbox corresponding to At Least one of the below inputs will be secret will provide you the following options:
   - Select an environment.
   - Select a username.
   - String – If selected, enter the string value.
   - Secret – If selected, existing secrets defined at the cluster level will be displayed. Select the appropriate secret.
6. Click Submit to create a secret.

**Note**: For Information related to defining a secret at cluster level, refer to [Kubernetes](https://kubernetes.io/docs/concepts/configuration/secret/) Documentation.
