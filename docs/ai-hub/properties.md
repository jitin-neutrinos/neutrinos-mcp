# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties>

## Properties

### config

> `readonly` **config**: [`ISDKConfig`](../interfaces/ISDKConfig.md)

Defined in: [sdk-client.ts:61](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-61)

The fully resolved configuration object used throughout the SDK.

### classification

> `readonly` **classification**: `object`

Defined in: [sdk-client.ts:76](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-76)

Provides access to classification functionality.

- `root`: Low-level access to classification APIs
- `text`: Run classification on plain text
- `doc`: Run classification on documents (PDF, image, etc.)

#### root

> **root**: [`ClassificationService`](/articles/ai-hub/classificationservice)

#### text

> **text**: [`ClassificationTextService`](/articles/ai-hub/classificationtextservice)

#### doc

> **doc**: [`ClassificationDocService`](/articles/ai-hub/classificationdocservice)

### extraction

> `readonly` **extraction**: `object`

Defined in: [sdk-client.ts:89](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-89)

Provides access to extraction functionality.

- `root`: Low-level access to extraction APIs
- `text`: Run extraction on plain text
- `doc`: Run extraction on documents (PDF, image, etc.)

#### doc

> **doc**: [`ExtractionDocService`](/articles/ai-hub/extractiondocservice)

#### text

> **text**: [`TextExtractionService`](/articles/ai-hub/textextractionservice)

### assistant

> `readonly` **assistant**: `object`

Defined in: [sdk-client.ts:102](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-102)

Provides access to assistant functionality.

- `root`: General-purpose assistant features
- `knowledge`: Knowledge-enhanced assistant (Q&A, retrieval, etc.)
- `embed`: Embedding service

#### root

> **root**: [`ConversationService`](/articles/ai-hub/conversationservice)

#### message

> **message**: [`MessageService`](/articles/ai-hub/messageservice)

#### knowledge

> **knowledge**: [`KnowledgeService`](/articles/ai-hub/knowledgeservice)

#### embed

> **embed**: [`EmbeddingService`](/articles/ai-hub/embeddingservice)

### file

> `readonly` **file**: `object`

Defined in: [sdk-client.ts:114](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-114)

Provides access to file management features.

- `root`: File upload, download, listing, and deletion

#### root

> **root**: [`FileService`](/articles/ai-hub/fileservice)

### model

> `readonly` **model**: `object`

Defined in: [sdk-client.ts:123](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-123)

Provides access to model catalog functionality.

- `root`: Model catalog features (list, version, token)

#### root

> **root**: [`ModelCatalogService`](/articles/ai-hub/modelcatalogservice)
