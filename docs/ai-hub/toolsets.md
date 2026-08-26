# Set Knowledge Source

<https://documentation.neutrinos.com/articles/#!ai-hub/toolsets>

This section explains the toolsets available in the Assistant and how they can be implemented.

## Set Knowledge Source

To add a knowledge source or data source for the assistant to reference and provide contextually relevant responses to user queries, follow the steps below:

1. Navigate to Assistant using the main navigation bar. Then, click Knowledge from the left-side navigation panel on the assistant page to open the knowledge panel for the selected assistant.
    ![assistant-knowledge-landing-page](/resources/Storage/ai-hub/images/assistant-knowledge-landing-page.png)
2. Click the **Map Source** button on the top right of the page to open the **Map Knowledge Source** pop-up window.
    ![assistant-knowledge-map-source](/resources/Storage/ai-hub/images/assistant-knowledge-map-source.png)
3. In the pop-up window, select the Source Type and the Source File from their respective dropdown menus. The source type can be an Excel file, a document, or a web page that has been previously added as a knowledge source on the Knowledge page. For more information on creating a knowledge source, refer [Knowledge](/articles/ai-hub/knowledge) topic.
    ![assistant-knowledge-map-source-pop-up](/resources/Storage/ai-hub/images/assistant-knowledge-map-source-pop-up.png)
4. Once the Source Type and Source File are selected, you will have the option to set this source as the default for the assistant. By default, this checkbox is unchecked. If enabled, the assistant will use the selected knowledge source as the default reference for generating responses to user queries.
5. Click the **Add** button in the pop-up window to finalize and add the selected data source for the assistant.

| ![Note](/resources/Storage/ai-hub/project-trailproject/note.png) | Note: You can add multiple knowledge sources to an Assistant. These sources are referenced when generating responses to user queries. An Assistant can have up to 10 knowledge sources. |
| --- | --- |

## Invoking Connectors

This section explains how to trigger a configured API or an MCP connector from the Assistant in the AI Hub platform.

### API Connector

Follow these steps to configure an API connector that can be triggered from an Assistant in the AI Hub platform:

1. Navigate to Assistant and open the specific Assistant from which you want to trigger a configured API, based on your requirements. In this example, a dummy Assistant is used to trigger the dummy API that was configured to return product details.
    ![ai-hub-api-config-call-api-initial](/resources/Storage/ai-hub/images/ai-hub-api-config-call-api-initial1.png)
2. On the opened Assistant page, select the required version from which you want to trigger the API, based on your requirements.
    ![ai-hub-api-config-seelct-version](/resources/Storage/ai-hub/images/ai-hub-api-config-seelct-version1.png)
3. In the opened Assistant version, use the left navigation menu to open the API Configuration page. If no APIs have been configured to be triggered, the page will not list any configurations. Otherwise, all APIs configured for the Assistant are displayed in a tabular format with the following columns:
  - Name – The name of the API configuration provided during setup.
  - Created Date – The date and timestamp when the API was configured on the platform.
  - Action – Contains a kebab menu (⋮) that allows you to delete an API configuration if it is no longer required by the Assistant.
4. To add a new API configuration, click the Map Source button at the top of the page.
5. In the pop-up window, choose the required configured API from the dropdown menu. If the API contains multiple endpoints, you can either select only the endpoints that need to be triggered from the Assistant or choose to trigger all endpoints by selecting All Endpoints. In this example, since there is only one endpoint, select it, and then click Add in the pop-up window to complete the configuration. The GIF below demonstrates how to select the required API configuration from the pop-up window and map it to be triggered from the Assistant.
    ![ai-hub-api-config-map-source1](/resources/Storage/ai-hub/images/ai-hub-api-config-map-source1.gif)
6. Once the API config source is mapped, click the Assistant icon to test the API mapping. This allows you to verify whether the correct API endpoint is being triggered and confirm that the response matches the expected result.
    ![ai-hub-api-config-triggering-api-assistant](/resources/Storage/ai-hub/images/ai-hub-api-config-triggering-api-assistant1.gif)

### MCP Connector

Follow these steps to configure an MCP connector that can be triggered from an Assistant in the AI Hub platform:

1. Navigate to Assistant and open the required Assistant from which you want to trigger the configured MCP connector. In this example, a dummy Assistant is used to trigger a dummy MCP connector configured to perform value conversion and calculation.
    ![ai-hub-connectors-integrate-assistant-mcp](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp.gif)
2. On the Assistant page, navigate to the Connectors section from the left navigation panel.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-section](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-section.png)
3. The Connectors page displays all connectors associated with the Assistant in a tabular format, including the following details:
    ![ai-hub-connectors-integrate-assistant-mcp-connector-section-empty](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-section-empty.png)
  - **Name**: Displays the name of the specific connector associated with the Assistant.
  - **Type**: Displays the type of the specific connector associated with the Assistant.
  - **Created Date**: Displays the creation timestamp of the specific connector associated with the Assistant.
  - **Action**: Contains a kebab menu (⋮) that allows you to delete an MCP configuration if it is no longer required by the Assistant.
4. If no connectors are associated with the Assistant, the table displays a message indicating that no connectors are mapped to the Assistant. To map a new connector to the Assistant, click Map Source at the top of the page.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-map-source](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-map-source.png)
5. In the pop-up window, select the connector type that you want to associate with the Assistant. In this example, the MCP connector is selected.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-choose-mcp](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-choose-mcp.png)
6. After selecting MCP from the first dropdown, choose the required MCP connector from the second dropdown. You can either scroll through the list or use the search bar within the dropdown to quickly find the connector.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp.png)
    From the selected MCP connector, choose the required endpoints from the list of available endpoints. These endpoints enable the Assistant to use them to provide context-aware responses to user queries.
7. Click Add at the bottom of the pop-up window to complete the connector integration with the Assistant.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp-add](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp-add.png)
8. Once the connector is successfully added, it appears in the list of connectors associated with the Assistant.
    ![ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp-add-success](/resources/Storage/ai-hub/images/ai-hub-connectors-integrate-assistant-mcp-connector-select-mcp-add-success.png)

The following illustration demonstrates how to trigger an MCP connector from the Assistant. After associating the connector in the Instructions tab, provide the required instructions for the Assistant based on your use case. The example below illustrates triggering an MCP connector:



![ai-hub-connectors-mcp-trigger-example](/resources/Storage/ai-hub/images/ai-hub-connectors-mcp-trigger-example.gif)
