# Deployment Destination

<https://documentation.neutrinos.com/articles/#!trinity-publication/deployment>

Trinity empowers you to deploy an application by creating a deployment configuration and linking it to new or existing builds.

Before deploying an application:

1. Once the build setup is completed, verify whether the build status indicates success.
   ![](/resources/Storage/trinity-publication/deployment/crbuild.png)
2. If the build status is Success, click on the build and navigate to the Deployment section.
   Or
   If the build status is failed, navigate to logs and check the errors within the logs section.
3. Click on New Deployment and navigate to the Deployment configuration screen.
   ![](https://lh7-us.googleusercontent.com/4UU9UuHrUlm7sPZje5HhYlP1XyWitWYWuTnwy1sG62ym3AC5hsotL6QkRa79k9PlMmTYILTaFSA82MO6AJehYrhVJRe0X-w3CyK-ehPrfcWFJV0qtItf0ou7LydmRJZqh51-4Hk7TmbhXsKSX2qdwYI)
4. The Create deployment screen is displayed.
   ![](/resources/Storage/trinity-publication/deployment/createdeploy.png)

**Create Deployment**

The create deployment screen allows you to select the environment and edit variables that were created during app creation.

In the create deployment screen:

##### Deployment Destination

1. Navigate to Deployment destination section > select the deployment environment and version from the drop-down list.
   ![](https://lh7-us.googleusercontent.com/IQmunfdGozDf0YlA5t-5bDZdb9hVGClMO7tdjw-JhBsmO9G1iTbP4vH650UELK8C5a4UR1ishMicCnLqzZ9ZR7ewo7_9rCIP9GwNqHuz8OYQq9Ib-UrUV4_RLyGC3T4KyOpES0pofhUls8MQC41Rr3o)
2. To create a new version, click on the ![](https://lh7-us.googleusercontent.com/7BimnuZhr6x0CP2TnBKR2ymlbiicndfRJF2uVVgU3XJFcU85bmhAohx_OwuzFzHeApfzjtWQehc1Kn-LCzsp5R9CIPw2d0mB0hhbCYJ0dgrAvY4CmT0ln3vSKDY5Tq08zG5WI3DxXD1jalHQ75VZEDs) icon and create a new version.

##### Resource Allocation

This section allows you Customize the allocated resources (CPU, memory, replicas).

1. Navigate to the Resource Allocation section > view the allocated resource.
   ![](https://lh7-us.googleusercontent.com/daGxi3VEqgqbnmqtV8KH8MgFFYzYHJvZmMT9YlK6XWuQoW4IlU35Sm_C_BfChwK6OsxFtlOkBv9N3-PestMn-eKTab8mexS_k6jF7R-4uupUvMQXGeG47YWIGBbHDYeE27ylmmE5iRJmY5KwZpLrYcU)
2. To Edit allocation, click on the icon and modify accordingly.

##### Domain

This section allows you to select the domain and enable private url.

1. Navigate to domain > select the Domain from the drop-down list (If no domain found create a new domain).
   ![](/resources/Storage/trinity-publication/deployment/domainenable.png)
2. Select the checkbox corresponding to private url to enable private url.
3. Enter the sub domain.

##### Registry Secrets

1. Select the container registry secret from the drop-down list.
2. Click Save and Continue.

##### 

##### Probes

Probes are used to configure the health checks for the containerized application.

- Liveness: Click checkbox to enable liveness probes, which checks if the application is running.
- Readiness: Click checkbox to enable readiness probes, which check if the application is ready to serve traffic.
- Startup: Click checkbox to enable startup probes, which check if the application has started successfully.

#### Variables

Trinity enables you to select variables based on your requirement. There are multiple ways that can be used to select variables. They are:

##### Studio Environment

Trinity generates pre-defined environment variables for each of your deployments, containing information inferred from your deployment. Utilize these environment variables to retrieve information about your deployment.

##### Previous Deployment

Selecting this option will enable you to draw the variable set from a previously deployed version. You have the freedom to edit existing variables and create custom variables, but you cannot select any variable set from the Neutrinos Studio environment.

1. Select Previous deployment.
2. Select the available options from the drop-down list.
   ![](https://lh7-us.googleusercontent.com/AfRt6TupEBbgQE4QmhiS4MCWXtaQlMtGTJFnKnhjP9cbNzTB4D0t_-nbKokrjr8T8tQSjzFgsP0rLv_OARSxm6mCofCuNg3j1lo-B7xkhUovoatLRrnIUqhiymTwm-UQ6RUF9BZqneUibr0dBFFKax4)
3. Preview the list of selected variables from the previous version.
4. Click Next.

#### Create Variables

In this option, you won't have any preset variables to use. However, you can create your very own set of variables curated specifically for this deployment.

To create a new variable:

1. Select Create Variables.
   ![](/resources/Storage/trinity-publication/deployment/createdeploy.png)
2. Click Next.
   The Variables screen is displayed.
   ![](/resources/Storage/trinity-publication/deployment/revert1.png)
3. Enter the Variable name.
4. Select the variable type from the drop-down list.
5. Enter the value.
6. Click on the ![](https://lh7-us.googleusercontent.com/nMaLVBLDaKEK_pEWFhCvNWaNMOgUMw-k5o3qKsSFo28YfJgk7jNNUp9a0olzLvR899zl-yXck5-tWfcz04NMqLRtUwV6ToCPNTPS9Xwr_Iz_Apa7yTkOmFfuQf8rRl8i--PicuBWWv_qYJMCKeoCUoo) icon to create a variable.

##### Configurations

This is an optional screen that allows you to configure deployment related components it consists of:

- Nodepool - Use this to explicitly deploy a Pod to a specific node pool by setting a nodeSelector in the Pod manifest. This forces a Pod to run only on nodes in that node pool.
- Nginx - Use this specify an ingress class.
- Nexus - Use this to specify the nexus repository url.

##### Revert Manual Updates

Revert Manual Updates on the deployment screen is an option that allows users to undo or discard any changes they have manually made to the deployment configuration. This feature is particularly useful in environments where deployment configurations can be complex and unwanted changes can occur easily.

![](/resources/Storage/trinity-publication/deployment/revert2.jpg)

##### Stage

Staging refers to the process of deploying an application to a staging environment. This environment is typically a replica of the production environment but isolated from it. The purpose of staging is to perform final testing before the application is made live.

##### Add Comment

A text field to add comments, with a character limit of 40 characters.

#### Review

This screen allows you to review your selections and deploy the application.

![](https://lh7-us.googleusercontent.com/vQGfbVJqvazha9O-Qk19gHMSqo29dI47KArOYOWBnZZ0QJcwYT92956PXlugKUfhelv0pPOZNzcKn7troPY7c0x7r0R7oMqHyrojYqnX4asVp31bb9O82lSr7XVCtNgQy5B4TvzocXX8UZsEPJ8r8Xk)

1. Verify your selections.
2. If you want to change anything, click Edit to return to a previous screen and change the selection.
3. Click Deploy.
4. Trinity deploys this application and, if successful, displays it within the all deployments screen.
   Or
   Click Stage to deploy the application later.
