# ValueSets

<https://documentation.neutrinos.com/articles/#!hypha/valuesets-metadata>

This section outlines the fields included in the ValueSets sheet of the Excel workbook.

| **Field  ** | **  Description  ** | **  Naming Convention** |
| --- | --- | --- |
| ValueSetAPIName | The ValueSetAPIName is a unique identifier assigned to a Value Set. A Value Set is typically used to define a controlled list of permissible values (e.g., dropdown options, status codes, categories) that can be associated with fields in an object. | Format:    Must be a string value.    Should be unique across the environment.    Commonly follows a CamelCase without spaces/      Allowed Characters:    Alphanumeric characters    Underscore ( _ ) may be allowed for readability/    No spaces, special symbols, or reserved keywords. |
| Label | The Label of a Value Set is the human-readable display name that identifies the Value Set in the user interface (UI) and documentation. The Label is intended for end users, administrators, and business stakeholders to easily recognize and understand the purpose of the value set. | Format    String value.    Written in Title Case (capitalize the first letter of major words).      Allowed characters:    Alphanuemric characters (A-Z, a-z, 0-9)    Spaces are permitterd    Limited punctuation such as hyphens, may be used sparingly. |
| Description | The Description of a Value Set is a textual explanation that documents the purpose, scope, and intended usage of the Value Set. It provides additional context to administrators, developers, and business users beyond what is expressed in the Label or ValueSetAPIName. | Format:    Free-text string, typically one or more sentences.    Should be written in sentence case (capitalize only the first word and proper nouns).    Can include spaces, punctuation, and extended details.      Allowed characters:    All standard alphanumeric characters (A–Z, a–z, 0–9).    Spaces, punctuation, and special characters are permitted.    Avoid non-standard symbols or markup unless supported by the platform. |
