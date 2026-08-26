# Table of Methods with API Links

<https://documentation.neutrinos.com/articles/#!ai-hub/file-service-usage>

This guide provides examples of how to use the File Service methods in the IDP Inference SDK. These methods allow you to perform various file upload, delete, and list operations.

## Table of Methods with API Links

| **Method Name** | **API Endpoint** | **API Docs Link** |
| --- | --- | --- |
| [`uploadFile`](/articles/ai-hub/file-service-usage/a/uploading-a-file) | `/file/upload` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/FileService.md#uploadfile) |
| [`deleteFile`](/articles/ai-hub/file-service-usage/a/deleting-a-file) | `/file/delete/{file_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/FileService.md#deletefile) |
| [`getFileList`](/articles/ai-hub/file-service-usage/a/listing-files) | `/file/find-all` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/FileService.md#getfilelist) |
| [`getFileInfo`](/articles/ai-hub/file-service-usage/a/getting-file-info) | `/file/info` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/FileService.md#getfileinfo) |
| [`downloadFile`](/articles/ai-hub/file-service-usage/a/downloading-a-file) | `/file/download/{file_id}` | [API Docs](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/api-docs/classes/FileService.md#downloadfile) |

## Uploading a File

To upload a file, use the `uploadFile` method. This method takes a file path as an argument and returns a `IFileUploadResponse` object.

**TypeScript**

```code
import { IUploadFileDto } from '@neutrinos/idp-inference-sdk';

const uploadFileDto: IUploadFileDto = {
  token: 'your-auth-token',
  file_path: '/path/to/file.txt',
};

try {
  const result = await sdk.file.root.uploadFile(uploadFileDto);
  console.log('File uploaded:', result);
} catch (error) {
  console.error('Error uploading file:', error);
}
```

**JavaScript**

```code
const uploadFileDto = {
  token: 'your-auth-token',
  file_path: '/path/to/file.txt',
};

try {
  const result = await sdk.file.root.uploadFile(uploadFileDto);
  console.log('File uploaded:', result);
} catch (error) {
  console.error('Error uploading file:', error);
}
```

## Deleting a File

To delete a file, use the `deleteFile` method. This method takes a file ID as an argument and returns a `IFileDeleteResponse` object.

**TypeScript**

```code
import { IDeleteFileDto } from '@neutrinos/idp-inference-sdk';

const deleteFileDto: IDeleteFileDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const result = await sdk.file.root.deleteFile(deleteFileDto);
  console.log('File deleted:', result);
} catch (error) {
  console.error('Error deleting file:', error);
}
```

**JavaScript**

```code
const deleteFileDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const result = await sdk.file.root.deleteFile(deleteFileDto);
  console.log('File deleted:', result);
} catch (error) {
  console.error('Error deleting file:', error);
}
```

## Listing Files

To list all uploaded files, use the `getFileList` method. This method takes no arguments and returns a `IFileListResponse` object.

**TypeScript**

```code
import { IFileListDto } from '@neutrinos/idp-inference-sdk';

const getFileListDto: IFileListDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort_order: 'desc',
};

try {
  const result = await sdk.file.root.getFileList(getFileListDto);
  console.log('File list:', result);
} catch (error) {
  console.error('Error getting file list:', error);
}
```

**JavaScript**

```code
const getFileListDto = {
  token: 'your-auth-token',
  page_number: 0,
  page_size: 10,
  sort_order: 'desc',
};

try {
  const result = await sdk.file.root.getFileList(getFileListDto);
  console.log('File list:', result);
} catch (error) {
  console.error('Error getting file list:', error);
}
```

## Getting file info

To retrieve information about a specific file, use the `getFileInfo` method. This method requires a file ID and returns detailed metadata about the file, including its name, size, type, upload time, and public URL.

**TypeScript**

```code
import { IFileInfoDto } from '@neutrinos/idp-inference-sdk';

const getFileInfoDto: IFileInfoDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const fileInfo = await sdk.file.root.getFileInfo(getFileInfoDto);
  console.log('File info:', fileInfo);
} catch (error) {
  console.error('Error retrieving file info:', error);
}
```

**JavaScript**

```code
const getFileInfoDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const fileInfo = await sdk.file.root.getFileInfo(getFileInfoDto);
  console.log('File info:', fileInfo);
} catch (error) {
  console.error('Error retrieving file info:', error);
}
```

## Downloading a File

To download a file, use the `downloadFile` method. This method takes a file ID as an argument and returns a `IFileDownloadResponse` object.

**TypeScript**

```code
import { IDownloadFileDto } from '@neutrinos/idp-inference-sdk';

const downloadFileDto: IDownloadFileDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const result = await sdk.file.root.downloadFile(downloadFileDto);
  console.log('File downloaded:', result);
} catch (error) {
  console.error('Error downloading file:', error);
}
```

**JavaScript**

```code
const downloadFileDto = {
  token: 'your-auth-token',
  file_id: '64b91a8f5d2a0f0012bfcabc',
};

try {
  const result = await sdk.file.root.downloadFile(downloadFileDto);
  console.log('File downloaded:', result);
} catch (error) {
  console.error('Error downloading file:', error);
}
```
