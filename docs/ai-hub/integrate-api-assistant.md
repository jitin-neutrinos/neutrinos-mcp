# Sync APIs

<https://documentation.neutrinos.com/articles/#!ai-hub/integrate-api-assistant>

The Assistant APIs allow you to integrate assistant or chatbot capabilities beyond the platform's user interface, enabling you to extend functionality and access services programmatically.

The APIs for assistant is broadly classified into 2 categories as listed below:

1. Sync APIs
2. Async APIs

### Sync APIs

Follow the steps to integrate the Sync APIs:

1. From the left side navigation pane, click Assistant to open the Assistant page.
    ![ai-hub-assistant-integration-landing-page](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-landing-page.png)
2. Select the desired Assistant model from the list of available models.
    ![ai-hub-assistant-integration-select-assistant](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-select-assistant.png)
3. On the Assistant Models page, click Integrations in the left navigation panel to access the list of available APIs.
    ![ai-hub-assistant-integration-page](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-page.png)
4. Select the appropriate assistant model version, deployed environment, and the Create batch conversation API option from the Version, Environment, and API drop-downs, respectively as shown in the image below:
    ![ai-hub-assistant-integration-sync-select-type-env-api](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-sync-select-type-env-api.png)
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: To use the APIs, the model must be deployed in either the production or sandbox environment. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
5. Copy the CURL from the right panel:
    ![ai-hub-assistant-sync-copy-curl](/resources/Storage/ai-hub/images/ai-hub-assistant-sync-copy-curl.png)
6. Paste the copied CURL command into any compatible API testing tool. For illustration purposes we have used postman application. The Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/conversation/create"
    The first step is to create a batch for testing. Use the API endpoint to initiate the conversation.
    Copy CodeJSON{
    "metadata": {
    "key": "value"
    },
    "translation_enabled": true
   }
    When triggered, this API returns a conversation ID (represented as _id), which must be used in subsequent steps to initiate conversations. The output of the API looks similar to the one below:
    Copy CodeJSON{
    "_id": "684fa26bdb93659c22dd5122",
    "tenant_id": "6225cde095f5119c54aa1234",
    "training_config_id": "684963981987a52681fcbc11",
    "training_id": "684963981987a52681fcbc10",
    "limit_reached": false,
    "status": "Pending",
    "is_batch": false,
    "metadata": {
    "key": "value"
    },
    "translation_enabled": true
   }
  - **metadata**: If metadata needs to be included in the request body, pass the required parameters as key-value pairs.
  - **translation_enabled**: Indicates whether the initiated conversation should be translated. If set to true, the conversation results will be translated. If set to false, the results will retain the original (native) language.
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: This feature must also be enabled on the platform UI. You can enable it from the Advanced Configuration section in the platform settings for specific Assistant models. By default, this setting is disabled.
      Important: If the translation option is not enabled in the platform UI, setting translation_enabled to true in the API request will not result in translated output. However, if the translation feature is enabled in the UI, you can choose to disable it for specific API calls by setting translation_enabled to false.
7. **Create message**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/message/create"
    Trigger this API to create a message that the Assistant will respond to. The following body parameters must be included in the request:
    ![ai-hub-assistant-sync-create-message](/resources/Storage/ai-hub/images/ai-hub-assistant-sync-create-message.png)
    By default, all available options for interacting with the API are enabled. You can select multiple options when initiating a conversation with the Assistant, with the exception of file and file_id—only one of these can be used at a time. Both file and file_id cannot be enabled simultaneously.
  - **conversation_id**: This is the _id obtained from the response of the previous API call. It is a mandatory field and must be included in the request.
  - **text**: This parameter contains the user’s text input, which the Assistant will process and generate a response for.
  - **sources**: This parameter contains the IDs of the knowledge sources that were added to the Assistant through the platform UI. To add a knowledge source, follow the steps below:
    1. Use the following endpoint to retrieve all knowledge sources associated with the selected Assistant: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/knowledge/find-all".
        Copy CodeJSON{
        "page_number": 0,
        "page_size": 10,
        "sort": {
        "updated_at": -1
        }
       }
        The response includes the _id and name of each knowledge source associated with the specific Assistant model as seen below:
        Copy CodeJSON{
        "data": [
        {
        "_id": "6825cf0629a827e353d38edd",
        "name": "ICD Code 2"
        }
        ],
        "total": 1
       }
    2. Pass the _id values of the required knowledge sources—retrieved from this API—in the Create Message API request. You can provide multiple file_id values as a comma-separated array.
  - **file**: Upload a file from your local machine for the Assistant to process. The Assistant will respond based on the instructions configured during its setup on the platform.
  - **file_id**: Enter the file_id returned by the corresponding generic API.
  - **metadata**: Provide any metadata required by the assistant as a key value pair.
8. Pass the parameters mentioned above as required to receive a response from the Assistant. The output can be returned in either raw text format or JSON format. When using JSON, you must define the structure that adheres to the platform’s formatting standards. The sample JSON format is as shown below:
    Copy CodeJSON{
    "name": "boarding_pass_details",
    "description": "Extracts key details from a boarding pass including passenger name, travel date, origin, and destination.",
    "parameters": {
    "type": "object",
    "properties": {
    "BoardingPass": {
    "type": "array",
    "minItems": 1,
    "items": {
    "type": "object",
    "properties": {
    "Name": {
    "type": "string",
    "description": "Name of the passenger"
    },
    "Date": {
    "type": "string",
    "description": "Date of the flight"
    },
    "From": {
    "type": "string",
    "description": "Origin or departure airport"
    },
    "To": {
    "type": "string",
    "description": "Destination or arrival airport"
    }
    },
    "required": [
    "Name",
    "Date",
    "From",
    "To"
    ],
    "additionalProperties": false
    }
    }
    },
    "required": [
    "BoardingPass"
    ],
    "additionalProperties": false
    }
   }
    ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
    Note: The name, type, and description of the input and output fields in the sample JSON can be modified as per your requirements.
    The output of this API is similar to the example shown below. Note: The response is displayed in raw text format.
    Copy CodeJSON{
    "is_batch": false,
    "_id": "684fdf89ba7e2dcd4a8a4767",
    "conversation_id": "684fa26bdb93659c22dd5122",
    "training_config_id": "684963981987a52681fcbc11",
    "training_id": "684963981987a52681fcbc10",
    "tenant_id": "6225cde095f5119c54aa1234",
    "text": "",
    "created_at": "2025-06-16T09:10:33.892Z",
    "output": {
    "text": "Certainly! Here’s the structured extraction of the requested information from your OCR data:
   ---
   ## **Invoice Number**
   - **86268868**
   ---
   ## **Seller Information**
   - **Name:** Harrison and Sons
   - **Address:** 8716 Tiffany Crescent, Markfurt, NH 79626
   - **Tax ID:** 974-70-5786
   - **IBAN:** GB90KGZY90567874189494
   ---
   ## **Total Bill Amount (Gross Worth)**
   - **$36,946.22**
   ---
   If you need any more details or further breakdowns, please let me know!"
    },
    "status": "Completed",
    "inference_time": 6.759836196899414,
    "created_by": "S****i N",
    "translation_enabled": true,
    "metadata": {
    "key": "value"
    }
   }

### Async APIs

Unlike sync APIs, these need multiple endpoints to be triggered to complete the Assistant conversation. Follow the steps below to initiate, create, and converse with the assistant using Async APIc:

1. From the left side navigation pane, click Assistant to open the Assistant page.
    ![ai-hub-assistant-integration-landing-page](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-landing-page.png)
2. Select the desired Assistant model from the list of available models.
    ![ai-hub-assistant-integration-select-assistant](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-select-assistant.png)
3. On the Assistant Models page, click Integrations in the left navigation panel to access the list of available APIs.
    ![ai-hub-assistant-integration-page](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-page.png)
4. To trigger a batch conversation in Assistant, multiple endpoints must be called. Use the following endpoints
  1. **Create batch type conversation**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/conversation/create/batch"
      ![ai-hub-assistant-integration-asysnc-create-conversation](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-asysnc-create-conversation.png)
      The first step is to create a batch for conversation. Use the mentioned API endpoint to initiate the batch.
      Copy CodeJSON{
      "metadata": {
      "key": "value"
      },
      "callback_url": "",
      "translation_enabled": true
     }
      The response includes a batch ID, represented by _id, which must be used in the next step to upload the batch file.
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: To use the APIs, the model must be deployed in either the production or sandbox environment. Additionally, a unique token must be generated for each model that requires API access. To know more on token generation, refer the [Tokens](/articles/ai-hub/tokens) topic.
    - **metadata**: Accepts key-value pairs of any metadata that needs to be passed as parameters when triggering the API.
    - **callback_url**: Accepts the webpage URL where the result will be sent.
    - **translation_enabled**: Indicates whether the initiated conversation should be translated. If set to true, the conversation results will be translated. If set to false, the results will retain the original (native) language.
        ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
        Note: This feature must also be enabled on the platform UI. You can enable it from the Advanced Configuration section in the platform settings for specific Assistant models. By default, this setting is disabled.
        Important: If the translation option is not enabled in the platform UI, setting translation_enabled to true in the API request will not result in translated output. However, if the translation feature is enabled in the UI, you can choose to disable it for specific API calls by setting translation_enabled to false.
  2. **Add message to existing batch**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/message/upload/batch"
      Trigger this endpoint to upload a batch of messages to the Assistant. This allows multiple messages to be submitted as a single conversation, enabling the Assistant to process them collectively and return a unified response.
      Note: Although this endpoint supports processing multiple messages as a batch, each message must be uploaded individually. Once all messages are uploaded, they are treated as a single conversation batch, and the Assistant (agent) generates a collective response based on the entire set.
      ![ai-hub-assistant-integration-batch-upload-batch](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-batch-upload-batch.png)
      By default, all available options for interacting with the API are enabled. You can select multiple options when initiating a conversation with the Assistant, with the exception of file and file_id—only one of these can be used at a time. Both file and file_id cannot be enabled simultaneously.
    - **conversation_id**: This is the _id obtained from the response of the previous API call. It is a mandatory field and must be included in the request.
    - **text**: This parameter contains the user’s text input, which the Assistant will process and generate a response for.
    - **sources**: This parameter contains the IDs of the knowledge sources that were added to the Assistant through the platform UI. To add a knowledge source, follow the steps below:
      1. Use the following endpoint to retrieve all knowledge sources associated with the selected Assistant:
          "https://aihub-staging.neutrinos.com/inferenceservice/assistant/knowledge/find-all".
          Copy CodeJSON{
          "page_number": 0,
          "page_size": 10,
          "sort": {
          "updated_at": -1
          }
         }
          The response includes the _id and name of each knowledge source associated with the specific Assistant model as seen below:
          Copy CodeJSON{
          "data": [
          {
          "_id": "6825cf0629a827e353d38edd",
          "name": "ICD Code 2"
          }
          ],
          "total": 1
         }
      2. Pass the _id values of the required knowledge sources—retrieved from this API—in the Create Message API request. You can provide multiple file_id values as a comma-separated array.
    - **file**: Upload a file from your local machine for the Assistant to process. The Assistant will respond based on the instructions configured during its setup on the platform.
    - **file_id**: Enter the file_id returned by the corresponding generic API.
    - **metadata**: Provide any metadata required by the assistant as a key-value pair.
  3. **Start batch type conversation**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/conversation/batch/start/{id}"
      Provide the batch ID (represented as _id, retrieved from the Create batch type conversation API) as a URL parameter to trigger the execution of this API as illustrated in the image below:
      ![ai-hub-assistant-integration-async-start-batch](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-async-start-batch.png)
      The response of the API is similar to the example shown below:
      Copy CodeJSON{
      "message": "Batch started successfully"
     }
  4. **Find batch type conversation**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/conversation/batch/find/{id}"
      Provide the batch ID (represented as _id, retrieved from the Create batch type conversation API) as a URL parameter to trigger the execution of this API as illustrated in the image below:
      ![ai-hub-assistant-integration-async-find-batch](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-async-find-batch.png)
      The response of the API is similar to the example shown below:
      Copy CodeJSON{
      "_id": "6850f42d7fefe8c9a3558d96",
      "tenant_id": "6225cde095f5119c54aa1234",
      "training_config_id": "684963981987a52681fcbc11",
      "training_id": "684963981987a52681fcbc10",
      "limit_reached": false,
      "status": "Completed",
      "is_batch": true,
      "task_id": null,
      "metadata": {
      "key": "value"
      },
      "callback_url": "",
      "translation_enabled": true
     }
      The response includes the status "Completed" once the batch conversation execution has successfully finished.
  5. **List messages**: Endpoint: "https://aihub-staging.neutrinos.com/inferenceservice/assistant/message/find-all/{id}"
      Provide the batch ID (represented as _id, retrieved from the Create batch type conversation API) as a URL parameter to trigger the execution of the API as illustrated in the image below:
      ![ai-hub-assistant-integration-async-find-all-messages-batch](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-async-find-all-messages-batch.png)
      You can configure how the output is presented by specifying parameters such as:
      Copy CodeJSON{
      "page_number": 0,
      "page_size": 10,
      "sort": {
      "updated_at": -1
      }
     }
      This API endpoint returns the conversation result status for the entire batch, formatted according to the model instructions defined in the platform UI. The output can be returned in either raw text or JSON format. When using JSON, you must define a structure that complies with the platform’s formatting standards. A sample JSON format is shown below:
      Copy CodeJSON{
      "name": "boarding_pass_details",
      "description": "Extracts key details from a boarding pass including passenger name, travel date, origin, and destination.",
      "parameters": {
      "type": "object",
      "properties": {
      "BoardingPass": {
      "type": "array",
      "minItems": 1,
      "items": {
      "type": "object",
      "properties": {
      "Name": {
      "type": "string",
      "description": "Name of the passenger"
      },
      "Date": {
      "type": "string",
      "description": "Date of the flight"
      },
      "From": {
      "type": "string",
      "description": "Origin or departure airport"
      },
      "To": {
      "type": "string",
      "description": "Destination or arrival airport"
      }
      },
      "required": [
      "Name",
      "Date",
      "From",
      "To"
      ],
      "additionalProperties": false
      }
      }
      },
      "required": [
      "BoardingPass"
      ],
      "additionalProperties": false
      }
     }
      ![Note](/resources/Storage/ai-hub/project-trailproject/note.png)
      Note: The name, type, and description of the input and output fields in the sample JSON can be modified as per your requirements.
      The output of this API is similar to the example shown below. Note: The response is displayed in raw text format.
      Copy CodeJSON{
      "data": [
      {
      "_id": "6850f4747fefe8c9a3558db8",
      "conversation_id": "6850f42d7fefe8c9a3558d96",
      "created_at": "2025-06-17T04:52:04.819Z",
      "output": {
      "text": "Thank you for providing the OCR data. Here is the structured information extracted from your invoice:
     ---
     ## **Invoice Details**
     - **Invoice Number:** 26020078
     - **Date of Issue:** 11/19/2019
     ---
     ## **Seller Information**
     - **Name:** Johnson, Coleman and Mccarthy
     - **Address:** Unit 1928 Box 1473, DPO AA 74927
     - **Tax ID:** 944-91-8763
     - **IBAN:** GB93YUAY48784201603098
     ---
     ## **Gross Worth**
     - **Total Gross Worth:** $116.52
     ---
     If you need further details or a breakdown of the items, please let me know!"
      },
      "status": "Completed",
      "created_by": "S****i N",
      "error": null,
      "translation_enabled": true,
      "metadata": {
      "key": "value"
      }
      },
      {
      "_id": "6850f46d7fefe8c9a3558db0",
      "conversation_id": "6850f42d7fefe8c9a3558d96",
      "created_at": "2025-06-17T04:51:57.213Z",
      "output": {
      "text": "Thank you for providing the OCR data. Here’s the structured information based on your instructions:
     ---
     ## **Invoice Details**
     - **Invoice Number:** 49565075
     - **Date of Issue:** 10/28/2019
     ---
     ## **Seller Information**
     - **Name:** Kane - Morgan Garcia Inc
     - **Address:** 968 Carr Mission Apt. 320, Bernardville, VA 28211
     - **Tax ID:** 964-95-3813
     - **IBAN:** GB73WCIJ55232646970614
     ---
     ## **Gross Worth**
     - **Total Gross Worth:** $96.73
     ---
     If you need any more details or a breakdown of the items, please let me know!"
      },
      "status": "Completed",
      "created_by": "S****i N",
      "error": null,
      "translation_enabled": true,
      "metadata": {
      "key": "value"
      }
      },
      {
      "_id": "6850f4647fefe8c9a3558da8",
      "conversation_id": "6850f42d7fefe8c9a3558d96",
      "created_at": "2025-06-17T04:51:48.493Z",
      "output": {
      "text": "Thank you for providing the OCR data. Here’s the structured information as per your request:
     ---
     ## **Invoice Details**
     - **Invoice Number:** 61356291
     - **Date of Issue:** 09/06/2012
     ---
     ## **Seller Information**
     - **Name:** Chapman, Kim and Green
     - **Address:** 64731 James Branch, Smithmouth, NC 26872
     - **Tax ID:** 949-84-9105
     - **IBAN:** GB50ACIE59715038217063
     ---
     ## **Gross Worth**
     - **Total Gross Worth:** $212.09
     ---
     If you need any more details or a breakdown of the items, feel free to ask!"
      },
      "status": "Completed",
      "created_by": "S****i N",
      "error": null,
      "translation_enabled": true,
      "metadata": {
      "key": "value"
      }
      },
      {
      "_id": "6850f45a7fefe8c9a3558da0",
      "conversation_id": "6850f42d7fefe8c9a3558d96",
      "created_at": "2025-06-17T04:51:38.418Z",
      "output": {
      "text": "Certainly! Here is the structured information extracted from your invoice:
     ---
     ## **Invoice Details**
     - **Invoice Number:** 40378170
     - **Date of Issue:** 10/15/2012
     ---
     ## **Seller Information**
     - **Name:** Patel, Thompson and Montgomery
     - **Address:** 356 Kyle Vista, New James, MA 46228
     - **Tax ID:** 958-74-3511
     - **IBAN:** GB77WRBQ31965128414006
     ---
     ## **Gross Worth**
     - **Total Gross Worth:** $8.25
     ---
     If you need further breakdowns or more details from the invoice, please let me know!"
      },
      "status": "Completed",
      "created_by": "S****i N",
      "error": null,
      "translation_enabled": true,
      "metadata": {
      "key": "value"
      }
      }
      ],
      "total": 4
     }
    - **page_number**: Set the starting page number to display the output.
    - **page_size**: Define the number of results per page.
    - **sort**: Determines the order in which the results are displayed.

## Using Script

Alternatively, you can embed the Assistant into your web application using a <script> tag. Note: To enable this integration, you must add your web application's domain to the Allowable Domains list under the Assistant's Advanced Settings.

1. Navigate to the Integration section of the desired Assistant. Click the Type dropdown and select Script from the available options as illustrated in the image below:
   ![ai-hub-assistant-integration-script-choice](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-script-choice.png)
2. On the right panel, you will find the script tag embed link, which can be used within the <script> tag of your web application to integrate the Assistant.
   ![ai-hub-assistant-integration-script-tag](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-script-tag.png)
3. Select the model version and the corresponding environment from their respective dropdowns.
   ![ai-hub-assistant-integration-sel-env-script-embed](/resources/Storage/ai-hub/images/ai-hub-assistant-integration-sel-env-script-embed.png)
4. In the body of your web application, paste the contents of the <chatbot-embed> tag to integrate and use the Assistant within your application.
