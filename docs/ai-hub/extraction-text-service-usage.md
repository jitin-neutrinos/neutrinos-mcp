# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/extraction-text-service-usage>

This guide provides examples of how to use the **Text Extraction Service** methods in the IDP Inference SDK. These methods allow you to create and manage batches for text-based NER extraction from plain text files or direct text content.

## Table of Methods with API Links

| **Method Name  ** | **  API Endpoint  ** | **  API Docs Link** |
| --- | --- | --- |
| [`createBatch`](/articles/ai-hub/extraction-text-service-usage/a/creating-a-batch) | `/extraction/create/batch` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#createbatch) |
| [`uploadFileToBatch`](/articles/ai-hub/extraction-text-service-usage/a/uploading-a-file-to-batch) | `/extraction/upload/batch/:batch_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#uploadfiletobatch) |
| [`insertToBatch`](/articles/ai-hub/extraction-text-service-usage/a/inserting-text-inputs) | `/extraction/insert/batch/:batch_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#inserttobatch) |
| [`startBatch`](/articles/ai-hub/extraction-text-service-usage/a/starting-the-batch) | `/extraction/start/batch/:batch_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#startbatch) |
| [`getBatchInfo`](/articles/ai-hub/extraction-text-service-usage/a/fetching-batch-info) | `/extraction/batch/find/:batch_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#getbatchinfo) |
| [`listBatchTest`](/articles/ai-hub/extraction-text-service-usage/a/listing-test-items-in-a-batch) | `/extraction/batch/data/:batch_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#listbatchtest) |
| [`listBatches`](/articles/ai-hub/extraction-text-service-usage/a/listing-all-batches) | `/extraction/batch/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#listbatches) |
| [`startSingle`](/articles/ai-hub/extraction-text-service-usage/a/starting-a-single-text-extraction-test) | `/extraction/start/text/single` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#startsingle) |
| [`listTest`](/articles/ai-hub/extraction-text-service-usage/a/listing-all-test-entries) | `/extraction/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#listtest) |
| [`listResults`](/articles/ai-hub/extraction-text-service-usage/a/listing-extraction-results) | `/extraction/results/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#listresults) |
| [`getResultInfo`](/articles/ai-hub/extraction-text-service-usage/a/getting-specific-result-info) | `/extraction/results/find-one/:result_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#getresultinfo) |
| [`sendFeedback`](/articles/ai-hub/extraction-text-service-usage/a/submitting-manual-feedback-for-a-result) | `/extraction/results/feedback/:result_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#sendfeedback) |
| [`downloadData`](/articles/ai-hub/extraction-text-service-usage/a/downloading-test-data-file) | `/extraction/download/:test_id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/TextExtractionService.md#downloaddata) |

## Creating a Batch

To create a new batch for text-based extraction:

**TypeScript**

```code
import { ITextExtractionCreateBatchDto } from '@neutrinos/idp-inference-sdk';

const createBatchDto: ITextExtractionCreateBatchDto = {
  token: 'your-auth-token',
  callback_url: 'https://example.com/webhook',
  is_file: true,
  metadata: {
    source: 'transcripts',
    user: 'analyst-002',
  },
};

try {
  const result = await sdk.extraction.text.createBatch(createBatchDto);
  console.log('Text Batch created:', result);
} catch (error) {
  console.error('Error creating text batch:', error);
}
```

**JavaScript**

```code
const createBatchDto = {
  token: 'your-auth-token',
  callback_url: 'https://example.com/webhook',
  is_file: true,
  metadata: {
    source: 'transcripts',
    user: 'analyst-002',
  },
};

try {
  const result = await sdk.extraction.text.createBatch(createBatchDto);
  console.log('Text Batch created:', result);
} catch (error) {
  console.error('Error creating text batch:', error);
}
```

## Uploading a File to Batch

To upload a text file or reference a file ID to an existing batch:

**TypeScript**

```code
import { ITextUploadFileToBatchDto } from '@neutrinos/idp-inference-sdk';

const uploadDto: ITextUploadFileToBatchDto = {
  token: 'your-auth-token',
  batch_id: '64f1d0e01c9a4f0012ab3456',
  file_path: '/files/input.csv',
};

try {
  const result = await sdk.extraction.text.uploadFileToBatch(uploadDto);
  console.log('Uploaded:', result.file_name);
} catch (error) {
  console.error('Error uploading file:', error);
}
```

**JavaScript**

```code
const uploadDto = {
  token: 'your-auth-token',
  batch_id: '64f1d0e01c9a4f0012ab3456',
  file_path: '/files/input.csv',
};

try {
  const result = await sdk.extraction.text.uploadFileToBatch(uploadDto);
  console.log('Uploaded:', result.file_name);
} catch (error) {
  console.error('Error uploading file:', error);
}
```

## Inserting Text Inputs

To insert one or more plain text inputs (with optional ground truth labels) into a batch:

**TypeScript**

```code
import { ITextExtractionInsertToBatchDto } from '@neutrinos/idp-inference-sdk';

const insertDto: ITextExtractionInsertToBatchDto = {
  token: 'your-auth-token',
  batch_id: '64f123abc456def789012345',
  input: [
    {
      text: 'The shipping was delayed by 3 days.',
      ground_truth: {
        'Policy Type': [
          {
            label: 'delay_reason',
            start: 4,
            end: 28,
          },
        ],
      },
    },
    {
      text: 'Please contact customer support.',
    },
  ],
};

try {
  const inserted = await sdk.extraction.text.insertToBatch(insertDto);
  console.log('Inserted:', inserted);
} catch (error) {
  console.error('Error inserting inputs:', error);
}
```

**JavaScript**

```code
const insertDto = {
  token: 'your-auth-token',
  batch_id: '64f123abc456def789012345',
  input: [
    {
      text: 'The shipping was delayed by 3 days.',
      ground_truth: {
        'Policy Type': [
          {
            label: 'delay_reason',
            start: 4,
            end: 28,
          },
        ],
      },
    },
    {
      text: 'Please contact customer support.',
    },
  ],
};

try {
  const inserted = await sdk.extraction.text.insertToBatch(insertDto);
  console.log('Inserted:', inserted);
} catch (error) {
  console.error('Error inserting inputs:', error);
}
```

## Starting the Batch

Once all required data has been added to the batch, you can start the extraction:

**TypeScript**

```code
const batchId = '64f123abc456def789012345';

try {
  const started = await sdk.extraction.text.startBatch({
    token: 'your-auth-token',
    batch_id: batchId,
  });
  console.log('Batch started:', started);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

**JavaScript**

```code
const batchId = '64f123abc456def789012345';

try {
  const started = await sdk.extraction.text.startBatch({
    token: 'your-auth-token',
    batch_id: batchId,
  });
  console.log('Batch started:', started);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

## Fetching Batch Info

To retrieve metadata of a batch such as its status, deployment, and progress:

**TypeScript**

```code
import { ITextExtractionBatchInfoDto } from '@neutrinos/idp-inference-sdk';

const batchInfoDto: ITextExtractionBatchInfoDto = {
  token: 'your-auth-token',
  batch_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const info = await sdk.extraction.text.getBatchInfo(batchInfoDto);
  console.log('Batch Info:', info);
} catch (error) {
  console.error('Error fetching batch info:', error);
}
```

**JavaScript**

```code
const batchInfoDto = {
  token: 'your-auth-token',
  batch_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const info = await sdk.extraction.text.getBatchInfo(batchInfoDto);
  console.log('Batch Info:', info);
} catch (error) {
  console.error('Error fetching batch info:', error);
}
```

## Listing Test Items in a Batch

To list the test input records uploaded into a **text-based extraction batch** with pagination and sorting:

**TypeScript**

```code
import { ITextExtractionBatchListTestDto } from '@neutrinos/idp-inference-sdk';

const listTestDto: ITextExtractionBatchListTestDto = {
  token: 'your-auth-token',
  batch_id: '64b8f5f9c9f0a40abc123456',
  page_number: 0,
  page_size: 20,
  sort: 'asc',
};

try {
  const tests = await sdk.extraction.text.listBatchTest(listTestDto);
  console.log('Tests in batch:', tests.data);
} catch (error) {
  console.error('Error listing batch tests:', error);
}
```

**JavaScript**

```code
const listTestDto = {
  token: 'your-auth-token',
  batch_id: '64b8f5f9c9f0a40abc123456',
  page_number: 0,
  page_size: 20,
  sort: 'asc',
};

try {
  const tests = await sdk.extraction.text.listBatchTest(listTestDto);
  console.log('Tests in batch:', tests.data);
} catch (error) {
  console.error('Error listing batch tests:', error);
}
```

## Listing All Batches

Lists all batches with support for pagination and sorting.

**TypeScript**

```code
import { ITextExtractionListBatchDto } from '@neutrinos/idp-inference-sdk';

const listDto: ITextExtractionListBatchDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listBatches(listDto);
  console.log('Batches:', result.data);
} catch (error) {
  console.error('Error listing batches:', error);
}
```

**JavaScript**

```code
const listDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listBatches(listDto);
  console.log('Batches:', result.data);
} catch (error) {
  console.error('Error listing batches:', error);
}
```

## Starting a Single Text Extraction Test

Initiates a one-off text extraction test without using batch logic. Useful for real-time testing or previewing extraction behavior.

**TypeScript**

```code
import { ITextExtractionSingleTestDto } from '@neutrinos/idp-inference-sdk';

const inputDto: ITextExtractionSingleTestDto = {
  token: 'your-auth-token',
  input: {
    text: 'Barack Obama was born in Hawaii.',
  },
  metadata: {
    origin: 'news-api',
  },
};

try {
  const result = await sdk.extraction.text.startSingle(inputDto);
  console.log('Extraction Result:', result);
} catch (error) {
  console.error('Error starting single test:', error);
}
```

**JavaScript**

```code
const inputDto = {
  token: 'your-auth-token',
  input: {
    text: 'Barack Obama was born in Hawaii.',
  },
  metadata: {
    origin: 'news-api',
  },
};

try {
  const result = await sdk.extraction.text.startSingle(inputDto);
  console.log('Extraction Result:', result);
} catch (error) {
  console.error('Error starting single test:', error);
}
```

## Listing All Test Entries

Lists all test entries (outside of batch) with support for pagination and sorting.

**TypeScript**

```code
import { ITextExtractionListTestDto } from '@neutrinos/idp-inference-sdk';

const listDto: ITextExtractionListTestDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listTest(listDto);
  console.log('Test list:', result.data);
} catch (error) {
  console.error('Error listing test entries:', error);
}
```

**JavaScript**

```code
const listDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listTest(listDto);
  console.log('Test list:', result.data);
} catch (error) {
  console.error('Error listing test entries:', error);
}
```

## Listing Extraction Results

Retrieves a paginated list of extraction results for text inputs.

**TypeScript**

```code
import { ITextExtractionTestResultsDto } from '@neutrinos/idp-inference-sdk';

const listDto: ITextExtractionTestResultsDto = {
  token: 'your-auth-token',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listResults(listDto);
  console.log('Results:', result.data);
} catch (error) {
  console.error('Error listing extraction results:', error);
}
```

**JavaScript**

```code
const listDto = {
  token: 'your-auth-token',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.extraction.text.listResults(listDto);
  console.log('Results:', result.data);
} catch (error) {
  console.error('Error listing extraction results:', error);
}
```

## Getting Specific Result Info

Gets metadata and output for a specific text extraction result.

**TypeScript**

```code
import { IExtractionTextResultInfoDto } from '@neutrinos/idp-inference-sdk';

const resultInfoDto: IExtractionTextResultInfoDto = {
  token: 'your-auth-token',
  result_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const result = await sdk.extraction.text.getResultInfo(resultInfoDto);
  console.log('Result Info:', result.output);
} catch (error) {
  console.error('Error getting result info:', error);
}
```

**JavaScript**

```code
const resultInfoDto = {
  token: 'your-auth-token',
  result_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const result = await sdk.extraction.text.getResultInfo(resultInfoDto);
  console.log('Result Info:', result.output);
} catch (error) {
  console.error('Error getting result info:', error);
}
```

## Submitting Manual Feedback for a Result

Allows manual correction of a specific text extraction result.

**TypeScript**

```code
import { ITextExtractionTestResultFeedbackDto } from '@neutrinos/idp-inference-sdk';

const feedbackDto: ITextExtractionTestResultFeedbackDto = {
  token: 'your-auth-token',
  result_id: '64b8f5f9c9f0a40abc123456',
  manual_extraction: {
    InvoiceNumber: 'INV-1001',
  },
  manual_reason: 'Corrected after human review.',
};

try {
  const response = await sdk.extraction.text.sendFeedback(feedbackDto);
  console.log('Feedback submitted:', response);
} catch (error) {
  console.error('Error submitting feedback:', error);
}
```

**JavaScript**

```code
const feedbackDto = {
  token: 'your-auth-token',
  result_id: '64b8f5f9c9f0a40abc123456',
  manual_extraction: {
    InvoiceNumber: 'INV-1001',
  },
  manual_reason: 'Corrected after human review.',
};

try {
  const response = await sdk.extraction.text.sendFeedback(feedbackDto);
  console.log('Feedback submitted:', response);
} catch (error) {
  console.error('Error submitting feedback:', error);
}
```

## Downloading Test Data File

Downloads test data file for a text extraction batch that was created using file upload.

**TypeScript**

```code
import { IExtractionTextTestDownloadDto } from '@neutrinos/idp-inference-sdk';

const downloadDto: IExtractionTextTestDownloadDto = {
  token: 'your-auth-token',
  test_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const response = await sdk.extraction.text.downloadData(downloadDto);
  console.log('Data downloaded:', response);
} catch (error) {
  console.error('Error downloading data file:', error);
}
```

**JavaScript**

```code
const downloadDto = {
  token: 'your-auth-token',
  test_id: '64b8f5f9c9f0a40abc123456',
};

try {
  const response = await sdk.extraction.text.downloadData(downloadDto);
  console.log('Data downloaded:', result);
} catch (error) {
  console.error('Error downloading data file:', error);
}
```

**Note:** This only works for batches where `is_file: true` was set, and file(s) were uploaded using `uploadFileToBatch`. It will not work for text-based batches created using `insertToBatch`.
