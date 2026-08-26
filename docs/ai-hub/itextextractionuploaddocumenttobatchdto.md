# Interface: ITextExtractionUploadDocumentToBatchDto

<https://documentation.neutrinos.com/articles/#!ai-hub/itextextractionuploaddocumenttobatchdto>

# Interface: ITextExtractionUploadDocumentToBatchDto

Defined in: [services/extraction/text/dto/document-upload-batch.dto.ts:67](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/extraction/text/dto/document-upload-batch.dto.ts#lines-67)

DTO for uploading a text document to a text extraction batch.

Either `file_path` or `file_id` must be provided. If both are present, `file_id` takes precedence.
