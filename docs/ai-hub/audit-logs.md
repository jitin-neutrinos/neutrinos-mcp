# Audit Logs

<https://documentation.neutrinos.com/articles/#!ai-hub/audit-logs>

This topic provides an overview of the Audit Logs accumulated over time on the platform. It explains each section of the audit logs, detailing what each log entry represents and how the information can be interpreted.




 To access the audit logs, click Audit Logs in the left-side navigation bar. The landing page displays the logs in a tabular format, organized under multiple tabs, as shown in the image below:




 ![audit-logs-landing-page](/resources/Storage/ai-hub/images/audit-logs-landing-page.png)

1. **Login/Logout**: This tab displays a list of users along with their login and logout actions, including the date and timestamp for each activity. The information is presented in a tabular format.
    ![audit-logs-login-logout-page](/resources/Storage/ai-hub/images/audit-login-logout-page.png)
  1. **TimeStamp**: Displays the date and time when a user logged in or logged out of the platform.
  2. **User**: Displays the name of the user who logged in or logged out of the platform.
  3. **Event type**: Displays the type of event performed by the user. This can be either Sign In or Sign Out.
  4. **Status**: Indicates whether the event was successful or not.
  5. **Error Message**: If an error occurred during a Sign In or Sign Out event, the corresponding message is recorded and displayed in this column.
2. **Training**: This tab displays a list of models that have been trained on the platform. The information is presented in a tabular format.
    ![audit-logs-training-tab](/resources/Storage/ai-hub/images/audit-logs-training-tab.png)
  1. **Timestamp**: Displays the date and time when the model was trained.
  2. **User**: Displays the name of the user who trained the model.
  3. **Status**: Displays the current status of the model training process. Possible values include Completed, In Progress, Draft, and Created.
  4. **Model ID**: Displays the unique identifier assigned to each model during its creation.
  5. **Model Name**: Displays the name assigned to the model during its creation.
  6. **Model Type**: Displays the type of model. Possible types include Prediction – Text, Prediction – Document, Extraction – Text, Extraction – Document, or Assistant.
  7. **Event Type**: Displays the type of training performed on each model. It can be either Train, indicating the model was trained for the first time, or Retrain, indicating the model was re-trained.
  8. **Action**: Displays the action performed on the individual model. Possible actions include Create, Update, Update-Draft, or Remove.
3. **Deployment**: This tab displays a list of deployed models. Models may be deployed in either the Sandbox or Production environment. The information is presented in a table that includes the following fields, as shown in the image below:
    ![audit-logs-deployment](/resources/Storage/ai-hub/images/audit-logs-deployment.png)
    You can search for a deployed model using the search bar at the top of the page. Additionally, deployment details can be filtered by date and time, including a custom date and time range. The number of rows displayed can also be adjusted using the Show By dropdown. By default, 10 rows are displayed.
  1. **Timestamp**: Displays the date and time when the model was deployed.
  2. **User**: Displays the name of the user who deployed the model.
  3. **Deployment ID**: Displays the deployment ID generated when the model is deployed.
  4. **Status**: Displays the current status of the model deployment process. Possible values include In Progress, Running, or null.
  5. **Environment**: Displays the environment in which the model was deployed—either Sandbox or Production.
  6. **Model Name**: Displays the name assigned to the model during its creation.
  7. **Version**: Displays the version of the model that is currently deployed.
  8. **Duration**:
  9. **Error Message**: Displays any error encountered during the deployment of the model.
4. **Inferencing**: This tab lists the models that call the Inference APIs. The details are presented in a table as shown in the image below.
    ![audit-logs-inferencing-tab](/resources/Storage/ai-hub/images/audit-logs-inferencing-tab.png)
  - **Timestamp**: Displays the date and time when the the Inference APIs was called.
  - **User**: Displays the name of the user who called the Inference APIs for the model.
  - **Inference ID**: Displays the ID generated for each Inference API call.
  - **Status**: Displays the status of each Inference API being called. It can be In Progress, Completed, or Created, or Initiated.
  - **Environment**: Displays the environment (Production or Sandbox) in which the Inference API was called. This depends on the environment where the model was deployed.
  - **Model Name**: Displays the model associated with the Inference API call.
  - **Version**: Displays the version of the model associated with the Inference API call.
5. **Token**: This tab displays a list of tokens created for specific models under the Tokens section. Token details are presented in a table as shown in the image below. To learn more about creating tokens, refer [Tokens](/articles/ai-hub/tokens) topic.
    ![audit-logs-tokens](/resources/Storage/ai-hub/images/audit-logs-tokens.png)
    Tokens can be searched using the search bar at the top of the page. Additionally, you can filter tokens by date and time, including a custom date and time range. The number of rows displayed can also be adjusted using the Show By dropdown. By default, 10 rows are displayed.
  1. **Timestamp**: Displays the date and time when the token was created.
  2. **User**: Displays the name of the user who created the token.
  3. **Token ID**: Displays the token ID generated at the time of token creation.
  4. **Action**: Displays the action performed on a specific token—Create if the token was created, or Remove if the token was removed or revoked.
  5. **Model**: Displays the name associated with the token that was created.
  6. **Environment**: Indicates whether the token was created in the Sandbox or Production environment for a specific model.
  7. **Expiry Date and Time**: Displays the expiration date and time set at the time of token creation.
  8. **Status**: Displays the token status—active or inactive—based on whether the expiration date and time has passed.
