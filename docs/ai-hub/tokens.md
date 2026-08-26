# View Tokens

<https://documentation.neutrinos.com/articles/#!ai-hub/tokens>

AI Hub APIs can be consumed using tools such as Swagger or Postman, or integrated into other applications to leverage the AI and ML capabilities offered by the platform. To access these APIs, an authorization token is required. This token can be generated directly from the AI Hub platform and serves as a centralized token that can be used across multiple applications.

Click Tokens from the left navigation bar to open the tokens page as shown in the image below:

![ai-hub-tokens-landing-page](/resources/Storage/ai-hub/images/ai-hub-tokens-landing-page.png)




 Tokens can be created for either the production environment or the sandbox environment.

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | Note: Tokens are model-specific. Each model must have its unique token to test its corresponding API or to integrate it for consumption by upper-layer services. |
| --- | --- |

## View Tokens

To view the tokens created in a specific environment, select either Production or Sandbox from the left side of the Access Tokens page. The image below illustrates tokens created in the Production environment. Token details are displayed in a tabular format for both Production and Sandbox environments.




 ![ai-hub-tokens-production](/resources/Storage/ai-hub/images/ai-hub-tokens-production.png)

- **Name**: Displays a list of names of the token created for the respective environment.
- **Created Date and Time**: Displays the date and time when the token was created.
- **Last Accessed Date and Time**: Displays the date and time when the token was last used.
- **Expiry**: Displays the expiry time for a token. The expiry can be 30 minutes, 3 hours, or set to Never.
- **Actions**: This column provides the option to revoke a token. Click the Revoke button to delete a token that is no longer needed or should not be used in the future.

You can also search for created tokens using the search bar at the top of the page. Additionally, you can choose to view up to 30 tokens in the table by selecting the number of rows to display from the control on the right side of the page. By default, 10 rows are displayed.




 ![ai-hub-tokens-search-view](/resources/Storage/ai-hub/images/ai-hub-tokens-search-view.png)

## Create Token

To create a token, follow the steps below:

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | Tokens can only be generated for models that have already been deployed. You can create a token for Prediction, Extraction, or Assistant models. |
| --- | --- |

1. Click Tokens in the left navigation bar to open the Tokens landing page.
2. Choose the environment for which you want to create a token. You can select either the Production or Sandbox environment. For illustration purposes, we have selected Sandbox as the environment, as shown in the image below:
    ![ai-hub-tokens-sandbox-env](/resources/Storage/ai-hub/images/ai-hub-tokens-sandbox-env.png)
3. Click the Add button at the top right of the page to open a pop-up window for adding an access token.
    ![ai-hub-tokens-sandbox-add-button](/resources/Storage/ai-hub/images/ai-hub-tokens-sandbox-add-button.png)
4. In the Add Access Token pop-up window, enter the following details to create a token.
    ![ai-hub-tokens-sandbox-add-access-token-pop-up](/resources/Storage/ai-hub/images/ai-hub-tokens-sandbox-add-access-token-pop-up.png)
  - **Name**: Enter a name for the token you are creating.
  - **Training Type**: Select the model type from the dropdown for which the token is being created: Prediction, Extraction, or Assistant.
  - **Data Type**: Select the type of data the model was originally created from from the dropdown: Text or Document.
  - **Models**: From the list of deployed models in the Models dropdown, select the model name.
  - **Model Version**: Choose the version of the model for which the token needs to be created. There may be multiple versions of a model available; select the one you require.
  - Choose the token expiry time from the dropdown: 30 minutes, 3 hours, or Never.
  - Click the Save button to complete the process and add the token to the selected environment.
5. Click the Okay button to finish the process of adding the token.
    ![ai-hub-tokens-sandbox-added](/resources/Storage/ai-hub/images/ai-hub-tokens-sandbox-added.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note that the token value generated is only available until the OK button is pressed. Make sure to store the token in a safe place for future use, as it will not be visible again. However, you can revoke and create a new token if you lose the original one.

The added token will be reflected in the list of tokens for the specific environment.




 ![ai-hub-tokens-sandbox-final](/resources/Storage/ai-hub/images/ai-hub-tokens-sandbox-final.png)
