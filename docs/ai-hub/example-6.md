# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-6>

## Example

```code
{
  "_id": "64f1d0e01c9a4f0012ab3456",
  "training_config_id": "64f1d0e01c9a4f0012ab3457",
  "training_id": "64f1d0e01c9a4f0012ab3458",
  "tenant_id": "64f1d0e01c9a4f0012ab3459",
  "deployment_id": "64f1d0e01c9a4f0012ab3461",
  "test_id": "64f1d0e01c9a4f0012ab3462",
  "test_type": "single",
  "data_type": "text",
  "status": "Completed",
  "file_name": "sample.pdf",
  "mime_type": "application/pdf",
  "file_url": "https://example.com/sample.pdf",
  "file_uuid": "123e4567-e89b-12d3-a456-426614174000",
  "file_id": "64f1d0e01c9a4f0012ab3463",
  "created_at": "2023-01-01T00:00:00.000Z",
  "updated_at": "2023-01-02T00:00:00.000Z",
  "processing_time": 2.15,
  "inference_time": 0.85,
  "metadata": {
    "source": "text-extraction-api"
  },
  "output": {
    "text": "John Doe works at Acme Corp in New York.",
    "entities": [
      {
        "text": "John Doe",
        "label": "PERSON",
        "start": 0,
        "end": 8,
        "confidence": 0.98
      },
      {
        "text": "Acme Corp",
        "label": "ORG",
        "start": 18,
        "end": 27,
        "confidence": 0.95
      },
      {
        "text": "New York",
        "label": "LOC",
        "start": 31,
        "end": 39,
        "confidence": 0.92
      }
    ]
  }
}
```
