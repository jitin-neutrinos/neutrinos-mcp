# Single Input Validation

<https://documentation.neutrinos.com/articles/#!ai-hub/integrate-apis-text-prediction>

APIs can be integrated into the upper service layer, enabling seamless consumption of the platform’s utility functions without relying on the UI. These APIs support both single predictions and batch predictions, allowing you to process individual text inputs or entire datasets containing multiple text inputs.

### Single Input Validation

To integrate single input validation API follow the steps below:

1. Navigate to prediction using the left navigation panel.
    ![ai-hub-prediction-integrate-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-land-page.png)
2. Open the desired model from the list of available prediction models.
    ![ai-hub-prediction-integrate-choose-model](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-choose-model.png)
3. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-prediction-text-integration-choose](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-choose.png)
4. Select the appropriate model version, deployed environment, and the Start Single Test API option from the Version, Environment, and API drop-downs, respectively as shown in the image below:
    ![ai-hub-prediction-text-integration-choose-version-env-api](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-choose-version-env-api.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The model should be deployed in either production or sandbox environments to use the APIs. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
5. Copy the cURL from the right panel:
    ![ai-hub-prediction-text-integration-copy-curl](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-copy-curl.png)
    Paste the copied cURL into any compatible API testing tool. Note: Ensure that you provide the required body parameters, including headers and values, formatted as key-value pairs. The input for the body parameters should correspond to the expected fields used when training the model. For example, if the model was trained using fields such as "ICD Code" and "Description of Disease", you must supply these as keys in the API request body, as shown below:
    Copy CodeJSON"input": {
    "ICD CODE": "NEU_A0104",
    "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Typhoid arthritis"
   }
6. Pass the authorization bearer token, which can be generated from IDS or from the AI Hub platform.
7. Upon successful execution, the API returns the prediction result in two distinct sections: Output and Result.
    Copy CodeJSON{
    "training_config_id": "6837e8ccb833a5a73e337d56",
    "training_id": "6837e8ccb833a5a73e337d55",
    "test_id": "683d8038e17e965047a08848",
    "tenant_id": "6225cde095f5119c54aa1234",
    "processing_time": 0.36,
    "ignored": false,
    "retrained": false,
    "input": {
    "ICD CODE": "NEU_A0104",
    "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Typhoid arthritis"
    },
    "output": {
    "category": {
    "name": "Typhoid",
    "confidence": 0.8310785293579102
    },
    "categories": [
    {
    "name": "infection",
    "confidence": 0.016671953722834587
    },
    {
    "name": "Shigellosis",
    "confidence": 0.020424792543053627
    },
    {
    "name": "Others",
    "confidence": 0.07316602766513824
    },
    {
    "name": "Tuberculosis",
    "confidence": 0.01846451498568058
    },
    {
    "name": "Salmonella",
    "confidence": 0.04019417241215706
    },
    {
    "name": "Typhoid",
    "confidence": 0.8310785293579102
    }
    ]
    },
    "result": {
    "predictions": [
    "Typhoid"
    ],
    "probabilities": [
    {
    "infection": 0.016671953722834587,
    "Shigellosis": 0.020424792543053627,
    "Others": 0.07316602766513824,
    "Tuberculosis": 0.01846451498568058,
    "Salmonella": 0.04019417241215706,
    "Typhoid": 0.8310785293579102
    }
    ]
    },
    "created_by": "Swathi N",
    "status": "Completed",
    "deleted": false,
    "test_type": "Single",
    "data_type": "Text",
    "model_type": "Classification",
    "deployment_id": "68398aa1b833a5a73e34497c",
    "merged": false,
    "manual_review_flag": false,
    "inference_time": 0.36,
    "review_status": "Pending",
    "metadata": {
    "key": "value"
    },
    "_id": "683d8038e17e965047a08852",
    "created_at": "2025-06-02T10:43:04.967Z",
    "updated_at": "2025-06-02T10:43:04.967Z",
    "id": "683d8038e17e965047a08852"
   }
  - The Output section presents the prediction in a structured format, typically under labeled fields such as name and confidence, organized within a nested dictionary. Each entry in the dictionary represents a predicted category label and its corresponding confidence score. This structured format allows the prediction results to be easily consumed by upper service layers or applications for further processing.
  - The Result section contains the raw output of the prediction, providing the unprocessed response returned by the model.

### Batch Input Validation

Unlike single input validation, batch input validation involves multiple endpoints that must be triggered to obtain the final output. Follow the steps below to validate batch inputs:

1. Navigate to prediction using the left navigation panel.
    ![ai-hub-prediction-integrate-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-land-page.png)
2. Open the desired model from the list of available prediction models.
    ![ai-hub-prediction-integrate-choose-model](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-choose-model.png)
3. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-prediction-text-integration-choose](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-choose.png)
4. To trigger a batch test, multiple endpoints must be called. Use the following endpoints:
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: To retrieve the result of a specific output ID, copy the desired ID from the Find All API response and pass it to the ../result/find-one/{id} API endpoint as a path parameter.
  1. **Create Batch Test**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/create/batch"
     The first step is to create a batch for testing. Use the following API endpoint to initiate the batch.
      Copy CodeJSON{
      "callback_url": "",
      "is_file": true,
      "metadata": {
      "key": "value"
      }
     }
      The response includes a batch ID, represented by _id, which must be used in the next step to upload the batch file.
      Copy CodeJSON{
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Classification",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "is_file": true,
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "metadata": {
      "key": "value"
      },
      "_id": "683d6e42e17e965047a07aaa",
      "created_at": "2025-06-02T09:26:26.649Z",
      "updated_at": "2025-06-02T09:26:26.649Z",
      "id": "683d6e42e17e965047a07aaa"
     }
    - **callback_url**: Accepts the webpage URL where the result will be sent.
    - **is_file**: Accepts a boolean value: true or false.
      - If set to true, you must pass the file as a parameter when triggering the API.
      - If set to false, you must pass the file_id, which can be generated using a generic API endpoint.
    - **metadata**: Accepts key-value pairs of any metadata that needs to be passed as parameters when triggering the API.
  2. **Upload Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/upload/batch/{id}"
     In this API endpoint, you must pass the batch ID—represented by _id and returned by the previous API—as a path parameter. Additionally, you must either provide the file_id generated using the generic upload API or upload a file in the required format, which can be downloaded from the platform. In this example, the file upload option is used, with a file obtained in the prescribed format.
      The image below illustrates both options—uploading a file or passing the file_id as a parameter—when triggering this API endpoint in Postman for demonstration purposes.
      ![ai-hub-prediction-text-integration-upload-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-upload-batch1.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: In this API endpoint, you must choose either the file upload option or provide the file_id. Both options cannot be used simultaneously.
      The API response will be similar to the example shown below, with a status of "Created" indicating that a batch with a specific ID has been successfully created.
      Copy CodeJSON{
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "tenant_id": "6225cde095f5119c54aa1234",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Classification",
      "file_name": "1748856465845-680b125c56652d55eccf2eef-sample.xls",
      "mime_type": "application/vnd.ms-excel",
      "file_url": "6225cde095f5119c54aa1234/6837e8ccb833a5a73e337d56/6837e8ccb833a5a73e337d55/683d6e42e17e965047a07aaa/975e4755-e4b2-48c7-a9b1-221b3f5e10d7/1748856465845-680b125c56652d55eccf2eef-sample.xls",
      "file_uuid": "975e4755-e4b2-48c7-a9b1-221b3f5e10d7",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "file_id": "683d6e92e17e965047a07ae2",
      "size": 11614,
      "_id": "683d6e92e17e965047a07ae8",
      "created_at": "2025-06-02T09:27:46.212Z",
      "updated_at": "2025-06-02T09:27:46.212Z",
      "id": "683d6e92e17e965047a07ae8"
     }
  3. **Start Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/start/batch/{id}"
     This initiates the execution of the batch created in the previous steps. You must pass the batch ID, represented as _id returned in the response from the Create Batch API in the CURL as a path parameter as illustrated in the image below.
      ![ai-hub-prediction-text-integration-start-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-start-batch.png)
      The batch size specifies the number of rows in the uploaded file that should be processed as a single batch. For example, if the file contains 100 rows and the batch size is set to 20, the data will be divided into 5 separate batches.
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: The batch size affects the results displayed in the Inference tab on the platform’s UI.
      The API should return a 201 Created response, with the status set to "PENDING" as illustrated in the image below:
      ![ai-hub-prediction-text-integration-complete-start-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-text-integration-complete-start-batch.png)
  4. **Batch Find**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/batch/find/{id}"
     Trigger this API by passing the _id returned by Create Batch API endpoint to check the status of the batch test. The response will return the current status of the batch, which progresses through the following states:
      The time taken for the status to transition from "PENDING" to "COMPLETED / FAILED" depends on the size of the sample provided to the model for prediction. The response from this API endpoint will be similar to the example shown below:
      Copy CodeJSON{
      "_id": "683d6e42e17e965047a07aaa",
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Classification",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "is_file": true,
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-02T09:26:26.649Z",
      "updated_at": "2025-06-02T09:29:00.562Z",
      "metrics": {
      "precision": 0.8392857142857143,
      "recall": 0.8441558441558442,
      "f1_score": 0.8410894422523867,
      "accuracy": 0.97
      },
      "processing_time": 13.49,
      "callback_info": [
      {
      "error": "Error during API request to : Request error: Request URL is missing an 'http://' or 'https://' protocol. for URL: "
      }
      ],
      "id": "683d6e42e17e965047a07aaa"
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      The callback_info error appears in the result when the batch is created without specifying a callback_url, or if the provided URL is invalid.
      Additionally, this API provides prediction metrics such as Precision, Recall, F1 Score, and Confidence, which are also reflected in the platform’s UI.
    - **PENDING**: when the batch is first triggered via the Start Batch API.
    - **IN_PROGRESS**: when the batch processing begins.
    - **COMPLETED**: once processing is finished.
    - **FAILED**: batch processing encountered an error.
  5. **Batch Data**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/batch/data/{id}"
     Pass the _id returned by the Create Batch API in the URL of the API endpoint. In the body of this API request, you can configure how the output is presented by specifying parameters such as:
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      }
     }
      The response from executing this API will be similar to the example shown below:
      Copy CodeJSON{
      "data": [
      {
      "_id": "683d6e92e17e965047a07ae8",
      "test_type": "Batch",
      "data_type": "Text",
      "file_name": "1748856465845-680b125c56652d55eccf2eef-sample.xls",
      "mime_type": "application/vnd.ms-excel",
      "file_url": "6225cde095f5119c54aa1234/6837e8ccb833a5a73e337d56/6837e8ccb833a5a73e337d55/683d6e42e17e965047a07aaa/975e4755-e4b2-48c7-a9b1-221b3f5e10d7/1748856465845-680b125c56652d55eccf2eef-sample.xls",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "file_id": "683d6e92e17e965047a07ae2",
      "created_at": "2025-06-02T09:27:46.212Z",
      "updated_at": "2025-06-02T09:29:00.361Z",
      "r_count": 100
      }
      ],
      "count": 1
     }
      The result of the execution is indicated by the status changing to "COMPLETED". To view the batch results, copy the ID represented by _id and use it in the API endpoint described in the next step.
    - **page_number**: Set the starting page number to display the output.
    - **page_size**: Define the number of results per page.
    - **sort**: Determines the order in which the results are displayed.
  6. **Results Find All**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/results/find-all"
     This API returns the results of the batch test. To retrieve the results, include the _id (returned from the Batch Data API in the previous step) in the request body under the parameter "test_id" as shown below:
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      },
      "test_id": "683d6e92e17e965047a07ae8",
      "merged": false
     }
      Upon successful execution, the API returns the prediction result in two distinct sections: Output and Result.
      Copy CodeJSON{
      "count": 100,
      "data": [
      {
      "_id": "683d6ec6e17e965047a07b8d",
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "test_id": "683d6e92e17e965047a07ae8",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      "Others"
      ],
      "input": {
      "ICD CODE": "NEU_A080",
      "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Rotaviral enteritis"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-02T09:28:38.139Z",
      "updated_at": "2025-06-02T09:28:48.325Z",
      "model_type": "Classification",
      "inference_time": 1.75,
      "output": {
      "category": {
      "name": "Others",
      "confidence": 0.9073771238327026
      },
      "categories": [
      {
      "name": "infection",
      "confidence": 0.012739913538098335
      },
      {
      "name": "Shigellosis",
      "confidence": 0.013693339191377163
      },
      {
      "name": "Others",
      "confidence": 0.9073771238327026
      },
      {
      "name": "Tuberculosis",
      "confidence": 0.014323481358587742
      },
      {
      "name": "Salmonella",
      "confidence": 0.03303829953074455
      },
      {
      "name": "Typhoid",
      "confidence": 0.01882784254848957
      }
      ]
      },
      "processing_time": 2.21,
      "result": {
      "predictions": [
      "Others"
      ],
      "probabilities": {
      "infection": 0.012739913538098335,
      "Shigellosis": 0.013693339191377163,
      "Others": 0.9073771238327026,
      "Tuberculosis": 0.014323481358587742,
      "Salmonella": 0.03303829953074455,
      "Typhoid": 0.01882784254848957
      }
      }
      },
      {
      "_id": "683d6ec6e17e965047a07b8e",
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "test_id": "683d6e92e17e965047a07ae8",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      "Others"
      ],
      "input": {
      "ICD CODE": "NEU_A0811",
      "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Acute gastroenteropathy due to Norwalk agent"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-02T09:28:38.218Z",
      "updated_at": "2025-06-02T09:28:48.325Z",
      "model_type": "Classification",
      "inference_time": 1.75,
      "output": {
      "category": {
      "name": "Others",
      "confidence": 0.9777830243110657
      },
      "categories": [
      {
      "name": "infection",
      "confidence": 0.0017449939623475075
      },
      {
      "name": "Shigellosis",
      "confidence": 0.012828943319618702
      },
      {
      "name": "Others",
      "confidence": 0.9777830243110657
      },
      {
      "name": "Tuberculosis",
      "confidence": 0.0021523330360651016
      },
      {
      "name": "Salmonella",
      "confidence": 0.002715703099966049
      },
      {
      "name": "Typhoid",
      "confidence": 0.002775003667920828
      }
      ]
      },
      "processing_time": 2.21,
      "result": {
      "predictions": [
      "Others"
      ],
      "probabilities": {
      "infection": 0.0017449939623475075,
      "Shigellosis": 0.012828943319618702,
      "Others": 0.9777830243110657,
      "Tuberculosis": 0.0021523330360651016,
      "Salmonella": 0.002715703099966049,
      "Typhoid": 0.002775003667920828
      }
      }
      },
      {
      "_id": "683d6ec6e17e965047a07b8f",
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "test_id": "683d6e92e17e965047a07ae8",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      "Others"
      ],
      "input": {
      "ICD CODE": "NEU_A0819",
      "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Acute gastroenteropathy due to other small round viruses"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-02T09:28:38.218Z",
      "updated_at": "2025-06-02T09:28:48.325Z",
      "model_type": "Classification",
      "inference_time": 1.75,
      "output": {
      "category": {
      "name": "Others",
      "confidence": 0.9854288101196289
      },
      "categories": [
      {
      "name": "infection",
      "confidence": 0.001213995972648263
      },
      {
      "name": "Shigellosis",
      "confidence": 0.0067148529924452305
      },
      {
      "name": "Others",
      "confidence": 0.9854288101196289
      },
      {
      "name": "Tuberculosis",
      "confidence": 0.0014358084881678224
      },
      {
      "name": "Salmonella",
      "confidence": 0.002300068037584424
      },
      {
      "name": "Typhoid",
      "confidence": 0.002906502690166235
      }
      ]
      },
      "processing_time": 2.21,
      "result": {
      "predictions": [
      "Others"
      ],
      "probabilities": {
      "infection": 0.001213995972648263,
      "Shigellosis": 0.0067148529924452305,
      "Others": 0.9854288101196289,
      "Tuberculosis": 0.0014358084881678224,
      "Salmonella": 0.002300068037584424,
      "Typhoid": 0.002906502690166235
      }
      }
      },
      {
      "_id": "683d6ec6e17e965047a07b90",
      "training_config_id": "6837e8ccb833a5a73e337d56",
      "training_id": "6837e8ccb833a5a73e337d55",
      "test_id": "683d6e92e17e965047a07ae8",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      "Others"
      ],
      "input": {
      "ICD CODE": "NEU_A082",
      "LONG DESCRIPTION (VALID ICD-10 FY2025)": "Adenoviral enteritis"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "683d6e42e17e965047a07aaa",
      "deployment_id": "68398aa1b833a5a73e34497c",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-02T09:28:38.218Z",
      "updated_at": "2025-06-02T09:28:48.325Z",
      "model_type": "Classification",
      "inference_time": 1.75,
      "output": {
      "category": {
      "name": "Others",
      "confidence": 0.8926535248756409
      },
      "categories": [
      {
      "name": "infection",
      "confidence": 0.01269503589719534
      },
      {
      "name": "Shigellosis",
      "confidence": 0.014884509146213531
      },
      {
      "name": "Others",
      "confidence": 0.8926535248756409
      },
      {
      "name": "Tuberculosis",
      "confidence": 0.014153346419334412
      },
      {
      "name": "Salmonella",
      "confidence": 0.04631384089589119
      },
      {
      "name": "Typhoid",
      "confidence": 0.01929972507059574
      }
      ]
      },
      "processing_time": 2.21,
      "result": {
      "predictions": [
      "Others"
      ],
      "probabilities": {
      "infection": 0.01269503589719534,
      "Shigellosis": 0.014884509146213531,
      "Others": 0.8926535248756409,
      "Tuberculosis": 0.014153346419334412,
      "Salmonella": 0.04631384089589119,
      "Typhoid": 0.01929972507059574
      }
      }
      },
      .
      .
      .
      .
      "processing_time": 2.21,
      "result": {
      "predictions": [
      "infection"
      ],
      "probabilities": {
      "infection": 0.931662917137146,
      "Shigellosis": 0.004713042639195919,
      "Others": 0.05526477098464966,
      "Tuberculosis": 0.0037297881208360195,
      "Salmonella": 0.002273030113428831,
      "Typhoid": 0.002356411889195442
      }
      }
      }
      ]
     }
    - The Output section presents the prediction in a structured format, typically under labeled fields such as name and confidence, organized within a nested dictionary. Each entry in the dictionary represents a predicted category label and its corresponding confidence score. This structured format allows the prediction results to be easily consumed by upper service layers or applications for further processing.
    - The Result section contains the raw output of the prediction, providing the unprocessed response returned by the model.
