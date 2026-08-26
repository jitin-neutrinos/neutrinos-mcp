# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-2>

## Properties

### token

> **token**: `string`

Defined in: [services/classification/text/dto/create-batch.dto.ts:50](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/create-batch.dto.ts#lines-50)

API token for authentication.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### is_file

> **is_file**: `boolean`

Defined in: [services/classification/text/dto/create-batch.dto.ts:58](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/create-batch.dto.ts#lines-58)

Indicates whether the batch is file-based.
 For text classification, this should be `false`.

#### Example

```code
false
```

#### Overrides

`z.infer.is_file`

### callback_url?

> `optional` **callback_url**: `string`

Defined in: [services/classification/text/dto/create-batch.dto.ts:65](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/create-batch.dto.ts#lines-65)

The callback URL to receive batch results when processing is complete.

#### Example

```code
'https://example.com/callback'
```

#### Overrides

`z.infer.callback_url`

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/create-batch.dto.ts:79](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/create-batch.dto.ts#lines-79)

Arbitrary metadata to associate with this batch.
 This can include tags, traceability data, or context for classification.

#### Example

```code
{
  "source": "api",
  "document_type": "invoice"
}
```

#### Overrides

`z.infer.metadata`

### group_callback_url?

> `optional` **group_callback_url**: `string`

Defined in: [services/classification/text/dto/create-batch.dto.ts:89](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/create-batch.dto.ts#lines-89)

Optional callback URL to receive batch group processing results.

If provided, this URL will be called with the batch processing results once the batch
 group has been processed.

#### Example

```code
'https://example.com/group-callback'
```

#### Overrides

`z.infer.group_callback_url`
