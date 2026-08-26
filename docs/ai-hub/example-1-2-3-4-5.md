# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-4-5>

## Example

```code
const sdk = new InferenceSDK(config);

// Create an extraction batch
const batch = await sdk.extraction.doc.createBatch({
  token: '1234567890abcdef',
  callback_url: 'https://example.com/callback',
  metadata: {
    source: 'document-upload',
    user_id: 'user-001'
  }
});

// Extract a single document
const results = await sdk.extraction.doc.startSingle({
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

// List extraction results
const list = await sdk.extraction.doc.listResults({
  token: '1234567890abcdef',
  test_id: '64f1d0e01c9a4f0012ab3456',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});
console.log('Results:', list.data);
```
