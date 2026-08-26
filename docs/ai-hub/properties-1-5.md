# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-5>

## Properties

### token

> **token**: `string`

Defined in: [services/extraction/doc/dto/list-results.dto.ts:43](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/list-results.dto.ts#lines-43)

Authentication token for API access.

#### Example

```code
"1234567890abcdef"
```

#### Overrides

`z.infer.token`

### test_id

> **test_id**: `string`

Defined in: [services/extraction/doc/dto/list-results.dto.ts:50](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/list-results.dto.ts#lines-50)

MongoDB ObjectId of the test whose results are to be listed.

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

#### Overrides

`z.infer.test_id`

### page_number

> **page_number**: `number`

Defined in: [services/extraction/doc/dto/list-results.dto.ts:57](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/list-results.dto.ts#lines-57)

Page number for pagination (0-indexed).

#### Example

```code
0
```

#### Overrides

`z.infer.page_number`

### page_size

> **page_size**: `number`

Defined in: [services/extraction/doc/dto/list-results.dto.ts:64](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/list-results.dto.ts#lines-64)

Number of results per page.

#### Example

```code
10
```

#### Overrides

`z.infer.page_size`

### sort?

> `optional` **sort**: `"asc"` | `"desc"`

Defined in: [services/extraction/doc/dto/list-results.dto.ts:73](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/list-results.dto.ts#lines-73)

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
