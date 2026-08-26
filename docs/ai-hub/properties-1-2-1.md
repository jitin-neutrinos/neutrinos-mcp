# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-1>

## Properties

### category

> **category**: [`IClassificationOutputCategory`](/articles/ai-hub/iclassificationoutputcategory)

Defined in: [services/classification/dto/single.dto.ts:34](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-34)

The top predicted category.

#### Example

```code
{
   *   "name": "positive",
   *   "confidence": 0.95
   * }
```

### categories

> **categories**: [`IClassificationOutputCategory`](/articles/ai-hub/iclassificationoutputcategory)[]

Defined in: [services/classification/dto/single.dto.ts:51](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/single.dto.ts#lines-51)

A ranked list of all predicted categories with their confidence scores.

#### Example

```code
[
  {
    "name": "positive",
    "confidence": 0.95
  },
  {
    "name": "neutral",
    "confidence": 0.03
  }
]
```
