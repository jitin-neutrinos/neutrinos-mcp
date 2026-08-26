# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-7-5>

## Properties

### _id

> **_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:241](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-241)

Unique ID of the inserted input record.

#### Example

```code
"64c143fbe9c3213e4f90cde3"
```

### training_config_id

> **training_config_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:248](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-248)

ID of the training configuration used for this batch.

#### Example

```code
"64c1401aebf02c76ef098cde"
```

### training_id

> **training_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:255](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-255)

Training run ID associated with this record.

#### Example

```code
"64c141c3f10cdb7a28e93bfa"
```

### tenant_id

> **tenant_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:262](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-262)

Tenant ID (multi-tenant context).

#### Example

```code
"64c1428ef8a8e67be21c2a12"
```

### deployment_id

> **deployment_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:269](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-269)

Deployment environment or version ID.

#### Example

```code
"64c143c7f56b97b82dd233ff"
```

### test_type

> **test_type**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:276](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-276)

Type of test this record belongs to.

#### Example

```code
"batch"
```

### data_type

> **data_type**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:283](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-283)

Type of input data (always "text" for this DTO).

#### Example

```code
"text"
```

### status

> **status**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:290](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-290)

Current processing status of the record.

#### Example

```code
"Created"
```

### batch_id

> **batch_id**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:297](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-297)

The ID of the batch this record was inserted into.

#### Example

```code
"64c13f63e85f3e6a4c1f8f99"
```

### input

> **input**: `object`[]

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:312](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-312)

Original input content and optional ground truth label.

#### text

> **text**: `string`

The raw input text submitted.

##### Example

```code
"Delayed shipment"
```

#### ground_truth?

> `optional` **ground_truth**: `Record`<`string`, `object`[]>

Optional ground truth label or structure.

##### Example

```code
{
     *   "Policy Type": [
     *     { label: "delay_reason", start: 4, end: 28 }
     *   ]
     * }
```

#### Example

```code
{
   *   "text": "Delayed shipment",
   *   "ground_truth": {
   *     "Policy Type": [
   *       { "label": "delay_reason", "start": 4, "end": 28 }
   *     ]
   *   }
   * }
```

### created_at

> **created_at**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:362](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-362)

ISO timestamp when this record was created.

#### Example

```code
"2023-01-01T00:00:00Z"
```

### updated_at

> **updated_at**: `string`

Defined in: [services/extraction/text/dto/insert-to-batch.dto.ts:369](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/insert-to-batch.dto.ts#lines-369)

ISO timestamp when this record was last updated.

#### Example

```code
"2023-01-01T01:00:00Z"
```
