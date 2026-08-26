# Create Assistant

<https://documentation.neutrinos.com/articles/#!ai-hub/assistant>

An AI Assistant (Chatbot) is an application that uses artificial intelligence (AI) and natural language processing (NLP) to simulate human conversation. It interacts with users through text interfaces and performs tasks such as answering queries and guiding processes.

The chatbot in AI Hub is designed to provide instant, context-aware support to users by interpreting their input, processing relevant data, and delivering responses in a conversational format.




 The Assistant landing page displays a table containing key information about the assistants created on the platform, as illustrated in the image below:




 ![assistant-landing-page](/resources/Storage/ai-hub/images/assistant-landing-page.png)

1. **Name**: Name of the assistant.
2. **Conversation**: Displays the number of conversations that have taken place with the specific assistant.
3. **Last Updated**: Displays the date and timestamp of the most recent update made to a specific assistant.
4. **Action**: This column contains a kebab menu icon (three vertical dots) that allows you to delete a specific assistant.
5. Additionally, the caret icon at the end of each row allows you to expand a specific assistant to view its available versions. The expanded view displays details such as the version number, status, author, last updated date and time, and includes a kebab menu icon in the Actions column, which allows you to delete individual versions of the assistant.

## Create Assistant

Follow the steps below to create an assistant in AI Hub:

1. Click Assistant from the left side navigation bar to open the Assistant page.
    ![assistant-navigate](/resources/Storage/ai-hub/images/assistant-navigate.png)
2. Click the **Create** button on the top right of the page to configure the assistant.
    ![assistant-create-button](/resources/Storage/ai-hub/images/assistant-create-button.png)
3. The left navigation panel on the landing page includes the following tabs: Dashboard, Instruction, Knowledge, Style, Review Hub, and Advanced. Fill in the details in the following sections as needed:
  1. **Dashboard**: You can view key performance metrics such as the assistant’s accuracy percentage, the number of successfully reviewed queries, pending queries awaiting review, and the average response time per conversation.
  2. **Instruction**: Provide guidance to the assistant on how to respond to users’ queries. Include key details such as the target audience, the expected tone and style, and the overall purpose of the assistant’s communication. This helps ensure that responses are consistent, relevant, and appropriately tailored. Additionally, you may specify the greeting message that the assistant should display as its initial response to the user. You may also assign a custom name to the assistant in this section. By default, the assistant's name is set to 'Untitled'. For more information on how to set instructions for an assistant, refer [Set Instruction](/articles/ai-hub/work-with-assistant/a/h2_968864786) section under Work with Assistant topic.
  3. **API Config**: Specify the APIs that need to be triggered from the Assistant. Before an API can be called from the Assistant, it must first be configured in the platform. Once configured, the APIs can be triggered through the Assistant. This section lists all the APIs mapped for use within the Assistant. Fro more information on how to configure API, refer [API Config](/smart/project-ai-hub/api-config) topic.
  4. **Knowledge**: Specify the data source to enable the assistant to generate responses. The assistant will use this data to enhance its understanding and improve the quality of its replies. For more information on how to set knowledge for an assistant, refer [Set Knowledge Source](/articles/ai-hub/work-with-assistant/a/h2_1158915101) section under Work with Assistant topic.
  5. **Style**: This section allows you to customize the assistant's appearance. This includes configuring the icon's shape and size, setting the theme, and adjusting visual elements such as the background color, border, text color, and bubble size of user queries. For more information on how to style the assistant, refer [Set Style](/articles/ai-hub/work-with-assistant/a/h2_1542863813) section under Work with Assistant topic.
  6. **Review Hub**: This section is used to review the responses provided by the assistant to user queries. Reviewing these responses helps improve the overall response quality. Click on individual responses to provide feedback for improvement. These feedback entries are later reflected on the assistant's dashboard. Additionally, this section includes tabs that display the number of queries reviewed, skipped, or ignored, along with the complete audit history for the selected assistant. For more information on review hub, refer [Review Hub](/articles/ai-hub/review-hub-assistant) topic.
  7. **Advanced**: In this section, you can configure the assistant’s public name and specify a placeholder text. You can also define the allowed domains from which the assistant can retrieve responses when no specific knowledge source is provided, especially for general queries. Additionally, you can set the permissible creativity probability and specify when any stored data should be removed. For more information on advanced options, refer [Advanced](/articles/ai-hub/advanced-configuration-assistant) topic.
4. After completing the required fields in the above sections, click Save to apply the changes. To publish the assistant, click the Publish button at the bottom of the page. You can choose to either:
    Enter the release notes, then click Save to finalize the publication.
  1. Save As New to publish a new version, or
  2. Select Overwrite to update the current version.

After publishing the assistant, you can test the published version using the **Test Version** option available on the platform. Click the **Test Version** button at the top of the section to test the assistant. For more information on testing the assistant, refer [Validate Assistant](/articles/ai-hub/validate-assistant) topic.
