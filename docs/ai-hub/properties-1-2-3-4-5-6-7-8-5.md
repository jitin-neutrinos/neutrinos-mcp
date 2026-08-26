# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-7-8-5>

## Properties

### token

> **token**: `string`

Defined in: [services/extraction/text/dto/start-batch.dto.ts:41](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/start-batch.dto.ts#lines-41)

Authentication token for API access.

#### Example

```code
"1234567890abcdef"
```

#### Overrides

`z.infer.token`

### batch_id

> **batch_id**: `string`

Defined in: [services/extraction/text/dto/start-batch.dto.ts:49](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/start-batch.dto.ts#lines-49)

The ID of the batch to extract.
Must be a valid MongoDB ObjectId.

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

#### Overrides

`z.infer.batch_id`

### batch_size

> **batch_size**: `number`

Defined in: [services/extraction/text/dto/start-batch.dto.ts:58](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/start-batch.dto.ts#lines-58)

Number of items to process in each sub-task (chunk).

Used to split the batch into smaller parallel jobs.

#### Example

```code
10
```

#### Overrides

`z.infer.batch_size`
