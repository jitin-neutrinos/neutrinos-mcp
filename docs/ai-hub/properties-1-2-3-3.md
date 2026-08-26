# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-3>

## Properties

### token

> **token**: `string`

Defined in: [services/extraction/doc/dto/single.dto.ts:86](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/single.dto.ts#lines-86)

Authentication token for API access.

#### Example

```code
"1234567890abcdef"
```

#### Overrides

`z.infer.token`

### file_path?

> `optional` **file_path**: `string`

Defined in: [services/extraction/doc/dto/single.dto.ts:95](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/single.dto.ts#lines-95)

Relative path to the document file to extract.

Useful when the file is stored on a local filesystem or accessible via a known internal path.

#### Example

```code
'/path/to/file.txt'
```

#### Overrides

`z.infer.file_path`

### file_id?

> `optional` **file_id**: `string`

Defined in: [services/extraction/doc/dto/single.dto.ts:104](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/single.dto.ts#lines-104)

MongoDB ObjectId referring to a previously uploaded file.

Used in systems where files are stored in a DB or external store (e.g., GridFS, S3).

#### Example

```code
'64c13f63e85f3e6a4c1f8f99'
```

#### Overrides

`z.infer.file_id`

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/extraction/doc/dto/single.dto.ts:120](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/single.dto.ts#lines-120)

Arbitrary metadata to associate with this extraction request.

This can include trace IDs, tags, source identifiers, customer info, etc.

#### Example

```code
{
  "source": "web-app",
  "customer_id": "C12345",
  "request_id": "abc-123"
}
```

#### Overrides

`z.infer.metadata`

### file_buffer?

> `optional` **file_buffer**: [`IMulterFile`](IMulterFile.md)

Defined in: [services/extraction/doc/dto/single.dto.ts:137](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/single.dto.ts#lines-137)

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
