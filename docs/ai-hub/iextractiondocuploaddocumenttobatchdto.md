# Interface: IExtractionDocUploadDocumentToBatchDto

<https://documentation.neutrinos.com/articles/#!ai-hub/iextractiondocuploaddocumenttobatchdto>

# Interface: IExtractionDocUploadDocumentToBatchDto

Defined in: [services/extraction/doc/dto/document-upload-batch.dto.ts:21](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/doc/dto/document-upload-batch.dto.ts#lines-21)

DTO for uploading a document for extraction within a batch.

Either `file_path` or `file_id` must be provided. If both are present, `file_id` takes precedence.
