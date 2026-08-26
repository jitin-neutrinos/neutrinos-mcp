# Installing the SDK

<https://documentation.neutrinos.com/articles/#!ai-hub/prerequisites>

Before using the Classification Document Service, ensure that you have the following:

- An active account with the IDP Inference Platform.
- The necessary authentication credentials (e.g., API token).
- The IDP Inference SDK installed in your project.
- Node.js and npm installed on your machine.
- A basic understanding of TypeScript or JavaScript.

## Installing the SDK

Create `.npmrc` file in your project root with the following content:

```code
@neutrinos:registry=https://pkgs.dev.azure.com/devops-neutrinos/_packaging/neutrinos-public-store/npm/registry
always-auth=true
```

To install the IDP Inference SDK, use the following command:

```code
npm install --save @neutrinos/idp-inference-sdk
```

## Initializing the SDK

**TypeScript**

```code
import { InferenceSDK } from '@neutrinos/idp-inference-sdk';

const sdk = new InferenceSDK({
  endpoint: 'https://aihub-staging.neutrinos.com',
});
```

**JavaScript**

```code
const { InferenceSDK } = require('@neutrinos/idp-inference-sdk');

const sdk = new InferenceSDK({
  endpoint: 'https://aihub-staging.neutrinos.com',
});
```
