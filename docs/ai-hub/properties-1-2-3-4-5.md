# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5>

## Properties

### token

> **token**: `string`

Defined in: [services/classification/doc/dto/list-results.dto.ts:53](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-53)

Token for authentication.

#### Overrides

`z.infer.token`

### test_id

> **test_id**: `string`

Defined in: [services/classification/doc/dto/list-results.dto.ts:60](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-60)

MongoDB ObjectId of the test whose results are to be listed.

#### Example

```code
"64f1d0e01c9a4f0012ab3456"
```

#### Overrides

`z.infer.test_id`

### page_number

> **page_number**: `number`

Defined in: [services/classification/doc/dto/list-results.dto.ts:67](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-67)

Page number for pagination (0-indexed).

#### Example

```code
0
```

#### Overrides

`z.infer.page_number`

### page_size

> **page_size**: `number`

Defined in: [services/classification/doc/dto/list-results.dto.ts:74](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-74)

Number of results per page.

#### Example

```code
10
```

#### Overrides

`z.infer.page_size`

### sort?

> `optional` **sort**: `"asc"` | `"desc"`

Defined in: [services/classification/doc/dto/list-results.dto.ts:83](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-83)

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

### merged?

> `optional` **merged**: `boolean`

Defined in: [services/classification/doc/dto/list-results.dto.ts:92](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/dto/list-results.dto.ts#lines-92)

Whether to return merged result entries for the given test.
 If true, only merged documents based on `test_id` grouping config are returned.

#### Default

```code
false
```

#### Example

```code
true
```

#### Overrides

`z.infer.merged`
