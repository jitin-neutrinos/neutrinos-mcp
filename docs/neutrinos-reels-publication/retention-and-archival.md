# Working

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/retention-and-archival>

This section defines how long process and process instance data are retained in the primary database and when they are archived or purged to optimize system performance, storage utilization, and compliance.




 ![pulse-settings-retension-archival-landing1](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-retension-archival-landing1.png)

- **Process Instance Archival**: Defines the duration after which a process instance is moved from the primary database to the archive database. Once the specified time elapses after process completion, the instance is eligible for archival.
- **Process Instance Retention**: Specifies how long a process instance remains available in the system (archived storage) before it is permanently deleted. After the retention period expires, the system purges the process instance data from storage.
- **Case Instance Archival**: Defines when a case instance is moved from the primary database to the archive database. After the specified duration post case completion/closure, the case is archived.
- **Case Instance Retention**: Determines how long case data is retained before being permanently deleted.
- **Archive Database Configuration**: This section defines the target database where archived data is stored.
  - **Enable Policy**: Toggle to enable or disable archival functionality. When enabled, Archivals are executed.
  - **Host**: Fully qualified domain name (FQDN) or IP address of the archive database server. For example: platform-dev-db.****.database.****.com
  - **Port**: Network port used to connect to the database. For example, 5432 for PostgreSQL
  - **Database Name**: Name of the database designated for storing archived data. For example, archive-db
  - **User Name**: Database user with sufficient privileges to write archived records.
  - **Password**: Authentication credential for the specified database user.
  - **Schema**: Logical namespace within the database where archive tables reside.
  - **Enable SSL**: Enables secure (encrypted) communication between the application and the archive database.
- **Test Connection**: Validates connectivity to the archive database using the specified configuration and displays a toast notification upon successful validation.

The next section of the configuration includes a dashboard that summarizes process data, cases, audit logs, and archived records. It also indicates the volume of data eligible for archival, such as completed processes older than 2 days and audit logs older than 2 days.




 ![pulse-settings-retension-archival-landing-dashboard](/resources/Storage/neutrinos-reels-publication/images/pulse-settings-retension-archival-landing-dashboard.png)

## Working

To configure Retention and Archival settings, provide values for the required parameters as described in the first section of this topic. After completing the configuration, click Save at the bottom of the page to persist and apply the settings across all processes within the project.

## Unarchive

Processes archived based on the Global Settings configuration are moved from the primary database to the archived database. This helps optimize storage utilization by separating inactive or completed processes from active data while retaining them for future reference.

Archived processes can be accessed and tracked from the Logs page under the Archived Processes tab.




 ![pulse-logs-achival-retention](/resources/Storage/neutrinos-reels-publication/images/pulse-logs-achival-retention.png)

| ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png) | Note: If no logs are available, the system displays an empty page with the message, "No logs found." |
| --- | --- |

To view archived processes, follow the steps below:

1. From the left navigation panel, select Logs to open the Logs page.
2. On the Logs page, select the Archival/Retention tab.
3. This tab lists all archived processes and their associated details. It also allows you to restore processes from the archived database to the primary database.
