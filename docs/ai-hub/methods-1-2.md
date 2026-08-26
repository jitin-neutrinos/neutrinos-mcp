# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1-2>

## Methods

### createBatch()

> **createBatch**(`input`): `Promise`<[`IClassificationTextCreateBatchResponse`](../interfaces/IClassificationTextCreateBatchResponse.md)>

Defined in: [services/classification/text/classification-text.service.ts:111](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/classification-text.service.ts#lines-111)

Creates a new classification batch.

This is commonly used to prepare a batch before uploading multiple JSON/text entries.

#### Parameters

##### input

[`IClassificationTextCreateBatchDto`](../interfaces/IClassificationTextCreateBatchDto.md)

Metadata and configuration for the batch.

#### Returns

`Promise`<[`IClassificationTextCreateBatchResponse`](../interfaces/IClassificationTextCreateBatchResponse.md)>

Batch creation response.

#### Example

```code
const batch = await sdk.classification.text.createBatch({
  token: '1234567890abcdef',
  is_file: false,
  metadata: { dataset: 'survey-2024' }
});
```

### insertToBatch()

> **insertToBatch**(`payload`): `Promise`<[`IClassificationTextInsertToBatchResponse`](../interfaces/IClassificationTextInsertToBatchResponse.md)[]>

Defined in: [services/classification/text/classification-text.service.ts:151](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/classification-text.service.ts#lines-151)

Inserts one or more structured JSON/text inputs into an existing batch.

Each entry may contain optional `ground_truth` for supervised learning or testing.

#### Parameters

##### payload

[`IClassificationTextInsertToBatchDto`](../interfaces/IClassificationTextInsertToBatchDto.md)

Batch ID and array of input entries.

#### Returns

`Promise`<[`IClassificationTextInsertToBatchResponse`](../interfaces/IClassificationTextInsertToBatchResponse.md)[]>

An array of inserted input metadata.

#### Example

```code
await sdk.classification.text.insertToBatch({
  token: '1234567890abcdef',
  batch_id: '64f123abc456def789012345',
  input: [
    {
      data: { text: 'This item arrived late.' },
      ground_truth: 'complaint'
    },
    {
      data: { text: 'Can I return this product?' }
    }
  ]
});
```

### startSingle()

> **startSingle**(`input`): `Promise`<[`IClassificationTextSingleResponse`](../interfaces/IClassificationTextSingleResponse.md)>

Defined in: [services/classification/text/classification-text.service.ts:190](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/classification-text.service.ts#lines-190)

Performs real-time classification on a single JSON/text input.

This is used when you want an instant classification result without batch management.

#### Parameters

##### input

[`IClassificationTextSingleDto`](../interfaces/IClassificationTextSingleDto.md)

Raw input data and optional metadata.

#### Returns

`Promise`<[`IClassificationTextSingleResponse`](../interfaces/IClassificationTextSingleResponse.md)>

Classification result for the input.

#### Example

```code
const result = await sdk.classification.text.startSingle({
  token: '1234567890abcdef',
  input: {
    message: 'I need a refund for this product'
  },
  metadata: {
    customer_id: 'cust-001',
    channel: 'email'
  }
});
```

### listResults()

> **listResults**(`input`): `Promise`<[`IClassificationTextListResultsResponse`](../interfaces/IClassificationTextListResultsResponse.md)>

Defined in: [services/classification/text/classification-text.service.ts:225](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/classification-text.service.ts#lines-225)

Retrieves a paginated list of classification results for a given test ID.

Sorting and pagination options are available, and `test_id` is required.

#### Parameters

##### input

[`IClassificationTextListResultsDto`](../interfaces/IClassificationTextListResultsDto.md)

Pagination and sorting config.

#### Returns

`Promise`<[`IClassificationTextListResultsResponse`](../interfaces/IClassificationTextListResultsResponse.md)>

List of classification results for the given test.

#### Example

```code
const response = await sdk.classification.text.listResults({
  token: '1234567890abcdef',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 20,
  sort: 'asc'
});
console.log(response.data);
```
