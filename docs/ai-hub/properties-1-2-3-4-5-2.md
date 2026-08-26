# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-2>

## Properties

### _id

> **_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:159](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-159)

MongoDB ID of this input record.

#### Example

```code
"64c143fbe9c3213e4f90cde3"
```

### training_config_id

> **training_config_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:166](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-166)

Training configuration ID used for this classification.

#### Example

```code
"64c1401aebf02c76ef098cde"
```

### training_id

> **training_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:173](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-173)

Training run ID this record belongs to.

#### Example

```code
"64c141c3f10cdb7a28e93bfa"
```

### tenant_id

> **tenant_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:180](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-180)

ID of the tenant (multi-tenant context).

#### Example

```code
"64c1428ef8a8e67be21c2a12"
```

### deployment_id

> **deployment_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:187](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-187)

Deployment version or environment ID.

#### Example

```code
"64c143c7f56b97b82dd233ff"
```

### test_type

> **test_type**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:194](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-194)

Type of the classification task.

#### Example

```code
"Batch"
```

### data_type

> **data_type**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:201](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-201)

Type of input data (always "Text" for this DTO).

#### Example

```code
"Text"
```

### status

> **status**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:208](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-208)

Current status of this record.

#### Example

```code
"Completed"
```

### input

> **input**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:213](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-213)

Input payload and label provided during insertion.

### batch_id

> **batch_id**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:220](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-220)

The batch ID this input is associated with.

#### Example

```code
"64c13f63e85f3e6a4c1f8f99"
```

### created_at

> **created_at**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:227](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-227)

Timestamp when this input was added.

#### Example

```code
"2023-01-01T00:00:00Z"
```

### updated_at

> **updated_at**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:234](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-234)

Timestamp when this record was last updated.

#### Example

```code
"2023-01-02T00:00:00Z"
```
