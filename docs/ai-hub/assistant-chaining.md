# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/assistant-chaining>

Assistant Chaining enables an Assistant to be linked to one or more other models, such as a Prediction Model, an Extraction Model, or other Assistants. This capability helps distribute responsibilities across multiple models, reducing the processing responsibility on a single model.

Assistant Chaining allows you to create a network of specialized Assistants, creating a modular approach that improves performance. When assistant chaining is configured, multiple AI Assistants, each designed for a specific task, are linked together to form a coordinated execution flow. A primary Assistant serves as the entry point for user requests and orchestrates interactions with specialized Assistants based on the request's nature. This approach distributes responsibilities across multiple purpose-built models, enabling efficient request handling and improved response quality without overloading a single model with diverse tasks.

To chain Assistants in the AI Hub platform, follow the steps below:

1. Navigate to the Assistants page from the left navigation panel. Then, select the Assistant to which you want to link other Assistants.
2. On the Assistant page, under the Versions tab, select the required Assistant version to chain with other Assistants.
3. Using the left navigation panel in the assistant page, navigate to the Link models.
    ![ai-hub-assistant-chaining-empty-table](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-empty-table.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: When no model is linked to the Assistant, an empty table is displayed.
  - **Model Name**: Displays the name of the model linked to the Assistant.
  - **Version**: Displays the version of the model linked to the Assistant.
  - **Model**: Displays the type of model linked to the Assistant, such as Prediction, Extraction, or another Assistant.
  - **Description**: Displays the description provided during the linking process, which gives context about the linked model and the capabilities available when it is associated with the Assistant.
  - **Last Updated**: Displays the date and time of the most recent modification made to the model linked to the Assistant.
  - **Action**: This column displays a kebab menu icon that provides options to edit or unlink the model from the Assistant. The Edit option allows you to select a different version of the model currently associated with the Assistant. The Unlink option allows you to completely unlink the model from the Assistant.
4. Click the Link Model button on the top right of the page.
    ![ai-hub-assistant-chaining](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining.png)
5. In the pop-up window, select the type of model to link from the first dropdown. The available options include Prediction, Extraction, or Assistant models.
    ![ai-hub-assistant-chaining-options](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-options.png)
6. When a Prediction, Extraction model, or an Assistant is selected, the required details must be provided as described in the following table:
    **Type of Model**
    **Fields**
    Prediction / Extraction
    **Data Type**: Select the type of model - Text Prediction/Extraction or Document Prediction/Extraction.
    **Model**: Select a prediction model from the list, or use the search option in the dropdown to locate a specific model to link to the Assistant.
    **Model Version**: Select the specific version of the chosen model to link to the Assistant.
    **Description**: Provide a description for the Assistant. This is a mandatory field that provides context for why a specific model version is linked to the Assistant.
    Assistant
    **Model**: Select an Assistant model from the list, or use the search option in the dropdown to locate and link a specific model to the Assistant.
    **Model Version**: Select the specific version of the chosen Assistant to associate with this Assistant.
    **Description**: Provide a description for the Assistant. This is a mandatory field that provides context for why a specific model version is linked to the Assistant.
7. After completing and verifying all the fields required to link the model to the Assistant, click Add at the bottom of the pop-up to successfully map the model to the Assistant.
    ![ai-hub-assistant-chaining-fields-added-save](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-fields-added-save.png)

### Example

This illustration shows the final (primary) Assistant to which other Assistants are linked through the Assistant Chaining process. In this example, an Assistant named Linked Try is configured as the primary Assistant. This Assistant internally invokes another Assistant named Try, which is configured with an MCP connector to convert measurements from one unit to the corresponding unit.




 ![ai-hub-assistant-chaining-example-gif](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-example-gif.gif)

## Invoking Modes

Models chained or linked to the primary Assistant can be invoked using one of two invocation modes: Assisted mode and Autonomous mode. This topic explains the behavior and intended use cases of each mode. To switch between the invocation modes, click the Assisted or Autonomous button at the top of the Link Model page.

![ai-hub-assistant-chaining-invoking-mode](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-invoking-mode.png)

### Autonomous

In this invocation mode, the primary Assistant autonomously invokes specialized Assistants to process different parts of a user request. At runtime, it identifies the Assistants required to fulfill the query, orchestrates their execution, and combines their outputs into a single, unified response without requiring manual intervention.

When you switch from the default Assisted invocation mode to Autonomous mode by clicking the Autonomous button, a confirmation dialog is displayed. The dialog contains an acknowledgment checkbox indicating that you understand the Assistant will operate in Autonomous mode instead of Assisted mode. You must select the checkbox before you can enable Autonomous mode, and click the Confirm button as illustrated in the image below:




 ![ai-hub-assistant-chaining-confirmation-checkbox](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-confirmation-checkbox.png)

When processing a request, the primary Assistant first searches for existing specialized Assistants that are configured on the platform for the required task. If one or more suitable Assistants are available, the primary Assistant dynamically links them and delegates the corresponding tasks.

If no suitable Assistant is available, the primary Assistant automatically spawns the required specialized Assistant, links it to itself, and invokes it to complete the requested task. This discovery, linking, and orchestration process is performed dynamically at runtime, enabling the primary Assistant to seamlessly execute the complete processing pipeline.

**Note**: To run the Assistant in Autonomous mode even when no Assistants are linked, enable the **Run in autonomous mode even when no models are configured. If disabled, it will fall back to the normal Assistant** checkbox. If this option is disabled, the Assistant runs in the default Assistant mode instead of spawning and orchestrating specialized Assistants at runtime.

![ai-hub-assistant-chaining-run-even-when-no-models-linked](/resources/Storage/ai-hub/images/ai-hub-assistant-chaining-run-even-when-no-models-linked.png)

### Assisted

In this invocation mode, although the Primary Assistant automatically invokes the linked Assistants, the orchestration logic is predefined by a human behind the scenes. The sequence in which Assistants are invoked, along with the execution pipeline, is configured in advance rather than determined dynamically at runtime. As a result, the invocation follows a predefined compile-and-execute approach, where the orchestration flow is established before execution. This differs from Autonomous invocation, in which the Primary Assistant determines the orchestration flow dynamically at runtime based on the user's request.




 Assisted invocation is the default invocation mode in which the Primary Assistant invokes the linked Assistants. In this mode, linking additional Assistants or models is a mandatory configuration step. The Primary Assistant can invoke only those Assistants that have been explicitly linked as part of the predefined orchestration flow. In contrast, Autonomous invocation enables the Primary Assistant to dynamically determine the orchestration flow at runtime, invoke the most appropriate models or Assistants based on the request, and, where supported, instantiate additional models as needed to fulfill the task.

In this mode, once the specialized Assistants or models are linked, the orchestration pipeline is generated and the execution plan is defined in advance. As a result, the Primary Assistant follows the predefined execution flow when processing user requests, rather than determining the orchestration dynamically at runtime.
