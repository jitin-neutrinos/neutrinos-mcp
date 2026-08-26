# Properties

<https://documentation.neutrinos.com/articles/#!ai-hub/properties-1-2-3-4-5-6-4>

## Properties

### _id

> **_id**: `string`

Defined in: [services/file/dto/file-info.dto.ts:78](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-78)

MongoDB ObjectId of the uploaded file.

Used internally for database lookups and operations.

### file_name

> **file_name**: `string`

Defined in: [services/file/dto/file-info.dto.ts:85](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-85)

Original name of the uploaded file, including its extension.

Example: `"report.csv"`

### size

> **size**: `number`

Defined in: [services/file/dto/file-info.dto.ts:92](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-92)

Size of the file in bytes.

Example: `1048576` for 1MB

### mime_type

> **mime_type**: `string`

Defined in: [services/file/dto/file-info.dto.ts:99](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-99)

MIME type of the file, used for content-type handling.

Example: `"image/png"`, `"application/pdf"`

### file_url

> **file_url**: `string`

Defined in: [services/file/dto/file-info.dto.ts:108](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-108)

Direct access URL for the uploaded file.

May be a public CDN link or a signed internal URL based on configuration.

Example: `"https://cdn.example.com/files/document.pdf"`

### file_uuid

> **file_uuid**: `string`

Defined in: [services/file/dto/file-info.dto.ts:117](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-117)

Universally unique identifier (UUID) for the file.

Used for cross-service tracking and deduplication.

Example: `"f47ac10b-58cc-4372-a567-0e02b2c3d479"`

### created_by

> **created_by**: `string`

Defined in: [services/file/dto/file-info.dto.ts:124](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-124)

Username or identifier of the user who created the file record.

Typically reflects the owner or system user.

### uploaded_by

> **uploaded_by**: `string`

Defined in: [services/file/dto/file-info.dto.ts:131](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-131)

Email or identifier of the user who performed the file upload.

Useful in audit logs and traceability.

### created_at

> **created_at**: `string`

Defined in: [services/file/dto/file-info.dto.ts:138](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-138)

ISO 8601 timestamp of when the file record was created.

Example: `"2025-07-09T10:15:30.123Z"`

### updated_at

> **updated_at**: `string`

Defined in: [services/file/dto/file-info.dto.ts:145](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/file/dto/file-info.dto.ts#lines-145)

ISO 8601 timestamp of the last update to the file record.

Example: `"2025-07-09T10:20:15.456Z"`
