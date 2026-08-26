# Azure DevOps

<https://documentation.neutrinos.com/articles/#!trinity-publication/azure-devops>

**Create a New Build**

If you have created a project using Azure, follow the steps given below to create a new build.

1. Navigate to the builds section and click on Create build.
   ![](/resources/Storage/trinity-publication/secrets/createnewbuild.png)
   This displays the Create Build pop-up window.
2. Select the build type.(In this case select build type as New).
3. Enter the following details:
   - Enter the Azure project name.
   - Enter the Azure DevOps application name.
   - Enter the branch.
   - Enter the base URL.
   ![](/resources/Storage/trinity-publication/secrets/Azure-1.png)
4. Click on Create to complete the build setup.

**Note**: After completing the above mentioned steps, navigate to the [Deploying Applications](/articles/trinity-publication/deploying-applications) section to deploy an application.

**Use an Existing Build**

1. Navigate to the builds section and click on Create build.
   ![](/resources/Storage/trinity-publication/secrets/createnewbuild.png)
   This displays the Create Build pop-up window.
2. Select the build type.(In this case select build type as Existing).
3. Enter the following details:
   - Enter the Docker Image URL.
   - Upload an app environment file.
   - Enter the base URL.
   ![](/resources/Storage/trinity-publication/secrets/Azurexist.png)
4. Click on Create to complete the build setup.
