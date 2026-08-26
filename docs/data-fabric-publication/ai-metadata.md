# AI Metadata

<https://documentation.neutrinos.com/articles/#!data-fabric-publication/ai-metadata>

This section outlines the fields included in the AI_Metadata sheet of the Excel workbook.

| **Field** | **Description** | **Naming Convention** |
| --- | --- | --- |
| ObjectAPIName | The ObjectAPIName in AI_Metadata specifies the unique programmatic identifier of the object to which the AI metadata belongs. This field ensures that metadata configurations (such as AI annotations, predictions, model mappings, or enrichment logic) are linked to the correct object | Type: String (alphanumeric with underscores).Use PascalCase or camelCase for entity names (depending on platform standards).Avoid spaces, special characters, or reserved keywords. |
| FieldAPIName | The FieldAPIName in AI_Metadata specifies the unique identifier of the field within the object that the AI metadata applies to. This allows AI services to target specific fields for enrichment, prediction, classification, or other AI-driven operations. | Type: String (alphanumeric, underscores allowed).Use camelCase or PascalCase for field names, depending on platform standards.Avoid spaces, special characters, or reserved keywords. |
| SemanticType | The SemanticType in AI_Metadata specifies the logical classification or meaning of a field within an object. It allows AI models and other intelligent services to understand the context or type of data being processed, enabling more accurate predictions, enrichment, and analysis. | Type: String (from predefined semantic type list). |
| Redact | The Redact field specifies whether the data in a particular object field should be masked or obfuscated when accessed, processed, or transmitted, especially in AI workflows. This is critical for protecting sensitive or personally identifiable information (PII) while still allowing AI models to work on anonymized or tokenized data. | Type: Boolean (true / false). |
| EmbeddingStrategy | The EmbeddingStrategy field defines the method or approach used to generate vector embeddings for a specific field in an object. Embeddings transform raw data (such as text, categorical, or numerical fields) into a mathematical vector representation that AI models can process for similarity search, recommendations, clustering, or predictive tasks. | Type: String (predefined strategy name). |
| EmbeddingDim | The EmbeddingDim field specifies the dimensionality of the vector embeddings generated for a particular field in an object. In AI and machine learning contexts, each field that is converted into a vector (via an embedding strategy) has a fixed number of dimensions, which determines the size of the vector representation used for similarity calculations, clustering, or predictive modeling. |  |
