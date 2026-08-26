# Interface

<https://documentation.neutrinos.com/articles/#!ai-hub/bring-your-own-model>

A Custom Model in AI Hub allows you to integrate user-owned or externally hosted AI models into the platform. These models can be connected by providing the required credentials and configuration details.

Once configured, the AI Hub platform establishes a secure connection to the model, making it available for use alongside built-in models. The Custom Model can then be selected and linked to Assistants to perform AI-driven tasks.

## Interface

The Custom Model interface is divided into two parts: the Configuration section and the Custom Models listing page, which displays the available custom models on the platform.

## Custom Model List

This page displays all custom models configured on the platform in a tabular format.




 ![ai-hub-custom-model-model-list](/resources/Storage/ai-hub/images/ai-hub-custom-model-model-list.png)

1. **Name**: Displays the name of the custom model created on the platform
2. **Model**: Displays the name of the model used to create the custom model on the platform.
3. **Last Updated**: Displays the most recent date and time of the latest modification made to the model.
4. **Created Date**: Displays the date and time when the custom model was created on the platform.
5. **Action**: Displays a kebab menu that provides options to edit or delete the custom model.

## Create Custom Model

To create a Custom Model on the platform, follow these steps:

1. You can create a Custom Model from any page in the platform. Click the Custom Model (![ai-hub-custom-model-icon](/resources/Storage/ai-hub/images/ai-hub-custom-model-icon.png)) icon at the top of the page to configure a new model or view the available Custom Models.
    ![ai-hub-custom-model-navigation](/resources/Storage/ai-hub/images/ai-hub-custom-model-navigation.png)
2. To create a new Custom Model, click Add Custom Model from the available options.
    ![ai-hub-custom-model-add-custom-model](/resources/Storage/ai-hub/images/ai-hub-custom-model-add-custom-model.png)
3. In the pop-up window, first select the provider. Available options include Azure OpenAI, OpenAI, Vertex AI, and Bedrock.
    ![ai-hub-custom-model-add-custom-model-available-providers](/resources/Storage/ai-hub/images/ai-hub-custom-model-add-custom-model-available-providers.png)
4. Based on the selected provider, the required fields are displayed to configure the model on the platform. The following table lists the fields specific to each provider:
    **Provider
    **
    **
    Fields**
    Azure OpenAI
    **Display Name**: Enter a name for the model being configured. This name is displayed for the model on the platform and is used when integrating the model with Assistants.
    **Model Deployment**: Select the model type to deploy, such as **GPT-4o**, **GPT-4.1-nano**, **GPT-4o Mini,** **GPT-4.1**, or **GPT-5**. Refer to the [models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai) available in Azure OpenAI to learn more about the supported model types.
    **API Base URL**: Provide the base endpoint URL for the model provider. This URL is used by the platform to connect to the deployed model. Example: https://YOUR-RESOURCE.openai.azure.com/
    **API Version:** Specify the API version supported by the provider. This ensures compatibility between the platform and the deployed model.
    **API Key**: Enter the authentication key used to access the model deployment securely. This key is provided by the model provider and is required to establish a secure connection.
    **Maximum Generation Tokens**: Define the maximum number of tokens the model can generate in a response. This helps control response length, performance, and cost.
    OpenAI
    **Display Name**: Enter a name for the model being configured. This name is displayed for the model on the platform and is used when integrating the model with Assistants.
    **Model Deployment**: Select the model type to deploy, such as **GPT-4o**, **GPT-4o Mini**, **GPT-4.1**, or **GPT-5**. Refer to the [models](https://developers.openai.com/api/docs/models/all) available in OpenAI to learn more about the supported model types.
    **API Key**: Enter the authentication key used to access the model deployment securely. This key is provided by the model provider and is required to establish a secure connection.
    **Maximum Generation Tokens**: Define the maximum number of tokens the model can generate in a response. This helps control response length, performance, and cost.
    Vertex Ai
    **Display Name**: Enter a name for the model being configured. This name is displayed for the model on the platform and is used when integrating the model with Assistants.
    **Model**: Select the Vertex AI model to be used for the custom model configuration. Available options include **Gemini 2.5 Pro**, **Gemini 2.5 Flash Lite**, and **Gemini 2.0 Flash**. Refer to the [models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/supported-models) available in Vertex AI to learn more about the supported model types.
    **GCP Project Name**: Provide the Google Cloud Project ID where the Vertex AI model is hosted.
    **GCP Location**: Specify the Google Cloud region where the Vertex AI model is deployed (for example, us-central1).
    **GCP Access Token**: Enter the access token used to authenticate requests to Vertex AI.
    **GCP Refresh Token**: Provide the refresh token used to generate new access tokens when the current token expires.
    **GCP Token URI**: Specify the token endpoint URI used to obtain and refresh authentication tokens.
    **GCP Client ID**: Enter the client ID associated with the Google Cloud service account or OAuth application.
    **GCP Client Secret**: Provide the client secret associated with the client ID for secure authentication.
    **Max Output Tokens**: Specify the maximum number of tokens the model can generate in a response.
    Bedrock
    **Display Name**: Enter a name to identify the custom model across the platform.
    **Model**: Select the AWS Bedrock model to be used for the custom model configuration. Available options include **Amazon Nova Lite v1**, **Amazon Nova Pro v1**, **Anthropic Claude Sonnet 4.5**, and **Anthropic Claude 3.7 Sonnet (APAC)**. Refer to the [models](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) available in Bedrock to learn more about the supported model types.
    AWS Region Name: Specify the AWS region where the model is deployed. Available options include **US East (N. Virginia)**, **US West (Oregon)**, **Asia Pacific (Tokyo)**, **Asia Pacific (Singapore)**, and **Asia Pacific (Mumbai)**.
    **AWS Access Key ID**: Provide the access key ID used to authenticate requests to AWS services.
    **AWS Secret Access Key**: Enter the secret access key associated with the AWS Access Key ID for secure authentication.
    **Max Tokens**: Specify the maximum number of tokens the model can generate in a response.
5. After providing the required configuration information for the custom model, click Test Connection at the bottom of the page.
6. After successfully testing the connection and verifying that the provided credentials and configuration details are correct, click Save Changes at the bottom of the page.

### Example

In this example, a custom model is created on the platform using the OpenAI provider.

1. From any screen on the platform, click the Custom Model icon on the top of the page, and choose Add Custom Model option from the dropdown.
2. In the pop-up window, provide the required configuration details for the custom model. The following image illustrates a sample configuration for creating a custom model using OpenAI.
    ![ai-hub-custom-model-add-custom-model-sample](/resources/Storage/ai-hub/images/ai-hub-custom-model-add-custom-model-sample.png)
3. After providing the configuration details, click Test Connection at the bottom of the page.
    ![ai-hub-custom-model-add-custom-model-sample-test](/resources/Storage/ai-hub/images/ai-hub-custom-model-add-custom-model-sample-test.png)
4. After the test connection is successful, click Save Changes at the bottom of the page to save the configuration.
    ![ai-hub-custom-model-add-custom-model-sample-test-save](/resources/Storage/ai-hub/images/ai-hub-custom-model-add-custom-model-sample-test-save.png)

## Integrate Custom Model

The custom model configured on the platform can be linked to an assistant after the configuration is completed successfully. To know more on integrating the custom model to an Assistant, refer [Link Custom Model](/articles/ai-hub/advanced-configuration-assistant/a/h2_1728526408) section, in Advanced Configuration - Assistant topic.
