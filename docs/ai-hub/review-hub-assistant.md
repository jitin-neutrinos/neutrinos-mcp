# Activity Logs

<https://documentation.neutrinos.com/articles/#!ai-hub/review-hub-assistant>

Human intervention is essential for reviewing the conversation made with the assistant, as it helps monitor and improve it’s performance. Feedback provided through the Review Hub contributes to enhancing the model's accuracy and effectiveness over time.

This section displays all the conversations made with users. Reviewing these queries helps the Assistant improve based on the feedback provided. It includes the following tabs as shown in the image below:




 ![assistant-review-hub](/resources/Storage/ai-hub/images/ai-hub-assistant-review-hub-landing-page.png)

- **Pending**: This tab displays all user queries that are pending review.
- **Verified**: This tab displays all the user queries that are verified from the pending review tab. To verify, or review a query follow the steps below:
  - To review queries, either click on a specific query or select multiple queries using the checkboxes, to open the review page.
      ![assistant-review-hub-pending-tab-click](/resources/Storage/ai-hub/images/ai-hub-assistant-review-hub-sample.png)
  - This page provides options such as Skip, Ignore, and Confirm. Click one of these options to review the query based on the quality of the Assistant’s response.
- **Skipped**: If any query from the Pending tab is skipped during review, it will be listed under the Skipped tab.
- **Ignored**: If any query from the Pending tab is ignored during review, it will be listed under the Ignored tab.
- **Audit History**: This tab lists all queries that have been reviewed, regardless of the review outcome—Confirmed, Ignored, or Skipped.

To review the conversations with assistant in the Review Hub, follow the steps below:

1. Navigate to the Assistant page using the left navigation panel. Select the desired assistant model from the list of available (created) assistants on the platform. Then, open the specific version of the model from the Versions page.
2. Click Review Hub in the left navigation panel to open the Review Hub page.
3. To review a conversation, either click on an individual conversation or select multiple conversations using the checkboxes to open the Review page. The sample review process is illustrated in the GIF below:
    ![ai-hub-review-hub-review-confirm](/resources/Storage/ai-hub/images/ai-hub-review-hub-review-confirm.gif)
4. The review provided are reflected on the dashboard page with accuracy, sentiment cloud, Feedback summary, and Average Token Consumed as illustrated in the image below:
    ![ai-hub-assistant-dashboard-after-review-hub](/resources/Storage/ai-hub/images/ai-hub-assistant-dashboard-after-review-hub.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The Feedback Summary is updated when the reviewer gives a thumbs-up for the assistant's response. The Sentiment Cloud is generated based on the written feedback provided through the review option for individual conversations in the Review Hub.

## Activity Logs

This section provides a detailed breakdown of each activity in the sequence of interactions within a conversation with the assistant. To view the activity sequence, follow the steps below:

1. In the Review Hub of any assistant, click on a conversation from any of the available tabs—Pending, Verified, Skipped, or Ignored—to view its details.
2. Under the response from assistant, click the book icon (![ai-hub-assistant-activity-lo-icon](/resources/Storage/ai-hub/images/ai-hub-assistant-activity-lo-icon.png)) to open the Activity Log panel on the right as illustrated in the image below:
    ![ai-hub-assistant-activity-log-panel](/resources/Storage/ai-hub/images/ai-hub-assistant-activity-log-panel.png)
  - Neutrinos DB: This step shows that each conversation performed with assistant, the first step is the Neitrinos DB where the conversation and other details are stored.
  - OCR Extraction: This step captures the user input based on the purpose for which the assistant was designed. If the assistant model requires OCR (Optical Character Recognition) to process information, this step performs the OCR extraction and converts the uploaded document or input into machine-readable text for further processing. For example, in the image below, the input is an invoice, and the output of the step is the OCR text extracted from the image:
      ![ai-hub-assistant-review-hub-activity-log-ocr](/resources/Storage/ai-hub/images/ai-hub-assistant-review-hub-activity-log-ocr.png)
  - Azure OpenAI: The underlying model processes the user input by utilizing pre-processed information, including OCR-extracted text if available.
      ![ai-hub-assistant-activity-log-azure-openai](/resources/Storage/ai-hub/images/ai-hub-assistant-activity-log-azure-openai.png)
  - Post Processing: It includes converting the output into the required JSON format—if such a format was specified in the assistant's configuration or inferred from the user's intent. For instance, in this sample, since no specific output format was defined, the response is retained in Raw text format, as illustrated in the image below:
      ![ai-hub-assistant-activity-log-postprocessing](/resources/Storage/ai-hub/images/ai-hub-assistant-activity-log-postprocessing.png)
