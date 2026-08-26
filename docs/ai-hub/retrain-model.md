# Retrain Model

<https://documentation.neutrinos.com/articles/#!ai-hub/retrain-model>

Retraining a model is the process of reinforcing or improving its learning. Retraining may be required due to changes in the format of the input data to be predicted or extracted. It may also be performed to enhance the model's accuracy, precision, and confidence scores. Regardless of the model type—whether it's a prediction model or an extraction model—the overall steps involved in retraining remain largely the same, as outlined in this topic.

For illustration purpose, we have used extraction model to illustrate the process of retraining. Follow the steps below to retrain the model:

1. From the left navigation panel, select either the Prediction or Extraction model option based on your requirement. In this example, we have chosen to retrain an Extraction type model.
    ![ai-hub-extraction-retrain-start-page](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-start-page.png)
2. On the Models page—whether Extraction or Prediction—select the model that you want to retrain.
    ![ai-hub-extraction-retrain-select-model](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-select-model.png)
3. On the Versions page, click the Retrain button located at the top-right corner of the screen.
    ![ai-hub-extraction-retrain-retrain-button](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-retrain-button.png)
4. After clicking the Retrain button, a prompt appears to select the model version you wish to retrain. You can either select an existing version from the dropdown list or choose to train a fresh model from scratch.
    Training a fresh model follows the same steps as creating a new model. For more information on model creation, refer to the [Prediction](/articles/ai-hub/prediction) or [Extraction](/articles/ai-hub/extraction) topics, depending on your requirements.
    For training an existing model, choose the version from the dropdown, and click Next at the bottom of the screen.
    ![ai-hub-extraction-retrain-select-version-next](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-select-version-next.png)
    Additionally, you can configure settings under the Advanced Configurations section for the new version being retrained. Click the gear icon on the top of the page to configure Advanced Configuration as illustrated in the image below:
    ![ai-hub-extraction-retrain-adv-congif-choose](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-adv-congif-choose.png)
5. In this step, choose the data to retrain the model. You can wish to retrain the data using the reviewed data available from a specific version or choose new data altogether.
  1. **Data from Specific Version**: On the Retrain page, use the left panel to select the version(s) available for retraining. You can choose one or more versions to fetch data from, which will be used to retrain the model. The data pulled from these versions corresponds to the records reviewed and approved in the Review Hub for each selected model version.
      ![ai-hub-extraction-retrain-choose-version](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-choose-version.png)
      Once the versions are selected, the right panel displays the corresponding data. Review and choose the specific data entries you want to include as training data for the model. If you wish to use all available data from the selected version(s), check the box at the top to select all entries at once.
      After selecting the required data, click the Next button at the bottom of the screen.
      ![ai-hub-extraction-retrain-use-old-data-next](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-use-old-data-next.png)
      Confirm the entries for each specified entity, then click Next. After reviewing and verifying the selected data, click Retrain to begin the retraining process.
      ![ai-hub-extraction-retrain-confirm-retrain](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-confirm-retrain.png)
      After clicking the Retrain button, a new version of the model is created and listed on the Versions page. Initially, the status of the new version will be displayed as “In Progress”, and it will automatically update to “Completed” once the retraining process is finished.
      ![ai-hub-extraction-retrain-new-version](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-new-version.png)
  2. **Add New Data**: You can retrain the model using an entirely new dataset by following the steps below:
      On the Retrain page, click the Add New Data button at the bottom of the screen to initiate the retraining process with the new dataset.
      ![ai-hub-extraction-retrain-add-new-data](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-add-new-data.png)
      You are prompted to either drag and drop a file or select one from your local computer. Choose the appropriate file and upload it to the platform and click submit to proceed:
      ![ai-hub-extraction-retrain-select-file-submit.png](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-select-file-submit.png)
      The right panel in the Retrain page, under the Data section, is updated with the contents of the newly uploaded file. A New tag is displayed against each row to indicate that the data is newly added and will be used to retrain the model.
      ![ai-hub-extraction-retrain-new-data-select](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-new-data-select.png)
      After selecting the required data for retraining, click the Next button at the bottom of the screen.
      ![ai-hub-extraction-retrain-select-data-next](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-select-data-next.png)
      On the next screen, you are presented with options to train the model using the newly uploaded data.
      Once the minimum number of entries is confirmed, the Retrain button becomes available. Click Retrain to initiate the training process. This action generates a new version of the model, which initially appears with the status In Progress and changes to Complete once training is successfully finished.
      ![ai-hub-extraction-retrain-retrain-confirm-button](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-retrain-confirm-button.png)
      After the Retrain button is clicked, a new version of the model becomes available in the Model Versions page, listed alongside the other existing versions of the selected model.
     ![ai-hub-extraction-retrain-complete](/resources/Storage/ai-hub/images/ai-hub-extraction-retrain-complete.png)
    - If you are retraining an extraction model, select the relevant entities.
    - If you are retraining a prediction model, review and confirm the predicted values.
