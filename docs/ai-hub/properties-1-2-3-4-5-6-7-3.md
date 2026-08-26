# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-7-3>

## Properties

### token

> **token**: `string`

Defined in: [services/extraction/doc/dto/result-feedback.dto.ts:70](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/result-feedback.dto.ts#lines-70)

Authentication token for API access.

#### Example

```code
"1234567890abcdef"
```

#### Overrides

`z.infer.token`

### result_id

> **result_id**: `string`

Defined in: [services/extraction/doc/dto/result-feedback.dto.ts:79](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/result-feedback.dto.ts#lines-79)

The unique identifier of the result being reviewed.

Must be a valid MongoDB ObjectId.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ab"
```

#### Overrides

`z.infer.result_id`

### manual_extraction

> **manual_extraction**: `Record`<`string`, `any`>

Defined in: [services/extraction/doc/dto/result-feedback.dto.ts:92](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/result-feedback.dto.ts#lines-92)

Manually assigned extraction label.
Typically used to correct or validate model predictions.

#### Example

```code
{
  "Technology": "2023-01-01"
}
```

#### Overrides

`z.infer.manual_extraction`

### manual_reason

> **manual_reason**: `string`

Defined in: [services/extraction/doc/dto/result-feedback.dto.ts:100](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/result-feedback.dto.ts#lines-100)

Reasoning behind the manual extraction decision.
Helps auditors or reviewers understand the human input.

#### Example

```code
"The document discusses machine learning innovations."
```

#### Overrides

`z.infer.manual_reason`
