# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-4-3>

## Example

```code
const response: IClassificationTextListResultsResponse = {
  data: [
    {
      _id: "64f1d0e01c9a4f0012ab0001",
      test_id: "64f1d0e01c9a4f0012ab3456",
      test_type: "single",
      data_type: "text",
      status: "Completed",
      file_name: "input.json",
      file_uuid: "b827c93e-d3f4-421f-a759-b1c64fce2ff3",
      file_url: "https://example.com/input.json",
      file_id: "64f1d0e01c9a4f0012ab0005",
      mime_type: "application/json",
      processing_time: 100,
      inference_time: 40,
      metadata: { origin: "feedback-loop" },
      output: {
        category: {
          name: "Support",
          confidence: 0.89
        },
        categories: [
          { name: "Support", confidence: 0.89 },
          { name: "Sales", confidence: 0.75 }
        ]
      },
      created_at: "2023-01-05T10:00:00Z",
      updated_at: "2023-01-05T11:00:00Z"
    }
  ],
  count: 1
};
```
