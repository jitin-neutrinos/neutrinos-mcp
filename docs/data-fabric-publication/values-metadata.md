# Values

<https://documentation.neutrinos.com/articles/#!data-fabric-publication/values-metadata>

This section outlines the fields included in the Values sheet of the Excel workbook.

| **Field** | **Description** | **Naming Convention** |
| --- | --- | --- |
| ValueSetAPIName | The ValueSetAPIName for a Value represents the association of an individual value to its parent Value Set. Establishes a programmatic relationship between a Value and its Value Set. | Type: String (must correspond to an existing Value Set).    Format:    Use PascalCase or CamelCase, consistent with the parent Value Set’s API name.    Must be unique across Value Sets, but multiple values can share the same ValueSetAPIName if they belong to the same set.    No spaces or special characters (underscores _ may be allowed). |
| Value | The Value field represents the actual entry or option within a Value Set. The Value is what the system stores or uses in processing | Type: String (can be alphanumeric).    Format:    Typically PascalCase or CamelCase for consistency, especially in API and integration contexts. |
| Label | The Label of a Value represents the user-friendly display name for a particular entry within a Value Set. While the Value is used programmatically and stored in the system, the Label is what is shown to end users | Type: String (human-readable text).    Format:    Written in Title Case (capitalize the first letter of major words).    Spaces between words are allowed.    Limited punctuation (e.g., hyphens -, parentheses ()) may be used sparingly for clarity. |
| IsActive | The IsActive field indicates whether a particular Value within a Value Set is active and available for use in the system. This allows administrators to deactivate values without deleting them, preserving historical data and maintaining integrity in existing records. | Type: Boolean (true / false or Yes/No). |
| SortOrder | The SortOrder field determines the display sequence of Values within a Value Set in the user interface or reports. It allows control over the ordering of options. | Type: Integer (whole number)    Format:    Positive integers (1, 2, 3, …) are used to define sequence.    Zero (0) may be allowed in some implementations to denote highest priority or default position.    No decimals or negative numbers unless specifically supported. |
