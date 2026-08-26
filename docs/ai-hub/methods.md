# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods>

## Methods

### createBatch()

> **createBatch**(`input`): `Promise`<[`IClassificationDocCreateBatchResponse`](../interfaces/IClassificationDocCreateBatchResponse.md)>

Defined in: [services/classification/doc/classification-doc.service.ts:129](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/classification-doc.service.ts#lines-129)

Creates a new classification batch for document-based input.

#### Parameters

##### input

[`IClassificationDocCreateBatchDto`](../interfaces/IClassificationDocCreateBatchDto.md)

Batch creation payload including optional callback URL and metadata.

#### Returns

`Promise`<[`IClassificationDocCreateBatchResponse`](../interfaces/IClassificationDocCreateBatchResponse.md)>

Created batch metadata.

#### Example

```code
const batch = await sdk.classification.doc.createBatch({
  token: '1234567890abcdef',
  callback_url: 'https://example.com/callback',
  metadata: { team: 'QA', project: 'invoice-analysis' },
  group_callback_url: 'https://example.com/group-callback'
});
```

### startSingle()

> **startSingle**(`input`): `Promise`<[`IClassificationDocSingleResponse`](../interfaces/IClassificationDocSingleResponse.md)[]>

Defined in: [services/classification/doc/classification-doc.service.ts:173](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/classification-doc.service.ts#lines-173)

Classifies a single document using either file path or file ID.

#### Parameters

##### input

[`IClassificationDocSingleDto`](../interfaces/IClassificationDocSingleDto.md)

Classification input containing `file_path` or `file_id`, plus optional metadata.

#### Returns

`Promise`<[`IClassificationDocSingleResponse`](../interfaces/IClassificationDocSingleResponse.md)[]>

List of classification results for the document.

#### Throws

If neither `file_path` nor `file_id` is provided.

#### Throws

If the file at `file_path` does not exist.

#### Example

```code
const result = await sdk.classification.doc.startSingle({
  token: '1234567890abcdef',
  file_path: '/documents/contract.pdf',
  metadata: { source: 'legal' },
  file_buffer: {
    fieldname: 'file',
    originalname: 'contract.pdf',
    encoding: '7bit',
    mimetype: 'application/pdf',
    buffer: Buffer.from('file content'),
    size: 1048576
  }
});
```

### listResults()

> **listResults**(`input`): `Promise`<[`IClassificationDocListResultsResponse`](../interfaces/IClassificationDocListResultsResponse.md)>

Defined in: [services/classification/doc/classification-doc.service.ts:244](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/classification-doc.service.ts#lines-244)

Retrieves a paginated list of classification results for documents.

Supports optional merging of results based on test ID grouping configuration.

#### Parameters

##### input

[`IClassificationDocListResultsDto`](../interfaces/IClassificationDocListResultsDto.md)

Pagination, sort, and merge flags.

#### Returns

`Promise`<[`IClassificationDocListResultsResponse`](../interfaces/IClassificationDocListResultsResponse.md)>

Paginated classification results with metadata.

#### Example

```code
const results = await sdk.classification.doc.listResults({
  token: '1234567890abcdef',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
  merged: true
});
console.log('Results:', results.data);
```
