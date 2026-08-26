# Interface: IClassificationDocumentUploadToBatchDto

<https://documentation.neutrinos.com/articles/#!ai-hub/iclassificationdocumentuploadtobatchdto>

# Interface: IClassificationDocumentUploadToBatchDto

Defined in: [services/classification/dto/document-upload-batch.dto.ts:32](https://bitbucket.org/bhivedevs/idp-inference-sdk/src/master/src/services/classification/dto/document-upload-batch.dto.ts#lines-32)

DTO for uploading a document for classification within a batch.

Either `file_path` or `file_id` must be provided. If both are present, `file_id` takes precedence.
