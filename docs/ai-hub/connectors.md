# Why Connectors

<https://documentation.neutrinos.com/articles/#!ai-hub/connectors>

Connectors allow agents to interact with external systems, services, and data sources. They act as bridges that enable agents to retrieve data, invoke APIs, trigger workflows, and communicate with external tools.

By integrating with enterprise systems, connectors enable AI agents to move beyond static reasoning and perform real-world actions.

## Why Connectors

AI systems typically need to:

- Retrieve external data
- Execute actions in third-party systems
- Call internal enterprise APIs
- Interact with databases
- Use external tools or services

**Note**: Connectors provide a standardized and reusable mechanism to enable these capabilities without hardcoding integrations inside agents.

## Types

AI platforms typically support the following connector types:

### API Connectors

API connectors enable agents to communicate with REST, GraphQL, or SOAP APIs.

**Capabilities**

- Send HTTP requests
- Handle authentication (OAuth, API key)
- Parse API responses
- Trigger external workflows

**Use Case**

- Fetch customer data from CRM
- Create tickets in support systems
- Query internal microservices

**Example Flow**: Agent -> Connector -> External API -> Response -> Agent

## MCP Connectors

MCP (Model Context Protocol) connectors enable agents to communicate with tools, services, and resources exposed through MCP-compliant endpoints.

**MCP provides**:

- Standardized tool discovery
- Structured tool execution
- Context-aware integrations
- Secure tool access

**Capabilities**:

- Discover available tools dynamically
- Execute tool functions
- Retrieve structured responses
- Maintain contextual memory

**Example Use Case**

- Connect to internal knowledge bases
- Execute automation tools
- Query structured enterprise systems
- Integrate AI-native services

**Exaple Flow**: Agent -> MCP Connector -> MCP Server -> Tool Execution -> Response -> Agent

## Interface

The Connectors page displays the list of connectors available on the platform in a tabular format.




 ![ai-hub-connectors-landing-page](/resources/Storage/ai-hub/images/ai-hub-connectors-landing-page.png)

1. **Connector**: Displays the name of the connector specified during connector creation.
2. **Type**: Displays the connector type. The supported types are API and MCP.
3. **Authentication**: Displays the authentication type configured for the connector during creation. Supported authentication types include None, API Key, OAuth2, Bearer, and Basic.
4. **Created Date**: Displays the timestamp indicating when the connector was created.
5. **Created By**: Displays the user ID of the individual who created the connector on the platform.
6. **Action**: Displays a kebab menu icon. Clicking the icon provides the option to delete the selected connector.
7. Click the caret icon at the end of a connector record to expand it. The expanded view displays details such as Version, Training Status, Deployment Status, Author, and Last Updated Date & Time. The Actions column includes a kebab icon that allows you to delete a specific version of the connector.

Additionally, you can use the checkbox at the beginning of each row to select individual connectors, or use the checkbox in the header row to select all connectors displayed on the current page.

You can search for a specific connector by name. The list can also be filtered using the available filter options, APIs, or MCP, located next to the search bar.

Pagination controls are available in the bottom-right corner of the page, allowing you to choose the number of connector records displayed per page and navigate between pages.
