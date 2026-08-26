# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-2>

## Properties

### token

> **token**: `string`

Defined in: [services/classification/text/dto/single.dto.ts:62](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/single.dto.ts#lines-62)

API token for authentication.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### input

> **input**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/single.dto.ts:74](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/single.dto.ts#lines-74)

The input data to classify.
 Can be any structured key-value data such as text, attributes, etc.

#### Example

```code
{
   *   "message": "Request approved",
   *   "type": "notification"
   * }
```

#### Overrides

`z.infer.input`

### metadata?

> `optional` **metadata**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/single.dto.ts:86](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/single.dto.ts#lines-86)

Optional metadata associated with the classification input.
 Useful for downstream tracking and analytics.

#### Example

```code
{
   *   "source": "web",
   *   "user_id": "u-234"
   * }
```

#### Overrides

`z.infer.metadata`
