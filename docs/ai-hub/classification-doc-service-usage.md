# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/classification-doc-service-usage>

This guide provides examples of how to use the Classification Document Service methods in the IDP Inference SDK. These methods allow you to perform various classification tasks, manage batches, and handle results.

## Table of Methods with API Links

| **Method Name  ** | **  API Endpoint  ** | **  API Docs Link** |
| --- | --- | --- |
| [`createBatch`](/articles/ai-hub/classification-doc-service-usage/a/creating-a-batch) | `/classification/batch/create` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationDocService.md#createbatch) |
| [`uploadDocumentToBatch`](/articles/ai-hub/classification-doc-service-usage/a/uploading-documents-to-a-batch) | `/classification/upload/batch/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#uploaddocumenttobatch) |
| [`startBatch`](/articles/ai-hub/classification-doc-service-usage/a/starting-a-batch) | `/classification/batch/start/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#startbatch) |
| [`listBatches`](/articles/ai-hub/classification-doc-service-usage/a/listing-batches) | `/classification/batch/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listbatches) |
| [`getBatchInfo`](/articles/ai-hub/classification-doc-service-usage/a/getting-batch-info) | `/classification/batch/find/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#getbatchinfo) |
| [`listBatchTest`](/articles/ai-hub/classification-doc-service-usage/a/listing-batch-test) | `/classification/batch/data/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listbatchtest) |
| [`listTest`](/articles/ai-hub/classification-doc-service-usage/a/listing-test) | `/classification/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listtest) |
| [`listResults`](/articles/ai-hub/classification-doc-service-usage/a/listing-results) | `/classification/results/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationDocService.md#listresults) |
| [`getResultInfo`](/articles/ai-hub/classification-doc-service-usage/a/getting-result-info) | `/classification/results/find-one/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#getresultinfo) |
| [`sendFeedback`](/articles/ai-hub/classification-doc-service-usage/a/sending-feedback) | `/classification/results/feedback/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#sendfeedback) |
| [`downloadData`](/articles/ai-hub/classification-doc-service-usage/a/downloading-data) | `/classification/download/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#downloadtest) |
| [`downloadResult`](/articles/ai-hub/classification-doc-service-usage/a/downloading-result) | `/classification/results/download/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#downloadresult) |
| [`startSingle`](/articles/ai-hub/classification-doc-service-usage/a/starting-a-single) | `/classification/start/doc/single` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationDocService.md#startsingle) |

## Creating a Batch

To create a new batch for document classification:

**TypeScript**

```code
import { IClassificationDocCreateBatchDto } from '@neutrinos/idp-inference-sdk';

const createBatchDto: IClassificationDocCreateBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document classification' },
  callback_url: 'https://example.com/callback',
  group_callback_url: 'https://example.com/group-callback',
};

try {
  const result = await sdk.classification.doc.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

**JavaScript**

```code
const createBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document classification' },
  callback_url: 'https://example.com/callback',
  group_callback_url: 'https://example.com/group-callback',
};

try {
  const result = await sdk.classification.doc.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

## Uploading Documents to a Batch

To upload documents to a document classification batch:

**TypeScript**

```code
import { IClassificationDocumentUploadToBatchDto } from '@neutrinos/idp-inference-sdk';

const uploadDto: IClassificationDocumentUploadToBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  file_path: 'your-file-path',
  file_id: 'your-file-id',
};

try {
  const result = await sdk.classification.root.uploadDocumentToBatch(uploadDto);
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
  const result = await sdk.classification.root.uploadDocumentToBatch(uploadDto);
  console.log('Documents uploaded:', result);
} catch (error) {
  console.error('Error uploading documents:', error);
}
```

## Starting a Batch

To start processing documents in a document classification batch:

**TypeScript**

```code
import { IClassificationStartBatchDto } from '@neutrinos/idp-inference-sdk';

const startBatchDto: IClassificationStartBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  batch_size: 10,
};

try {
  const result = await sdk.classification.root.startBatch(startBatchDto);
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
  const result = await sdk.classification.root.startBatch(startBatchDto);
  console.log('Batch started:', result);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

## Listing Batches

To list all document classification batches:

**TypeScript**

```code
import { IClassificationListBatchDto } from '@neutrinos/idp-inference-sdk';

const listBatchDto: IClassificationListBatchDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.classification.root.listBatches(listBatchDto);
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
  const result = await sdk.classification.root.listBatches(listBatchDto);
  console.log('Batches:', result);
} catch (error) {
  console.error('Error getting batches:', error);
}
```

## Getting Batch Info

To get info of a specific document classification batch:

**TypeScript**

```code
import { IClassificationBatchInfoDto } from '@neutrinos/idp-inference-sdk';

const getBatchDto: IClassificationBatchInfoDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
};

try {
  const result = await sdk.classification.root.getBatchInfo(getBatchDto);
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
  const result = await sdk.classification.root.getBatchInfo(getBatchDto);
  console.log('Batch info:', result);
} catch (error) {
  console.error('Error getting batch info:', error);
}
```

## Listing Batch Test

To list all data in a specific document classification batch with pagination:

**TypeScript**

```code
import { IClassificationBatchListTestDto } from '@neutrinos/idp-inference-sdk';

const listTestDto: IClassificationBatchListTestDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.classification.root.listBatchTest(listTestDto);
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
  const result = await sdk.classification.root.listBatchTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

## Listing Test

To list all document classification data which are not related to batch with pagination:

**TypeScript**

```code
import { IClassificationListTestDto } from '@neutrinos/idp-inference-sdk';

const listTestDto: IClassificationListTestDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.classification.root.listTest(listTestDto);
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
  const result = await sdk.classification.root.listTest(listTestDto);
  console.log('Batch data:', result);
} catch (error) {
  console.error('Error getting batch data:', error);
}
```

## Listing Results

To list all document classification results for a batch with pagination:

**TypeScript**

```code
import { IClassificationDocListResultsDto } from '@neutrinos/idp-inference-sdk';

const listResultsDto: IClassificationDocListResultsDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.classification.doc.listResults(listResultsDto);
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
  const result = await sdk.classification.doc.listResults(listResultsDto);
  console.log('Data results:', result);
} catch (error) {
  console.error('Error getting data results:', error);
}
```

## Getting Result Info

To get info of a specific document classification result:

**TypeScript**

```code
import { IClassificationResultInfoDto } from '@neutrinos/idp-inference-sdk';

const getResultDto: IClassificationResultInfoDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.classification.root.getResultInfo(getResultDto);
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
  const result = await sdk.classification.root.getResultInfo(getResultDto);
  console.log('Result info:', result);
} catch (error) {
  console.error('Error getting result info:', error);
}
```

## Sending Feedback

To send feedback for a specific document classification result:

**TypeScript**

```code
import { IClassificationResultFeedbackDto } from '@neutrinos/idp-inference-sdk';

const feedbackDto: IClassificationResultFeedbackDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
  manual_classification: 'positive',
  manual_reason: 'This is a positive document',
};

try {
  const result = await sdk.classification.root.sendFeedback(feedbackDto);
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
  const result = await sdk.classification.root.sendFeedback(feedbackDto);
  console.log('Feedback sent:', result);
} catch (error) {
  console.error('Error sending feedback:', error);
}
```

## Downloading Data

To download the data document of a specific document classification data:

**TypeScript**

```code
import { IClassificationTestDownloadDto } from '@neutrinos/idp-inference-sdk';

const downloadDto: IClassificationTestDownloadDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
};

try {
  const result = await sdk.classification.root.downloadTest(downloadDto);
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
  const result = await sdk.classification.root.downloadTest(downloadDto);
  console.log('Data downloaded:', result);
} catch (error) {
  console.error('Error downloading data:', error);
}
```

## Downloading Result

To download the result document of a specific document classification result:

**TypeScript**

```code
import { IClassificationResultDownloadDto } from '@neutrinos/idp-inference-sdk';

const downloadDto: IClassificationResultDownloadDto = {
  token: 'your-auth-token',
  result_id: 'your-result-id',
};

try {
  const result = await sdk.classification.root.downloadResult(downloadDto);
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
  const result = await sdk.classification.root.downloadResult(downloadDto);
  console.log('Result downloaded:', result);
} catch (error) {
  console.error('Error downloading result:', error);
}
```

## Starting a Single

To start a single document classification:

**TypeScript**

```code
import { IClassificationDocSingleDto } from '@neutrinos/idp-inference-sdk';

const singleDto: IClassificationDocSingleDto = {
  token: 'your-auth-token',
  file_path: 'your-file-path',
  file_id: 'your-file-id',
  metadata: {
    document_type: 'invoice',
    document_name: 'July Invoice',
  },
};

try {
  const result = await sdk.classification.doc.startSingle(singleDto);
  console.log('Single classification started:', result);
} catch (error) {
  console.error('Error starting single classification:', error);
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
  const result = await sdk.classification.doc.startSingle(singleDto);
  console.log('Single classification started:', result);
} catch (error) {
  console.error('Error starting single classification:', error);
}
```
