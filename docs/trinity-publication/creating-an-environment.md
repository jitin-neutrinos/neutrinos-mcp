# Creating an Environment

<https://documentation.neutrinos.com/articles/#!trinity-publication/creating-an-environment>

When logging into Trinity for the first time, an environment has to be Initialized. The steps for the same are provided below.

**Pre-requisites**:

- Obtain the Kubernetes configuration file.
- Obtain the Service access Key file.

To create a new environment:

1. Within the left navigation panel, Click on ENVs > New Environment.
   ![](/resources/Storage/trinity-publication/creating-an-environment/Newenv_2.png)
   The Initialise environment screen is displayed.
   ![](/resources/Storage/trinity-publication/creating-an-environment/Init.png)
2. There are currently five available clusters supported by Trinity:
   - Google
   - AWS
   - On Local Premise
   - Microsoft Azure
   - Oracle
3. Select one of the cluster provider (we have considered an example of Microsoft Azure) and:
4. Select the auth type as: ACLI (Azure Command Line Interface. This is used to connect to Azure and execute administrative commands on Azure resources) **Or** SPN (Service principals that can be used to authenticate applications and services).
5. Upload the already obtained Kubernetes config file.
6. If there are multiple clusters within the Kubernetes config file, select the appropriate cluster from the list.
   ![](/resources/Storage/trinity-publication/creating-an-environment/multipleclusters.png)
7. Upload the Service account file.
8. Enter the environment name, description and click Initialise.
9. If the initialisation process is successful, the all environments screen will display the environment details with a status as "Success".
   Or
   If the initialization process is failed, the all environments screen will display the environment details with status as “Failed”.
