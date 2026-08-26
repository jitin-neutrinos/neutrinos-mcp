# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2>

## Properties

### group_callback_url?

> `optional` **group_callback_url**: `string`

Defined in: [services/classification/doc/dto/create-batch.dto.ts:51](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/create-batch.dto.ts#lines-51)

Optional callback URL to receive batch group processing results.

If provided, this URL will be called with the batch processing results once the batch
 group has been processed.

#### Example

```code
'https://example.com/group-callback'
```

### token

> **token**: `string`

Defined in: [services/dto/create-batch.dto.ts:83](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/create-batch.dto.ts#lines-83)

The API token used to authenticate the request.

This must be a valid token issued by the AIHub platform.

#### Example

```code
"1234567890abcdef"
```

#### Inherited from

`ICreateBatchDto.token`

### callback_url?

> `optional` **callback_url**: `string`

Defined in: [services/dto/create-batch.dto.ts:92](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/create-batch.dto.ts#lines-92)

The URL where the system will send the batch results once processing is complete.

This must be a publicly accessible HTTPS endpoint that can receive a POST request with results.

#### Example

```code
'https://example.com/callback'
```

#### Inherited from

`ICreateBatchDto.callback_url`

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/dto/create-batch.dto.ts:106](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/create-batch.dto.ts#lines-106)

Optional metadata that can be used to associate extra information with the batch request.

#### Example

```code
{
  "project": "invoice-categorization",
  "user": "john.doe",
  "tags": ["urgent", "finance"]
}
```

#### Inherited from

`ICreateBatchDto.metadata`
