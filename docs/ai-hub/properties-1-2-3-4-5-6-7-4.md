# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-7-4>

## Properties

### token

> **token**: `string`

Defined in: [services/file/dto/file-list.dto.ts:35](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-list.dto.ts#lines-35)

The authentication token for API requests.

#### Example

```code
'1234567890abcdef'
```

#### Overrides

`z.infer.token`

### page_number

> **page_number**: `number`

Defined in: [services/file/dto/file-list.dto.ts:42](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-list.dto.ts#lines-42)

The current page number (starting from **0**).

#### Example

```code
0
```

#### Overrides

`z.infer.page_number`

### page_size

> **page_size**: `number`

Defined in: [services/file/dto/file-list.dto.ts:49](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-list.dto.ts#lines-49)

The number of items to retrieve per page.

#### Example

```code
10
```

#### Overrides

`z.infer.page_size`

### sort?

> `optional` **sort**: `"asc"` | `"desc"`

Defined in: [services/file/dto/file-list.dto.ts:58](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-list.dto.ts#lines-58)

Sort order for the results.
Must be either `'asc'` or `'desc'`.

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
