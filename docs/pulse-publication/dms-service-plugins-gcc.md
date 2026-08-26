# Features

<https://documentation.neutrinos.com/articles/#!pulse-publication/dms-service-plugins-gcc>

The Alpha Module DMS Service is a comprehensive Document Management System service that provides powerful capabilities for managing documents, files, folders, search operations, and downloads in Alpha applications. It offers a complete solution for document lifecycle management with support for metadata handling, file operations, and advanced search capabilities.

### Features

- File Management: Upload, download, update, and delete files with metadata
- Folder Operations: Create, manage, and organize document folders
- Advanced Search: Powerful search capabilities with pagination and filtering
- Metadata Handling: Comprehensive file metadata management and updates
- Download Management: Efficient file download operations with progress tracking
- File Validation: Built-in file type validation and security checks
- Pagination Support: Built-in pagination for large result sets

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

#### Basic DMS Service Access

```javascript
// Access DMS service via ap.dmsService
const dmsService = ap.dmsService;

// Access different service modules
const searchService = dmsService.searchDef;
const downloadService = dmsService.downloadDef;
const fileService = dmsService.fileDef;
const folderService = dmsService.folderDef;
```

#### File Operations

#### Upload File

```javascript
// Upload a new file with metadata
const uploadArgs = {
  relativePath: '/documents/projects',
  properties: {
    title: 'Project Report',
    description: 'Quarterly project status report',
    category: 'reports',
    tags: ['project', 'quarterly', 'status']
  },
  options: {
    overwrite: false,
    createPath: true
  },
  fileConfig: {
    acceptedFileTypes: ['.pdf', '.docx', '.xlsx'],
    maxFileSize: 10485760 // 10MB
  },
  validator_token: 'your-validation-token'
};

try {
  const result = await dmsService.fileDef.uploadFile(uploadArgs);
  console.log('File uploaded successfully:', result);
} catch (error) {
  console.error('Upload failed:', error);
}
```

#### Add File Metadata

```javascript
// Add metadata to an existing file
const metadataArgs = {
  relativePath: '/documents/projects',
  metadata: {
    author: 'John Doe',
    department: 'Engineering',
    projectCode: 'PRJ-001',
    reviewDate: '2024-01-15'
  },
  options: {
    createPath: true,
    overwrite: false
  },
  fileConfig: {
    acceptedFileTypes: ['.pdf', '.docx']
  },
  validator_token: 'your-validation-token'
};

const result = await dmsService.fileDef.addFileMetadata(metadataArgs);
console.log('Metadata added:', result);
```

#### Update File Metadata

```javascript
// Update existing file metadata
const updateArgs = {
  nodeId: 'node-123',
  fileName: 'project-report.pdf',
  majorVersion: true,
  metadata: {
    status: 'reviewed',
    reviewer: 'Jane Smith',
    reviewDate: '2024-01-20',
    comments: 'Approved with minor changes'
  },
  fileConfig: {
    acceptedFileTypes: ['.pdf']
  },
  validator_token: 'your-validation-token'
};

const result = await dmsService.fileDef.updateFileMetadata(updateArgs);
console.log('Metadata updated:', result);
```

#### Delete File

```javascript
// Delete a file
const deleteArgs = {
  nodeId: 'node-123',
  fileName: 'project-report.pdf',
  validator_token: 'your-validation-token'
};

const result = await dmsService.fileDef.deleteFile(deleteArgs);
console.log('File deleted:', result);
```

#### Search Operations

#### Basic Search

```javascript
// Search for nodes
const searchArgs = {
  query: 'project report',
  maxItems: 20,
  skipCount: 0,
  pageNumber: 0,
  pageSize: 20
};

const searchResult = await dmsService.searchDef.searchNode(searchArgs);
console.log('Search results:', searchResult);
```
