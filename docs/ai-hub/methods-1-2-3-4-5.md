# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1-2-3-4-5>

## Methods

### createBatch()

> **createBatch**(`input`): `Promise`<[`IExtractionDocCreateBatchResponse`](../interfaces/IExtractionDocCreateBatchResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:188](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-188)

Creates a new extraction batch for document-based input.

#### Parameters

##### input

[`IExtractionDocCreateBatchDto`](../interfaces/IExtractionDocCreateBatchDto.md)

Batch creation payload including optional callback URL and metadata.

#### Returns

`Promise`<[`IExtractionDocCreateBatchResponse`](../interfaces/IExtractionDocCreateBatchResponse.md)>

Created batch metadata.

#### Example

```code
const batch = await sdk.extraction.doc.createBatch({
  token: '1234567890abcdef',
  callback_url: 'https://example.com/callback',
  metadata: { team: 'QA', project: 'invoice-analysis' }
});
```

### uploadDocumentToBatch()

> **uploadDocumentToBatch**(`input`): `Promise`<[`IExtractionDocUploadDocumentToBatchResponse`](../interfaces/IExtractionDocUploadDocumentToBatchResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:215](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-215)

Uploads a document or file ID to an extraction batch.

#### Parameters

##### input

[`IExtractionDocUploadDocumentToBatchDto`](../interfaces/IExtractionDocUploadDocumentToBatchDto.md)

Document upload request data.

#### Returns

`Promise`<[`IExtractionDocUploadDocumentToBatchResponse`](../interfaces/IExtractionDocUploadDocumentToBatchResponse.md)>

Response confirming successful upload.

#### Example

```code
const result = await sdk.extraction.doc.uploadDocumentToBatch({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  file_path: '/files/sample.pdf'
});
console.log('Upload success:', result);
```

### startBatch()

> **startBatch**(`input`): `Promise`<[`IExtractionDocStartBatchResponse`](../interfaces/IExtractionDocStartBatchResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:277](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-277)

Starts extraction on a specified batch.

#### Parameters

##### input

[`IExtractionDocStartBatchDto`](../interfaces/IExtractionDocStartBatchDto.md)

Batch start config with `batch_id` and `batch_size`.

#### Returns

`Promise`<[`IExtractionDocStartBatchResponse`](../interfaces/IExtractionDocStartBatchResponse.md)>

Batch start confirmation with job metadata.

#### Example

```code
const res = await sdk.extraction.doc.startBatch({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  batch_size: 100
});
console.log('Batch started:', res);
```

### listBatches()

> **listBatches**(`input`): `Promise`<[`IExtractionDocListBatchResponse`](../interfaces/IExtractionDocListBatchResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:309](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-309)

Lists all extraction batches (paginated).

#### Parameters

##### input

[`IExtractionDocListBatchDto`](../interfaces/IExtractionDocListBatchDto.md)

Filters such as `page_number`, `page_size`, `sort`.

#### Returns

`Promise`<[`IExtractionDocListBatchResponse`](../interfaces/IExtractionDocListBatchResponse.md)>

Paginated list of batch metadata.

#### Example

```code
const list = await sdk.extraction.doc.listBatches({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Batches:', list.data);
```

### getBatchInfo()

> **getBatchInfo**(`input`): `Promise`<[`IExtractionDocBatchInfoResponse`](../interfaces/IExtractionDocBatchInfoResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:340](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-340)

Fetches metadata of a specific batch using its ID.

#### Parameters

##### input

[`IExtractionDocBatchInfoDto`](../interfaces/IExtractionDocBatchInfoDto.md)

Object with `batch_id`.

#### Returns

`Promise`<[`IExtractionDocBatchInfoResponse`](../interfaces/IExtractionDocBatchInfoResponse.md)>

Batch metadata.

#### Example

```code
const info = await sdk.extraction.doc.getBatchInfo({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456'
});
console.log('Batch Info:', info);
```

### listBatchTest()

> **listBatchTest**(`input`): `Promise`<[`IExtractionDocBatchListTestResponse`](../interfaces/IExtractionDocBatchListTestResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:371](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-371)

Lists test items uploaded to a batch.

#### Parameters

##### input

[`IExtractionDocBatchListTestDto`](../interfaces/IExtractionDocBatchListTestDto.md)

DTO with `batch_id`, pagination and sorting.

#### Returns

`Promise`<[`IExtractionDocBatchListTestResponse`](../interfaces/IExtractionDocBatchListTestResponse.md)>

List of test inputs under the batch.

#### Example

```code
const tests = await sdk.extraction.doc.listBatchTest({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  page_number: 0,
  page_size: 20,
  sort: 'asc'
});
console.log('Tests in batch:', tests.data);
```

### startSingle()

> **startSingle**(`input`): `Promise`<[`IExtractionDocSingleResponse`](../interfaces/IExtractionDocSingleResponse.md)[]>

Defined in: [services/extraction/doc/extraction-doc.service.ts:408](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-408)

Extracts a single document using either file path or file ID.

#### Parameters

##### input

[`IExtractionDocSingleDto`](../interfaces/IExtractionDocSingleDto.md)

Extraction input containing `file_path` or `file_id`, plus optional metadata.

#### Returns

`Promise`<[`IExtractionDocSingleResponse`](../interfaces/IExtractionDocSingleResponse.md)[]>

List of extraction results for the document.

#### Throws

If neither `file_path` nor `file_id` is provided.

#### Throws

If the file at `file_path` does not exist.

#### Example

```code
const result = await sdk.extraction.doc.startSingle({
  token: '1234567890abcdef',
  file_path: '/documents/contract.pdf',
  metadata: { source: 'legal' }
});
```

### listTest()

> **listTest**(`input`): `Promise`<[`IExtractionDocListTestResponse`](../interfaces/IExtractionDocListTestResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:469](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-469)

Lists all test entries (outside batch).

#### Parameters

##### input

[`IExtractionDocListTestDto`](../interfaces/IExtractionDocListTestDto.md)

Filters like `page_number`, `page_size`, `sort`.

#### Returns

`Promise`<[`IExtractionDocListTestResponse`](../interfaces/IExtractionDocListTestResponse.md)>

List of extraction tests.

#### Example

```code
const list = await sdk.extraction.doc.listTest({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Test list:', list.data);
```

### listResults()

> **listResults**(`input`): `Promise`<[`IExtractionDocListResultsResponse`](../interfaces/IExtractionDocListResultsResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:503](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-503)

Retrieves a paginated list of extraction results for documents.

#### Parameters

##### input

[`IExtractionDocListResultDto`](../interfaces/IExtractionDocListResultDto.md)

Pagination, sort, and merge flags.

#### Returns

`Promise`<[`IExtractionDocListResultsResponse`](../interfaces/IExtractionDocListResultsResponse.md)>

Paginated extraction results with metadata.

#### Example

```code
const results = await sdk.extraction.doc.listResults({
  token: '1234567890abcdef',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Results:', results.data);
```

### getResultInfo()

> **getResultInfo**(`input`): `Promise`<[`IExtractionDocResultInfoResponse`](../interfaces/IExtractionDocResultInfoResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:536](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-536)

Gets metadata and output for a specific result.

#### Parameters

##### input

[`IExtractionDocResultInfoDto`](../interfaces/IExtractionDocResultInfoDto.md)

Object with `result_id`.

#### Returns

`Promise`<[`IExtractionDocResultInfoResponse`](../interfaces/IExtractionDocResultInfoResponse.md)>

Result info with extraction output.

#### Example

```code
const result = await sdk.extraction.doc.getResultInfo({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456'
});
console.log('Result Info:', result.output);
```

### sendFeedback()

> **sendFeedback**(`input`): `Promise`<[`IExtractionDocResultFeedbackResponse`](../interfaces/IExtractionDocResultFeedbackResponse.md)>

Defined in: [services/extraction/doc/extraction-doc.service.ts:569](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-569)

Sends manual feedback for an extraction result.

#### Parameters

##### input

[`IExtractionDocResultFeedbackDto`](../interfaces/IExtractionDocResultFeedbackDto.md)

Feedback details including corrected label.

#### Returns

`Promise`<[`IExtractionDocResultFeedbackResponse`](../interfaces/IExtractionDocResultFeedbackResponse.md)>

Feedback submission result.

#### Example

```code
await sdk.extraction.doc.sendFeedback({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456',
  manual_extraction: {
    "entity": "corrected_entity",
  },
  manual_reason: 'Corrected label by reviewer'
});
```

### downloadTest()

> **downloadTest**(`input`): `Promise`<`Readable`>

Defined in: [services/extraction/doc/extraction-doc.service.ts:603](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-603)

Downloads the original file from a test entry.

#### Parameters

##### input

[`IExtractionDocTestDownloadDto`](../interfaces/IExtractionDocTestDownloadDto.md)

Object with `test_id`.

#### Returns

`Promise`<`Readable`>

Stream of the file content.

#### Example

```code
const response = await sdk.extraction.doc.downloadTest({
  token: '1234567890abcdef',
  test_id: '64b8f5f9c9f0a40abc123456'
});
response.pipe(fs.createWriteStream('test.pdf'));
console.log('Test saved to:', 'test.pdf');
```

### downloadResult()

> **downloadResult**(`input`): `Promise`<`Readable`>

Defined in: [services/extraction/doc/extraction-doc.service.ts:633](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-633)

Downloads extraction result output as a file.

#### Parameters

##### input

[`IExtractionDocResultDownloadDto`](../interfaces/IExtractionDocResultDownloadDto.md)

Object with `result_id`.

#### Returns

`Promise`<`Readable`>

Stream of the file content.

#### Example

```code
const result = await sdk.extraction.doc.downloadResult({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456'
});
result.pipe(fs.createWriteStream('result.png'));
console.log('Result saved to:', 'result.png');
```
