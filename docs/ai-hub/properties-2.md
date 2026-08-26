# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-2>

## Properties

### token

> **token**: `string`

Defined in: [services/classification/dto/start-batch.dto.ts:41](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/start-batch.dto.ts#lines-41)

API token for authentication.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### batch_id

> **batch_id**: `string`

Defined in: [services/classification/dto/start-batch.dto.ts:49](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/start-batch.dto.ts#lines-49)

The ID of the batch to classify.
 Must be a valid MongoDB ObjectId.

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

#### Overrides

`z.infer.batch_id`

### batch_size

> **batch_size**: `number`

Defined in: [services/classification/dto/start-batch.dto.ts:58](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/start-batch.dto.ts#lines-58)

Number of items to process in each sub-task (chunk).

Used to split the batch into smaller parallel jobs. A higher value processes more items per task.

#### Example

```code
10
```

#### Overrides

`z.infer.batch_size`
