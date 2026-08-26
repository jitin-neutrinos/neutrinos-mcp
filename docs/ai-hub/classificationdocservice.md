# Class: ClassificationDocService

<https://documentation.neutrinos.com/articles/#!ai-hub/classificationdocservice>

# Class: ClassificationDocService

Defined in: [services/classification/doc/classification-doc.service.ts:81](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/doc/classification-doc.service.ts#lines-81)

Provides APIs to perform document classification (e.g., PDFs, images).

Supports:

- Creating classification batches for document/file-based input
- Classifying a single document using a file path or file ID
- Listing classification results with optional merge behavior

Files can be passed directly from the local file system via `file_path`,
 or by referencing an uploaded file using `file_id`.
