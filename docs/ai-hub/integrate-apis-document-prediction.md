# Single Input Document Validation

<https://documentation.neutrinos.com/articles/#!ai-hub/integrate-apis-document-prediction>

APIs can be integrated into the upper service layer, enabling seamless consumption of the platform’s utility functions without relying on the UI. These APIs support both single predictions and batch predictions, allowing you to process individual document inputs or multiple document inputs.

### Single Input Document Validation

To integrate single input validation API follow the steps below:

1. Navigate to prediction using the left navigation panel.
    ![ai-hub-prediction-integrate-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-land-page.png)
2. Click the document tab on the prediction page.
    ![ai-hub-prediction-document-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-document-land-page.png)
3. Open the desired model from the list of available prediction models.
    ![ai-hub-prediction-document-select-model-single-validate](/resources/Storage/ai-hub/images/ai-hub-prediction-document-select-model-single-validate.png)
4. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-prediction-document-integration-click](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-click.png)
5. Select the appropriate model version, deployed environment, and the Start Single Test API option from the Version, Environment, and API drop-downs, respectively as shown in the image below:
    ![ai-hub-prediction-document-integration-select-version-env-api](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-select-version-env-api.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: To use the APIs, the model must be deployed in either the production or sandbox environment. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
6. Copy the CURL from the right panel.
    ![ai-hub-prediction-document-integration-copy-curl](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-copy-curl.png)
    Paste the copied CURL command into any compatible API testing tool. Upload the document either directly from your local machine or by using the file_id.
  1. **Upload File**: In this API endpoint, ensure that only the file field is selected in the request body; uncheck the file_id field. Upload an image from your local machine to initiate the prediction process as shown in the image below. Note: For illustration purposes, we have used Postman as the API testing tool. However, you may use any compatible tool based on your preference.
      ![ai-hub-prediction-document-integration-file-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-file-upload.png)
  2. **Generate file_id**: To generate the file_id required for this API endpoint, use the generic file upload endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/file/upload". Upload the file using the file parameter in the request body. The response will contain an _id field, which represents the file_id.
      Copy CodeJSON{
      "file_name": "5.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/005b9fbf-e193-4fd5-ad40-bbd32ec6bb4e/5.jpg",
      "size": 150870,
      "page_count": 1,
      "file_uuid": "005b9fbf-e193-4fd5-ad40-bbd32ec6bb4e",
      "created_by": "S****i N",
      "deleted": false,
      "tenant_id": "6225cde095f5119c54aa1234",
      "_id": "683ffa54e17e965047a10470",
      "input_urls": [],
      "created_at": "2025-06-04T07:48:36.465Z",
      "updated_at": "2025-06-04T07:48:36.465Z",
      "id": "683ffa54e17e965047a10470"
     }
      This _id should then be passed as a parameter in the body of the Start Single Test API as illustrated in the image below:
      ![ai-hub-prediction-document-integration-file-id-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-file-id-upload.png)
7. Pass the authorization bearer token, which can be generated from IDS or from the AI Hub platform.
8. Upon successful execution, the API returns the prediction result in two distinct sections: Output and Result.
    Copy CodeJSON[
    {
    "training_config_id": "681af95974d546f5b4b06987",
    "training_id": "681af95974d546f5b4b06986",
    "test_id": "68400589e17e965047a10515",
    "tenant_id": "6225cde095f5119c54aa1234",
    "processing_time": 2.55,
    "ignored": false,
    "retrained": false,
    "output": {
    "category": {
    "name": "aadhaar_front",
    "confidence": 0.8494129776954651
    },
    "categories": [
    {
    "name": "eid_front",
    "confidence": 0.06112699955701828
    },
    {
    "name": "eid_back",
    "confidence": 0.03759494796395302
    },
    {
    "name": "aadhaar_front",
    "confidence": 0.8494129776954651
    },
    {
    "name": "aadhaar_back",
    "confidence": 0.051865145564079285
    }
    ]
    },
    "result": {
    "predictions": [
    "aadhaar_front"
    ],
    "probabilities": [
    {
    "eid_front": 0.06112699955701828,
    "eid_back": 0.03759494796395302,
    "aadhaar_front": 0.8494129776954651,
    "aadhaar_back": 0.051865145564079285
    }
    ]
    },
    "created_by": "S****i N",
    "updated_by": "S****i N",
    "status": "Completed",
    "deleted": false,
    "test_type": "Single",
    "data_type": "Document",
    "file_name": "1749026185283-5.png",
    "mime_type": "image/png",
    "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/684005896f37302a56dafd42/3257e94b-e2df-460d-86ca-89a4e35f5ec5/1749026185283-5.png",
    "size": 1147147,
    "deployment_id": "681b095374d546f5b4b07241",
    "merged": false,
    "page_count": 1,
    "group_id": null,
    "manual_review_flag": false,
    "thumbnail_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/684005896f37302a56dafd42/3257e94b-e2df-460d-86ca-89a4e35f5ec5/thumbnails/e51c566d-4ab3-47b9-97de-aefd3ae23102_thumbnail.jpg",
    "inference_time": 1.55,
    "review_status": "Pending",
    "thumbnail_size": 13340,
    "_id": "6840058ce17e965047a1051c",
    "created_at": "2025-06-04T08:36:28.352Z",
    "updated_at": "2025-06-04T08:36:28.352Z",
    "id": "6840058ce17e965047a1051c"
    }
   ]
  - The Output section presents the prediction in a structured format, typically under labeled fields such as name and confidence, organized within a nested dictionary. Each entry in the dictionary represents a predicted category label and its corresponding confidence score. This structured format allows the prediction results to be easily consumed by upper service layers or applications for further processing.
  - The Result section contains the raw output of the prediction, providing the unprocessed response returned by the model.

### Batch Input Document Validation

Unlike single input validation, batch input validation involves multiple endpoints that must be triggered to obtain the final output. Follow the steps below to validate batch inputs:

1. Navigate to prediction using the left navigation panel.
    ![ai-hub-prediction-integrate-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-integrate-land-page.png)
2. Click the document tab on the prediction page.
    ![ai-hub-prediction-document-land-page](/resources/Storage/ai-hub/images/ai-hub-prediction-document-land-page.png)
3. Open the desired model from the list of available prediction models.
    ![ai-hub-prediction-document-select-model-single-validate](/resources/Storage/ai-hub/images/ai-hub-prediction-document-select-model-single-validate.png)
4. On the model page, click Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-prediction-document-integration-click](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-click.png)
5. To trigger a batch test, multiple endpoints must be called. Use the following endpoints:
  1. **Create Batch Test**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/create/batch"
      The first step is to create a batch for testing. Use the endpoint provided above to initiate the creation of a new test batch.
      Copy CodeJSON{
      "callback_url": "",
      "is_file": true,
      "metadata": {
      "key": "value"
      }
     }
      The response includes a batch ID, represented by _id, which must be used in the next step to upload the batch file.
      Copy CodeJSON{
      "training_config_id": "681af95974d546f5b4b06987",
      "training_id": "681af95974d546f5b4b06986",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "681b095374d546f5b4b07241",
      "test_type": "Batch",
      "data_type": "Document",
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
      "_id": "684141e4e17e965047a11d00",
      "created_at": "2025-06-05T07:06:12.053Z",
      "updated_at": "2025-06-05T07:06:12.053Z",
      "id": "684141e4e17e965047a11d00"
     }
    - **callback_url**: Accepts the webpage URL where the result will be sent.
    - **is_file**: Accepts a boolean value: true or false.
      - If set to true, you must pass the file as a parameter when triggering the API.
      - If set to false, you must pass the file_id, which can be generated using a generic API endpoint.
    - **metadata**: Accepts key-value pairs of any metadata that needs to be passed as parameters when triggering the API.
  2. **Upload Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/upload/batch/{id}"
      At this endpoint, you must either provide the file_id obtained from the generic file upload API or directly upload a single document. Note: This API supports uploading only one document at a time. It does not support uploading multiple documents in a single request. To add multiple documents to the same batch, trigger this API separately for each document upload.
      The image below illustrates both options—uploading a file or passing the file_id as a parameter—when triggering this API endpoint in Postman for demonstration purposes.
      ![ai-hub-prediction-document-integration-batch-upload](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-batch-upload.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: In this API endpoint, you must choose either the file upload option or provide the file_id. Both options cannot be used simultaneously.
      The API response will be similar to the example shown below, with a status of "Created" indicating that a batch with a specific ID has been successfully created.
      Copy CodeJSON{
      "training_config_id": "681af95974d546f5b4b06987",
      "training_id": "681af95974d546f5b4b06986",
      "tenant_id": "6225cde095f5119c54aa1234",
      "test_type": "Batch",
      "data_type": "Document",
      "model_type": "Classification",
      "file_name": "1749184176415-5.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/684141e4e17e965047a11d00/bc58d065-9449-43da-a980-6ad3a1f4a1f5/1749184176415-5.jpg",
      "file_uuid": "bc58d065-9449-43da-a980-6ad3a1f4a1f5",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "batch_id": "684141e4e17e965047a11d00",
      "deployment_id": "681b095374d546f5b4b07241",
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "file_id": "68426eb1e17e965047a14079",
      "page_count": 1,
      "size": 150870,
      "_id": "68426eb1e17e965047a1407f",
      "created_at": "2025-06-06T04:29:37.387Z",
      "updated_at": "2025-06-06T04:29:37.387Z",
      "id": "68426eb1e17e965047a1407f"
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: To upload multiple documents, you must trigger this API endpoint separately for each document. Repeat the API call for the required number of document uploads.
  3. **Start Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/start/batch/{id}"
      This endpoint initiates the execution of the batch created in the previous steps. You must pass the batch ID, represented as _id returned in the response from the Create Batch API in the CURL as illustrated in the image below.
      ![ai-hub-prediction-document-integration-start-batch](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-start-batch.png)
      The batch size defines the number of documents to be processed together in a single batch. For example, if 100 documents are uploaded and the batch size is set to 20, the system will divide the documents into 5 separate batches of 20 each.
      The API should return a 201 Created response, with the status set to "PENDING" as illustrated in the image below:
      ![ai-hub-prediction-document-integration-batch-start](/resources/Storage/ai-hub/images/ai-hub-prediction-document-integration-batch-start.png)
  4. **Batch Information**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/batch/find/{id}"
      Trigger this API to check the status of the batch test. Pass the id represented by _id returned from the Create Batch endpoint as a path parameter. The response will indicate the current status of the batch, which progresses through the following states:
      The time taken for the status to transition from "PENDING" to "COMPLETED" / "FAILED" depends on the size of the sample provided to the model for prediction. The response from this API endpoint will be similar to the example shown below:
      Copy CodeJSON{
      "_id": "684141e4e17e965047a11d00",
      "training_config_id": "681af95974d546f5b4b06987",
      "training_id": "681af95974d546f5b4b06986",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "681b095374d546f5b4b07241",
      "test_type": "Batch",
      "data_type": "Document",
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
      "created_at": "2025-06-05T07:06:12.053Z",
      "updated_at": "2025-06-06T04:47:06.023Z",
      "processing_time": 31.61,
      "callback_info": [
      {
      "error": "Error during API request to : Request error: Request URL is missing an 'http://' or 'https://' protocol. for URL: "
      }
      ],
      "id": "684141e4e17e965047a11d00"
     }
    - **PENDING**: when the batch is first triggered via the Start Batch API.
    - **IN_PROGRESS**: when the batch processing begins.
    - **COMPLETED**: once processing is finished.
    - **FAILED**: batch processing encountered an error.
  5. **Batch test data**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/classification/batch/data/{id}"
      This API endpoint returns the prediction results status for the entire batch, including the outcomes for each document within the batch. Each document in the batch is associated with a unique id, represented as _id in the response. This id can be used to retrieve the prediction details of an individual document.
      Copy CodeJSON{
      "data": [
      {
      "_id": "684294e1e17e965047a14370",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749193953239-5.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/6842945ce17e965047a1435e/179cc3d7-1ac3-4569-8493-df52a9416657/1749193953239-5.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "6842945ce17e965047a1435e",
      "deployment_id": "681b095374d546f5b4b07241",
      "file_id": "684294e1e17e965047a1436a",
      "created_at": "2025-06-06T07:12:33.609Z",
      "updated_at": "2025-06-06T07:14:46.153Z",
      "r_count": 1
      },
      {
      "_id": "684294eee17e965047a1437e",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749193965710-51.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/6842945ce17e965047a1435e/bb13e4f3-b016-407d-bc1a-21eaa8baf516/1749193965710-51.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "6842945ce17e965047a1435e",
      "deployment_id": "681b095374d546f5b4b07241",
      "file_id": "684294ede17e965047a14378",
      "created_at": "2025-06-06T07:12:46.075Z",
      "updated_at": "2025-06-06T07:14:46.153Z",
      "r_count": 1
      },
      {
      "_id": "684294f6e17e965047a1438c",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749193974476-52.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/6842945ce17e965047a1435e/da5aeb5c-4008-4b93-97f3-0a1b4dec0b6d/1749193974476-52.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "6842945ce17e965047a1435e",
      "deployment_id": "681b095374d546f5b4b07241",
      "file_id": "684294f6e17e965047a14386",
      "created_at": "2025-06-06T07:12:54.856Z",
      "updated_at": "2025-06-06T07:14:46.153Z",
      "r_count": 1
      }
      ],
      "count": 3
     }
  6. **List batch data**: Endpoint: https://aihub-staging.neutrinos.com/inferenceservice/classification/results/find-all
      This endpoint returns the prediction result of an individual document from the batch. It accepts the id of the specific document—generated by the Batch Data endpoint—as a body parameter, and returns the corresponding prediction result.
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      },
      "test_id": "684294eee17e965047a1437e",
      "merged": false
     }
      The response returned by this call is as illustrated below:
      Copy CodeJSON{
      "count": 1,
      "data": [
      {
      "_id": "68429555e17e965047a143ca",
      "training_config_id": "681af95974d546f5b4b06987",
      "training_id": "681af95974d546f5b4b06986",
      "test_id": "684294eee17e965047a1437e",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749193965710-51.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/6842945ce17e965047a1435e/89feb783-65fb-4a50-ae10-28667575ee06/1749193965710-51.jpg",
      "size": 389328,
      "page_number": 1,
      "batch_id": "6842945ce17e965047a1435e",
      "deployment_id": "681b095374d546f5b4b07241",
      "merged": false,
      "manual_review_flag": false,
      "thumbnail_url": "6225cde095f5119c54aa1234/681af95974d546f5b4b06987/681af95974d546f5b4b06986/6842945ce17e965047a1435e/0dba0bd3-ba78-4d57-9ca7-fbb5381b3801/thumbnails/1749193965710-51_thumb.jpg",
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "thumbnail_size": 7424,
      "created_at": "2025-06-06T07:14:29.811Z",
      "updated_at": "2025-06-06T07:14:35.177Z",
      "model_type": "Classification",
      "inference_time": 1.49,
      "output": {
      "category": {
      "name": "aadhaar_front",
      "confidence": 0.590658962726593
      },
      "categories": [
      {
      "name": "eid_front",
      "confidence": 0.361062616109848
      },
      {
      "name": "eid_back",
      "confidence": 0.025128742679953575
      },
      {
      "name": "aadhaar_front",
      "confidence": 0.590658962726593
      },
      {
      "name": "aadhaar_back",
      "confidence": 0.023149680346250534
      }
      ]
      },
      "processing_time": 2.8,
      "result": {
      "predictions": [
      "aadhaar_front"
      ],
      "probabilities": {
      "eid_front": 0.361062616109848,
      "eid_back": 0.025128742679953575,
      "aadhaar_front": 0.590658962726593,
      "aadhaar_back": 0.023149680346250534
      }
      }
      }
      ]
     }
    - The Output section presents the prediction in a structured format, typically under labeled fields such as name and confidence, organized within a nested dictionary. Each entry in the dictionary represents a predicted category label and its corresponding confidence score. This structured format allows the prediction results to be easily consumed by upper service layers or applications for further processing.
    - The Result section contains the raw output of the prediction, providing the unprocessed response returned by the model.
