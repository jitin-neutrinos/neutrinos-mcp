# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-1>

## Properties

### _id

> **_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:74](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-74)

Unique identifier for the classification test (MongoDB ObjectId).

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

### training_config_id

> **training_config_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:81](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-81)

ID of the training configuration used during inference (MongoDB ObjectId).

#### Example

```code
"64f1f1e01c9a4f0012ab5678"
```

### training_id

> **training_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:88](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-88)

ID of the training run executed (MongoDB ObjectId).

#### Example

```code
"64f1f2e01c9a4f0012ab6789"
```

### tenant_id

> **tenant_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:95](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-95)

ID of the tenant that owns this test data (MongoDB ObjectId).

#### Example

```code
"64f1f3e01c9a4f0012ab7890"
```

### deployment_id

> **deployment_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:102](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-102)

ID of the deployment used for this test (MongoDB ObjectId).

#### Example

```code
"64f1f4e01c9a4f0012ab8901"
```

### batch_id

> **batch_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:109](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-109)

ID of the batch this test belongs to (MongoDB ObjectId).

#### Example

```code
"64f1f5e01c9a4f0012ab9012"
```

### test_type

> **test_type**: [`TestType`](../enumerations/TestType.md)

Defined in: [services/classification/dto/test-info.dto.ts:116](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-116)

Type of test run — "Batch" or "Single".

#### Example

```code
"batch"
```

### data_type

> **data_type**: [`DataType`](../enumerations/DataType.md)

Defined in: [services/classification/dto/test-info.dto.ts:123](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-123)

Type of input data used — e.g., "Document", "Text".

#### Example

```code
"Document"
```

### status

> **status**: [`Status`](../enumerations/Status.md)

Defined in: [services/classification/dto/test-info.dto.ts:131](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-131)

Current status of the classification test.
 Can be "Created", "In-Progress", "Completed", "Failed", etc.

#### Example

```code
"Completed"
```

### file_name

> **file_name**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:138](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-138)

Name of the input file used for this test.

#### Example

```code
"invoice-test.pdf"
```

### mime_type

> **mime_type**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:145](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-145)

MIME type of the input file.

#### Example

```code
"application/pdf"
```

### file_url

> **file_url**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:152](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-152)

Publicly accessible URL to the file stored.

#### Example

```code
"https://storage.example.com/files/invoice-test.pdf"
```

### file_uuid

> **file_uuid**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:159](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-159)

Universally unique identifier of the uploaded file.

#### Example

```code
"a1b2c3d4-e5f6-7890-abcd-1234567890ef"
```

### file_id

> **file_id**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:166](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-166)

Internal file ID from storage system (MongoDB ObjectId).

#### Example

```code
"64f1f6e01c9a4f0012ab0123"
```

### input

> **input**: `Record`<`string`, `any`>

Defined in: [services/classification/dto/test-info.dto.ts:177](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-177)

Raw input or request parameters used in this test.

#### Example

```code
{
   *   "source": "mobile-app",
   *   "language": "en"
   * }
```

### created_at

> **created_at**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:184](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-184)

Timestamp when the test record was created.

#### Example

```code
"2023-01-01T00:00:00.000Z"
```

### updated_at

> **updated_at**: `string`

Defined in: [services/classification/dto/test-info.dto.ts:191](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-191)

Timestamp when the test record was last updated.

#### Example

```code
"2023-01-02T00:00:00.000Z"
```

### metadata

> **metadata**: `Record`<`string`, `any`>

Defined in: [services/classification/dto/test-info.dto.ts:202](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/test-info.dto.ts#lines-202)

Arbitrary metadata for audit or traceability.

#### Example

```code
{
   *   "user_id": "admin@example.com",
   *   "execution_context": "unit-test"
   * }
```
