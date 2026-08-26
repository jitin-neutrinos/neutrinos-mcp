# Key Features

<https://documentation.neutrinos.com/articles/#!alpha-platform/environment-variables>

In Neutrinos Alpha Workflow Studio, Environment variables store sensitive values that should remain on the server side rather than being exposed in the UI. In Alpha Deployment, such environment variables are managed within the "Request App" of the application.
 The values of these environment variables are deployed at the cluster level and are not part of the UI application. They remain inaccessible outside the "Request App."

Due to the deployment topology, all requests from the Case Manager and Admin UI are routed through the Make Request application. The Make Request app resolves environment variables, retrieves the required values, and substitutes them before sending the HTTP request.

![environmentVariable](/resources/Storage/alpha-platform/images/environmentVariable.jpg)

## Key Features

1. **Global Scope**
  - Useful for defining common configurations like API base URLs and authentication tokens.
2. **Secure Storage**
  - Sensitive data such as API keys or credentials can be stored as environment variables instead of hardcoding them in application.

You can define the variables in the application as per the business process requirements. To add a new environment variable, follow the steps below:

1. In Config editor > Navigate to Environment Variable editor.
2. Click the **Add Variable** button > Enter the variable name. Ensure that name of the variable is same in both Workflow studio and the make request app.
3. Click the **Save** button.

The GIF below illustrates adding an Environment Variable in Workflow Studio:

![add-enviroment-variable-gif](/resources/Storage/alpha-platform/images/workflow-studio-config-add-enviroment-variable-gif.gif)

To access variables from Environment Variables when an event or trigger is called, follow these steps::

1. Select the component in a page to which the trigger or event needs to be added.
2. Double-click the component and navigate to the Trigger section.
3. Choose the event that should activate the trigger.
4. Click the **Plus** (+) button and select API Request > Expand the API request tab.
5. In attributes that support Environment Variables:
  1. Select **Environment** from the dropdown.
  2. Choose the applicable environment variable from the **Select Variable** dropdown.

The GIF below demonstrates how to use environment variables within an API trigger on submit button click.

![access-env-variables](/resources/Storage/alpha-platform/images/workflow-studio-config-trigger-access-env-variables-gif.gif)
