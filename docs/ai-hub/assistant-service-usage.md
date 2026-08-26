# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/assistant-service-usage>

This guide provides examples of how to use the Assistant Service methods in the IDP Inference SDK. These methods support message handling, file processing, batch operations, and audio transcription in assistant conversations.

## Table of Methods with API Links

| **Method Name  ** | **  API Endpoint  ** | **  API Docs Link** |
| --- | --- | --- |
| [`createBatch`](/articles/ai-hub/assistant-service-usage/a/creating-a-batch) | `/assistant/conversation/create/batch` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ConversationService.md#createbatch) |
| [`uploadBatchMessage`](/articles/ai-hub/assistant-service-usage/a/uploading-batch-message) | `/assistant/message/upload/batch` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/MessageService.md#uploadbatchmessage) |
| [`startBatch`](/articles/ai-hub/assistant-service-usage/a/starting-batch) | `/assistant/conversation/batch/start/:id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ConversationService.md#startbatch) |
| [`getBatchInfo`](/articles/ai-hub/assistant-service-usage/a/getting-batch-info) | `/assistant/conversation/batch/find/:id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/MessageService.md#getbatchinfo) |
| [`listMessages`](/articles/ai-hub/assistant-service-usage/a/listing-messages) | `/assistant/message/find-all/:id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/MessageService.md#listmessages) |
| [`createConversation`](/articles/ai-hub/assistant-service-usage/a/creating-a-conversation) | `/assistant/conversation/create` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ConversationService.md#createconversation) |
| [`createMessage`](/articles/ai-hub/assistant-service-usage/a/creating-a-message) | `/assistant/message/create` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/MessageService.md#createmessage) |
| [`transcribeAudio`](/articles/ai-hub/assistant-service-usage/a/transcribing-voice-message) | `/assistant/message/transcribe` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/MessageService.md#transcribeaudio) |
| [`listKnowledgeSources`](/articles/ai-hub/assistant-service-usage/a/listing-knowledge-sources) | `/assistant/knowledge/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/KnowledgeService.md#listknowledgesources) |
| [`addEmbeddings`](/articles/ai-hub/assistant-service-usage/a/adding-embeddings) | `/assistant/embed/add` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/EmbeddingService.md#addembeddings) |
| [`updateEmbeddings`](/articles/ai-hub/assistant-service-usage/a/updating-embeddings) | `/assistant/embed/update` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/EmbeddingService.md#updateembeddings) |
| [`deleteEmbeddings`](/articles/ai-hub/assistant-service-usage/a/deleting-embeddings) | `/assistant/embed/delete` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/EmbeddingService.md#deleteembeddings) |
| [`listEmbeddings`](/articles/ai-hub/assistant-service-usage/a/listing-embeddings) | `/assistant/embed/list` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/EmbeddingService.md#listembeddings) |
| [`deleteAllEmbeddings`](/articles/ai-hub/assistant-service-usage/a/deleting-all-embeddings) | `/assistant/embed/delete-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/EmbeddingService.md#deleteallembeddings) |
| [`reviewConversation`](/articles/ai-hub/assistant-service-usage/a/review-conversation) | `/assistant/conversation/review/:id` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ConversationService.md#reviewconversation) |

## Creating a Batch

To create a new batch conversation:

**TypeScript**

```code
import { ICreateBatchConversationDto } from '@neutrinos/idp-inference-sdk';

const requestBody: ICreateBatchConversationDto = {
  token: 'your-auth-token',
  translation_enabled: true,
  metadata: {},
  callback_url: 'https://hooks.example.com/notify',
};

try {
  const result = await sdk.assistant.root.createBatch(requestBody);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

**JavaScript**

```code
const requestBody = {
  token: 'your-auth-token',
  translation_enabled: true,
  metadata: {},
  callback_url: 'https://hooks.example.com/notify',
};

try {
  const result = await sdk.assistant.root.createBatch(requestBody);
  console.log('Batch created:', result);
} catch (error) {
  console.error('Error creating batch:', error);
}
```

## Uploading Batch Message

To upload a message to a batch conversation:

**TypeScript**

```code
import { IUploadBatchMessageDto } from '@neutrinos/idp-inference-sdk';

const batchDto: IUploadBatchMessageDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  text: 'Hello!',
  file_ids: ['file-id-1', 'file-id-2'],
  metadata: {},
};

try {
  const result = await sdk.assistant.message.uploadBatchMessage(batchDto);
  console.log('Batch message uploaded:', result);
} catch (error) {
  console.error('Error uploading message to batch:', error);
}
```

**JavaScript**

```code
const batchDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  text: 'Hello!',
  file_ids: ['file-id-1', 'file-id-2'],
  metadata: {},
};

try {
  const result = await sdk.assistant.message.uploadBatchMessage(batchDto);
  console.log('Batch message uploaded:', result);
} catch (error) {
  console.error('Error uploading message to batch:', error);
}
```

## Starting Batch

Once all required data has been added to the batch, you can start the batch conversation:

**TypeScript**

```code
import { IConversationIdDto } from '@neutrinos/idp-inference-sdk';

const batchDto: IConversationIdDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
};

try {
  const started = await sdk.assistant.root.startBatch(batchDto);
  console.log('Batch started:', started);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

**JavaScript**

```code
const batchDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
};

try {
  const started = await sdk.assistant.root.startBatch(batchDto);
  console.log('Batch started:', started);
} catch (error) {
  console.error('Error starting batch:', error);
}
```

## Getting Batch Info

To get information on a specific batch conversation:

**TypeScript**

```code
import { IConversationIdDto } from '@neutrinos/idp-inference-sdk';

const batchDto: IConversationIdDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
};

try {
  const batchInfo = await sdk.assistant.root.getBatchInfo(batchDto);
  console.log('Batch info:', batchInfo);
} catch (error) {
  console.error('Error getting batch info:', error);
}
```

**JavaScript**

```code
const batchDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
};

try {
  const batchInfo = await sdk.assistant.root.getBatchInfo(batchDto);
  console.log('Batch info:', batchInfo);
} catch (error) {
  console.error('Error getting batch info:', error);
}
```

## Listing Messages

To list all messages for a specific conversation:

**TypeScript**

```code
import { IListMessagesDto } from '@neutrinos/idp-inference-sdk';

const listDto: IListMessagesDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  page_size: 10,
  page_number: 0,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.message.listMessages(listDto);
  console.log('Message list:', result);
} catch (error) {
  console.error('Error listing messages:', error);
}
```

**JavaScript**

```code
const listDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  page_size: 10,
  page_number: 0,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.message.listMessages(listDto);
  console.log('Message list:', result);
} catch (error) {
  console.error('Error listing messages:', error);
}
```

## Creating a Conversation

To create a new conversation:

**TypeScript**

```code
import { ICreateConversationDto } from '@neutrinos/idp-inference-sdk';

const requestBody: ICreateConversationDto = {
  token: 'your-auth-token',
  translation_enabled: false,
  metadata: {},
};

try {
  const result = await sdk.assistant.root.createConversation(requestBody);
  console.log('Conversation created:', result);
} catch (error) {
  console.error('Error creating conversation:', error);
}
```

**JavaScript**

```code
const requestBody = {
  token: 'your-auth-token',
  translation_enabled: false,
  metadata: {},
};

try {
  const result = await sdk.assistant.root.createConversation(requestBody);
  console.log('Conversation created:', result);
} catch (error) {
  console.error('Error creating conversation:', error);
}
```

## Creating a Message

To create a new message in a conversation:

**TypeScript**

```code
import { ICreateMessageDto } from '@neutrinos/idp-inference-sdk';

const requestBody: ICreateMessageDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  text: 'Hello!',
  file_path: '/path/to/file.pdf',
  metadata: {},
};

try {
  const result = await sdk.assistant.message.createMessage(requestBody);
  console.log('Message created:', result);
} catch (error) {
  console.error('Error creating message:', error);
}
```

**JavaScript**

```code
const requestBody = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  text: 'Hello!',
  file_path: '/path/to/file.pdf',
  metadata: {},
};

try {
  const result = await sdk.assistant.message.createMessage(requestBody);
  console.log('Message created:', result);
} catch (error) {
  console.error('Error creating message:', error);
}
```

## Transcribing Voice Message

To transcribe a voice message in a conversation:

**TypeScript**

```code
import { ITranscribeAudioDto } from '@neutrinos/idp-inference-sdk';

const transcribeDto: ITranscribeAudioDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  file_path: '/path/to/audio.wav',
};

try {
  const result = await sdk.assistant.message.transcribeAudio(transcribeDto);
  console.log('Transcription result:', result);
} catch (error) {
  console.error('Error transcribing voice:', error);
}
```

**JavaScript**

```code
const transcribeDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  file_path: '/path/to/audio.wav',
};

try {
  const result = await sdk.assistant.message.transcribeAudio(transcribeDto);
  console.log('Transcription result:', result);
} catch (error) {
  console.error('Error transcribing voice:', error);
}
```

## Listing Knowledge Sources

To retrieve a paginated list of knowledge sources:

**TypeScript**

```code
import { IPaginateDto } from '@neutrinos/idp-inference-sdk';

const paginateDto: IPaginateDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.knowledge.listSources(paginateDto);
  console.log('Knowledge sources:', result);
} catch (error) {
  console.error('Error listing knowledge sources:', error);
}
```

**JavaScript**

```code
const paginateDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.knowledge.listSources(paginateDto);
  console.log('Knowledge sources:', result);
} catch (error) {
  console.error('Error listing knowledge sources:', error);
}
```

## Adding Embeddings

To add embeddings for a knowledge source:

**TypeScript**

```code
import { IEmbeddingAddDto } from '@neutrinos/idp-inference-sdk';

const addEmbeddingsDto: IEmbeddingAddDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: ['hello world', 'hello world 2', 'hello world 3'],
};

try {
  const result = await sdk.assistant.embed.addEmbeddings(addEmbeddingsDto);
  console.log('Embeddings added:', result);
} catch (error) {
  console.error('Error adding embeddings:', error);
}
```

**JavaScript**

```code
const addEmbeddingsDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: ['hello world', 'hello world 2', 'hello world 3'],
};

try {
  const result = await sdk.assistant.embed.addEmbeddings(addEmbeddingsDto);
  console.log('Embeddings added:', result);
} catch (error) {
  console.error('Error adding embeddings:', error);
}
```

## Updating Embeddings

To update embeddings for a knowledge source:

**TypeScript**

```code
import { IEmbeddingUpdateDto } from '@neutrinos/idp-inference-sdk';

const updateEmbeddingsDto: IEmbeddingUpdateDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: [
    {
      id: 'embedding-id',
      text: 'hello world',
    },
    {
      id: 'embedding-id-2',
      text: 'hello world 2',
    },
    {
      id: 'embedding-id-3',
      text: 'hello world 3',
    },
  ],
};

try {
  const result = await sdk.assistant.embed.updateEmbeddings(updateEmbeddingsDto);
  console.log('Embeddings updated:', result);
} catch (error) {
  console.error('Error updating embeddings:', error);
}
```

**JavaScript**

```code
const updateEmbeddingsDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: [
    {
      id: 'embedding-id',
      text: 'hello world',
    },
    {
      id: 'embedding-id-2',
      text: 'hello world 2',
    },
    {
      id: 'embedding-id-3',
      text: 'hello world 3',
    },
  ],
};

try {
  const result = await sdk.assistant.embed.updateEmbeddings(updateEmbeddingsDto);
  console.log('Embeddings updated:', result);
} catch (error) {
  console.error('Error updating embeddings:', error);
}
```

## Deleting Embeddings

To delete embeddings for a knowledge source:

**TypeScript**

```code
import { IEmbeddingDeleteDto } from '@neutrinos/idp-inference-sdk';

const deleteEmbeddingsDto: IEmbeddingDeleteDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: ['embedding-id', 'embedding-id-2', 'embedding-id-3'],
};

try {
  const result = await sdk.assistant.embed.deleteEmbeddings(deleteEmbeddingsDto);
  console.log('Embeddings deleted:', result);
} catch (error) {
  console.error('Error deleting embeddings:', error);
}
```

**JavaScript**

```code
const deleteEmbeddingsDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  items: ['embedding-id', 'embedding-id-2', 'embedding-id-3'],
};

try {
  const result = await sdk.assistant.embed.deleteEmbeddings(deleteEmbeddingsDto);
  console.log('Embeddings deleted:', result);
} catch (error) {
  console.error('Error deleting embeddings:', error);
}
```

## Listing Embeddings

To list embeddings for a knowledge source:

**TypeScript**

```code
import { IEmbeddingListDto } from '@neutrinos/idp-inference-sdk';

const listEmbeddingsDto: IEmbeddingListDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  search: 'search-query',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.embed.listEmbeddings(listEmbeddingsDto);
  console.log('Embeddings:', result);
} catch (error) {
  console.error('Error listing embeddings:', error);
}
```

**JavaScript**

```code
const listEmbeddingsDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
  search: 'search-query',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.assistant.embed.listEmbeddings(listEmbeddingsDto);
  console.log('Embeddings:', result);
} catch (error) {
  console.error('Error listing embeddings:', error);
}
```

## Deleting all embeddings

To delete all embeddings for a knowledge source:

**TypeScript**

```code
import { IEmbeddingDeleteAllDto } from '@neutrinos/idp-inference-sdk';

const deleteAllEmbeddingsDto: IEmbeddingDeleteAllDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
};

try {
  const result = await sdk.assistant.embed.deleteAllEmbeddings(deleteAllEmbeddingsDto);
  console.log('Embeddings deleted:', result);
} catch (error) {
  console.error('Error deleting embeddings:', error);
}
```

**JavaScript**

```code
const deleteAllEmbeddingsDto = {
  token: 'your-auth-token',
  source_id: 'knowledge-source-id',
};

try {
  const result = await sdk.assistant.embed.deleteAllEmbeddings(deleteAllEmbeddingsDto);
  console.log('Embeddings deleted:', result);
} catch (error) {
  console.error('Error deleting embeddings:', error);
}
```

## Review Conversation

To review a conversation, use the `reviewConversation` method. This method lets you set a review status and add per-message feedback, such as marking a message as positive or negative with comments.

**TypeScript**

```code
import { IReviewConversationDto, ReviewStatusEnum } from '@neutrinos/idp-inference-sdk';

const reviewDto: IReviewConversationDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  review_status: ReviewStatusEnum.Pending, // or Verified, Skipped, Ignored
  messages: [
    {
      message_id: 'message-id-1',
      is_positive: true,
      comment: 'This message was helpful.',
    },
    {
      message_id: 'message-id-2',
      is_positive: false,
      comment: 'This message was incorrect.',
    },
  ],
};

try {
  const result = await sdk.assistant.root.reviewConversation(reviewDto);
  console.log('Conversation reviewed:', result);
} catch (error) {
  console.error('Error reviewing conversation:', error);
}
```

**JavaScript**

```code
const { ReviewStatusEnum } = require('@neutrinos/idp-inference-sdk');

const reviewDto = {
  token: 'your-auth-token',
  conversation_id: 'conversation-id',
  review_status: ReviewStatusEnum.Pending, // or Verified, Skipped, Ignored
  messages: [
    {
      message_id: 'message-id-1',
      is_positive: true,
      comment: 'This message was helpful.',
    },
    {
      message_id: 'message-id-2',
      is_positive: false,
      comment: 'This message was incorrect.',
    },
  ],
};

try {
  const result = await sdk.assistant.root.reviewConversation(reviewDto);
  console.log('Conversation reviewed:', result);
} catch (error) {
  console.error('Error reviewing conversation:', error);
}
```

**API Reference:**


 [API Docs - reviewConversation](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ConversationService.md#reviewconversation)
