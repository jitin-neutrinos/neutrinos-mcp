# Create Deployment Unit

<https://documentation.neutrinos.com/articles/#!ai-hub/deployment>

Model deployment is the process of integrating a trained machine learning or AI model into a production environment where it can serve predictions and deliver real-time insights. On Neutrinos AI Hub platform, deployment enables users to operationalize their models—making them accessible via APIs or UI.

This step transforms a static, trained model into a functional service that can be consumed by external services. The Neutrinos AI Hub platform supports seamless deployment with configuration options for versioning, scalability, ensuring models are robust, secure, and performance-optimized in live environments.

## Create Deployment Unit

Creating a deployment unit is a critical step in operationalizing AI solutions, as it ensures that the model is portable, reproducible, and ready for integration with production systems. To create a deployment unit follow the steps below:

1. Click the Deployment from the left navigation panel.
    ![ai-hub-deployment-landing-page](/resources/Storage/ai-hub/images/ai-hub-deployment-landing-page.png)
2. On the Deployment page, you can create a deployment unit under either the Production environment or the Sandbox environment.
    ![ai-hub-deployment-select-environments](/resources/Storage/ai-hub/images/ai-hub-deployment-select-environments.png)
3. Select the preferred environment, then click the Add button located in the top-right corner of the page as shown in the image below:
    ![a-hub-deployement-envi-add-button](/resources/Storage/ai-hub/images/a-hub-deployement-envi-add-button.png)
4. Once the Add button is clicked, a pop-up window appears, prompting you to enter the name of the deployment unit, license key, and a description, as shown in the image below.
    ![ai-hub-deployment-unit-add](/resources/Storage/ai-hub/images/ai-hub-deployment-unit-add.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    For the Licence Key contact: subscription@neutrinos.com
5. Click the Submit button to create the deployment unit.

## Deploy Models

To add a model—either a prediction model or an extraction model—to the deployment unit, follow the steps below:

1. Click the desired model on the Model page. In the following steps, an extraction model is used to demonstrate how to deploy a model in a sandbox environment.
    ![ai-hub-deployment-select-model](/resources/Storage/ai-hub/images/ai-hub-deployment-select-model.gif)
2. From the model's Version page, select the version that you want to deploy:
    ![ai-hub-deployment-select-version](/resources/Storage/ai-hub/images/ai-hub-deployment-select-version.gif)
3. On the model’s Details page, click the kebab icon (three vertical dots) in the top-right corner of the page:
    ![ai-hub-deploy-model-kebab](/resources/Storage/ai-hub/images/ai-hub-deploy-model-kebab.png)
4. Select the environment in which the deployment unit was created. In this example, since the deployment unit was created in the Sandbox environment, select Sandbox. Then, enable the toggle next to Deploy to Sandbox.
    ![ai-hub-deployment-toggle](/resources/Storage/ai-hub/images/ai-hub-deployment-toggle.png)
5. Once the toggle is enabled, a pop-up screen appears prompting you to select a deployment unit. Choose the appropriate deployment unit from the available options in the dropdown list.
    ![ai-hub-deployment-select-unit](/resources/Storage/ai-hub/images/ai-hub-deployment-select-unit.png)
6. After selecting the deployment unit, click the Submit button in the pop-up window:
    ![ai-hub-deployment-submit](/resources/Storage/ai-hub/images/ai-hub-deployment-submit.png)
    The model is deployed to the selected unit, and a notification is displayed to inform users of the deployment progress.
    ![ai-hub-deployment-progress](/resources/Storage/ai-hub/images/ai-hub-deployment-progress.png)
7. After the process is completed, the environment where the model is deployed appears next to the Dashboard on the model’s Details page, displayed within a green, rounded rectangle. You can also refresh the page to see the updated deployment status.
    ![ai-hub-deployment-done](/resources/Storage/ai-hub/images/ai-hub-deployment-done.png)
    Additionally, the deployed version will display a Running status on the model’s Version page.
    ![ai-hub-deployment-running-version](/resources/Storage/ai-hub/images/ai-hub-deployment-running-version.png)

## Undeploy Model

To remove a model from a deployment unit, follow the steps below:

1. From the Model page—whether prediction or extraction—open the model, then open the deployed version of that model.
2. On the model’s Details page, in the Dashboard section, click the kebab icon located in the top-right corner of the page.
    ![ai-hub-deployment-undeploy-1](/resources/Storage/ai-hub/images/ai-hub-deployment-undeploy-1.png)
3. Disable the toggle next to the environment where the model is currently deployed.
    ![ai-hub-deployement-disable-toggle-undeploy](/resources/Storage/ai-hub/images/ai-hub-deployement-disable-toggle-undeploy.png)
4. In the pop-up window, click the confirm button to undeploy the model from the deployment unit.
    ![ai-hub-deployment-undeploy-confirm](/resources/Storage/ai-hub/images/ai-hub-deployment-undeploy-confirm.png)
5. Once the model is undeployed, the environment name previously displayed next to the Dashboard on the model’s Details page will be removed. Additionally, the deployment status on the Version page will change from Running to Stopped.
