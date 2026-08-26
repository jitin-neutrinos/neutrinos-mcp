# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example>

## Example

```code
const sdk = new InferenceSDK(config);

// Create a classification batch
const batch = await sdk.classification.doc.createBatch({
  token: '1234567890abcdef',
  callback_url: 'https://example.com/callback',
  metadata: {
    source: 'document-upload',
    user_id: 'user-001'
  },
  group_callback_url: 'https://example.com/group-callback'
});

// Classify a single document
const results = await sdk.classification.doc.startSingle({
  token: '1234567890abcdef',
  file_path: '/files/sample.pdf',
  metadata: { origin: 'web' },
  file_buffer: {
    fieldname: 'file',
    originalname: 'invoice.pdf',
    encoding: '7bit',
    mimetype: 'application/pdf',
    buffer: Buffer.from('file content'),
    size: 1048576
  }
});

// List classification results
const list = await sdk.classification.doc.listResults({
  token: '1234567890abcdef',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
  merged: true
});
console.log('Results:', list.data);
```
