# Access Model

<https://documentation.neutrinos.com/articles/#!ai-hub/work-with-document-extraction-models>

The Document Extraction Model available on Neutrinos AI Hub enables developers to build intelligent applications that can interpret and generate responses based on inputs such as documents, images, PDFs, and more.

This documentation provides a step-by-step guide to help you integrate, configure, and utilize the Document Extraction Model within your applications.

## Access Model

To access the extraction model for documents created on the platform follow the steps below:

1. Click Extraction in the left navigation bar to open the Extraction landing page.
2. On the Versions page of the model, the left panel includes two options: Versions and Integrations.
  - Click Versions to display the list of available model versions in the right panel.
      ![ai-hub-extraction-document-versions](/resources/Storage/ai-hub/images/ai-hub-extraction-document-versions.png)
    - Click Integrations to view the APIs associated with the selected model. The right panel will display all available APIs that can be consumed by upper layers.
        ![ai-hub-extraction-document-integration](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration.png)
3. Click the desired model version from the versions page to view its detailed information as illustrated in the below image:
    ![ai-hub-extraction-document-details-page](/resources/Storage/ai-hub/images/ai-hub-extraction-document-details-page.png)
    The dashboard displays the following information:
    Below the dashboard, a summary of information regarding the extracted fields is displayed. It includes Field Name, Accuracy Percentage, Precision, Recall, F1 Score, and Field Count as shown in the image below:
    ![ai-hub-extraction-document-details-page-summary](/resources/Storage/ai-hub/images/ai-hub-extraction-document-details-page-summary.png)
  - **Accuracy**: Displays the model's accuracy percentage for extracting information from the provided input.
  - **F1 Score**: Displays the performance of the extraction model by evaluating both the accuracy and completeness of the extracted information.
  - **Precision**: Displays the precision or accuracy of the trained model.
  - **Recall**: Displays the sensitivity or the true positive rate of the trained model.
  - **Processing Time**: Displays the time taken by the model to extract relevant information from the dataset and return the result.
  - **No. Of Documents**: Displays the total number of documents used for validation, which is 20% of the total uploaded documents used for training. In this case, 58 documents were uploaded, hence the dashboard reflects 12 documents used for validation.

## Versions

On the Model Versions page, multiple versions of the selected model are displayed in a tabular format. Each row includes details such as Version, Created Date, Training Status, Deployment Status, Action, and a caret symbol at the end for additional options. The image below illustrates the layout of the Versions page:




 ![ai-hub-extraction-document-version-page](/resources/Storage/ai-hub/images/ai-hub-extraction-document-version-page.png)

- **Version**: Displays all available versions of the model.
- **Created Date**: Displays the creation date of a specific model version.
- **Training Status**: Displays the training status of the model version.
  - **Completed**: Indicates that the model creation process is finished.
  - **In Progress**: Indicates that the model version is still being trained.
  - **Running**: Indicates that the model version is deployed and running in either the sandbox or production environment.
- **Deployment Status**: Indicates whether a model version is deployed. A hyphen (–) denotes that the model is not deployed, while Running indicates an active deployment, as shown in the image below.
    ![ai-hub-extraction-document-deployment-status](/resources/Storage/ai-hub/images/ai-hub-extraction-document-deployment-status.png)
- **Action**: This column contains a kebab menu icon. Clicking it reveals an option to delete the corresponding version of the extraction model.
- The caret icon at the end of each row allows users to expand the corresponding extraction model entry. When expanded, it reveals additional details such as
  - Documents: Displays the total number of documents used while training the model.
  - Category: Displays the categories present in the trained model.
  - Confidence Percentage: Represents the model's degree of certainty in the extracted results, shown as a confidence percentage for the selected version.
  - F1 Score: This metric evaluates the performance of an extraction model by displaying the F1 score for the selected version.
  - Processing Time: Displays the processing time taken to train the model version.

Click on a specific model version to view its detailed information, as illustrated in the GIF below:

Clicking on any available model version opens a summary page that displays information about the extracted sections (fields), such as the extracted text, Accuracy, Precision, Recall, F1 Score, and Field Count for each.

The left panel provides the following navigation possibilities:

- **Details**:The details about the trained model. This page contains 2 primary tabs, Training, and Inferencing. The Training tab displays detailed information about the data and the extracted texts generated during the training phase, as illustrated in the image below:
   ![ai-hub-extraction-document-versions-details-training-page](/resources/Storage/ai-hub/images/ai-hub-extraction-document-versions-details-training-page.png)
    The Inferencing tab displays the model’s inferences. Once the extraction model is trained, validated and deployed, the inferences API can be used. for the test data provided during the validation phase. Inference data is generated each time the inference API is called. When using the UI, these API calls are triggered through the test inputs provided by the user. If the model is configured with a rule that requires human review (i.e., the "Review by human intervention" option is set to "Always"), then the corresponding entries appear in the Review Hub during inference.
   ![ai-hub-extraction-document-inference-check](/resources/Storage/ai-hub/images/ai-hub-extraction-document-inference-check.gif)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The information in the Inferencing tab is populated only after a model is deployed and tested. The test data must be reviewed in the Review Hub to evaluate the model’s performance, as reflected in the Inferencing tab.
    The sample information that can be viewed on the Inferencing tab is shown in the image below:
   ![ai-hub-extraction-document-inference-page](/resources/Storage/ai-hub/images/ai-hub-extraction-document-inference-page.png)
- **Test**: This tab lists information about tests performed on the trained model. Testing can be either single or batch, corresponding to the two primary tabs available on the page as illustrated in the image below:
   ![ai-hub-extraction-document-test-landing](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-landing.png)
    To learn more about testing extraction models, refer [Testing Document Models](/articles/ai-hub/testing-document-extraction-models) topic.
- **Review Hub**: This section displays information related to reviews that require human involvement to enhance the model's performance. Every tested query is recorded here. Authorized reviewers can evaluate the system’s responses and confirm whether the answers are accurate.
    If the response is correct, clicking Confirm accepts the review and contributes to improving the model’s performance. Alternatively, reviewers can choose to Skip the question or Ignore the review.
    All reviews are organized into categorized tabs, including Pending, Verified, Skipped, Ignored, and a well-maintained Audit History of the model's review activity. To learn more about review hub, refer [Review Hub](/articles/ai-hub/review-hub-document-extraction-model) topic.
   ![ai-hub-extraction-document-review-hub-page](/resources/Storage/ai-hub/images/ai-hub-extraction-document-review-hub-page.png)
- **Rules**Displays the rules configured during the model creation process. This includes Feedback Loop Configuration, Retention, and other available configuration options. If needed, you can reconfigure the model and click the Save button at the bottom of the screen.
- **Advanced Configuration**: This section displays a list of advanced configuration options that were available during model creation. These configurations are view-only and cannot be edited after the model has been deployed. To learn more on advanced configurations, refer [Advanced Configuration](/articles/ai-hub/document-extraction-model/a/h2__469963410) section.
