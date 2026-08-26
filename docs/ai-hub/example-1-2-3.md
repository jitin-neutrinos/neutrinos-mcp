# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3>

## Example

```code
const sdk = new InferenceSDK(config);

const convo = await sdk.assistant.conversation.create({
  token: '1234567890abcdef',
  metadata: { source: 'bot', channel: 'web' },
  translation_enabled: true
});

const batch = await sdk.assistant.conversation.createBatch({
  token: '1234567890abcdef',
  metadata: { use_case: 'bulk-import' },
  callback_url: 'https://hooks.example.com/callback'
});

const started = await sdk.assistant.conversation.startBatch({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8'
});

const info = await sdk.assistant.conversation.getBatchInfo({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8'
});

const reviewed = await sdk.assistant.conversation.reviewConversation({
  token: '1234567890abcdef',
  conversation_id: '686ce940102a8e192d80b1f8',
  review_status: 'Pending',
  messages: [
    {
      message_id: '6863b5492c8e9444541d60c8',
      is_positive: true,
      comment: 'This message is positive'
    }
  ]
});
```
