# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-7>

## Example

```code
const result: ITextExtractionTestResultDto = {
  _id: "64f1d0e01c9a4f0012ab0001",
  training_config_id: "64f1d0e01c9a4f0012ab0002",
  training_id: "64f1d0e01c9a4f0012ab0003",
  test_id: "64f1d0e01c9a4f0012ab3456",
  deployment_id: "64f1d0e01c9a4f0012ab0004",
  test_type: "Batch",
  data_type: "Text",
  status: "Completed",
  text: "John Doe works at Microsoft in Seattle.",
  entities: [
    { text: "John Doe", label: "PERSON", start: 0, end: 8, confidence: 0.95 },
    { text: "Microsoft", label: "ORG", start: 18, end: 27, confidence: 0.88 },
    { text: "Seattle", label: "GPE", start: 31, end: 38, confidence: 0.92 }
  ],
  processing_time: 156,
  inference_time: 67,
  metadata: {
    source: "manual-input"
  },
  output: {
    entities: [
      { text: "John Doe", label: "PERSON", start: 0, end: 8, confidence: 0.95 }
    ]
  },
  created_at: "2023-01-01T00:00:00Z",
  updated_at: "2023-01-02T00:00:00Z"
};
```
