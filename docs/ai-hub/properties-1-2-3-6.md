# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-6>

## Properties

### _id

> **_id**: `string`

Defined in: [services/dto/result-info.dto.ts:101](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-101)

MongoDB ObjectId of the result document.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ab"
```

#### Inherited from

`IResultInfoResponse._id`

### training_config_id

> **training_config_id**: `string`

Defined in: [services/dto/result-info.dto.ts:108](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-108)

MongoDB ObjectId of the associated training configuration.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ac"
```

#### Inherited from

`IResultInfoResponse.training_config_id`

### training_id

> **training_id**: `string`

Defined in: [services/dto/result-info.dto.ts:115](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-115)

MongoDB ObjectId of the associated training session.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ad"
```

#### Inherited from

`IResultInfoResponse.training_id`

### tenant_id

> **tenant_id**: `string`

Defined in: [services/dto/result-info.dto.ts:122](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-122)

MongoDB ObjectId of the tenant who owns this result.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ae"
```

#### Inherited from

`IResultInfoResponse.tenant_id`

### deployment_id

> **deployment_id**: `string`

Defined in: [services/dto/result-info.dto.ts:129](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-129)

MongoDB ObjectId of the deployment used to run inference.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6af"
```

#### Inherited from

`IResultInfoResponse.deployment_id`

### test_id

> **test_id**: `string`

Defined in: [services/dto/result-info.dto.ts:136](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-136)

MongoDB ObjectId of the test or batch this result belongs to.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6b0"
```

#### Inherited from

`IResultInfoResponse.test_id`

### test_type

> **test_type**: [`TestType`](../enumerations/TestType.md)

Defined in: [services/dto/result-info.dto.ts:143](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-143)

The type of test performed (e.g., 'Batch', 'Single').

#### Example

```code
"Batch"
```

#### Inherited from

`IResultInfoResponse.test_type`

### data_type

> **data_type**: [`DataType`](../enumerations/DataType.md)

Defined in: [services/dto/result-info.dto.ts:150](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-150)

The type of input data (e.g., 'Document', 'Image').

#### Example

```code
"Document"
```

#### Inherited from

`IResultInfoResponse.data_type`

### status

> **status**: [`Status`](../enumerations/Status.md)

Defined in: [services/dto/result-info.dto.ts:157](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-157)

The status of the result (e.g., 'Created', 'Completed').

#### Example

```code
"Completed"
```

#### Inherited from

`IResultInfoResponse.status`

### file_name

> **file_name**: `string`

Defined in: [services/dto/result-info.dto.ts:164](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-164)

The original name of the uploaded file.

#### Example

```code
"invoice.pdf"
```

#### Inherited from

`IResultInfoResponse.file_name`

### mime_type

> **mime_type**: `string`

Defined in: [services/dto/result-info.dto.ts:171](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-171)

MIME type of the uploaded file.

#### Example

```code
"application/pdf"
```

#### Inherited from

`IResultInfoResponse.mime_type`

### file_url

> **file_url**: `string`

Defined in: [services/dto/result-info.dto.ts:178](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-178)

Public URL where the file can be accessed.

#### Example

```code
"https://example.com/invoice.pdf"
```

#### Inherited from

`IResultInfoResponse.file_url`

### file_uuid

> **file_uuid**: `string`

Defined in: [services/dto/result-info.dto.ts:185](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-185)

UUID of the file used for storage or traceability.

#### Example

```code
"abcd1234-abcd-1234-abcd-12345678abcd"
```

#### Inherited from

`IResultInfoResponse.file_uuid`

### file_id

> **file_id**: `string`

Defined in: [services/dto/result-info.dto.ts:192](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-192)

MongoDB ObjectId of the file in the system.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6b1"
```

#### Inherited from

`IResultInfoResponse.file_id`

### created_at

> **created_at**: `string`

Defined in: [services/dto/result-info.dto.ts:199](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-199)

ISO timestamp when the result was created.

#### Example

```code
"2023-01-01T00:00:00.000Z"
```

#### Inherited from

`IResultInfoResponse.created_at`

### updated_at

> **updated_at**: `string`

Defined in: [services/dto/result-info.dto.ts:206](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-206)

ISO timestamp when the result was last updated.

#### Example

```code
"2023-01-01T01:00:00.000Z"
```

#### Inherited from

`IResultInfoResponse.updated_at`

### processing_time

> **processing_time**: `number`

Defined in: [services/dto/result-info.dto.ts:213](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-213)

Total time in seconds taken to process the result.

#### Example

```code
120
```

#### Inherited from

`IResultInfoResponse.processing_time`

### inference_time

> **inference_time**: `number`

Defined in: [services/dto/result-info.dto.ts:220](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-220)

Time in seconds taken for inference execution only.

#### Example

```code
30
```

#### Inherited from

`IResultInfoResponse.inference_time`

### metadata

> **metadata**: `Record`<`string`, `any`>

Defined in: [services/dto/result-info.dto.ts:233](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-233)

Arbitrary metadata relevant to the result.

#### Example

```code
{
  "source": "mobile-app",
  "notes": "test run"
}
```

#### Inherited from

`IResultInfoResponse.metadata`

### output

> **output**: `Record`<`string`, `any`>

Defined in: [services/dto/result-info.dto.ts:246](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-246)

Inference output generated by the model.

#### Example

```code
{
  "invoice_number": "INV-1001",
  "total": 199.99
}
```

#### Inherited from

`IResultInfoResponse.output`

### text?

> `optional` **text**: `string`

Defined in: [services/extraction/text/dto/list-results.dto.ts:118](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/list-results.dto.ts#lines-118)

The input text that was processed for extraction.

#### Example

```code
"John Doe works at Microsoft in Seattle."
```

### entities?

> `optional` **entities**: `object`[]

Defined in: [services/extraction/text/dto/list-results.dto.ts:123](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/list-results.dto.ts#lines-123)

Array of named entities extracted from the text.

#### text

> **text**: `string`

The extracted entity text.

##### Example

```code
"John Doe"
```

#### label

> **label**: `string`

The entity label/type.

##### Example

```code
"PERSON"
```

#### start

> **start**: `number`

Start position of the entity in the original text.

##### Example

```code
0
```

#### end

> **end**: `number`

End position of the entity in the original text.

##### Example

```code
8
```

#### confidence

> **confidence**: `number`

Confidence score for the entity extraction.

##### Example

```code
0.95
```
