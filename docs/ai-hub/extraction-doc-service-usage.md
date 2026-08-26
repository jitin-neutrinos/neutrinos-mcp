# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/extraction-doc-service-usage>

This guide provides examples of how to use the Extraction Document Service methods in the IDP Inference SDK. These methods allow you to perform various extraction tasks, manage batches, and handle results.

## Table of Methods with API Links

| **Method Name  ** | **  API Endpoint  ** | **  API Docs Link** |
| --- | --- | --- |
| [`createBatch`](/articles/ai-hub/extraction-doc-service-usage/a/creating-a-batch) | `/extraction/batch/create` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#createbatch) |
| [`uploadDocumentToBatch`](/articles/ai-hub/extraction-doc-service-usage/a/uploading-documents-to-a-batch) | `/extraction/upload/batch/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#uploaddocumenttobatch) |
| [`startBatch`](/articles/ai-hub/extraction-doc-service-usage/a/starting-a-batch) | `/extraction/batch/start/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#startbatch) |
| [`listBatches`](/articles/ai-hub/extraction-doc-service-usage/a/listing-batches) | `/extraction/batch/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#listbatches) |
| [`getBatchInfo`](/articles/ai-hub/extraction-doc-service-usage/a/getting-batch-info) | `/extraction/batch/find/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#getbatchinfo) |
| [`listBatchTest`](/articles/ai-hub/extraction-doc-service-usage/a/listing-batch-test) | `/extraction/batch/data/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#listbatchtest) |
| [`listTest`](/articles/ai-hub/extraction-doc-service-usage/a/listing-test) | `/extraction/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#listtest) |
| [`listResults`](/articles/ai-hub/extraction-doc-service-usage/a/listing-results) | `/extraction/results/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#listresults) |
| [`getResultInfo`](/articles/ai-hub/extraction-doc-service-usage/a/getting-result-info) | `/extraction/results/find-one/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#getresultinfo) |
| [`sendFeedback`](/articles/ai-hub/extraction-doc-service-usage/a/sending-feedback) | `/extraction/results/feedback/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#sendfeedback) |
| [`downloadData`](/articles/ai-hub/extraction-doc-service-usage/a/downloading-data) | `/extraction/download/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#downloadtest) |
| [`downloadResult`](/articles/ai-hub/extraction-doc-service-usage/a/downloading-result) | `/extraction/results/download/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#downloadresult) |
| [`startSingle`](/articles/ai-hub/extraction-doc-service-usage/a/starting-a-single) | `/extraction/start/doc/single` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ExtractionDocService.md#startsingle) |

## Creating a Batch

To create a new batch for document extraction:

**TypeScript**

```code
import { IExtractionDocCreateBatchDto } from '@neutrinos/idp-inference-sdk';

const createBatchDto: IExtractionDocCreateBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document extraction' },
  callback_url: 'https://example.com/callback',
};

try {
  const result = await sdk.extraction.doc.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

**JavaScript**

```code
const createBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document extraction' },
  callback_url: 'https://example.com/callback',
};

try {
  const result = await sdk.extraction.doc.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

## Uploading Documents to a Batch

To upload documents to a document extraction batch:

**TypeScript**

```code
import { IExtractionDocumentUploadToBatchDto } from '@neutrinos/idp-inference-sdk';

const uploadDto: IExtractionDocumentUploadToBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  file_path: 'your-file-path',
  file_id: 'your-file-id','
};

try {
  const result = await sdk.extraction.doc.uploadDocumentToBatch(uploadDto);
  console.log('Documents uploaded:', result);
} catch (error) {
  console.error('Error uploading documents:', error);
}
```

**JavaScript**

```code
const uploadDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  file_path: 'your-file-path',
  file_id: 'your-file-id',
};

try {
  const result = await sdk.extraction.doc.uploadDocumentToBatch(uploadDto);
  console.log('Documents uploaded:', result);
} catch (error) {
  console.error('Error uploading documents:', error);
}
```

## Starting a Batch

To start processing documents in a document extraction batch:

**TypeScript**

```code
import { IExtractionStartBatchDto } from '@neutrinos/idp-inference-sdk';

const startBatchDto: IExtractionStartBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  batch_size: 10,
};

try {
  const result = await sdk.extraction.doc.startBatch(startBatchDto);
  console.log('Batch started:', result);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

**JavaScript**

```code
const startBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  batch_size: 10,
};

try {
  const result = await sdk.extraction.doc.startBatch(startBatchDto);
  console.log('Batch started:', result);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

## Listing Batches

To list all document extraction batches:

**TypeScript**

```code
import { IExtractionListBatchDto } from '@neutrinos/idp-inference-sdk';

const listBatchDto: IExtractionListBatchDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listBatches(listBatchDto);
  console.log('Batches:', result);
} catch (error) {
  console.error('Error getting batches:', error);
}
```

**JavaScript**

```code
const listBatchDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listBatches(listBatchDto);
  console.log('Batches:', result);
} catch (error) {
  console.error('Error getting batches:', error);
}
```

## Getting Batch Info

To get information about a specific document extraction batch:

**TypeScript**

```code
import { IExtractionBatchInfoDto } from '@neutrinos/idp-inference-sdk';

const getBatchDto: IExtractionBatchInfoDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
};

try {
  const result = await sdk.extraction.doc.getBatchInfo(getBatchDto);
  console.log('Batch info:', result);
} catch (error) {
  console.error('Error getting batch info:', error);
}
```

**JavaScript**

```code
const getBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
};

try {
  const result = await sdk.extraction.doc.getBatchInfo(getBatchDto);
  console.log('Batch info:', result);
} catch (error) {
  console.error('Error getting batch info:', error);
}
```

## Listing Batch Test

To list all data in a specific document extraction batch with pagination:

**TypeScript**

```code
import { IExtractionBatchListTestDto } from '@neutrinos/idp-inference-sdk';

const listTestDto: IExtractionBatchListTestDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listBatchTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

**JavaScript**

```code
const listTestDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listBatchTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

## Listing Test

To list all document extraction data that are not related to the batch with pagination:

**TypeScript**

```code
import { IExtractionListTestDto } from '@neutrinos/idp-inference-sdk';

const listTestDto: IExtractionListTestDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

**JavaScript**

```code
const listTestDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.doc.listTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

## Listing Results

To list all document extraction results for a batch with pagination:

**TypeScript**

```code
import { IExtractionDocListResultsDto } from '@neutrinos/idp-inference-sdk';

const listResultsDto: IExtractionDocListResultsDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.extraction.doc.listResults(listResultsDto);
  console.log('Data results:', result);
} catch (error) {
  console.error('Error getting data results:', error);
}
```

**JavaScript**

```code
const listResultsDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.extraction.doc.listResults(listResultsDto);
  console.log('Data results:', result);
} catch (error) {
  console.error('Error getting data results:', error);
}
```

## Getting Result Info

To get info of a specific document extraction result:

**TypeScript**

```code
import { IExtractionResultInfoDto } from '@neutrinos/idp-inference-sdk';

const getResultDto: IExtractionResultInfoDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.extraction.doc.getResultInfo(getResultDto);
  console.log('Result info:', result);
} catch (error) {
  console.error('Error getting result info:', error);
}
```

**JavaScript**

```code
const getResultDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.extraction.doc.getResultInfo(getResultDto);
  console.log('Result info:', result);
} catch (error) {
  console.error('Error getting result info:', error);
}
```

## Sending Feedback

To send feedback for a specific document extraction result:

**TypeScript**

```code
import { IExtractionResultFeedbackDto } from '@neutrinos/idp-inference-sdk';

const feedbackDto: IExtractionResultFeedbackDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
  manual_classification: 'positive',
  manual_reason: 'This is a positive document',
};

try {
  const result = await sdk.extraction.doc.sendFeedback(feedbackDto);
  console.log('Feedback sent:', result);
} catch (error) {
  console.error('Error sending feedback:', error);
}
```

**JavaScript**

```code
const feedbackDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
  manual_classification: 'positive',
  manual_reason: 'This is a positive document',
};

try {
  const result = await sdk.extraction.doc.sendFeedback(feedbackDto);
  console.log('Feedback sent:', result);
} catch (error) {
  console.error('Error sending feedback:', error);
}
```

## Downloading Test

To download the data document of a specific document extraction data:

**TypeScript**

```code
import { IExtractionTestDownloadDto } from '@neutrinos/idp-inference-sdk';

const downloadDto: IExtractionTestDownloadDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.extraction.doc.downloadTest(downloadDto);
  console.log('Data downloaded:', result);
} catch (error) {
  console.error('Error downloading data:', error);
}
```

**JavaScript**

```code
const downloadDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.extraction.doc.downloadTest(downloadDto);
  console.log('Data downloaded:', result);
} catch (error) {
  console.error('Error downloading data:', error);
}
```

## Downloading Result

To download the result document of a specific document extraction result:

**TypeScript**

```code
import { IExtractionResultDownloadDto } from '@neutrinos/idp-inference-sdk';

const downloadDto: IExtractionResultDownloadDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.extraction.doc.downloadResult(downloadDto);
  console.log('Result downloaded:', result);
} catch (error) {
  console.error('Error downloading result:', error);
}
```

**JavaScript**

```code
const downloadDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.extraction.doc.downloadResult(downloadDto);
  console.log('Result downloaded:', result);
} catch (error) {
  console.error('Error downloading result:', error);
}
```

## Starting a Single

To start a single document extraction:

**TypeScript**

```code
import { IExtractionDocSingleDto } from '@neutrinos/idp-inference-sdk';

const singleDto: IExtractionDocSingleDto = {
  token: 'your-auth-token',
  file_path: 'your-file-path',
  file_id: 'your-file-id',
  metadata: {
    document_type: 'invoice',
    document_name: 'July Invoice',
  },
};

try {
  const result = await sdk.extraction.doc.startSingle(singleDto);
  console.log('Single extraction started:', result);
} catch (error) {
  console.error('Error starting single extraction:', error);
}
```

**JavaScript**

```code
const singleDto = {
  token: 'your-auth-token',
  file_path: 'your-file-path',
  file_id: 'your-file-id',
  metadata: {
    document_type: 'invoice',
    document_name: 'July Invoice',
  },
};

try {
  const result = await sdk.extraction.doc.startSingle(singleDto);
  console.log('Single extraction started:', result);
} catch (error) {
  console.error('Error starting single extraction:', error);
}
```
