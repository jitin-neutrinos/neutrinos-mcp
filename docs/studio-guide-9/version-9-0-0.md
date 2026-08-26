# Locales:

<https://documentation.neutrinos.com/articles/#!studio-guide-9/version-9-0-0>

Here is a list of new features and enhancements introduced in Neutrinos Studio version 9.0.0:

### Locales:

- User can access the added languages in the locales through `page.locales.languages`.
- User can add new locale entry to an already existing group.
- User cannot add duplicate key at the root level as well as with in the group.

### Dependencies:

- `**d3**` dependency changes
  - `**d3**` dependency has been removed for any new apps created in version **9.0.0**.
  - For the old apps that are migrated to **9.0.0**, d3 will be converted as custom dependency.
- Angular version support upgraded to **13.x.x**
- Nodejs version support upgraded from **14.x.x** to **16.x.x**
- Signature widget component dependency has been upgraded.
  - `signature_pad` to **'4.0.7'**
  - Added new events `(beginStroke)`, `(endStroke)`,`(beforeUpdateStroke)` and `(afterUpdateStroke)`, and removed `[onBegin]` and `[onEnd]` properties.
  - Refer manual migration guide on how to update this component attributes.

### Cordova:

- Cordova 11 is now required to build iOS and Android apps.
- Upgraded platforms engines to the latest versions.
- Upgraded the default Cordova plugins to support Cordova 11.

## Nodes:

The following nodes and dependencies have been upgraded.

### Common:

- Async
  - User can navigate to the start node from Async node’s attribute window.
  - User can now add the multiple same flow calls.

### Server:

- MongoDB
- GlobalMongoSession
- SQL The Following new properties have been added:  The following properties have been removed from the MSSQL configuration
  - idleTimeoutMillis (defaults to 30000)
  - trustServerCertificate (defaults to true)
  - maxWaitingClients
  - fifo
  - priorityRange
  - autostart
  - evictionRunIntervalMillis
  - numTestsPerRun
  - softIdleTimeoutMillis
- EmailOut
- SOAP
- CSV

### 

### Bug Fixes

To learn about bug fixes, see [Release 9.0.0](/smart/project-change-log/release-9-0-0)
