# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-4>

## Example

```code
const sdk = new InferenceSDK(config);
const embeddings = await sdk.assistant.embed.listEmbeddings({
  token: '1234567890abcdef',
  source_id: '6543210987654321',
  search: 'hello world',
  page_number: 0,
  page_size: 10,
  sort: 'desc',
});
```
