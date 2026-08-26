# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-6>

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

`IResultFeedbackResponse._id`

### training_config_id

> **training_config_id**: `string`

Defined in: [services/dto/result-info.dto.ts:108](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-108)

MongoDB ObjectId of the associated training configuration.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ac"
```

#### Inherited from

`IResultFeedbackResponse.training_config_id`

### training_id

> **training_id**: `string`

Defined in: [services/dto/result-info.dto.ts:115](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-115)

MongoDB ObjectId of the associated training session.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ad"
```

#### Inherited from

`IResultFeedbackResponse.training_id`

### tenant_id

> **tenant_id**: `string`

Defined in: [services/dto/result-info.dto.ts:122](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-122)

MongoDB ObjectId of the tenant who owns this result.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6ae"
```

#### Inherited from

`IResultFeedbackResponse.tenant_id`

### deployment_id

> **deployment_id**: `string`

Defined in: [services/dto/result-info.dto.ts:129](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-129)

MongoDB ObjectId of the deployment used to run inference.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6af"
```

#### Inherited from

`IResultFeedbackResponse.deployment_id`

### test_id

> **test_id**: `string`

Defined in: [services/dto/result-info.dto.ts:136](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-136)

MongoDB ObjectId of the test or batch this result belongs to.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6b0"
```

#### Inherited from

`IResultFeedbackResponse.test_id`

### test_type

> **test_type**: [`TestType`](../enumerations/TestType.md)

Defined in: [services/dto/result-info.dto.ts:143](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-143)

The type of test performed (e.g., 'Batch', 'Single').

#### Example

```code
"Batch"
```

#### Inherited from

`IResultFeedbackResponse.test_type`

### data_type

> **data_type**: [`DataType`](../enumerations/DataType.md)

Defined in: [services/dto/result-info.dto.ts:150](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-150)

The type of input data (e.g., 'Document', 'Image').

#### Example

```code
"Document"
```

#### Inherited from

`IResultFeedbackResponse.data_type`

### status

> **status**: [`Status`](../enumerations/Status.md)

Defined in: [services/dto/result-info.dto.ts:157](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-157)

The status of the result (e.g., 'Created', 'Completed').

#### Example

```code
"Completed"
```

#### Inherited from

`IResultFeedbackResponse.status`

### file_name

> **file_name**: `string`

Defined in: [services/dto/result-info.dto.ts:164](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-164)

The original name of the uploaded file.

#### Example

```code
"invoice.pdf"
```

#### Inherited from

`IResultFeedbackResponse.file_name`

### mime_type

> **mime_type**: `string`

Defined in: [services/dto/result-info.dto.ts:171](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-171)

MIME type of the uploaded file.

#### Example

```code
"application/pdf"
```

#### Inherited from

`IResultFeedbackResponse.mime_type`

### file_url

> **file_url**: `string`

Defined in: [services/dto/result-info.dto.ts:178](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-178)

Public URL where the file can be accessed.

#### Example

```code
"https://example.com/invoice.pdf"
```

#### Inherited from

`IResultFeedbackResponse.file_url`

### file_uuid

> **file_uuid**: `string`

Defined in: [services/dto/result-info.dto.ts:185](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-185)

UUID of the file used for storage or traceability.

#### Example

```code
"abcd1234-abcd-1234-abcd-12345678abcd"
```

#### Inherited from

`IResultFeedbackResponse.file_uuid`

### file_id

> **file_id**: `string`

Defined in: [services/dto/result-info.dto.ts:192](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-192)

MongoDB ObjectId of the file in the system.

#### Example

```code
"64acdc4b2f9e4c12a7d9e6b1"
```

#### Inherited from

`IResultFeedbackResponse.file_id`

### created_at

> **created_at**: `string`

Defined in: [services/dto/result-info.dto.ts:199](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-199)

ISO timestamp when the result was created.

#### Example

```code
"2023-01-01T00:00:00.000Z"
```

#### Inherited from

`IResultFeedbackResponse.created_at`

### updated_at

> **updated_at**: `string`

Defined in: [services/dto/result-info.dto.ts:206](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-206)

ISO timestamp when the result was last updated.

#### Example

```code
"2023-01-01T01:00:00.000Z"
```

#### Inherited from

`IResultFeedbackResponse.updated_at`

### processing_time

> **processing_time**: `number`

Defined in: [services/dto/result-info.dto.ts:213](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-213)

Total time in seconds taken to process the result.

#### Example

```code
120
```

#### Inherited from

`IResultFeedbackResponse.processing_time`

### inference_time

> **inference_time**: `number`

Defined in: [services/dto/result-info.dto.ts:220](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/result-info.dto.ts#lines-220)

Time in seconds taken for inference execution only.

#### Example

```code
30
```

#### Inherited from

`IResultFeedbackResponse.inference_time`

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

`IResultFeedbackResponse.metadata`

### output

> **output**: [`IExtractionTextOutput`](IExtractionTextOutput.md)

Defined in: [services/extraction/text/dto/result-feedback.dto.ts:199](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/result-feedback.dto.ts#lines-199)

The structured output returned by the model.
Includes original text, extracted entities, and optional metadata.

#### Example

```code
{
  "text": "Invoice INV-1002 issued by Acme Corp on July 1, 2023.",
  "entities": [
    {
      "text": "INV-1002",
      "label": "InvoiceNumber",
      "start": 8,
      "end": 16,
      "confidence": 0.95
    },
    {
      "text": "Acme Corp",
      "label": "Vendor",
      "start": 28,
      "end": 37,
      "confidence": 0.93
    }
  ],
  "metadata": {
    "language": "en",
    "model_version": "v1.0.3"
  }
}
```

#### Overrides

`IResultFeedbackResponse.output`

### manual_extraction

> **manual_extraction**: `Record`<`string`, `any`>

Defined in: [services/extraction/text/dto/result-feedback.dto.ts:213](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/result-feedback.dto.ts#lines-213)

Manually assigned extraction correction.
Used to override or validate the model prediction.

#### Example

```code
{
  "InvoiceNumber": "INV-1002",
  "Vendor": "Acme Corp"
}
```

### manual_reason

> **manual_reason**: `string`

Defined in: [services/extraction/text/dto/result-feedback.dto.ts:220](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/result-feedback.dto.ts#lines-220)

Explanation provided by the human reviewer for the correction.

#### Example

```code
"Entities corrected manually after reviewing the model's predictions."
```
