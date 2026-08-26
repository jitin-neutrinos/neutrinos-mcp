# Methods

<https://documentation.neutrinos.com/articles/#!ai-hub/methods-1-2-3-4-5-6>

## Methods

### uploadFile()

> **uploadFile**(`input`): `Promise`<[`IFileInfoResponse`](../interfaces/IFileInfoResponse.md)>

Defined in: [services/file/file.service.ts:126](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/file.service.ts#lines-126)

Uploads a file to the backend via multipart/form-data.

The file is read from the local filesystem using the `file_path` and sent as a buffer.

#### Parameters

##### input

[`IFileUploadDto`](../interfaces/IFileUploadDto.md)

The DTO containing the full local file path.

#### Returns

`Promise`<[`IFileInfoResponse`](../interfaces/IFileInfoResponse.md)>

A promise that resolves with metadata of the uploaded file.

#### Throws

If the file does not exist at the provided path.

#### Example

```code
const result = await fileService.uploadFile({
  token: '1234567890abcdef',
  file_path: '/home/user/data.xlsx'
});
console.log(result.file_url); // Use to preview/download
```

### getFileList()

> **getFileList**(`input`): `Promise`<[`IFileListResponse`](../interfaces/IFileListResponse.md)[]>

Defined in: [services/file/file.service.ts:185](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/file.service.ts#lines-185)

Retrieves a paginated list of all uploaded files, with optional sorting.

This method fetches metadata for uploaded files, including file name, size, type,
 upload time, and public access URL.

#### Parameters

##### input

[`IFileListDto`](../interfaces/IFileListDto.md)

The pagination and sorting options.

#### Returns

`Promise`<[`IFileListResponse`](../interfaces/IFileListResponse.md)[]>

A promise resolving to an array of file metadata objects.

#### Remarks

- The sorting order can be `'asc'` or `'desc'` based on file creation time.
- Pagination supports `page_number` (zero-based) and `page_size`.

#### Example

```code
const files = await fileService.getFileList({
  token: '1234567890abcdef',
  page_number: 0,
  page_size: 20,
  sort: 'asc'
});
console.log(files); // Logs an array of file metadata
```

### getFileInfo()

> **getFileInfo**(`input`): `Promise`<[`IFileInfoResponse`](../interfaces/IFileInfoResponse.md)>

Defined in: [services/file/file.service.ts:219](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/file.service.ts#lines-219)

Retrieves information about a specific file by its ID.

This method fetches detailed metadata for a file, including name, size, type,
 upload time, and public access URL.

#### Parameters

##### input

[`IFileInfoDto`](../interfaces/IFileInfoDto.md)

The file ID to retrieve information for.

#### Returns

`Promise`<[`IFileInfoResponse`](../interfaces/IFileInfoResponse.md)>

A promise resolving to the file metadata object.

#### Example

```code
const fileInfo = await fileService.getFileInfo({
  token: '1234567890abcdef',
  file_id: 'abc123',
});
console.log(fileInfo); // Logs the file metadata
```

### downloadFile()

> **downloadFile**(`input`): `Promise`<`Readable`>

Defined in: [services/file/file.service.ts:244](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/file.service.ts#lines-244)

Downloads a file by its unique file ID.

#### Parameters

##### input

[`IFileDownloadDto`](../interfaces/IFileDownloadDto.md)

DTO containing the file ID.

#### Returns

`Promise`<`Readable`>

Stream of the file content.

#### Example

```code
const response = await fileService.downloadFile({
  token: '1234567890abcdef',
  file_id: 'abc123',
});
response.pipe(fs.createWriteStream('./downloaded.pdf'));
console.log('Downloaded file:', './downloaded.pdf');
```

### deleteFile()

> **deleteFile**(`input`): `Promise`<[`IFileDeleteResponse`](../interfaces/IFileDeleteResponse.md)>

Defined in: [services/file/file.service.ts:267](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/file.service.ts#lines-267)

Deletes a file permanently from the server using its ID.

This operation is irreversible.

#### Parameters

##### input

[`IFileInfoDto`](../interfaces/IFileInfoDto.md)

DTO containing the file ID.

#### Returns

`Promise`<[`IFileDeleteResponse`](../interfaces/IFileDeleteResponse.md)>

A promise resolving to a confirmation response.

#### Example

```code
await fileService.deleteFile({ token: '1234567890abcdef', file_id: 'abc123' });
```
