# Single Input Validation

<https://documentation.neutrinos.com/articles/#!ai-hub/integrate-apis-text-extraction>

The text extraction APIs enable you to leverage the platform’s extraction capabilities beyond the user interface, maximizing the utility of the service programmatically. They support both single and batch extractions, making it possible to process individual text inputs or entire datasets containing multiple inputs efficiently.

### Single Input Validation

To integrate single input validation API follow the steps below:

1. Navigate to extraction using the left navigation panel.
    ![ai-hub-extraction-text-integration-batch-models](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-batch-models.png)
2. Open the desired model from the list of available extraction models.
    ![ai-hub-extraction-text-integration-select-model](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-select-model1.png)
3. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-extraction-text-integration-click](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-click1.png)
4. Select the appropriate model version, deployed environment, and the Start Single Test API option from the Version, Environment, and API drop-downs, respectively as shown in the image below:
    ![ai-hub-extraction-text-integration-version-env-api-select](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-version-env-api-select1.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The model should be deployed in either production or sandbox environments to use the APIs. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
5. Copy the CURL from the right panel:
    ![ai-hub-extraction-text-integration-copy-curl](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-copy-curl1.png)
    Paste the copied CURL into any compatible API testing tool. Note: Ensure that you provide the required body parameters, including headers and values, formatted as key-value pairs. The input for the body parameters can contain a statement, from which you want the model to extract the expected fields used when training the model. For example, if the model was trained to extract fields such as "State" and "Captital", you must supply these as keys in the API request body, as shown below:
    Copy CodeJSON{
    "input": {
    "text": "Karnataka Bengaluru Kannada Information Technology"
    },
    "metadata": {
    "key": ""
    }
   }
6. Pass the authorization bearer token, which can be generated from IDS or from the AI Hub platform.
7. Upon successful execution, the API returns the prediction result in two distinct sections: Output and Result.
    Copy CodeJSON{
    "training_config_id": "6847df52e648c6d2495ebe87",
    "training_id": "6847df52e648c6d2495ebe86",
    "test_id": "684809a1e648c6d2495ecd93",
    "tenant_id": "6225cde095f5119c54aa1234",
    "processing_time": 6.26,
    "ignored": false,
    "retrained": false,
    "input": {
    "text": "Karnataka Bengaluru Kannada Information Technology"
    },
    "output": {
    "entities": [
    {
    "entity": "State",
    "text": "Karnataka",
    "confidence": 0.99609375
    },
    {
    "entity": "Capital",
    "text": "Bengaluru",
    "confidence": 0.9501953125
    }
    ]
    },
    "result": {
    "row_0": [
    {
    "entity": "State",
    "text": "Karnataka",
    "confidence": 0.99609375,
    "probabilities": {
    "State": 0.99609375,
    "Capital": 0.0025997161865234375
    },
    "position": {
    "start": 0,
    "end": 9
    }
    },
    {
    "entity": "Capital",
    "text": "Bengaluru",
    "confidence": 0.9501953125,
    "probabilities": {
    "State": 0.039703369140625,
    "Capital": 0.9501953125
    },
    "position": {
    "start": 10,
    "end": 19
    }
    },
    {
    "summary": [
    {
    "entity": "State",
    "total_text": 1,
    "avg_confidence": 0.9961
    },
    {
    "entity": "Capital",
    "total_text": 1,
    "avg_confidence": 0.9502
    }
    ]
    }
    ]
    },
    "created_by": "S****i N",
    "status": "Completed",
    "deleted": false,
    "test_type": "Single",
    "data_type": "Text",
    "model_type": "Extraction",
    "deployment_id": "6847ed13e648c6d2495ec205",
    "merged": false,
    "manual_review_flag": false,
    "inference_time": 6.26,
    "review_status": "Pending",
    "metadata": {
    "key": ""
    },
    "_id": "684809a7e648c6d2495ecd9d",
    "created_at": "2025-06-10T10:32:07.947Z",
    "updated_at": "2025-06-10T10:32:07.947Z",
    "id": "684809a7e648c6d2495ecd9d"
   }
  - The Output section presents the extracted data in a structured format, typically organized under labeled fields such as entity, text, and confidence, within a nested dictionary. Each entry in the dictionary corresponds to an extracted category along with its associated confidence score. This structured format facilitates seamless integration with higher-level service layers or applications for further processing.
  - The Result section displays the raw output of the extraction, representing the unprocessed response returned directly by the model.

### Batch Input Validation

Unlike single input validation, batch input validation involves multiple endpoints that must be triggered to obtain the final output. Follow the steps below to validate batch inputs:

1. Navigate to prediction using the left navigation panel.
    ![ai-hub-extraction-text-integration-batch-models](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-batch-models.png)
2. Open the desired model from the list of available extraction models.
    ![ai-hub-extraction-text-integration-select-model](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-select-model1.png)
3. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-extraction-text-integration-click](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-click1.png)
4. To trigger a batch test, multiple endpoints must be called. Use the following endpoints
  1. **Create Batch Test**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/create/batch"
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
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Extraction",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "is_file": true,
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "metadata": {
      "key": "value"
      },
      "_id": "68481200e648c6d2495ed0f7",
      "created_at": "2025-06-10T11:07:44.634Z",
      "updated_at": "2025-06-10T11:07:44.634Z",
      "id": "68481200e648c6d2495ed0f7"
     }
    - **callback_url**: Accepts the webpage URL where the result will be sent.
    - **is_file**: Accepts a boolean value: true or false.
      - If set to true, you must pass the file as a parameter when triggering the API.
      - If set to false, you must pass the file_id, which can be generated using a generic API endpoint.
    - **metadata**: Accepts key-value pairs of any metadata that needs to be passed as parameters when triggering the API.
  2. **Upload Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/upload/batch/{id}"
      To use this API endpoint, provide the _id obtained from the Create Batch endpoint in the URL. Additionally, you must either give the file_id generated via the generic file upload API or upload a file in the required format, which can be downloaded from the platform. In this example, we demonstrate the file upload option using a file downloaded in the prescribed format.
      The image below illustrates both options—uploading a file or passing the file_id as a parameter—when triggering this API endpoint in Postman for demonstration purposes.
      ![ai-hub-extraction-text-integration-file-file-id-upload-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-text-integration-file-file-id-upload-batch.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: In this API endpoint, you must choose either the file upload option or provide the file_id. Both options cannot be used simultaneously.
      The API response will be similar to the example shown below, with a status of "Created" indicating that a batch with a specific ID has been successfully created.
      Copy CodeJSON{
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "tenant_id": "6225cde095f5119c54aa1234",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Extraction",
      "file_name": "1749555612377-Batch test - Text Prediction.xls",
      "mime_type": "application/vnd.ms-excel",
      "file_url": "6225cde095f5119c54aa1234/6847df52e648c6d2495ebe87/6847df52e648c6d2495ebe86/68481200e648c6d2495ed0f7/83d43bdc-fc5a-4a5e-a7fe-6044e4e037e7/1749555612377-Batch test - Text Prediction.xls",
      "file_uuid": "83d43bdc-fc5a-4a5e-a7fe-6044e4e037e7",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "file_id": "6848199ce648c6d2495ed1ec",
      "size": 9750,
      "_id": "6848199ce648c6d2495ed1f2",
      "created_at": "2025-06-10T11:40:12.819Z",
      "updated_at": "2025-06-10T11:40:12.819Z",
      "id": "6848199ce648c6d2495ed1f2"
     }
  3. **Start Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/start/batch/{id}"
      This initiates the execution of the batch created in the previous steps. You must pass the batch ID, represented as _id returned in the response from the Create Batch API in the CURL as illustrated in the image below.
      ![ai-hub-extraction-text-batch-start-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-text-batch-start-batch.png)
     The batch size specifies the number of rows in the uploaded file that should be processed as a single batch. For example, if the file contains 100 rows and the batch size is set to 20, the data will be divided into 5 separate batches.
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: The batch size affects the results displayed in the Inference tab on the platform’s UI.
      The API should return a 201 Created response, with the status set to "PENDING" as illustrated in the image below:
      ![ai-hub-extraction-text-start-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-text-start-batch.png)
  4. **Bach Find**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/batch/find/{id}"
      Use this API to check the status of a batch test. Pass the _id returned by the Create Batch API as a parameter in the URL. The response returns the current status of the batch as it progresses through the following states:
      The time taken for the status to transition from "PENDING" to "COMPLETED" / "FAILED" depends on the size of the sample provided to the model for extraction. The response from this API endpoint will be similar to the example shown below:
      Copy CodeJSON{
      "_id": "6848fb1be648c6d2495ede94",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Extraction",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "is_file": true,
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-11T03:42:19.884Z",
      "updated_at": "2025-06-11T03:43:49.357Z",
      "metrics": {
      "precision": 1,
      "recall": 0.9285714285714286,
      "f1_score": 0.9615384615384616,
      "accuracy": 0.9285714285714286,
      "average_confidence": 0.9712665264423077,
      "total_text_count": 13
      },
      "processing_time": 18.18,
      "callback_info": [
      {
      "error": "Error during API request to : Request error: Request URL is missing an 'http://' or 'https://' protocol. for URL: "
      }
      ],
      "id": "6848fb1be648c6d2495ede94"
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      The callback_info error appears in the result when the batch is created without specifying a callback_url, or if the provided URL is invalid.
      Additionally, this API provides prediction metrics such as Precision, Recall, F1 Score, and Confidence, which are reflected in the platform’s UI.
    - **PENDING**: when the batch is first triggered via the Start Batch API.
    - **IN_PROGRESS**: when the batch processing begins.
    - **COMPLETED**: once processing is finished.
    - **FAILED**: batch processing encountered an error.
  5. **Batch Data**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/batch/data/{id}"
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
      "_id": "6848fb39e648c6d2495edeac",
      "test_type": "Batch",
      "data_type": "Text",
      "file_name": "1749613369203-Batch test - Text Prediction.xls",
      "mime_type": "application/vnd.ms-excel",
      "file_url": "6225cde095f5119c54aa1234/6847df52e648c6d2495ebe87/6847df52e648c6d2495ebe86/6848fb1be648c6d2495ede94/403354b4-a1ef-4449-9da7-b2425bc338d6/1749613369203-Batch test - Text Prediction.xls",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "6848fb1be648c6d2495ede94",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "file_id": "6848fb39e648c6d2495edea6",
      "created_at": "2025-06-11T03:42:49.614Z",
      "updated_at": "2025-06-11T03:43:49.151Z",
      "r_count": 7
      }
      ],
      "count": 1
     }
      The result of the execution is indicated by the status changing to "COMPLETED". To view the batch results, copy the ID represented by _id and use it in the API endpoint described in the next step.
    - **page_number**: Set the starting page number to display the output.
    - **page_size**: Define the number of results per page.
    - **sort**: Determines the order in which the results are displayed.
  6. **Batch Information**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/batch/find/{id}"
      This API endpoint returns the status of the previously triggered batch test. The response structure is similar to the example shown below:
     Copy CodeJSON{
      "_id": "6848fb1be648c6d2495ede94",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "test_type": "Batch",
      "data_type": "Text",
      "model_type": "Extraction",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "is_file": true,
      "deployment_unit_id": "6809efef56652d55eccf07dd",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-11T03:42:19.884Z",
      "updated_at": "2025-06-11T03:43:49.357Z",
      "metrics": {
      "precision": 1,
      "recall": 0.9285714285714286,
      "f1_score": 0.9615384615384616,
      "accuracy": 0.9285714285714286,
      "average_confidence": 0.9712665264423077,
      "total_text_count": 13
      },
      "processing_time": 18.18,
      "callback_info": [
      {
      "error": "Error during API request to : Request error: Request URL is missing an 'http://' or 'https://' protocol. for URL: "
      }
      ],
      "id": "6848fb1be648c6d2495ede94"
     }
  7. **Results Find All**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/extraction/results/find-all"
      This API returns the results of the batch test. To retrieve the results, include the _id (returned from the Batch Data API in the previous step) in the request body under the parameter "test_id" as shown below:
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      },
      "test_id": "6848199ce648c6d2495ed1f2",
      "merged": false
     }
      Upon successful execution, the API returns the prediction result in two distinct sections: Output and Result.
      Copy CodeJSON{
      "count": 7,
      "data": [
      {
      "_id": "68481b47e648c6d2495ed300",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Kerala"
      ],
      "Capital": [
      "Thiruvananthapuram"
      ]
      }
      ],
      "input": {
      "text": "Kerala Thiruvananthapuram Malayalam Tourism and Spices"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.062Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Kerala",
      "confidence": 0.98388671875
      },
      {
      "entity": "Capital",
      "text": "Thiruvananthapuram",
      "confidence": 0.94970703125
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Kerala",
      "confidence": 0.98388671875,
      "probabilities": {
      "State": 0.98388671875,
      "Capital": 0.01200103759765625
      },
      "position": {
      "start": 0,
      "end": 6
      }
      },
      {
      "entity": "Capital",
      "text": "Thiruvananthapuram",
      "confidence": 0.94970703125,
      "probabilities": {
      "State": 0.024505615234375,
      "Capital": 0.94970703125
      },
      "position": {
      "start": 7,
      "end": 25
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9839
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.9497
      },
      {
      "item_id": "68481b47e648c6d2495ed300",
      "inference_time": 6.81,
      "row": "row_1"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed305",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Chhattisgarh"
      ],
      "Capital": [
      "Raipur"
      ]
      }
      ],
      "input": {
      "text": "Chhattisgarh Raipur Hindi Steel Production"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.064Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Chhattisgarh",
      "confidence": 0.99267578125
      },
      {
      "entity": "Capital",
      "text": "Raipur",
      "confidence": 0.974609375
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Chhattisgarh",
      "confidence": 0.99267578125,
      "probabilities": {
      "State": 0.99267578125,
      "Capital": 0.005100250244140625
      },
      "position": {
      "start": 0,
      "end": 12
      }
      },
      {
      "entity": "Capital",
      "text": "Raipur",
      "confidence": 0.974609375,
      "probabilities": {
      "State": 0.0142974853515625,
      "Capital": 0.974609375
      },
      "position": {
      "start": 13,
      "end": 19
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9927
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.9746
      },
      {
      "item_id": "68481b47e648c6d2495ed305",
      "inference_time": 6.81,
      "row": "row_6"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed2ff",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Gujarat"
      ],
      "Capital": [
      "Gandhinagar"
      ]
      }
      ],
      "input": {
      "text": "Gujarat Gandhinagar Gujarati Diamond and Textile"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.062Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Gujarat",
      "confidence": 0.9921875
      },
      {
      "entity": "Capital",
      "text": "Gandhinagar",
      "confidence": 0.9501953125
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Gujarat",
      "confidence": 0.9921875,
      "probabilities": {
      "State": 0.9921875,
      "Capital": 0.00469970703125
      },
      "position": {
      "start": 0,
      "end": 7
      }
      },
      {
      "entity": "Capital",
      "text": "Gandhinagar",
      "confidence": 0.9501953125,
      "probabilities": {
      "State": 0.0287017822265625,
      "Capital": 0.9501953125
      },
      "position": {
      "start": 8,
      "end": 19
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9922
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.9502
      },
      {
      "item_id": "68481b47e648c6d2495ed2ff",
      "inference_time": 6.81,
      "row": "row_0"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed304",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Rajasthan"
      ],
      "Capital": [
      "Jaipur"
      ]
      }
      ],
      "input": {
      "text": "Rajasthan Jaipur Hindi Tourism and Handicrafts"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.064Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Rajasthan",
      "confidence": 0.98583984375
      },
      {
      "entity": "Capital",
      "text": "Jaipur",
      "confidence": 0.94140625
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Rajasthan",
      "confidence": 0.98583984375,
      "probabilities": {
      "State": 0.98583984375,
      "Capital": 0.0110015869140625
      },
      "position": {
      "start": 0,
      "end": 9
      }
      },
      {
      "entity": "Capital",
      "text": "Jaipur",
      "confidence": 0.94140625,
      "probabilities": {
      "State": 0.01450347900390625,
      "Capital": 0.94140625
      },
      "position": {
      "start": 10,
      "end": 16
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9858
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.9414
      },
      {
      "item_id": "68481b47e648c6d2495ed304",
      "inference_time": 6.81,
      "row": "row_5"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed301",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Jharkhand"
      ],
      "Capital": [
      "Ranchi"
      ]
      }
      ],
      "input": {
      "text": "Jharkhand Ranchi Hindi Mining"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.062Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Jharkhand",
      "confidence": 0.9951171875
      },
      {
      "entity": "Capital",
      "text": "Ranchi",
      "confidence": 0.9814453125
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Jharkhand",
      "confidence": 0.9951171875,
      "probabilities": {
      "State": 0.9951171875,
      "Capital": 0.0027008056640625
      },
      "position": {
      "start": 0,
      "end": 9
      }
      },
      {
      "entity": "Capital",
      "text": "Ranchi",
      "confidence": 0.9814453125,
      "probabilities": {
      "State": 0.01409912109375,
      "Capital": 0.9814453125
      },
      "position": {
      "start": 10,
      "end": 16
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9951
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.9814
      },
      {
      "item_id": "68481b47e648c6d2495ed301",
      "inference_time": 6.81,
      "row": "row_2"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed302",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Mizoram"
      ],
      "Capital": [
      "Aizawl"
      ]
      }
      ],
      "input": {
      "text": "Mizoram Aizawl Mizo Bamboo and Handicrafts"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.062Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Mizoram",
      "confidence": 0.990234375
      },
      {
      "entity": "Capital",
      "text": "Aizawl",
      "confidence": 0.958984375
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Mizoram",
      "confidence": 0.990234375,
      "probabilities": {
      "State": 0.990234375,
      "Capital": 0.004001617431640625
      },
      "position": {
      "start": 0,
      "end": 7
      }
      },
      {
      "entity": "Capital",
      "text": "Aizawl",
      "confidence": 0.958984375,
      "probabilities": {
      "State": 0.00930023193359375,
      "Capital": 0.958984375
      },
      "position": {
      "start": 8,
      "end": 14
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9902
      },
      {
      "entity": "Capital",
      "total_text": 1,
      "avg_confidence": 0.959
      },
      {
      "item_id": "68481b47e648c6d2495ed302",
      "inference_time": 6.81,
      "row": "row_3"
      }
      ]
      }
      ]
      },
      {
      "_id": "68481b47e648c6d2495ed303",
      "training_config_id": "6847df52e648c6d2495ebe87",
      "training_id": "6847df52e648c6d2495ebe86",
      "test_id": "6848199ce648c6d2495ed1f2",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "ground_truth": [
      {
      "State": [
      "Assam"
      ],
      "Capital": [
      "Dispur"
      ]
      }
      ],
      "input": {
      "text": "Assam Dispur Assamese Tea Industry"
      },
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Text",
      "batch_id": "68481200e648c6d2495ed0f7",
      "deployment_id": "6847ed13e648c6d2495ec205",
      "merged": false,
      "manual_review_flag": false,
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-10T11:47:19.064Z",
      "updated_at": "2025-06-10T11:47:27.723Z",
      "model_type": "Extraction",
      "inference_time": 6.81,
      "output": {
      "entities": [
      {
      "entity": "State",
      "text": "Assam",
      "confidence": 0.93017578125
      }
      ]
      },
      "processing_time": 7.04,
      "result": [
      {
      "entity": "State",
      "text": "Assam",
      "confidence": 0.93017578125,
      "probabilities": {
      "State": 0.93017578125,
      "Capital": 0.0570068359375
      },
      "position": {
      "start": 0,
      "end": 5
      }
      },
      {
      "summary": [
      {
      "entity": "State",
      "total_text": 1,
      "avg_confidence": 0.9302
      },
      {
      "item_id": "68481b47e648c6d2495ed303",
      "inference_time": 6.81,
      "row": "row_4"
      }
      ]
      }
      ]
      }
      ]
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: To retrieve the result of a specific output ID, copy the desired ID and pass it to the following API endpoint: "../extraction/results/find-one/{id}" Use the output ID for a specific output entity returned by the find-all API as the path parameter in this request.
    - The Output section presents the extraction results in a structured format, typically organized as a nested dictionary. Each entry includes labeled fields such as entity, text, and confidence, where the key represents the predicted category label and the value contains its corresponding confidence score. This structured format enables seamless integration with higher-level service layers or downstream applications for further processing.
    - The Result section contains the raw output of the extraction, providing the unprocessed response returned by the model.
