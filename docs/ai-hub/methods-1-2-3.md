# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1-2-3>

## Methods

### createConversation()

> **createConversation**(`input`): `Promise`<[`IConversation`](../interfaces/IConversation.md)>

Defined in: [services/assistant/conversation/conversation.service.ts:112](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/conversation/conversation.service.ts#lines-112)

Creates a single assistant conversation.

#### Parameters

##### input

[`ICreateConversationDto`](../interfaces/ICreateConversationDto.md)

Metadata and optional translation flag.

#### Returns

`Promise`<[`IConversation`](../interfaces/IConversation.md)>

The created conversation details.

#### Example

```code
const convo = await sdk.assistant.conversation.create({
  token: '1234567890abcdef',
  metadata: { source: 'bot', channel: 'web' },
  translation_enabled: true
});
```

### createBatch()

> **createBatch**(`input`): `Promise`<[`IConversation`](../interfaces/IConversation.md)>

Defined in: [services/assistant/conversation/conversation.service.ts:136](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/conversation/conversation.service.ts#lines-136)

Creates a batch of conversations with optional callback support.

#### Parameters

##### input

[`ICreateBatchConversationDto`](../interfaces/ICreateBatchConversationDto.md)

Batch metadata and callback configuration.

#### Returns

`Promise`<[`IConversation`](../interfaces/IConversation.md)>

Metadata of the created batch conversation.

#### Example

```code
const batch = await sdk.assistant.conversation.createBatch({
  token: '1234567890abcdef',
  metadata: { use_case: 'bulk-import' },
  callback_url: 'https://hooks.example.com/callback'
});
```

### startBatch()

> **startBatch**(`input`): `Promise`<[`IStartConversationBatchResponse`](../interfaces/IStartConversationBatchResponse.md)>

Defined in: [services/assistant/conversation/conversation.service.ts:159](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/conversation/conversation.service.ts#lines-159)

Starts a conversation batch.

#### Parameters

##### input

[`IConversationIdDto`](../interfaces/IConversationIdDto.md)

Conversation ID of the batch to be started.

#### Returns

`Promise`<[`IStartConversationBatchResponse`](../interfaces/IStartConversationBatchResponse.md)>

Task ID and status message.

#### Example

```code
const started = await sdk.assistant.conversation.startBatch({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8'
});
```

### getBatchInfo()

> **getBatchInfo**(`input`): `Promise`<[`IConversation`](../interfaces/IConversation.md)>

Defined in: [services/assistant/conversation/conversation.service.ts:186](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/conversation/conversation.service.ts#lines-186)

Retrieves metadata and status of a specific batch conversation.

#### Parameters

##### input

[`IConversationIdDto`](../interfaces/IConversationIdDto.md)

Conversation ID of the batch to fetch.

#### Returns

`Promise`<[`IConversation`](../interfaces/IConversation.md)>

Detailed batch information.

#### Example

```code
const info = await sdk.assistant.conversation.getBatchInfo({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8'
});
```

### reviewConversation()

> **reviewConversation**(`input`): `Promise`<[`IReviewConversation`](../interfaces/IReviewConversation.md)>

Defined in: [services/assistant/conversation/conversation.service.ts:221](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/conversation/conversation.service.ts#lines-221)

Reviews a conversation.

#### Parameters

##### input

[`IReviewConversationDto`](../interfaces/IReviewConversationDto.md)

Conversation ID of the conversation to review.

#### Returns

`Promise`<[`IReviewConversation`](../interfaces/IReviewConversation.md)>

The reviewed conversation details.

#### Example

```code
const reviewed = await sdk.assistant.conversation.reviewConversation({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8',
  review_status: 'Pending',
  messages: [
    {
      message_id: '6863b5492c8e9444541d60c8',
      is_positive: true,
      comment: 'This message is positive'
    }
  ]
});
```
