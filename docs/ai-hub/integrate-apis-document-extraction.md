# Single Input Document Validation

<https://documentation.neutrinos.com/articles/#!ai-hub/integrate-apis-document-extraction>

The document extraction APIs enable you to leverage the platform’s extraction capabilities beyond the user interface, maximizing the utility of the service programmatically. They support both single and batch extractions, making it possible to process individual document inputs or entire datasets containing multiple inputs efficiently.

### Single Input Document Validation

To integrate single input validation API follow the steps below:

1. Navigate to extraction using the left navigation panel.
    ![ai-hub-extraction-document-open-model](/resources/Storage/ai-hub/images/ai-hub-extraction-document-open-model.png)
2. Click the document tab on the extraction page.
    ![ai-hub-extraction-document-tab-open](/resources/Storage/ai-hub/images/ai-hub-extraction-document-tab-open.png)
3. Open the desired model from the list of available extraction models.
    ![ai-hub-extraction-document-select-model](/resources/Storage/ai-hub/images/ai-hub-extraction-document-select-model.png)
4. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-extraction-document-integration-select](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-select.png)
5. Select the appropriate model version, deployed environment, and the Start Single Test API option from the Version, Environment, and API drop-downs, respectively as shown in the image below:
    ![ai-hub-extraction-document-integration-version-env-api](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-version-env-api.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: To use the APIs, the model must be deployed in either the production or sandbox environment. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
6. Copy the CURL from the right panel.
    ![ai-hub-extraction-document-integration-start-single](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-start-single.png)
7. Paste the copied CURL command into any compatible API testing tool. Upload the document either directly from your local machine or by using the file_id.
  - **Upload File**: In this API endpoint, ensure that only the file field is selected in the request body; uncheck the file_id field. Upload an image from your local machine to initiate the prediction process as shown in the image below. Note: For illustration purposes, we have used Postman as the API testing tool. However, you may use any compatible tool based on your preference.
      ![ai-hub-extraction-document-integration-file-upload](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-file-upload.png)
  - **Generate file_id**: To generate the file_id required for this API endpoint, use the generic file upload endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/file/upload". Upload the file using the file parameter in the request body. The response will contain an _id field, which represents the file_id.
      Copy CodeJSON{
      "file_name": "invoice_1.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/4f05e6eb-bc8c-49e0-9a4a-6ae1e7d9ea2c/invoice_1.jpg",
      "size": 300363,
      "page_count": 1,
      "file_uuid": "4f05e6eb-bc8c-49e0-9a4a-6ae1e7d9ea2c",
      "created_by": "S****i N",
      "deleted": false,
      "tenant_id": "6225cde095f5119c54aa1234",
      "_id": "684926ff1987a52681fc7451",
      "input_urls": [],
      "created_at": "2025-06-11T06:49:35.184Z",
      "updated_at": "2025-06-11T06:49:35.184Z",
      "id": "684926ff1987a52681fc7451"
     }
      This _id should then be passed as a parameter in the body of the Start Single Test API as illustrated in the image below:
      ![ai-hub-extraction-document-integration-file-id-generic-api](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-file-id-generic-api.png)
8. Pass the authorization bearer token, which can be generated from IDS or from the AI Hub platform.
9. Upon successful execution, the API returns the extraction result in two distinct sections: Output and Result.
    Copy CodeJSON[
    {
    "training_config_id": "6825986529a827e353d3631a",
    "training_id": "6825986529a827e353d36319",
    "test_id": "6847c705e648c6d2495eb905",
    "tenant_id": "6225cde095f5119c54aa1234",
    "processing_time": 2.8,
    "ignored": false,
    "retrained": false,
    "output": [
    {
    "section_name": "AdaDocSnap",
    "entities": [
    {
    "bbox": [
    1224.3875732421875,
    644.1024169921875,
    1944.2435302734375,
    925.9374389648438
    ],
    "confidence": 0.9994310736656189,
    "name": "ClData",
    "value": "cropped_images/58de498b-d96d-4ac1-883e-5551456fd65a__image__AdaDocSnap.ClData.jpg"
    }
    ]
    },
    {
    "section_name": "Section 1",
    "entities": [
    {
    "bbox": [
    2140.717041015625,
    1930.475830078125,
    2252.34130859375,
    1959.716552734375
    ],
    "confidence": 0.9898132681846619,
    "name": "Gross Worth",
    "value": "$ 8.25"
    },
    {
    "bbox": [
    529.1290283203125,
    116.12836456298828,
    799.7160034179688,
    153.08544921875
    ],
    "confidence": 0.9995067119598389,
    "name": "Invoice No",
    "value": "40378170"
    }
    ]
    }
    ],
    "result": [
    {
    "/mnt/data/6225cde095f5119c54aa1234/6ad6be5b-5f11-4729-b9e8-dc01c4825c28/invoice_1.png": {
    "Section_1.Invoice_No": {
    "bbox": [
    529.1290283203125,
    116.12836456298828,
    799.7160034179688,
    153.08544921875
    ],
    "confidence": 0.9995067119598389,
    "field_count": 1,
    "value": "40378170"
    },
    "AdaDocSnap.ClData": {
    "bbox": [
    1224.3875732421875,
    644.1024169921875,
    1944.2435302734375,
    925.9374389648438
    ],
    "confidence": 0.9994310736656189,
    "field_count": 1,
    "value": "cropped_images/58de498b-d96d-4ac1-883e-5551456fd65a__image__AdaDocSnap.ClData.jpg"
    },
    "Section_1.Gross_Worth": {
    "bbox": [
    2140.717041015625,
    1930.475830078125,
    2252.34130859375,
    1959.716552734375
    ],
    "confidence": 0.9898132681846619,
    "field_count": 1,
    "value": "$ 8.25"
    }
    }
    },
    {
    "bboxes_info": {
    "/mnt/data/6225cde095f5119c54aa1234/6ad6be5b-5f11-4729-b9e8-dc01c4825c28/invoice_1.png": {
    "Section_1.Invoice_No": {
    "bbox": [
    529.1290283203125,
    116.12836456298828,
    799.7160034179688,
    153.08544921875
    ],
    "confidence": 0.9995067119598389
    },
    "AdaDocSnap.ClData": {
    "bbox": [
    1224.3875732421875,
    644.1024169921875,
    1944.2435302734375,
    925.9374389648438
    ],
    "confidence": 0.9994310736656189
    },
    "Section_1.Gross_Worth": {
    "bbox": [
    2140.717041015625,
    1930.475830078125,
    2252.34130859375,
    1959.716552734375
    ],
    "confidence": 0.9898132681846619
    }
    }
    },
    "cropped_images_info": {
    "entity_cropped_combined_image_path": [
    "cropped_images/5ec3241b-701f-4d92-bd25-df4e11ae075b__combined.jpg"
    ],
    "entity_table_cropped_path": [],
    "entity_image_cropped_path": [
    "cropped_images/58de498b-d96d-4ac1-883e-5551456fd65a__image__AdaDocSnap.ClData.jpg"
    ],
    "field_counts": {
    "AdaDocSnap.ClData": 1
    }
    },
    "extracted_ocr_entites": {
    "Section_1.Invoice_No": "40378170",
    "Section_1.Gross_Worth": "$ 8.25",
    "AdaDocSnap.ClData": "cropped_images/58de498b-d96d-4ac1-883e-5551456fd65a__image__AdaDocSnap.ClData.jpg"
    }
    }
    ],
    "created_by": "S****i N",
    "status": "Completed",
    "deleted": false,
    "test_type": "Single",
    "data_type": "Document",
    "model_type": "Extraction",
    "file_name": "invoice_1.png",
    "mime_type": "image/png",
    "file_url": "6225cde095f5119c54aa1234/6ad6be5b-5f11-4729-b9e8-dc01c4825c28/invoice_1.png",
    "size": 944418,
    "deployment_id": "6825d33d29a827e353d392a7",
    "merged": false,
    "manual_review_flag": false,
    "inference_time": 2.8,
    "review_status": "Pending",
    "_id": "6847c709e648c6d2495eb90f",
    "created_at": "2025-06-10T05:47:53.577Z",
    "updated_at": "2025-06-10T05:47:53.577Z",
    "id": "6847c709e648c6d2495eb90f"
    }
   ]
  - The Output section presents the extraction in a structured format, typically under labeled fields such as confidence, name, and value, organized within a nested dictionary. Each entry in the dictionary represents an extracted category label and its corresponding confidence score. This structured format allows the extraction results to be easily consumed by upper service layers or applications for further processing.
  - The Result section contains the raw output of the extraction, providing the unprocessed response returned by the model.

### Batch Input Document Validation

Unlike single input validation, batch input validation involves multiple endpoints that must be triggered to obtain the final output. Follow the steps below to validate batch inputs:

1. Navigate to extraction using the left navigation panel.
    ![ai-hub-extraction-document-open-model](/resources/Storage/ai-hub/images/ai-hub-extraction-document-open-model.png)
2. Click the document tab on the extraction page.
    ![ai-hub-extraction-document-tab-open](/resources/Storage/ai-hub/images/ai-hub-extraction-document-tab-open.png)
3. Open the desired model from the list of available extraction models.
    ![ai-hub-extraction-document-select-model](/resources/Storage/ai-hub/images/ai-hub-extraction-document-select-model.png)
4. On the model page, click on Integration from the left navigation panel to open the Integrations page.
    ![ai-hub-extraction-document-integration-select](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-select.png)
5. To trigger a batch test, multiple endpoints must be called. Use the following endpoints:
  1. **Create Batch Test**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/create/batch"
      The first step is to create a batch for testing. Use the following API endpoint to initiate the batch.
      Copy CodeJSON{
      "callback_url": "",
      "metadata": {
      "key": "value"
      }
     }
      The response includes a batch ID, represented by _id, which must be used in the next step to upload the batch file.
      Copy CodeJSON{
      "training_config_id": "6825986529a827e353d3631a",
      "training_id": "6825986529a827e353d36319",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "6825d33d29a827e353d392a7",
      "test_type": "Batch",
      "data_type": "Document",
      "model_type": "Extraction",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "is_file": true,
      "metadata": {
      "key": "value"
      },
      "_id": "68492b341987a52681fc79b0",
      "created_at": "2025-06-11T07:07:32.579Z",
      "updated_at": "2025-06-11T07:07:32.579Z",
      "id": "68492b341987a52681fc79b0"
     }
    - **callback_url**: Accepts the webpage URL where the result will be sent.
    - **is_file**: Accepts a boolean value: true or false.
      - If set to true, you must pass the file as a parameter when triggering the API.
      - If set to false, you must pass the file_id, which can be generated using a generic API endpoint.
    - **metadata**: Accepts key-value pairs of any metadata that needs to be passed as parameters when triggering the API.
  2. **Upload Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/upload/batch/{id}"
      To use this API endpoint, provide the _id obtained from the Create Batch endpoint in the URL. Additionally, you must either give the file_id generated via the generic file upload API or upload a file. In this example, we demonstrate the file upload option.
      The image below illustrates both options—uploading a file or passing the file_id as a parameter—when triggering this API endpoint in Postman for demonstration purposes.
      ![ai-hub-extraction-document-integration-file-upload-methods](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-file-upload-methods.png)
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: In this API endpoint, you must choose either the file upload option or provide the file_id. Both options cannot be used simultaneously.
      The API response will be similar to the example shown below, with a status of "Created" indicating that a batch with a specific ID has been successfully created.
      Copy CodeJSON{
      "training_config_id": "6825986529a827e353d3631a",
      "training_id": "6825986529a827e353d36319",
      "tenant_id": "6225cde095f5119c54aa1234",
      "test_type": "Batch",
      "data_type": "Document",
      "model_type": "Extraction",
      "file_name": "1749626955657-invoice_1.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/68492b341987a52681fc79b0/ab7d387c-26f8-4319-b16f-e77c0e7489d2/1749626955657-invoice_1.jpg",
      "file_uuid": "ab7d387c-26f8-4319-b16f-e77c0e7489d2",
      "created_by": "S****i N",
      "status": "Created",
      "deleted": false,
      "batch_id": "68492b341987a52681fc79b0",
      "deployment_id": "6825d33d29a827e353d392a7",
      "file_id": "6849304b1987a52681fc7c88",
      "page_count": 1,
      "size": 300363,
      "_id": "6849304c1987a52681fc7c8e",
      "created_at": "2025-06-11T07:29:16.025Z",
      "updated_at": "2025-06-11T07:29:16.025Z",
      "id": "6849304c1987a52681fc7c8e"
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: The response sample above represents a single document upload to the batch. To upload multiple files to the same batch, repeat this step N times—once for each file.
  3. **Start Batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/start/batch/{id}"
      This initiates the execution of the batch created in the previous steps. You must pass the batch ID, represented as _id returned in the response from the Create Batch API in the CURL as illustrated in the image below.
      ![ai-hub-extraction-document-batch-start-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-document-batch-start-batch.png)
      The batch size defines the number of documents to be processed together as a single batch within the uploaded set.
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: The batch size affects the results displayed in the Inference tab on the platform’s UI.
      The API should return a 201 Created response, with the status set to "PENDING" as illustrated in the image below:
      ![ai-hub-extraction-document-integration-start-batch](/resources/Storage/ai-hub/images/ai-hub-extraction-document-integration-start-batch.png)
  4. **Batch Find**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/batch/find/{id}"
      Use this API to check the status of a batch test. Pass the _id returned by the Create Batch API as a path parameter. The response returns the current status of the batch as it progresses through the following states:
      The time taken for the status to transition from "PENDING" to "COMPLETED" / "FAILED" depends on the size of the sample provided to the model for extraction. The response from this API endpoint will be similar to the example shown below:
      Copy CodeJSON{
      "_id": "684950c61987a52681fc9532",
      "training_config_id": "6825986529a827e353d3631a",
      "training_id": "6825986529a827e353d36319",
      "tenant_id": "6225cde095f5119c54aa1234",
      "deployment_id": "6825d33d29a827e353d392a7",
      "test_type": "Batch",
      "data_type": "Document",
      "model_type": "Extraction",
      "callback_url": "",
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "is_file": true,
      "metadata": {
      "key": "value"
      },
      "created_at": "2025-06-11T09:47:50.231Z",
      "updated_at": "2025-06-11T09:49:47.865Z",
      "updated_by": "Swathi N",
      "processing_time": 41.22,
      "callback_info": [
      {
      "error": "Error during API request to : Request error: Request URL is missing an 'http://' or 'https://' protocol. for URL: "
      }
      ],
      "id": "684950c61987a52681fc9532"
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      The callback_info error appears in the result when the batch is created without specifying a callback_url, or if the provided URL is invalid.
    - **PENDING**: when the batch is first triggered via the Start Batch API.
    - **IN_PROGRESS**: when the batch processing begins.
    - **COMPLETED**: once processing is finished.
    - **FAILED**: batch processing encountered an error.
  5. **Batch Data**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/batch/data/{id}"
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
      "_id": "684950eb1987a52681fc9561",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749635307050-invoice_1.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/684950c61987a52681fc9532/0c7b6eeb-7e5e-48a1-8c92-2310a6608835/1749635307050-invoice_1.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "684950c61987a52681fc9532",
      "deployment_id": "6825d33d29a827e353d392a7",
      "file_id": "684950eb1987a52681fc955b",
      "created_at": "2025-06-11T09:48:27.427Z",
      "updated_at": "2025-06-11T09:49:47.661Z",
      "r_count": 1
      },
      {
      "_id": "684950f41987a52681fc957b",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749635316473-invoice_2.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/684950c61987a52681fc9532/96fe9538-e6f8-48da-aae4-a01deac0b940/1749635316473-invoice_2.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "684950c61987a52681fc9532",
      "deployment_id": "6825d33d29a827e353d392a7",
      "file_id": "684950f41987a52681fc9575",
      "created_at": "2025-06-11T09:48:36.844Z",
      "updated_at": "2025-06-11T09:49:47.661Z",
      "r_count": 1
      },
      {
      "_id": "684950fe1987a52681fc95a4",
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749635326340-invoice_3.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/684950c61987a52681fc9532/da401748-ce4f-48bc-91e6-d23ca1ae6219/1749635326340-invoice_3.jpg",
      "created_by": "S****i N",
      "status": "Completed",
      "batch_id": "684950c61987a52681fc9532",
      "deployment_id": "6825d33d29a827e353d392a7",
      "file_id": "684950fe1987a52681fc959e",
      "created_at": "2025-06-11T09:48:46.711Z",
      "updated_at": "2025-06-11T09:49:47.661Z",
      "r_count": 1
      }
      ],
      "count": 3
     }
      This API endpoint returns the prediction results status for the entire batch, including the outcomes for each document within the batch. Each document in the batch is associated with a unique id, represented as _id in the response. This id can be used to retrieve the prediction details of an individual document.
    - **page_number**: Set the starting page number to display the output.
    - **page_size**: Define the number of results per page.
    - **sort**: Determines the order in which the results are displayed.
  6. **List batch data**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/document/ner/results/find-all"
      This endpoint returns the prediction result of an individual document from the batch. It accepts the id of the specific document—generated by the Batch Data endpoint—as a body parameter, and returns the corresponding prediction result:
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      },
      "test_id": "684950fe1987a52681fc95a4",
      "merged": false
     }
      The response returned by this call is as illustrated below:
      Copy CodeJSON{
      "count": 1,
      "data": [
      {
      "_id": "6849510c1987a52681fc95e9",
      "training_config_id": "6825986529a827e353d3631a",
      "training_id": "6825986529a827e353d36319",
      "test_id": "684950fe1987a52681fc95a4",
      "tenant_id": "6225cde095f5119c54aa1234",
      "ignored": false,
      "retrained": false,
      "created_by": "S****i N",
      "status": "Completed",
      "deleted": false,
      "test_type": "Batch",
      "data_type": "Document",
      "file_name": "1749635326340-invoice_3.jpg",
      "mime_type": "image/jpeg",
      "file_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/6133580c-5813-4644-9163-737ddaf36cab/predicted_1749635326340-invoice_3.jpg",
      "size": 686734,
      "page_number": 1,
      "batch_id": "684950c61987a52681fc9532",
      "deployment_id": "6825d33d29a827e353d392a7",
      "merged": false,
      "manual_review_flag": false,
      "thumbnail_url": "6225cde095f5119c54aa1234/6825986529a827e353d3631a/6825986529a827e353d36319/684950c61987a52681fc9532/bb18045d-33b1-479c-ba83-8144db37b0c0/thumbnails/1749635326340-invoice_3_thumb.jpg",
      "review_status": "Pending",
      "metadata": {
      "key": "value"
      },
      "thumbnail_size": 4173,
      "created_at": "2025-06-11T09:49:00.957Z",
      "updated_at": "2025-06-11T09:49:36.634Z",
      "model_type": "Extraction",
      "output": [
      {
      "section_name": "AdaDocSnap",
      "entities": [
      {
      "bbox": [
      1205.8868408203125,
      633.4660034179688,
      1885.874755859375,
      919.7622680664062
      ],
      "confidence": 0.9996820688247681,
      "name": "ClData",
      "value": "cropped_images/5b5ecb36-5749-433f-a421-432c804c8219__image__AdaDocSnap.ClData.jpg"
      }
      ]
      },
      {
      "section_name": "Section 1",
      "entities": [
      {
      "bbox": [
      2163.453857421875,
      2145.58935546875,
      2250.88330078125,
      2171.292236328125
      ],
      "confidence": 0.9636932015419006,
      "name": "Gross Worth",
      "value": "96.73"
      },
      {
      "bbox": [
      528.9864501953125,
      116.1617202758789,
      799.179443359375,
      153.1668701171875
      ],
      "confidence": 0.9992390871047974,
      "name": "Invoice No",
      "value": "49565075"
      }
      ]
      }
      ],
      "processing_time": 28.694562435150146,
      "result": {
      "AdaDocSnap.ClData": {
      "bbox": [
      1205.8868408203125,
      633.4660034179688,
      1885.874755859375,
      919.7622680664062
      ],
      "confidence": 0.9996820688247681,
      "field_count": 1,
      "value": "cropped_images/5b5ecb36-5749-433f-a421-432c804c8219__image__AdaDocSnap.ClData.jpg"
      },
      "Section_1.Invoice_No": {
      "bbox": [
      528.9864501953125,
      116.1617202758789,
      799.179443359375,
      153.1668701171875
      ],
      "confidence": 0.9992390871047974,
      "field_count": 1,
      "value": "49565075"
      },
      "Section_1.Gross_Worth": {
      "bbox": [
      2163.453857421875,
      2145.58935546875,
      2250.88330078125,
      2171.292236328125
      ],
      "confidence": 0.9636932015419006,
      "field_count": 1,
      "value": "96.73"
      }
      }
      }
      ]
     }
    - The Output section presents the extraction results in a structured format, typically organized as a nested dictionary. Each entry includes labeled fields such as:
      - **bbox**: The bounding box coordinates indicating where the entity was found on the document.
      - **confidence**: The confidence score of the extraction.
      - **name**: The extracted category label.
      - **value**: The extracted value associated with the label
    - The Result section contains the raw output of the extraction, providing the unprocessed response returned by the model.
