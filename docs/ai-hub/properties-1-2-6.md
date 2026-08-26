# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-6>

## Properties

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

`IListResultsResponse.count`

### data

> **data**: [`ITextExtractionTestResultDto`](/articles/ai-hub/itextextractiontestresultdto)[]

Defined in: [services/extraction/text/dto/list-results.dto.ts:205](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/list-results.dto.ts#lines-205)

The list of text extraction test results.

#### Overrides

`IListResultsResponse.data`
