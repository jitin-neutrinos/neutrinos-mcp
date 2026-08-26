# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1>

## Properties

### token

> **token**: `string`

Defined in: [services/assistant/message/dto/list-messages.dto.ts:116](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/message/dto/list-messages.dto.ts#lines-116)

The token to use for authentication.

#### Example

```code
"1234567890abcdef"
```

#### Overrides

[`IPaginateDto`](IPaginateDto.md).[`token`](IPaginateDto.md#token)

### conversation_id

> **conversation_id**: `string`

Defined in: [services/assistant/message/dto/list-messages.dto.ts:123](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/assistant/message/dto/list-messages.dto.ts#lines-123)

The ID of the conversation to fetch messages for.

#### Example

```code
"5f9d2c3b6e8af1000d7a4ad2"
```

### page_number

> **page_number**: `number`

Defined in: [services/dto/paginate.dto.ts:72](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/paginate.dto.ts#lines-72)

The page number. Starts from 0 (zero-based indexing).

#### Default

```code
0
```

#### Example

```code
0
```

#### Inherited from

[`IPaginateDto`](IPaginateDto.md).[`page_number`](IPaginateDto.md#page_number)

### page_size

> **page_size**: `number`

Defined in: [services/dto/paginate.dto.ts:80](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/paginate.dto.ts#lines-80)

The number of items to include in each page.

#### Default

```code
10
```

#### Example

```code
20
```

#### Inherited from

[`IPaginateDto`](IPaginateDto.md).[`page_size`](IPaginateDto.md#page_size)

### sort?

> `optional` **sort**: `"asc"` | `"desc"`

Defined in: [services/dto/paginate.dto.ts:90](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/paginate.dto.ts#lines-90)

The sort order of the results.
 Only `'asc'` (ascending) or `'desc'` (descending) are accepted.
 Defaults to `'desc'`.

#### Default

```code
'desc'
```

#### Example

```code
'asc'
```

#### Inherited from

[`IPaginateDto`](IPaginateDto.md).[`sort`](IPaginateDto.md#sort)
