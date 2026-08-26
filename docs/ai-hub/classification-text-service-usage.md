# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/classification-text-service-usage>

This guide provides examples of how to use the Classification Text Service methods in the IDP Inference SDK. These methods allow you to perform various classification tasks, manage batches, and handle results.

## Table of Methods with API Links

| **Method Name  ** | **  API Endpoint  ** | **  API Docs Link** |
| --- | --- | --- |
| [`createBatch`](/articles/ai-hub/classification-text-service-usage/a/creating-a-batch) | `/classification/batch/create` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationTextService.md#createbatch) |
| [`uploadDocumentToBatch`](/articles/ai-hub/classification-text-service-usage/a/uploading-documents-to-a-batch) | `/classification/upload/batch/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#uploaddocumenttobatch) |
| [`insertToBatch`](/articles/ai-hub/classification-text-service-usage/a/insert-to-a-batch) | `/classification/batch/insert/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationTextService.md#inserttobatch) |
| [`startBatch`](/articles/ai-hub/classification-text-service-usage/a/starting-a-batch) | `/classification/batch/start/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#startbatch) |
| [`listBatches`](/articles/ai-hub/classification-text-service-usage/a/listing-batches) | `/classification/batch/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listbatches) |
| [`getBatchInfo`](/articles/ai-hub/classification-text-service-usage/a/getting-batch-info) | `/classification/batch/find/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#getbatchinfo) |
| [`listBatchTest`](/articles/ai-hub/classification-text-service-usage/a/listing-batch-test) | `/classification/batch/data/{batch_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listbatchtest) |
| [`listTest`](/articles/ai-hub/classification-text-service-usage/a/listing-test) | `/classification/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#listtest) |
| [`listResults`](/articles/ai-hub/classification-text-service-usage/a/listing-results) | `/classification/results/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationTextService.md#listresults) |
| [`getResultInfo`](/articles/ai-hub/classification-text-service-usage/a/getting-result-info) | `/classification/results/find-one/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#getresultinfo) |
| [`sendFeedback`](/articles/ai-hub/classification-text-service-usage/a/sending-feedback) | `/classification/results/feedback/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#sendfeedback) |
| [`downloadTest`](/articles/ai-hub/classification-text-service-usage/a/downloading-data) | `/classification/download/{result_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationService.md#downloadtest) |
| [`startSingle`](/articles/ai-hub/classification-text-service-usage/a/starting-a-single) | `/classification/start/text/single` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ClassificationTextService.md#startsingle) |

## Creating a Batch

**TypeScript**

```code
import { IClassificationTextCreateBatchDto } from '@neutrinos/idp-inference-sdk';

const createBatchDto: IClassificationTextCreateBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document classification', is_file: true },
  callback_url: 'https://example.com/callback',
  group_callback_url: 'https://example.com/group-callback',
};

try {
  const result = await sdk.classification.text.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

**JavaScript**

```code
const createBatchDto = {
  token: 'your-auth-token',
  metadata: { name: 'My Batch', description: 'A batch for document classification', is_file: true },
  callback_url: 'https://example.com/callback',
  group_callback_url: 'https://example.com/group-callback',
};

try {
  const result = await sdk.classification.text.createBatch(createBatchDto);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

## Uploading Documents to a Batch

**TypeScript**

```code
import { IClassificationDocumentUploadToBatchDto } from '@neutrinos/idp-inference-sdk';

const uploadDto: IClassificationDocumentUploadToBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  file: 'path/to/document.pdf',
  file_id: 'unique-file-id',
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
  file: 'path/to/document.pdf',
  file_id: 'unique-file-id',
};

try {
  const result = await sdk.classification.root.uploadDocumentToBatch(uploadDto);
  console.log('Documents uploaded:', result);
} catch (error) {
  console.error('Error uploading documents:', error);
}
```

## Insert to a Batch

**TypeScript**

```code
import { IClassificationTextInsertToBatchDto } from '@neutrinos/idp-inference-sdk';

const insertDto: IClassificationTextInsertToBatchDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  input: [
    {
      data: {
        key: 'value',
        key2: 'value2',
      },
      ground_truth: 'value',
    },
  ],
};

try {
  const result = await sdk.classification.text.insertToBatch(insertDto);
  console.log('Texts added:', result);
} catch (error) {
  console.error('Error adding texts:', error);
}
```

**JavaScript**

```code
const insertDto = {
  token: 'your-auth-token',
  batch_id: 'your-batch-id',
  input: [
    {
      data: {
        key: 'value',
        key2: 'value2',
      },
      ground_truth: 'value',
    },
  ],
};

try {
  const result = await sdk.classification.text.insertToBatch(insertDto);
  console.log('Texts added:', result);
} catch (error) {
  console.error('Error adding texts:', error);
}
```

## Starting a Batch

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

To list all text classification batches:

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

To get info of a specific text classification batch:

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

To list all data in a specific text classification batch with pagination:

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

To list all text classification data that are not related to the batch with pagination:

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

To list all text classification results for a batch with pagination:

**TypeScript**

```code
import { IClassificationTextListResultsDto } from '@neutrinos/idp-inference-sdk';

const listResultsDto: IClassificationTextListResultsDto = {
  token: 'your-auth-token',
  test_id: 'your-test-id',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.classification.text.listResults(listResultsDto);
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
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.classification.text.listResults(listResultsDto);
  console.log('Data results:', result);
} catch (error) {
  console.error('Error getting data results:', error);
}
```

## Getting Result Info

To get information about a specific text classification result:

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

To send feedback for a specific text classification result:

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

To download the data document of a specific text classification data:

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

## Starting a Single

To start a single text classification:

**TypeScript**

```code
import { IClassificationTextSingleDto } from '@neutrinos/idp-inference-sdk';

const singleDto: IClassificationTextSingleDto = {
  token: 'your-auth-token',
  text: 'your-text',
  metadata: {
    text_type: 'invoice',
  },
};

try {
  const result = await sdk.classification.text.startSingle(singleDto);
  console.log('Single classification started:', result);
} catch (error) {
  console.error('Error starting single classification:', error);
}
```

**JavaScript**

```code
const singleDto = {
  token: 'your-auth-token',
  text: 'your-text',
  metadata: {
    text_type: 'invoice',
  },
};

try {
  const result = await sdk.classification.text.startSingle(singleDto);
  console.log('Single classification started:', result);
} catch (error) {
  console.error('Error starting single classification:', error);
}
```
