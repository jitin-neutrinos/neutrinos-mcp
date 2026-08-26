# API Connector

<https://documentation.neutrinos.com/articles/#!ai-hub/add-connector>

To add a connector, follow these steps:

1. Navigate to the Connectors page using the left navigation panel.
2. On the Connectors page, click Add in the top-right corner.
3. The dropdown displays two options: API and MCP. Select the appropriate option based on your requirement.
    ![ai-hub-connectors-add-connector](/resources/Storage/ai-hub/images/ai-hub-connectors-add-connector.png)

## API Connector

API connectors refer to the configuration settings used to connect and integrate external and/or internal APIs with the Neutrinos platform. It allows users to seamlessly plug these services into the Assistant without requiring custom integration code.

To create a new API Connector on the AI Hub platform, follow the steps below:

1. After selecting API from the Add dropdown in the previous step, a window is displayed prompting you to enter the API name, authentication type, and JSON payload.
    ![ai-hub-connectors-add-api-config](/resources/Storage/ai-hub/images/ai-hub-connectors-add-api-config.png)
2. On the Create API Config page, enter the following details:
    Note: The parameters required to authenticate the API will vary depending on the selected authorization type as shown in the GIF below.
    ![ai-hub-connectors-api-connector-gif](/resources/Storage/ai-hub/images/ai-hub-connectors-api-connector-gif.gif)
    The table below outlines the required parameters for each supported Authentication Type:
    **
    Type
    **
    **
    Description**
    None
    This authentication type does not require any authorization credentials.
    API Key
    Requires a header key and value, as specified in the API key configuration..
    OAuth2
    Requires Client ID, Client Secret, Token URL, Scopes, and Grant Type, along with the token exchange method (either GET or POST).
    Bearer
    Requires the Bearer token to be passed as an authorization parameter in the request header.
    Basic
    Requires the username and password to be passed as authentication parameters.
    In the configuration section, define the API specification either in JSON (OpenAPI 3) format or in YAML. Regardless of the format, the editor automatically converts the input into a valid OpenAPI 3 structure.
  - Name: Provide a name for the API to help identify the configuration on the platform.
  - Authorization Type: Select the required authentication method. Options include None, API Key, OAuth2, Bearer, or Basic.
3. Once all required parameters are filled in and the JSON is provided in the correct format, click the Validate button at the bottom of the editor. This action validates the JSON input, and if it is valid, it dynamically generates the next sections of the page. These sections allow you to configure actions and define static values for various parameters—such as headers and other fixed parameters—that will always be included in API requests.
4. After providing the required headers and static (fixed) parameters, click the Create button at the bottom of the page to complete the configuration process. Once created, the API configuration will appear in the API Config page, as shown in the image below.
    ![api-config-created-list](/resources/Storage/ai-hub/images/api-config-created-list1.png)

# Example

This section demonstrates how to create an API configuration using a dummy JSON dataset for products. The example shows how to fetch product details through the API.

1. To create a new API configuration, navigate to the API Config page from the left navigation pane, and then click Add Config in the top-right corner.
2. On the Create API Config page, enter a name for the API and select the required authentication type—OAuth2, API Key, Bearer, or Basic—based on the API’s requirements. In this example, since the dummy API does not require authentication, select None.
3. In the editor, enter the JSON in OpenAPI 3 format for the Dummy JSON, and then click Validate at the bottom of the editor. The GIF below demonstrates how to enter the API name, set the authorization type, provide the JSON in the required format, and validate the JSON.
    ![ai-hub-api-config-creating-gif1](/resources/Storage/ai-hub/images/ai-hub-api-config-creating-gif1.gif)
4. Enter a static value for the parameters required by the API during execution (if any). In this example, a static parameter is added for the query, where the id value is set to 1. This returns the API response containing the data associated with an ID equal to 1. Click Save to save the parameters you have added. Then, click Create to generate the API configuration on the platform. The GIF below demonstrates how to add a static parameter and create the configuration.
    ![ai-hub-api-config-providing-static-parameters1](/resources/Storage/ai-hub/images/ai-hub-api-config-providing-static-parameters1.gif)
5. This configured API can now be triggered (used) from the assistant. For more information on how to trigger the configured API from Assistant, refer the [Trigger API - Assistant](/articles/ai-hub/toolsets/a/h2__1663136794) topic.

## MCP Connector

1. After selecting MCP from the Add dropdown in the previous step, a window is displayed prompting you to either create a new custom MCP or select from the list of available MCPs on the platform in the section below.
    ![ai-hub-connectors-add-mcp-config](/resources/Storage/ai-hub/images/ai-hub-connectors-add-mcp-config.png)
    Additionally, when selecting from the available MCP connectors, you can use the search bar to locate the required connector.
2. To add a new MCP connector, click the Add Custom MCP
    ![ai-hub-connectors-add--new-mcp-config](/resources/Storage/ai-hub/images/ai-hub-connectors-add--new-mcp-config.png)
3. On the next screen, you are prompted to provide details such as Name, MCP Server URL, Authentication Type, and an optional Description.
    ![ai-hub-connectors-add--new-mcp-config-details](/resources/Storage/ai-hub/images/ai-hub-connectors-add--new-mcp-config-details.png)
4. The authentication type selected in the previous step prompts you to provide additional details based on the chosen authentication method. The table below lists the supported authentication types and the corresponding details required for each type.
    **Authentication Type
    **
    **
    Details**
    None
    No additional details are required.
    API Key
    You are prompted to provide the Header Key and Header Value.
    OAuth2
    You are prompted to provide Client ID, Client Secret, Token URL, Scopes (read, write), Grant Type, and the Token Exchange Method (POST or GET).
    Bearer
    You are prompted to provide the Bearer Token.
    Basic
    You are prompted to provide the Username and Password.
5. After providing the required details, such as the connector name and authentication type, click Test Connection at the bottom of the page.
6. The tools available in the selected MCP are listed. Select the required tools using the corresponding checkboxes.
7. After selecting the required tools from the list, click Create to complete the connector creation process.
    A sample illustration of the steps to create the MCP connector is shown below.
    ![ai-hub-connectors-mcp-connector-example](/resources/Storage/ai-hub/images/ai-hub-connectors-mcp-connector-example.gif)

Additionally, you can add an icon for MCP connectors. This option is not available for API connectors. To change the icon for a connector, click the icon displayed to the left of the connector name. Select the option to change the icon, upload the required image, and follow the remaining steps as outlined above.




 ![ai-hub-connectors-add-connector-add-icon](/resources/Storage/ai-hub/images/ai-hub-connectors-add-connector-add-icon.png)

**Note:** Ensure that the servers for the MCP connectors are up and running before configuring the connectors. The servers can be hosted either locally or remotely.
