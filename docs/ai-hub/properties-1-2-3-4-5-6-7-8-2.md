# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-7-8-2>

## Properties

### data

> **data**: `Record`<`string`, `any`>

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:76](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-76)

The classification input as key-value pairs.

#### Example

```code
{
  "text": "Sample sentence",
  "language": "en"
}
```

### ground_truth?

> `optional` **ground_truth**: `string`

Defined in: [services/classification/text/dto/insert-to-batch.dto.ts:83](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/text/dto/insert-to-batch.dto.ts#lines-83)

The expected classification label, if available.

#### Example

```code
"delay_alert"
```
