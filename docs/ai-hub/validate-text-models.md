# Single Test

<https://documentation.neutrinos.com/articles/#!ai-hub/validate-text-models>

Every model created on the platform must be tested for accuracy to ensure that its responses can be trusted. This is a crucial phase in the model lifecycle and can be performed using either a Single Test or a Batch Test. In the case of batch testing, data is provided in the form of an Excel or CSV file, which is then used to evaluate the model's performance.

### Single Test

To perform single test on the model, follow the steps below:

1. To begin testing, click on a specific model version from the Versions page. You will be redirected to the model's dashboard. From the left-hand panel, select Test to open the All Tests page, which features two main tabs: Single and Batch—each representing a distinct testing method.
    ![ai-hub-prediction-text-testing-landing](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-landing.gif)
2. Click the Single tab, then click the Add button in the top-right corner to create a new test.
    ![ai-hub-prediction-text-test-single-test](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-single-test.png)
3. Click Single from the available drop-down options.
    ![ai-hub-prediction-text-single-test-add](/resources/Storage/ai-hub/images/ai-hub-prediction-text-single-test-add.png)
4. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
    ![ai-hub-prediction-text-testing-select-the-environment](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-select-the-environment.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
5. On the next page, you will be prompted to enter input information that the model will use to predict the target text, as shown in the image below. In this example, we provide the ICD Code and a Long Description of the disease. Based on this input, the model predicts the possible disease.
    ![ai-hub-prediction-text-testing-cases2](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-cases2.png)
6. After entering the details in all the required fields needed for the model to perform the prediction, click the Predict Text button on the bottom of the screen to predict the text entered.
    ![ai-hub-prediction-text-testing-predict-test](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-predict-test.png)

### Batch Test

To perform batch test on the model, follow the steps below:

1. Click on a specific model version from the Versions page. You will be directed to the All Tests page, which contains two primary tabs: Single and Batch, each representing a different type of testing.
    ![ai-hub-prediction-text-testing-landing](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-landing.gif)
2. Click the Batch tab, then click the Add button in the top-right corner to create a new test.
    ![ai-hub-prediction-text-test-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-batch.png)
3. In the next step, select the environment in which the model is deployed. This can be either the Sandbox or Production environment. In the example below, only the Sandbox environment is displayed in the dropdown, as it is the only one configured as illustrated in the image below:
    ![ai-hub-prediction-text-testing-select-the-environment-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-text-testing-select-the-environment-batch.png)
    After selecting the environment on which the model should be tested, click the Next button to proceed. Note: The model must be deployed to the selected environment before you can proceed. If the model is not deployed, testing cannot be performed.
4. On the next page, you will be prompted to choose the file type—either Excel or CSV. Select the desired file type, then click Next at the bottom of the screen as illustrated in the image below:
    ![ai-hub-prediction-text-test-batch-file-type](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-batch-file-type.png)
5. In the next page, you have an option to upload the file. Note: The uploaded file must contain the Ground Truth column integrated within them. Ground Truth is a column that contains the expected outcome of the prediction.
    You can download a sample sheet from the platform to enter test data in the required format by clicking the Sample Excel File button.
    ![ai-hub-prediction-text-test-batch-sample-file](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-batch-sample-file.png)
    Once the required test data is uploaded, click the Start Testing button at the bottom of the page.
    ![ai-hub-prediction-text-test-batch-start-test](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-batch-start-test.png)
6. After clicking the Start Testing button, you will be directed to the Batch tab on the test page, where the batch file appears in the In Progress state. Once testing is complete, the status will be updated to Completed.
    ![ai-hub-prediction-text-test-batch-list](/resources/Storage/ai-hub/images/ai-hub-prediction-text-test-batch-list.png)
7. Click a specific batch test entry to open and view its detailed results as illustrated in the GIF below:
   ![ai-hub-prediction-text-batch-test-detailed](/resources/Storage/ai-hub/images/ai-hub-prediction-text-batch-test-detailed.gif)
