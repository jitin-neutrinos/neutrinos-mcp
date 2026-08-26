# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1>

## Methods

### uploadDocumentToBatch()

> **uploadDocumentToBatch**(`input`): `Promise`<[`IClassificationDocumentUploadToBatchResponse`](../interfaces/IClassificationDocumentUploadToBatchResponse.md)>

Defined in: [services/classification/classification.service.ts:148](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-148)

Uploads a document or file ID to a classification batch.

#### Parameters

##### input

[`IClassificationDocumentUploadToBatchDto`](../interfaces/IClassificationDocumentUploadToBatchDto.md)

Document upload request data.

#### Returns

`Promise`<[`IClassificationDocumentUploadToBatchResponse`](../interfaces/IClassificationDocumentUploadToBatchResponse.md)>

Response confirming successful upload.

#### Example

```code
const result = await sdk.classification.root.uploadDocumentToBatch({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  file_path: '/files/sample.pdf',
  file_buffer: {
    fieldname: 'file',
    originalname: 'invoice.pdf',
    encoding: '7bit',
    mimetype: 'application/pdf',
    buffer: Buffer.from('file content'),
    size: 1048576
  }
});
console.log('Upload success:', result);
```

### startBatch()

> **startBatch**(`input`): `Promise`<[`IClassificationStartBatchResponse`](../interfaces/IClassificationStartBatchResponse.md)>

Defined in: [services/classification/classification.service.ts:210](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-210)

Starts classification on a specified batch.

#### Parameters

##### input

[`IClassificationStartBatchDto`](../interfaces/IClassificationStartBatchDto.md)

Batch start config with `batch_id` and `batch_size`.

#### Returns

`Promise`<[`IClassificationStartBatchResponse`](../interfaces/IClassificationStartBatchResponse.md)>

Batch start confirmation with job metadata.

#### Example

```code
const res = await sdk.classification.root.startBatch({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  batch_size: 100
});
console.log('Batch started:', res);
```

### listBatches()

> **listBatches**(`input`): `Promise`<[`IClassificationListBatchResponse`](../interfaces/IClassificationListBatchResponse.md)>

Defined in: [services/classification/classification.service.ts:244](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-244)

Lists all classification batches (paginated).

#### Parameters

##### input

[`IClassificationListBatchDto`](../interfaces/IClassificationListBatchDto.md)

Filters such as `page_number`, `page_size`, `sort`.

#### Returns

`Promise`<[`IClassificationListBatchResponse`](../interfaces/IClassificationListBatchResponse.md)>

Paginated list of batch metadata.

#### Example

```code
const list = await sdk.classification.root.listBatches({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Batches:', list.data);
```

### getBatchInfo()

> **getBatchInfo**(`input`): `Promise`<[`IClassificationBatchInfoResponse`](../interfaces/IClassificationBatchInfoResponse.md)>

Defined in: [services/classification/classification.service.ts:275](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-275)

Fetches metadata of a specific batch using its ID.

#### Parameters

##### input

[`IClassificationBatchInfoDto`](../interfaces/IClassificationBatchInfoDto.md)

Object with `batch_id`.

#### Returns

`Promise`<[`IClassificationBatchInfoResponse`](../interfaces/IClassificationBatchInfoResponse.md)>

Batch metadata.

#### Example

```code
const info = await sdk.classification.root.getBatchInfo({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456'
});
console.log('Batch Info:', info);
```

### listBatchTest()

> **listBatchTest**(`input`): `Promise`<[`IClassificationBatchListTestResponse`](../interfaces/IClassificationBatchListTestResponse.md)>

Defined in: [services/classification/classification.service.ts:308](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-308)

Lists test items uploaded to a batch.

#### Parameters

##### input

[`IClassificationBatchListTestDto`](../interfaces/IClassificationBatchListTestDto.md)

DTO with `batch_id`, pagination and sorting.

#### Returns

`Promise`<[`IClassificationBatchListTestResponse`](../interfaces/IClassificationBatchListTestResponse.md)>

List of test inputs under the batch.

#### Example

```code
const tests = await sdk.classification.root.listBatchTest({
  token: '1234567890abcdef',
  batch_id: '64b8f5f9c9f0a40abc123456',
  page_number: 0,
  page_size: 20,
  sort: 'asc'
});
console.log('Tests in batch:', tests.data);
```

### listTest()

> **listTest**(`input`): `Promise`<[`IClassificationListTestResponse`](../interfaces/IClassificationListTestResponse.md)>

Defined in: [services/classification/classification.service.ts:344](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-344)

Lists all test entries (outside batch).

#### Parameters

##### input

[`IClassificationListTestDto`](../interfaces/IClassificationListTestDto.md)

Filters like `page_number`, `page_size`, `sort`.

#### Returns

`Promise`<[`IClassificationListTestResponse`](../interfaces/IClassificationListTestResponse.md)>

List of classification tests.

#### Example

```code
const list = await sdk.classification.root.listTest({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Test list:', list.data);
```

### getResultInfo()

> **getResultInfo**(`input`): `Promise`<[`IClassificationResultInfoResponse`](../interfaces/IClassificationResultInfoResponse.md)>

Defined in: [services/classification/classification.service.ts:375](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-375)

Gets metadata and output for a specific result.

#### Parameters

##### input

[`IClassificationResultInfoDto`](../interfaces/IClassificationResultInfoDto.md)

Object with `result_id`.

#### Returns

`Promise`<[`IClassificationResultInfoResponse`](../interfaces/IClassificationResultInfoResponse.md)>

Result info with classification output.

#### Example

```code
const result = await sdk.classification.root.getResultInfo({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456'
});
console.log('Result Info:', result.output);
```

### sendFeedback()

> **sendFeedback**(`input`): `Promise`<[`IClassificationResultFeedbackResponse`](../interfaces/IClassificationResultFeedbackResponse.md)>

Defined in: [services/classification/classification.service.ts:406](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-406)

Sends manual feedback for a classification result.

#### Parameters

##### input

[`IClassificationResultFeedbackDto`](../interfaces/IClassificationResultFeedbackDto.md)

Feedback details including corrected label.

#### Returns

`Promise`<[`IClassificationResultFeedbackResponse`](../interfaces/IClassificationResultFeedbackResponse.md)>

Feedback submission result.

#### Example

```code
await sdk.classification.root.sendFeedback({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456',
  manual_classification: 'Approved',
  manual_reason: 'Corrected label by reviewer'
});
```

### downloadTest()

> **downloadTest**(`input`): `Promise`<`Readable`>

Defined in: [services/classification/classification.service.ts:440](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-440)

Downloads the original file from a test entry.

#### Parameters

##### input

[`IClassificationTestDownloadDto`](../interfaces/IClassificationTestDownloadDto.md)

Object with `test_id`.

#### Returns

`Promise`<`Readable`>

Stream of the downloaded file.

#### Example

```code
const response = await sdk.classification.root.downloadTest({
  token: '1234567890abcdef',
  test_id: '64b8f5f9c9f0a40abc123456'
});
response.pipe(fs.createWriteStream('test.pdf'));
console.log('Test downloaded to:', 'test.pdf');
```

### downloadResult()

> **downloadResult**(`input`): `Promise`<`Readable`>

Defined in: [services/classification/classification.service.ts:470](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/classification.service.ts#lines-470)

Downloads classification result output as a file.

#### Parameters

##### input

[`IClassificationResultDownloadDto`](../interfaces/IClassificationResultDownloadDto.md)

Object with `result_id`.

#### Returns

`Promise`<`Readable`>

Stream of the downloaded file.

#### Example

```code
const response = await sdk.classification.root.downloadResult({
  token: '1234567890abcdef',
  result_id: '64b8f5f9c9f0a40abc123456',
});
response.pipe(fs.createWriteStream('result.json'));
console.log('Result downloaded to:', 'result.json');
```
