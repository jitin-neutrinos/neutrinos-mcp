# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-3>

## Properties

### data

> **data**: [`IClassificationTestInfoResponse`](/articles/ai-hub/iclassificationtestinforesponse)[]

Defined in: [services/classification/dto/list-test.dto.ts:94](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/list-test.dto.ts#lines-94)

The paginated array of classification test records.

#### Overrides

`IListTestResponse.data`

### count

> **count**: `number`

Defined in: [services/dto/paginate.dto.ts:138](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/dto/paginate.dto.ts#lines-138)

The total number of items across all pages.
 This helps clients calculate how many pages are available.

#### Example

```code
100
```

#### Inherited from

`IListTestResponse.count`
