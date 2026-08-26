# Class: InferenceSDK

<https://documentation.neutrinos.com/articles/#!ai-hub/inferencesdk>

# Class: InferenceSDK

Defined in: [sdk-client.ts:57](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-57)

The main entry point for interacting with the Inference API platform.

`InferenceSDK` provides unified access to domain-specific services including:

- Classification (text, document, raw)
- Extraction (text, document, raw)
- File operations (upload/download)
- Assistant capabilities (general + knowledge-based + embedding)
- Model catalog (list, version, token)

It handles:

- Authentication token management
- HTTP request orchestration
- OpenTelemetry-based tracing/logging (if configured)
