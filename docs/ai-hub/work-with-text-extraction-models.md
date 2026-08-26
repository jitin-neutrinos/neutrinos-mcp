# Access Model

<https://documentation.neutrinos.com/articles/#!ai-hub/work-with-text-extraction-models>

The Text Extraction Model available on Neutrinos AI Hub enables developers to build intelligent applications that can understand and generate natural language responses based on contextual input.

This documentation provides a step-by-step guide to help you integrate, configure, and utilize the Text Extraction Model within your applications.

## Access Model

To access the extraction model created on the platform follow the steps below:

1. Click Extraction in the left navigation bar to open the Extraction landing page.
2. On the Versions page of the model, the left panel includes two options: Versions and Integrations.
  - Click **Versions** to display the list of available model versions in the right panel.
      ![ai-hub-extraction-text-versions](/resources/Storage/ai-hub/images/ai-hub-extraction-text-versions.png)
  - Click **Integrations** to view the APIs associated with the selected model. The right panel will display all available APIs that can be consumed by upper layers.
      ![ai-hub-extraction-text-integration](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration.png)
3. Click the desired model version to view its detailed information as illustrated in the below image:
    ![ai-hub-extraction-text-version-model-landing-page](/resources/Storage/ai-hub/images/ai-hub-extraction-text-version-model-landing-page.png)
    The dashboard displays the following information:
  - **Texts**: Total number of text entries used to train the model.
  - **F1 Score**: This metric evaluates the performance of an extraction model by measuring both the accuracy and completeness of its outputs.
  - **Precision**: Displays the precision or accuracy of the trained model.
  - **Recall**: Displays the sensitivity or the true positive rate of the trained model.
  - **Processing Time**: Displays the time it takes for the model to train on a dataset and make extractions on the new data.
  - **Confidence**: Displays a confidence value representing the system’s estimated probability that the classified text is accurate.

## Versions

On the Model Versions page, all available versions of the selected model are displayed in a tabular format. Each row contains key details, including Version, Created Date, Status, Action, and a caret icon at the end for accessing additional options. The image below illustrates the layout of the Model Versions page:




 ![ai-hub-extraction-text-version-available](/resources/Storage/ai-hub/images/ai-hub-extraction-text-version-available.png)

- **Version**: Displays all available versions of the model.
- **Created Date**: Displays the creation date of a specific model version.
- **Status**: Displays the status of the model version.
  - **Completed**: Indicates that the model creation process is finished.
  - **In Progress**: Indicates that the model version is still being trained.
  - **Running**: Indicates that the model version is deployed and running in either the sandbox or production environment.
- **Action**: This column contains a kebab menu icon. Clicking it reveals an option to delete the corresponding version of the extraction model.
- The caret icon at the end of each row allows users to expand the corresponding extraction model entry. When expanded, it reveals additional details such as
  - Total Text: Displays the total number of texts used while training the model.
  - Caterogies: Displays the categories that the trained model is capable of extracting.
  - Confidence Percentage: Displays the model’s confidence percentage for each extraction in the selected version, indicating the degree of certainty.
  - F1 Score: A metric used to evaluate the performance of a classification model. Displays the F1 score for the selected version of the model.
  - Processing Time: Displays the processing time taken to train the model version.

Click on a specific model version to view its detailed information, as illustrated in the GIF below:

Click on any available model version to open a summary page that displays information about the extracted text categories, their individual occurrences, and the confidence score associated with each category.




 The left panel provides the following navigation possibilities:

- **Details**: This page provides detailed information about the trained model and includes two primary tabs: Training and Inferencing. The Training tab displays comprehensive details about the data and the extracted texts used during the training phase, as illustrated in the image below:
    ![ai-hub-extraction-text-dashboard-details](/resources/Storage/ai-hub/images/ai-hub-extraction-text-dashboard-details.png)
    The Inferencing tab displays the model’s inferences. Once the extraction model is trained, validated and deployed, the inferences API can be used. for the test data provided during the validation phase. Inference data is generated each time the inference API is called. When using the UI, these API calls are triggered through the test inputs provided by the user. If the model is configured with a rule that requires human review (i.e., the "Review by human intervention" option is set to "Always"), then the corresponding entries appear in the Review Hub during inference.
   ![ai-hub-extraction-review-hub-inference](/resources/Storage/ai-hub/images/ai-hub-extraction-review-hub-inference.gif)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The information in the Inferencing tab is populated only after a model is deployed and tested. The test data must be reviewed in the Review Hub to evaluate the model’s performance, as reflected in the Inferencing tab.
    The sample information that can be viewed on the Inferencing tab is shown in the image below:
   ![ai-hub-extraction-details-inference-tab](/resources/Storage/ai-hub/images/ai-hub-extraction-details-inference-tab.png)
- **Test**: This tab displays information about both single and batch tests performed on the trained model. Testing can be conducted in either mode, corresponding to the two primary tabs available on the page. For more details, refer to the [Testing Text Extraction Models](/articles/ai-hub/testing-text-extraction-models) topic.
- **Review Hub**: This section displays information related to reviews that require human involvement to enhance the model's performance. Every tested query is recorded here. Authorized reviewers can evaluate the system’s responses and confirm whether the answers are accurate.
    If the response is correct, clicking Confirm accepts the review and contributes to improving the model’s performance. Alternatively, reviewers can choose to Skip the question or Ignore the review.
    All reviews are organized into categorized tabs, including Pending, Verified, Skipped, Ignored, and a well-maintained Audit History of the model's review activity. To learn more about review hub, refer [Review Hub](/articles/ai-hub/review-hub-text-extraction-model) topic.
   ![ai-hub-extraction-review-hub-landing-page](/resources/Storage/ai-hub/images/ai-hub-extraction-review-hub-landing-page.png)
- **Rules**: Displays the rules configured during the model creation process. This includes Feedback Loop Configuration, Retention, and other available configuration options. If needed, you can reconfigure the model and click the Save button at the bottom of the screen.
- **Advanced Configuration**: This section displays a list of advanced configuration options that were available during model creation. These configurations are view-only and cannot be edited after the model has been deployed. To learn more on advanced configurations, refer [Advanced Configuration](/articles/ai-hub/text-extraction-model/a/h2__469963410) section.
