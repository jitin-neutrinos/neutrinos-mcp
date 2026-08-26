# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/model-catalog-service-usage>

This guide provides examples of how to use the Model Catalog Service methods in the IDP Inference SDK. These methods allow you to perform various model catalog operations.

## Table of Methods with API Links

| **Method Name** | **API Endpoint** | **API Docs Link** |
| --- | --- | --- |
| [`modelList`](/articles/ai-hub/model-catalog-service-usage/a/model-list) | `/model-catalog/model-list` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ModelCatalogService.md#modellist) |
| [`versionList`](/articles/ai-hub/model-catalog-service-usage/a/version-list) | `/model-catalog/version-list` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ModelCatalogService.md#versionlist) |
| [`environmentList`](/articles/ai-hub/model-catalog-service-usage/a/environment-list) | `/model-catalog/environment-list` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ModelCatalogService.md#environmentlist) |
| [`generateToken`](/articles/ai-hub/model-catalog-service-usage/a/generate-token) | `/model-catalog/generate-token` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/ModelCatalogService.md#generatetoken) |

## Model List

To get a list of models, use the `modelList` method. This method returns a `IModelListResponse` object.

**TypeScript**

```code
import { IModelListDto, IModelListResponse } from '@neutrinos/idp-inference-sdk';

const modelListDto: IModelListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_type: 'Classification',
  data_type: 'Text',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
  search: 'my-model',
};

try {
  const result: IModelListResponse = await sdk.model.root.modelList(modelListDto);
  console.log('Model list:', result);
} catch (error) {
  console.error('Error getting model list:', error);
}
```

**JavaScript**

```code
const modelListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_type: 'Classification',
  data_type: 'Text',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
  search: 'my-model',
};

try {
  const result = await sdk.model.root.modelList(modelListDto);
  console.log('Model list:', result);
} catch (error) {
  console.error('Error getting model list:', error);
}
```

## Version List

To get a list of model versions, use the `versionList` method. This method returns a `IVersionListResponse` object.

**TypeScript**

```code
import { IVersionListDto, IVersionListResponse } from '@neutrinos/idp-inference-sdk';

const versionListDto: IVersionListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_config_id: '1234567890',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result: IVersionListResponse = await sdk.model.root.versionList(versionListDto);
  console.log('Version list:', result);
} catch (error) {
  console.error('Error getting version list:', error);
}
```

**JavaScript**

```code
const versionListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_config_id: '1234567890',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
};

try {
  const result = await sdk.model.root.versionList(versionListDto);
  console.log('Version list:', result);
} catch (error) {
  console.error('Error getting version list:', error);
}
```

## Environment List

To get a list of model environments, use the `environmentList` method. This method returns a `IEnvironmentListResponse` object.

**TypeScript**

```code
import { IEnvironmentListDto, IEnvironmentListResponse } from '@neutrinos/idp-inference-sdk';

const environmentListDto: IEnvironmentListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
};

try {
  const result: IEnvironmentListResponse = await sdk.model.root.environmentList(environmentListDto);
  console.log('Environment list:', result);
} catch (error) {
  console.error('Error getting environment list:', error);
}
```

**JavaScript**

```code
const environmentListDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
};

try {
  const result = await sdk.model.root.environmentList(environmentListDto);
  console.log('Environment list:', result);
} catch (error) {
  console.error('Error getting environment list:', error);
}
```

## Generate Token

To generate a token, use the `generateToken` method. This method returns a `IGenerateTokenResponse` object.

**TypeScript**

```code
import { IGenerateTokenDto, IGenerateTokenResponse } from '@neutrinos/idp-inference-sdk';

const generateTokenDto: IGenerateTokenDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_config_id: '1234567890',
  training_id: '1234567890',
  environment_id: '1234567890',
  expire: '1h',
};

try {
  const result: IGenerateTokenResponse = await sdk.model.root.generateToken(generateTokenDto);
  console.log('Token:', result);
} catch (error) {
  console.error('Error generating token:', error);
}
```

**JavaScript**

```code
const generateTokenDto = {
  token:
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c',
  training_config_id: '1234567890',
  training_id: '1234567890',
  environment_id: '1234567890',
  expire: '1h',
};

try {
  const result = await sdk.model.root.generateToken(generateTokenDto);
  console.log('Token:', result);
} catch (error) {
  console.error('Error generating token:', error);
}
```
