# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-4>

## Properties

### text

> **text**: `string`

Defined in: [services/extraction/text/dto/output.dto.ts:25](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/output.dto.ts#lines-25)

The original text that was processed.

#### Example

```code
"John Doe works at Acme Corp in New York."
```

### entities?

> `optional` **entities**: [`ITextEntity`](ITextEntity.md)[]

Defined in: [services/extraction/text/dto/output.dto.ts:30](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/output.dto.ts#lines-30)

Array of entities found in the text.

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/extraction/text/dto/output.dto.ts:35](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/output.dto.ts#lines-35)

Additional metadata about the extraction.
