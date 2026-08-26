# Dashboard

<https://documentation.neutrinos.com/articles/#!ai-hub/work-with-assistant>

Creating the Assistant is the first step. The more critical phase lies in how you work and use the Assistant after it has been created. This stage—using and interacting with the Assistant—is crucial for deriving value from your workflow.

## Dashboard

You can view key performance metrics such as the assistant’s accuracy percentage, the number of successfully reviewed queries, pending queries awaiting review, and the average response time per conversation. Additionally, if a user has liked a response or provided feedback on a specific query, that information is also displayed. Metrics such as average tokens consumed and average conversation duration are presented.




 ![ai-hub-assistant-dashboard](/resources/Storage/ai-hub/images/ai-hub-assistant-dashboard.png)

## Set Instruction

To provide instructions to the assistant, follow the steps below:

1. Navigate to Assistant using the main navigation bar. Then, click Instruction from the left-side navigation panel on the assistant page to open the instruction panel for the selected assistant.
    ![assistant-instruction-landing-page](/resources/Storage/ai-hub/images/assistant-instruction-landing-page.png)
2. Enter the assistant's name in the text field under "Name of the Assistant". This name will help identify the assistant later, especially when making modifications, updates, or even versioning.
    ![assistant-instruction-name-assistant](/resources/Storage/ai-hub/images/assistant-instruction-name-assistant1.png)
3. Under the Directive section, specify clear instructions that the Assistant should follow when responding to user queries. These are essentially prompts that guide the Assistant’s behavior and shape its response style for each interaction. The directives act as predefined guidelines, enabling the Assistant to tailor its answers according to the context provided. If no directive is defined, the Assistant defaults to a formal tone, similar to that of a standard chatbot. For example, in the image below, the Assistant is instructed to extract the invoice number, Bill number, and seller information from a document uploaded by the user.
    ![assistant-instruction-directive](/resources/Storage/ai-hub/images/assistant-instruction-directive2.png)
4. Enter the greeting message that the assistant should use as its first response when a user submits a query.
    ![assistant-instruction-greetings](/resources/Storage/ai-hub/images/assistant-instruction-greetings1.png)
5. Set the output format. You can choose between Raw text and JSON formats. By default, the output is generated in Raw text format.
   ![assistant-instruction-output-format](/resources/Storage/ai-hub/images/assistant-instruction-output-format.png)
   If you select JSON as the output format, you can further specify the desired structure of the JSON output. A sample JSON format is illustrated below:
   Copy CodeJSON{
    "name": "boarding_pass_details",
    "description": "Extracts key details from a boarding pass including passenger name, travel date, origin, and destination.",
    "parameters": {
    "type": "object",
    "properties": {
    "BoardingPass": {
    "type": "array",
    "minItems": 1,
    "items": {
    "type": "object",
    "properties": {
    "Name": {
    "type": "string",
    "description": "Name of the passenger"
    },
    "Date": {
    "type": "string",
    "description": "Date of the flight"
    },
    "From": {
    "type": "string",
    "description": "Origin or departure airport"
    },
    "To": {
    "type": "string",
    "description": "Destination or arrival airport"
    }
    },
    "required": [
    "Name",
    "Date",
    "From",
    "To"
    ],
    "additionalProperties": false
    }
    }
    },
    "required": [
    "BoardingPass"
    ],
    "additionalProperties": false
    }
   }
6. Click the **Save** button to apply and save the configuration.
    ![assistant-instruction-save-button](/resources/Storage/ai-hub/images/assistant-instruction-save-button1.png)

## Set Knowledge Source

To add a Knowledge Source for the Assistant to reference—similar to a data source—and enable contextually relevant responses, refer to the [Set Knowledge Source](/articles/ai-hub/toolsets/a/h2_1158915101) section under the Toolsets topic.

## Set Style

To set styling for the assistant, follow the steps below:

1. Navigate to Assistant using the main navigation bar. Then, click Style from the left-side navigation panel on the assistant page to open the style configuration section for the selected assistant.
    ![assistant-style-landing-page](/resources/Storage/ai-hub/images/assistant-style-landing-page.png)
2. In the **Embed Icon** section, choose the shape and size for the assistant icon. To upload a custom image for the assistant, click the image placeholder on the right side of the page and select the image of your choice.
    ![assistant-style-icon-shape-size](/resources/Storage/ai-hub/images/assitant-style-icon-shape-size.png)
3. Enable the Automatically display your greeting message after a few seconds toggle to show a prompt that encourages the user to interact with the assistant.
    ![assistant-style-automatic-reply](/resources/Storage/ai-hub/images/assistant-style-automatic-reply.png)
4. Set the theme by specifying the Brand Color, selecting the Icon Color, and choosing the desired border smoothness from the dropdown menu.
    ![assistant-style-theme](/resources/Storage/ai-hub/images/assistant-style-theme.png)
5. Select the font color and text bubble color for user queries by using the color palette or entering a HEX code in the input field for both Text Color and Text Bubble Color.
    ![assistant-style-user-message](/resources/Storage/ai-hub/images/assistant-style-user-message.png)
6. Click the **Save** button to apply and save the configuration.
    ![assistant-style-save-button](/resources/Storage/ai-hub/images/assistant-style-save-button.png)
