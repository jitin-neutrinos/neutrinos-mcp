# Example

<https://documentation.neutrinos.com/articles/#!ai-hub/example-1-2-3-4-5-6>

## Example

```code
const sdk = new InferenceSDK(config);
const fileService = sdk.file.root;

// Upload a file
const uploadResponse = await fileService.uploadFile({
  token: '1234567890abcdef',
  file_path: '/tmp/report.csv',
  file_buffer: {
    fieldname: 'file',
    originalname: 'invoice.pdf',
    encoding: '7bit',
    mimetype: 'application/pdf',
    buffer: Buffer.from('file content'),
    size: 1048576
  }
});

// List uploaded files
const files = await fileService.getFileList({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 10,
  sort: 'desc'
});

// Get file information
const fileInfo = await fileService.getFileInfo({
  token: '1234567890abcdef',
  file_id: uploadResponse._id
});

// Download a file
const downloadStream = await fileService.downloadFile({
  token: '1234567890abcdef',
  file_id: uploadResponse._id
});

// Delete a file
await fileService.deleteFile({
  token: '1234567890abcdef',
  file_id: uploadResponse._id
});
```
