# Class: ExtractionDocService

<https://documentation.neutrinos.com/articles/#!ai-hub/extractiondocservice>

# Class: ExtractionDocService

Defined in: [services/extraction/doc/extraction-doc.service.ts:142](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/extraction-doc.service.ts#lines-142)

Provides APIs to perform document extraction (e.g., PDFs, images).

Supports:

- Creating extraction batches for document/file-based input
- Extracting a single document using a file path or file ID
- Listing extraction results

Files can be passed directly from the local file system via `file_path`,
or by referencing an uploaded file using `file_id`.
