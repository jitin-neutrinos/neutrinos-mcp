# Single Test

<https://documentation.neutrinos.com/articles/#!ai-hub/testing-text-extraction-models>

Every model created on the platform must be tested for accuracy to ensure that its responses can be trusted. This is a crucial phase in the model lifecycle and can be performed using either a Single Test or a Batch Test. In the case of batch testing, data is provided in the form of an Excel or CSV file, which is then used to evaluate the model's performance.

### Single Test

To perform single test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
    ![ai-hub-extraction-single-test-navigate](/resources/Storage/ai-hub/images/ai-hub-extraction-single-test-navigate.gif)
2. Click the Single tab, then click the Add button in the top-right corner to create a new test.
    ![ai-hub-extraction-test-single](/resources/Storage/ai-hub/images/ai-hub-extraction-test-single.png)
3. Click Single from the available drop-down options.
    ![ai-hub-extraction-test-single-add](/resources/Storage/ai-hub/images/ai-hub-extraction-test-single-add.png)
4. Select the environment in which the model is deployed. It can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
    ![ai-hub-extraction-test-single-environment](/resources/Storage/ai-hub/images/ai-hub-extraction-test-single-environment.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
5. You are prompted to enter input text that the model will use to extract the target information, as shown in the image below. In this example, the input includes details such as State and Capital. Based on this input, the model extracts the State name and Capital from the text.
    ![ai-hub-extraction-test-input](/resources/Storage/ai-hub/images/ai-hub-extraction-test-input.png)
6. Enter the required details needed for the model to perform the extraction, click the Predict Text button at the bottom of the screen to extract the relevant information from the input text.
    ![ai-hub-extraction-test-single-predict-text-button](/resources/Storage/ai-hub/images/ai-hub-extraction-test-single-predict-text-button.png)

### Batch Test

To perform batch test on the model, follow the steps below:

1. Click on a specific model version from the Versions page. You will be directed to the All Tests page, which contains two primary tabs: Single and Batch, each representing a different type of testing.
    ![ai-hub-extraction-single-test-navigate](/resources/Storage/ai-hub/images/ai-hub-extraction-single-test-navigate.gif)
2. Click the Batch tab, then click the Add button in the top-right corner to create a new test.
   ![ai-hub-extraction-text-test-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch.png)
3. Select the environment in which the model is deployed. It can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
   ![ai-hub-extraction-text-test-batch-select-environment](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch-select-environment.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
4. You are prompted to choose the file type—either Excel or CSV. Select the desired file type, then click Next at the bottom of the screen as illustrated in the image below:
   ![ai-hub-extraction-text-test-batch-select-file](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch-select-file.png)
5. On the next page, upload the file. Note: The uploaded file must include a text column containing the input text to be extracted and processed by the model.
    You can download a sample sheet from the platform to enter test data in the required format by clicking the **Sample Excel File** button.
   ![ai-hub-extraction-text-batch-test-download-sample](/resources/Storage/ai-hub/images/ai-hub-extraction-text-batch-test-download-sample.png)
    Once the required test data is uploaded, click the Start Testing button at the bottom of the page.
   ![ai-hub-extraction-text-test-batch-uploaded-file](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch-uploaded-file.png)
6. After clicking the Start Testing button, you will be directed to the Batch tab on the test page, where the batch file appears in the In Progress state. Once testing is complete, the status will be updated to Completed.
   ![ai-hub-extraction-text-test-batch-final](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch-final.png)
7. Click a specific batch test entry to open and view its detailed results as illustrated in the GIF below:
   ![ai-hub-extraction-text-test-batch-open](/resources/Storage/ai-hub/images/ai-hub-extraction-text-test-batch-open.gif)
