# Create New Prediction Model

<https://documentation.neutrinos.com/articles/#!ai-hub/prediction>

Prediction is used to configure and deploy AI models that analyze and classify incoming text or document-based data. These models are trained on labeled inputs to learn patterns and are applied in real-time to generate outputs such as classifications, intent tags, or confidence scores.

In AI Hub, Prediction supports the full lifecycle of a classifier—from data upload to training and evaluation—enabling teams to automate tasks such as message classification, content sorting, and document tagging with high precision. Prediction instances can be either text-based or document-based and are managed through a unified interface.

Users can upload training files, tag inputs to train the model, evaluate predictions, and iteratively refine performance by updating datasets or adjusting metrics. Once trained and validated, the model can be used for real-time classification or batch processing, enhancing operational efficiency and decision accuracy.

The image below illustrates the Prediction page within the platform:




 ![ai-hub-prediction-landing-page](/resources/Storage/ai-hub/images/ai-hub-prediction-landing-page2.png)

The details on this page are displayed in a tabular format, including information such as Prediction Name, Description, Last Updated Date and Time, and available Actions.

1. **Prediction Name**: Displays the name of the prediction model as defined during its creation.
2. **Decription**: Displays the description of the model as provided during its creation.
3. **Udapte Date and Time**: Displays the date and time when the prediction model was last updated.
4. **Actions**: This column contains a kebab menu icon. Clicking it reveals an option to delete the corresponding prediction model.
5. The caret icon at the end of each row allows users to expand the corresponding prediction model entry. When expanded, it reveals additional details such as the available versions of the model, its current status, the author who created it, the last updated date and time, and a kebab menu icon that includes a delete option.

The page is organized into two primary tabs:

- **Text**: Displays models configured for text-based predictions such as classification or intent detection.
- **Document**: Displays models configured for document-based predictions.

Use the search bar to locate specific models by name, or use the status filter to narrow down the list based on the workflow stage.

## Create New Prediction Model

To create a new prediction model, follow the steps below:

1. Click Prediction in the left navigation bar to open the Prediction page.
2. On the Prediction page, click the **Add** button in the top-right corner to begin setting up a new prediction.
    ![ai-hub-prediction-add-button](/resources/Storage/ai-hub/images/ai-hub-prediction-add-button1.png)
3. A configuration page opens, displaying a detailed step-by-step outline of the process. Click the **Get Started** button at the bottom of the page to proceed.
    ![ai-hub-prediction-get-started](/resources/Storage/ai-hub/images/ai-hub-prediction-get-started1.png)
4. Select the type of data on the create page that the prediction model will be based on. It can be either text (Excel file or CSV) or a document (PDF, image, or other formats).
    ![ai-hub-prediction-types](/resources/Storage/ai-hub/images/ai-hub-prediction-types1.png)
5. To create a Text based prediction model, See [Text Prediction Model](/articles/ai-hub/text-prediction-model) topic.
6. To create a Document based prediction model, see [Document Prediction Model](/articles/ai-hub/document-prediction-model) topic.
