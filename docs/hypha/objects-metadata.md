# Objects

<https://documentation.neutrinos.com/articles/#!hypha/objects-metadata>

This section of the topic outlines the fields in the Object sheet of the Excel:

| **Field  ** | **  Description  ** | **  Naming Convention** |
| --- | --- | --- |
| ObjectLabel | The ObjectLabel field defines the human-readable display name of the object. The ObjectLabel is user-facing and appears in the interface, reports, and object listings. It helps users quickly identify and understand the purpose of the object without needing to interpret technical identifiers. | Must be a string value      Use title case (capitalize the first letter of each main word)      Avoid abbreviations unless widely understood in the domain. |
| ObjectAPIName | The ObjectAPIName field specifies the unique identifier assigned to an object. This identifier is used by APIs and integrations to reference the object programmatically. Unlike the display name or description (which are user-facing), the ObjectAPIName acts as a system-level key that ensures consistent and unambiguous identification of the object across processes, flows, and API calls. | Must be unique within the environment to avoid conflicts. Note: Once created, changes to the ObjectAPIName may disrupt dependent APIs or integrations, so it should be carefully defined at creation time.      Must be a string identifier without spaces. Underscores (_) to replace spaces or separate words.      Case Sensitive |
| Description | Enter a brief description of the object being created. This field provides contextual information to help users understand the purpose or usage of the object. | The value must be a string.        Spaces are allowed between words.        Special characters (such as . , : ; - _ ( )) are permitted but should be used sparingly for readability. |
| Owner | The owner is typically the creator of the object, but can be reassigned if needed. This field establishes accountability by linking the object to a specific individual or team. | Use the system-generated User ID or Group ID.        No spaces are allowed.         Underscores (_) may be used if separation is required.         Case sensitivity depends on the system configuration. |
| Issues | The Issues field captures any known problems, anomalies, or alerts associated with the object. It is primarily used for tracking, troubleshooting, and governance purposes. By documenting issues at the object level, users, administrators, and data stewards can quickly identify potential risks, monitor data quality, and take corrective actions. |  |
