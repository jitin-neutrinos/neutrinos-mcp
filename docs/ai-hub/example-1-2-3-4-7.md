# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-4-7>

## Example

```code
{
  "_id": "64acdc4b2f9e4c12a7d9e6ab",
  "training_config_id": "64acdc4b2f9e4c12a7d9e6ac",
  "training_id": "64acdc4b2f9e4c12a7d9e6ad",
  "tenant_id": "64acdc4b2f9e4c12a7d9e6ae",
  "test_id": "64acdc4b2f9e4c12a7d9e6af",
  "deployment_id": "64acdc4b2f9e4c12a7d9e6b0",
  "test_type": "single",
  "data_type": "text",
  "status": "Completed",
  "file_name": "invoice.txt",
  "file_uuid": "a1b2c3d4-e5f6-7890-1234-56789abcdef0",
  "file_url": "https://example.com/invoice.txt",
  "file_id": "64acdc4b2f9e4c12a7d9e6b1",
  "mime_type": "text/plain",
  "processing_time": 1.5,
  "inference_time": 0.8,
  "metadata": {
    "source": "qa-platform",
    "reviewer": "qa-user-01"
  },
  "output": {
    "text": "Invoice INV-1002 issued by Acme Corp on July 1, 2023.",
    "entities": [
      {
        "text": "INV-1002",
        "label": "InvoiceNumber",
        "start": 8,
        "end": 16,
        "confidence": 0.95
      },
      {
        "text": "Acme Corp",
        "label": "Vendor",
        "start": 28,
        "end": 37,
        "confidence": 0.93
      }
    ],
    "metadata": {
      "language": "en",
      "model_version": "v1.0.3"
    }
  },
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-02T00:00:00Z",
  "manual_extraction": {
    "InvoiceNumber": "INV-1002",
    "Vendor": "Acme Corp"
  },
  "manual_reason": "Entities corrected manually after reviewing the model's predictions."
}
```
