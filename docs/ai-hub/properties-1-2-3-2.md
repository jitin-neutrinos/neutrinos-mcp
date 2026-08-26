# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-2>

## Properties

### _id

> **_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:104](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-104)

Unique identifier for the classification result (MongoDB ObjectId).

#### Example

```code
"64f123abc456def789012345"
```

#### Inherited from

`IClassificationSingleResponse._id`

### training_config_id

> **training_config_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:111](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-111)

ID of the training configuration used.

#### Example

```code
"64f123abc456def789012300"
```

#### Inherited from

`IClassificationSingleResponse.training_config_id`

### training_id

> **training_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:118](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-118)

ID of the training session/model used.

#### Example

```code
"64f123abc456def789012301"
```

#### Inherited from

`IClassificationSingleResponse.training_id`

### tenant_id

> **tenant_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:125](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-125)

ID of the tenant to whom this classification belongs.

#### Example

```code
"64f123abc456def789012302"
```

#### Inherited from

`IClassificationSingleResponse.tenant_id`

### deployment_id

> **deployment_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:132](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-132)

ID of the deployed model instance used.

#### Example

```code
"64f123abc456def789012303"
```

#### Inherited from

`IClassificationSingleResponse.deployment_id`

### test_id

> **test_id**: `string`

Defined in: [services/classification/dto/single.dto.ts:139](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-139)

ID of the test or evaluation task associated with this result.

#### Example

```code
"64f123abc456def789012304"
```

#### Inherited from

`IClassificationSingleResponse.test_id`

### test_type

> **test_type**: [`TestType`](../enumerations/TestType.md)

Defined in: [services/classification/dto/single.dto.ts:146](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-146)

The type of classification test (e.g., "Single", "Batch").

#### Example

```code
"Single"
```

#### Inherited from

`IClassificationSingleResponse.test_type`

### data_type

> **data_type**: [`DataType`](../enumerations/DataType.md)

Defined in: [services/classification/dto/single.dto.ts:153](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-153)

The type of input data used (e.g., "Text", "Document").

#### Example

```code
"Text"
```

#### Inherited from

`IClassificationSingleResponse.data_type`

### status

> **status**: [`Status`](../enumerations/Status.md)

Defined in: [services/classification/dto/single.dto.ts:160](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-160)

The processing status of the result.

#### Example

```code
"Completed"
```

#### Inherited from

`IClassificationSingleResponse.status`

### created_at

> **created_at**: `string`

Defined in: [services/classification/dto/single.dto.ts:167](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-167)

ISO timestamp when the result was created.

#### Example

```code
"2023-01-01T00:00:00Z"
```

#### Inherited from

`IClassificationSingleResponse.created_at`

### updated_at

> **updated_at**: `string`

Defined in: [services/classification/dto/single.dto.ts:174](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-174)

ISO timestamp when the result was last updated.

#### Example

```code
"2023-01-01T00:05:00Z"
```

#### Inherited from

`IClassificationSingleResponse.updated_at`

### processing_time

> **processing_time**: `number`

Defined in: [services/classification/dto/single.dto.ts:181](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-181)

Total processing time in milliseconds.

#### Example

```code
210
```

#### Inherited from

`IClassificationSingleResponse.processing_time`

### inference_time

> **inference_time**: `number`

Defined in: [services/classification/dto/single.dto.ts:188](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-188)

Inference time (model prediction only) in milliseconds.

#### Example

```code
98
```

#### Inherited from

`IClassificationSingleResponse.inference_time`

### output?

> `optional` **output**: [`IClassificationOutput`](IClassificationOutput.md)

Defined in: [services/classification/dto/single.dto.ts:193](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-193)

The classification result output.

#### Inherited from

`IClassificationSingleResponse.output`

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/classification/dto/single.dto.ts:204](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-204)

Optional metadata provided with the input, returned back for reference.

#### Example

```code
{
   *   "source": "api",
   *   "user_id": "u-007"
   * }
```

#### Inherited from

`IClassificationSingleResponse.metadata`

### input

> **input**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/single.dto.ts:142](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/single.dto.ts#lines-142)

The original input that was classified.

#### Example

```code
{
   *   "message": "Server down in EU region",
   *   "severity": "high"
   * }
```
