# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-3>

## Example

```code
{
  "_id": "64f70e301b2f5c4567c89abc",
  "training_config_id": "64f70e301b2f5c4567c89aaa",
  "training_id": "64f70e301b2f5c4567c89aab",
  "test_id": "64f70e301b2f5c4567c89aad",
  "tenant_id": "64f70e301b2f5c4567c89aae",
  "deployment_id": "64f70e301b2f5c4567c89aaf",
  "test_type": "Single",
  "data_type": "Text",
  "status": "Completed",
  "input": {
    "message": "I want a refund",
    "channel": "email"
  },
  "output": {
    "category": {
      "name": "complaint",
      "confidence": 0.92
    },
    "categories": [
      {
        "name": "complaint",
        "confidence": 0.92
      }
    ]
  },
  "processing_time": 310,
  "inference_time": 120,
  "metadata": {
    "source": "web"
  },
  "created_at": "2023-01-01T00:00:00Z",
  "updated_at": "2023-01-01T00:01:00Z"
}
```
