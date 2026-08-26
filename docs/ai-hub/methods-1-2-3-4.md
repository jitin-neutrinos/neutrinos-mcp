# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1-2-3-4>

## Methods

### listEmbeddings()

> **listEmbeddings**(`input`): `Promise`<[`IEmbeddingListResponse`](../interfaces/IEmbeddingListResponse.md)>

Defined in: [services/assistant/embedding/embedding.service.ts:107](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/embedding/embedding.service.ts#lines-107)

Lists embeddings for a knowledge source.

#### Parameters

##### input

[`IEmbeddingListDto`](../interfaces/IEmbeddingListDto.md)

The input data for listing embeddings.

#### Returns

`Promise`<[`IEmbeddingListResponse`](../interfaces/IEmbeddingListResponse.md)>

A promise that resolves to the list of embeddings.

#### Example

```code
const embeddings = await sdk.assistant.embed.listEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
  search: 'hello world',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
});
```

### addEmbeddings()

> **addEmbeddings**(`input`): `Promise`<[`IEmbeddingAddResponse`](../interfaces/IEmbeddingAddResponse.md)>

Defined in: [services/assistant/embedding/embedding.service.ts:138](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/embedding/embedding.service.ts#lines-138)

Adds embeddings for a knowledge source.

#### Parameters

##### input

[`IEmbeddingAddDto`](../interfaces/IEmbeddingAddDto.md)

The input data for adding embeddings.

#### Returns

`Promise`<[`IEmbeddingAddResponse`](../interfaces/IEmbeddingAddResponse.md)>

A promise that resolves to the response of adding embeddings.

#### Example

```code
const response = await sdk.assistant.embed.addEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
  items: ['hello world', 'hello world 2', 'hello world 3'],
});
```

### updateEmbeddings()

> **updateEmbeddings**(`input`): `Promise`<[`IEmbeddingUpdateResponse`](../interfaces/IEmbeddingUpdateResponse.md)>

Defined in: [services/assistant/embedding/embedding.service.ts:177](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/embedding/embedding.service.ts#lines-177)

Updates embeddings for a knowledge source.

#### Parameters

##### input

[`IEmbeddingUpdateDto`](../interfaces/IEmbeddingUpdateDto.md)

The input data for updating embeddings.

#### Returns

`Promise`<[`IEmbeddingUpdateResponse`](../interfaces/IEmbeddingUpdateResponse.md)>

A promise that resolves to the response of updating embeddings.

#### Example

```code
const response = await sdk.assistant.embed.updateEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
  items: [
    {
      id: '6543210987654321',
      text: 'hello world',
    },
    {
      id: '6543210987654322',
      text: 'hello world 2',
    },
  ],
});
```

### deleteEmbeddings()

> **deleteEmbeddings**(`input`): `Promise`<[`IEmbeddingDeleteResponse`](../interfaces/IEmbeddingDeleteResponse.md)>

Defined in: [services/assistant/embedding/embedding.service.ts:207](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/embedding/embedding.service.ts#lines-207)

Deletes embeddings for a knowledge source.

#### Parameters

##### input

[`IEmbeddingDeleteDto`](../interfaces/IEmbeddingDeleteDto.md)

The input data for deleting embeddings.

#### Returns

`Promise`<[`IEmbeddingDeleteResponse`](../interfaces/IEmbeddingDeleteResponse.md)>

A promise that resolves to the response of deleting embeddings.

#### Example

```code
const response = await sdk.assistant.embed.deleteEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
  items: ['6543210987654321', '6543210987654322'],
});
```

### deleteAllEmbeddings()

> **deleteAllEmbeddings**(`input`): `Promise`<[`IEmbeddingDeleteAllResponse`](../interfaces/IEmbeddingDeleteAllResponse.md)>

Defined in: [services/assistant/embedding/embedding.service.ts:236](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/embedding/embedding.service.ts#lines-236)

Deletes all embeddings for a knowledge source.

#### Parameters

##### input

[`IEmbeddingDeleteAllDto`](../interfaces/IEmbeddingDeleteAllDto.md)

The input data for deleting all embeddings.

#### Returns

`Promise`<[`IEmbeddingDeleteAllResponse`](../interfaces/IEmbeddingDeleteAllResponse.md)>

A promise that resolves to the response of deleting all embeddings.

#### Example

```code
const response = await sdk.assistant.embed.deleteAllEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
});
```
