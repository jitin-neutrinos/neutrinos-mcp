# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1>

## Example

```code
const sdk = new InferenceSDK(config);
const res = await sdk.classification.root.uploadDocumentToBatch({
  batch_id: 'batch123',
  file_path: '/path/to/file.pdf',
});
```
