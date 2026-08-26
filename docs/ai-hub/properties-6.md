# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-6>

## Properties

### token

> **token**: `string`

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:74](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-74)

API token for authentication.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### file_path?

> `optional` **file_path**: `string`

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:81](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-81)

Path to the local file for upload (optional if `file_id` is provided).

#### Example

```code
'/files/input.csv'
```

#### Overrides

`z.infer.file_path`

### file_id?

> `optional` **file_id**: `string`

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:88](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-88)

ID of an already uploaded file (preferred over `file_path` if both are given).

#### Example

```code
'64f1d0e01c9a4f0012ab3456'
```

#### Overrides

`z.infer.file_id`

### batch_id

> **batch_id**: `string`

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:95](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-95)

ID of the batch where the file should be uploaded.

#### Example

```code
'64f1d0e01c9a4f0012ab3456'
```

#### Overrides

`z.infer.batch_id`

### file_buffer?

> `optional` **file_buffer**: [`IMulterFile`](IMulterFile.md)

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:112](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-112)

The buffer of the file to upload.

#### Example

```code
{
  fieldname: 'file',
  originalname: 'invoice.pdf',
  encoding: '7bit',
  mimetype: 'application/pdf',
  buffer: Buffer.from('file content'),
  size: 1048576
}
```

#### Overrides

`z.infer.file_buffer`
