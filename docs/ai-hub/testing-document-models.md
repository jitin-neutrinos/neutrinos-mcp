# Single Test

<https://documentation.neutrinos.com/articles/#!ai-hub/testing-document-models>

Every model created on the platform must undergo accuracy testing to ensure its responses are reliable. This is a critical phase in the model lifecycle and can be conducted through either a Single Test or a Batch Test. In a Batch Test, multiple documents are uploaded and processed collectively to evaluate the model’s overall performance.

### Single Test

To perform a single test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
    ![ai-hub-prediction-document-test-navigate](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-navigate.gif)
2. Click the Single tab, then click the Add button in the top-right corner to create a new test.
    ![ai-hub-prediction-document-test-start](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-start.png)
3. Click Single from the available drop-down options.
    ![ai-hub-prediction-document-test-single-test](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-single-test.png)
4. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
    ![ai-hub-prediction-document-test-select-env](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-select-env.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
5. On the next page, you will be prompted to upload a single document in the required format. The model will use this document to perform prediction and classification, as illustrated in the image below. In this example, a dummy Aadhaar card is used as the sample input. Based on the uploaded document, the model predicts and classifies whether it is the front side of the Aadhaar card.
    ![ai-hub-prediction-document-test-single-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-single-upload.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: Ensure the file size is 20 MB or less in PDF,TIFF,PNG or JEPG format and it is not password protected.
6. After uploading the document needed for the model to perform the prediction, click the Predict Document button on the bottom of the screen to predict the text entered.
    ![ai-hub-prediction-document-test-single-predict-doc](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-single-predict-doc.png)
    Once the Predict Document button is clicked, the model predicts and provides the output as illustrated in the GIF below:
    ![ai-hub-prediction-document-test-final](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-final.gif)
    The page displays the tested document along with its file name, the category it was classified into, and the confidence score, as illustrated in the image below:
    ![ai-hub-prediction-document-test-result](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-result.png)

### Batch Test

To perform batch test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
    ![ai-hub-prediction-document-test-navigate](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-navigate.gif)
2. Click the Batch tab, then click the Add button in the top-right corner to create a new test.
    ![ai-hub-prediction-document-test-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch.png)
3. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
    ![ai-hub-prediction-document-test-batch-select-env](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch-select-env.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
4. On the next page, you will be prompted to upload set of documents to the platform. The model will use this document to perform prediction and classification, as illustrated in the image below. In this example, a dummy Aadhaar card is used as the sample input. Based on the uploaded document, the model predicts and classifies whether it is the front side of the Aadhaar card.
    ![ai-hub-prediction-document-test-batch-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch-upload.png)
    Once the required test documents are uploaded, click the Start Testing button at the bottom of the page:
    ![ai-hub-prediction-document-test-batch-file-uploads-start-test](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch-file-uploads-start-test.png)
5. After clicking the Start Testing button, you will be directed to the Batch tab on the test page, where the batch file appears in the In Progress state. Once testing is complete, the status will be updated to Completed.
    ![ai-hub-prediction-document-test-batch-complete](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch-complete.png)
6. Click a specific batch test entry to open and view its detailed results as illustrated in the GIF below:
   ![ai-hub-prediction-document-test-batch-view](/resources/Storage/ai-hub/images/ai-hub-prediction-document-test-batch-view.gif)
