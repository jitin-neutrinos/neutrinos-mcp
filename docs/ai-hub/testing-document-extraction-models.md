# Single Test

<https://documentation.neutrinos.com/articles/#!ai-hub/testing-document-extraction-models>

Every model created on the platform must undergo accuracy testing to ensure its responses are reliable. This is a critical phase in the model lifecycle and can be conducted through either a Single Test or a Batch Test. In a Batch Test, multiple documents are uploaded and processed collectively to evaluate the model’s overall performance.

### Single Test

To perform a single test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
   ![ai-hub-extraction-document-navigate-single-test](/resources/Storage/ai-hub/images/ai-hub-extraction-document-navigate-single-test.gif)
2. Click the Single tab, then click the Add button in the top-right corner to create a new test.
   ![ai-hub-extraction-document-single-test-tab](/resources/Storage/ai-hub/images/ai-hub-extraction-document-single-test-tab.png)
3. Click Single from the available drop-down options.
   ![ai-hub-extraction-document-test-add-single](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-add-single.png)
4. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
   ![ai-hub-extraction-document-test-select-environment](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-select-environment1.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
5. On the next page, you will be prompted to upload a single document in the required format.
   ![ai-hub-extraction-document-test-single-upload-image](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-single-upload-image.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: Ensure the file size is 20 MB or less in PDF,TIFF,PNG or JEPG format and it is not password protected.
6. After uploading the document needed for the model to perform the extraction, click the Extract Document button on the bottom of the screen to extract the content from the uploaded document.
   ![ai-hub-extraction-document-test-single-extract-document-button](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-single-extract-document-button.png)
    Once the Extract Document button is clicked, the model extracts and provides the output as illustrated in the GIF below. In the example shown, a sample invoice is used as input. Based on the uploaded document, the model extracts key details such as the invoice number, seller information, seller tax ID, client information, client tax ID, and date of issue.:
   ![ai-hub-extraction-document-test-final-gif](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-final-gif.gif)
7. To test for another document, click the Test New Case button at the bottom of the page.

### Batch Test

To perform batch test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
    ![ai-hub-extraction-document-navigate-single-test](/resources/Storage/ai-hub/images/ai-hub-extraction-document-navigate-single-test.gif)
2. Click the Batch tab, then click the Add button in the top-right corner to create a new test.
   ![ai-hub-extraction-document-test-batch-add](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-add.png)
3. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
   ![ai-hub-extraction-document-test-batch-select-env-next](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-select-env-next.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
4. On the next page, you will be prompted to upload a set of documents in the required format. The model will use this document to perform data extraction, as illustrated in the image below. In the example shown, a sample invoice is used as input. Based on the uploaded document, the model extracts key details such as the invoice number, seller information, seller tax ID, client information, client tax ID, and date of issue.
   ![ai-hub-extraction-document-test-batch-upload](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-upload.png)
    Once the required test documents are uploaded, click the Start Testing button at the bottom of the page:
   ![ai-hub-extraction-document-test-batch-start-test](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-start-test.png)
5. After clicking the Start Testing button, you will be directed to the Batch tab on the test page, where the batch file appears in the In Progress state. Once testing is complete, the status will be updated to Completed.
   ![ai-hub-extraction-document-test-batch-in-progress](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-in-progress.png)
6. Click a specific batch test entry to open and view its detailed results as illustrated in the GIF below:
   ![ai-hub-extraction-document-test-batch-open](/resources/Storage/ai-hub/images/ai-hub-extraction-document-test-batch-open.gif)
