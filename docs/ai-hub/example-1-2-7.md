# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-7>

## Example

```code
{
  "data": [
    {
      "_id": "64f1d0e01c9a4f0012ab0001",
      "test_id": "64f1d0e01c9a4f0012ab3456",
      "text": "John Doe works at Microsoft in Seattle.",
      "entities": [
        {
          "text": "John Doe",
          "label": "PERSON",
          "start": 0,
          "end": 8,
          "confidence": 0.95
        },
        {
          "text": "Microsoft",
          "label": "ORG",
          "start": 18,
          "end": 27,
          "confidence": 0.88
        },
        {
          "text": "Seattle",
          "label": "GPE",
          "start": 31,
          "end": 38,
          "confidence": 0.92
        }
      ],
      "processing_time": 156,
      "inference_time": 67,
      "status": "Completed",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-02T00:00:00Z"
    }
  ],
  "count": 1
}
```
