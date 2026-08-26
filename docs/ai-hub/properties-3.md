# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-3>

## Properties

### token

> **token**: `string`

Defined in: [services/classification/text/dto/list-results.dto.ts:41](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/list-results.dto.ts#lines-41)

API token for authentication.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### test_id

> **test_id**: `string`

Defined in: [services/classification/text/dto/list-results.dto.ts:48](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/list-results.dto.ts#lines-48)

MongoDB ObjectId of the test whose results are to be listed.

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

#### Overrides

`z.infer.test_id`

### page_number

> **page_number**: `number`

Defined in: [services/classification/text/dto/list-results.dto.ts:55](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/list-results.dto.ts#lines-55)

Page number for pagination (0-indexed).

#### Example

```code
0
```

#### Overrides

`z.infer.page_number`

### page_size

> **page_size**: `number`

Defined in: [services/classification/text/dto/list-results.dto.ts:62](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/list-results.dto.ts#lines-62)

Number of results per page.

#### Example

```code
10
```

#### Overrides

`z.infer.page_size`

### sort?

> `optional` **sort**: `"asc"` | `"desc"`

Defined in: [services/classification/text/dto/list-results.dto.ts:71](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/list-results.dto.ts#lines-71)

Sort order of the results.
 Either ascending ('asc') or descending ('desc').

#### Default

```code
'desc'
```

#### Example

```code
'desc'
```

#### Overrides

`z.infer.sort`
