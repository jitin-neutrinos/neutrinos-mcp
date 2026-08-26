# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-5>

## Example

```code
const result: IExtractionDocListResultResponse = {
  _id: "64f1d0e01c9a4f0012ab0001",
  training_config_id: "64f1d0e01c9a4f0012ab0002",
  training_id: "64f1d0e01c9a4f0012ab0003",
  test_id: "64f1d0e01c9a4f0012ab3456",
  deployment_id: "64f1d0e01c9a4f0012ab0004",
  test_type: "Batch",
  data_type: "Document",
  status: "Completed",
  file_name: "contract.json",
  file_uuid: "b827c93e-d3f4-421f-a759-b1c64fce2ff3",
  file_url: "https://example.com/contract.json",
  file_id: "64f1d0e01c9a4f0012ab0005",
  mime_type: "application/json",
  processing_time: 123,
  inference_time: 45,
  metadata: {
    source: "manual-upload",
    department: "legal"
  },
  output: {
    category: {
      name: "Legal",
      confidence: 0.92
    },
    categories: [
      { name: "Legal", confidence: 0.92 },
      { name: "Finance", confidence: 0.65 }
    ]
  },
  created_at: "2023-01-01T00:00:00Z",
  updated_at: "2023-01-02T00:00:00Z"
};
```
