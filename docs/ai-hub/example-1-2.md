# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2>

## Example

```code
const sdk = new InferenceSDK(config);

// Create a text classification batch
const batch = await sdk.classification.text.createBatch({
  token: '1234567890abcdef',
  is_file: false,
  metadata: { project: 'customer-feedback' }
});

// Insert inputs into the batch
await sdk.classification.text.insertToBatch({
  token: '1234567890abcdef',
  batch_id: batch._id,
  input: [
    {
      data: { text: 'This product is faulty' },
      ground_truth: 'complaint'
    }
  ]
});

// Run classification on a single JSON input
const result = await sdk.classification.text.startSingle({
  token: '1234567890abcdef',
  input: { subject: 'Need help with account access' },
  metadata: { source: 'support-ticket' }
});
```
