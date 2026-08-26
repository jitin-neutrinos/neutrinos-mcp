# Access Model

<https://documentation.neutrinos.com/articles/#!ai-hub/work-with-text-models>

Creating the model is the first step. The more critical phase lies in how you work with the model after it has been created. This stage—using and interacting with the trained model—is crucial for deriving value from your machine-learning workflow.

This documentation provides a step-by-step guide to help you integrate, configure, and utilize the Text Prediction Model within your applications.

## Access Model

To access the prediction model created on the platform, follow the steps below:

1. Click Prediction in the left navigation bar to open the Prediction landing page.
2. On the Versions page of the model, the left panel includes two options: Versions and Integrations.
  - Click **Versions** to display the list of available model versions in the right panel.
      ![ai-hub-prediction-text-versions](/resources/Storage/ai-hub/images/ai-hub-prediction-text-versions.png)
  - Click **Integrations** to view the APIs associated with the selected model. The right panel will display all available APIs that can be consumed by upper layers.
      ![ai-hub-prediction-text-integrations](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integrations.png)
3. Click the desired model version to view its detailed information as illustrated in the below image:
    ![ai-hub-prediction-text-model-landing](/resources/Storage/ai-hub/images/ai-hub-prediction-text-model-landing.png)
    The dashboard displays the following information:
  - **Texts**: Represents the total number of text entries available in the trained model. In the Dashboard, only 20% of the total dataset is displayed. Of the entire dataset used for training, 80% is used to train the model, while the remaining 20% is used for validation.
  - **Precision**: Precision measures the proportion of correct positive predictions out of all positive predictions made by the model. In other words, it answers the question: "Of all the instances the model predicted as positive, how many were actually correct?" Precision is important in scenarios where false positives carry significant consequences. Common examples include:
    - In medical diagnosis, misclassifying a healthy patient as sick.
    - In spam detection, classifying a legitimate email as spam.
  - **Recall**: Displays the recall (sensitivity or true positive rate) of the trained model. Recall measures the proportion of correct positive predictions out of all actual positive instances in the dataset. It answers the question: "Of all the cases where the model should have predicted 'Yes', how many times did it actually do so?
      This metric emphasizes the completeness of the model's positive predictions. Recall is important when missing relevant results (false negatives) can be costly or dangerous. For example:
    - Disease detection: Failing to identify a sick patient can have serious consequences.
  - **F1 Score**: This displays the F1 Score - the harmonic mean of precision and recall, commonly used to evaluate the performance of classification models. It provides a balanced measure by considering both the accuracy of positive predictions (precision) and the completeness of those predictions (recall). For example, in a spam detection task, spam messages typically represent a small portion of the total data. In such cases, relying solely on accuracy can be misleading—a model might label all messages as non-spam and still achieve high accuracy. The F1 Score addresses this limitation by factoring in both false positives and false negatives, offering a more reliable measure of model performance.
  - **Processing Time**: Displays the time it takes for the model to train on a dataset.
  - **Confidence**: Displays a confidence value representing the system’s estimated probability that the classified text is accurate.

## Versions

On the Model Versions page, multiple versions of the selected model are displayed in a tabular format. Each row includes details such as Version, Created Date, Status, Action, and a caret symbol at the end for additional options. The image below illustrates the layout of the Versions page:




 ![ai-hub-prediction-version-landing-page](/resources/Storage/ai-hub/images/ai-hub-prediction-version-landing-page.png)

- **Version**: Displays all available versions of the model.
- **Created Date**: Displays the creation date of a specific model version.
- **Status**: Displays the status of the model version.
  - **Completed**: Indicates that the model creation process is finished.
  - **In Progress**: Indicates that the model version is still being trained.
  - **Running**: Indicates that the model version is deployed and running in either the sandbox or production environment.
- **Action**: This column contains a kebab menu icon. Clicking it reveals an option to delete the corresponding version of the prediction model.
- The caret icon at the end of each row allows users to expand the corresponding prediction model entry. When expanded, it displays additional details, as illustrated in the image below:
    ![ai-hub-prediction-text-version-expand](/resources/Storage/ai-hub/images/ai-hub-prediction-version-expand.png)
  - Total Text: Displays the total number of texts used while training the model.
  - Caterogies: Displays the categories present in the trained model.
  - Confidence Percentage: Represents the model's degree of certainty in its predictions. Displays the confidence percentage for the selected version of the model.
  - F1 Score: A metric used to evaluate the performance of a classification model. Displays the F1 score for the selected version of the model.
  - Processing Time: Displays the processing time taken to train the model version.

Click on a specific model version to view its detailed information, as illustrated in the GIF below:




 ![ai-hub-prediction-text-version-details](/resources/Storage/ai-hub/images/ai-hub-prediction-text-version-details.gif)


 When you click on any available model version, a summary page opens displaying information about the predicted texts, their individual occurrences, and the confidence score associated with each prediction.

The left panel provides the following navigation possibilities:

- **Details**: The details about the trained model. This page contains 2 primary tabs, Training, and Inferencing. The Training tab displays detailed information about the data and the predicted texts generated during the training phase, as illustrated in the image below:
    ![ai-hub-prediction-version-details](/resources/Storage/ai-hub/images/ai-hub-prediction-version-details.png)
    The Inferencing tab displays the model’s inferences. Once the prediction model is trained, validated and deployed, the inferences API can be used. for the test data provided during the validation phase. Inference data is generated each time the inference API is called. When using the UI, these API calls are triggered through the test inputs provided by the user. If the model is configured with a rule that requires human review (i.e., the "Review by human intervention" option is set to "Always"), then the corresponding entries appear in the Review Hub during inference.
    ![ai-hub-prediction-text-inferencing](/resources/Storage/ai-hub/images/ai-hub-prediction-text-inferencing.gif)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The information in the Inferencing tab is populated only after a model is deployed and tested. The test data must be reviewed in the Review Hub to evaluate the model’s performance, as reflected in the Inferencing tab.
    The sample information that can be viewed on the Inferencing tab is shown in the image below:
    ![ai-hub-prediction-text-inference-tab](/resources/Storage/ai-hub/images/ai-hub-prediction-text-inference-tab.png)
- **Test**: This tab lists information about both single and batch tests performed on the trained model. Testing can be either single or batch, corresponding to the two primary tabs available on the page. To learn more about testing prediction models, refer [Validate Text Models](/articles/ai-hub/validate-text-models) topic.
- **Review Hub**: This section displays information related to reviews that require human intervention to improve the model’s performance. Each prediction is recorded here if the model is configured with the rule "Always" for human review. If the rule is set to "Never", predictions are made but are not listed for human validation. When the rule is set to "Confidence", entries appear only if the model’s confidence score falls below the defined threshold during rule configuration.
    To learn more about review hub, refer [Review Hub](/articles/ai-hub/review-hub-text-model) topic.
    ![ai-hub-prediction-text-review-hub](/resources/Storage/ai-hub/images/ai-hub-prediction-text-review-hub.png)
- **Rules**: Displays the rules configured during the model creation process. This includes Feedback Loop Configuration, Retention, and other available configuration options. If needed, you can reconfigure the model and click the Save button at the bottom of the screen.
    ![ai-hub-prediction-text--review-hub-page](/resources/Storage/ai-hub/images/ai-hub-prediction-text--review-hub-page.png)
- **Advanced Configuration**: This section displays a list of advanced configuration options that were available during model creation. These configurations are view-only and cannot be edited after the model has been deployed. To learn more on advanced configurations, refer [Advanced Configuration](/articles/ai-hub/text-prediction-model/a/h2__469963410) section.
