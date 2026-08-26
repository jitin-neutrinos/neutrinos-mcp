# Constructors

<https://documentation.neutrinos.com/articles/#!ai-hub/constructors>

## Constructors

### Constructor

> **new InferenceSDK**(`config`): `InferenceSDK`

Defined in: [sdk-client.ts:147](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/sdk-client.ts#lines-147)

Constructs and initializes the SDK with provided configuration.

This also sets up OpenTelemetry tracing/logging based on the `trace_oltp_endpoint` and `log_oltp_endpoint`.

#### Parameters

##### config

[`ISDKConfig`](../interfaces/ISDKConfig.md)

The SDK configuration object.

- `endpoint`: Base URL for all API requests
- `timeout`: Optional timeout for HTTP requests
- `trace_oltp_endpoint`: Optional OTLP trace endpoint (for distributed tracing)
- `log_oltp_endpoint`: Optional OTLP log endpoint (for log streaming)

#### Returns

`InferenceSDK`

#### Throws

If the configuration is invalid

#### Example

```code
const sdk = new InferenceSDK({
  endpoint: 'https://api.aihub.com',
});
```
