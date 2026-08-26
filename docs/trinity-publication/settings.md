# Logs

<https://documentation.neutrinos.com/articles/#!trinity-publication/settings>

The Settings screen is organized into three distinct sections to streamline configuration and management:

- [Logs](/articles/trinity-publication/settings/a/h4__104783573)
- [Insights](/articles/trinity-publication/settings/a/insig)
- Nexus

Each of these sections are described in detail below.

#### Logs

The Logger Configuration screen allows you to enter and update essential details for setting up and managing a logger. This ensures a proper connection and authentication by requiring the following information:

- Username: Enter your username in this required field.
- Password: Enter your password in this required field. The password is masked for security.
- Elastic IP: Enter the elastic IP address in this required field. The IP address is also masked for security.

![](/resources/Storage/trinity-publication/settings/Logger%20Configurations.png)

#### Insights

The All Insights screen is a key component within the settings section, designed specifically for managing insights. The fields within the insights section are explained below:

| Field | Description |
| --- | --- |
| Search bar | This feature allows users to search through their insights. |
| Environment | Lists the environments associated with each insight. |
| Url | Displays the URL for each insight. |
| Username | Shows the username associated with each insight. |
| Password | Displays the password, which is masked for security. |
| Edit | Provides an option to edit the insight details. |

**Creating an Insight**

To create an insight follow these steps:

1. Within the All Insights screen click on Create Insight.
   The create new insight pop-up window is displayed.
   ![](/resources/Storage/trinity-publication/settings/createinsight.png)
2. Enter the following details:
   - Select an environment from the drop-down list.
   - Enter url
   - Enter username
   - Enter password
3. Click Create to create an insight.

#### Nexus

Nexus is a Sonatype Artifactory repository manager, that allows you to store, distribute, and retrieve build artifacts whenever it’s required. Using Nexus, you can easily access and deploy build artifacts in an organization from a single location.

The fields within the nexus section are explained in the below table.

| Field | Description |
| --- | --- |
| Search | This feature allows users to search within nexus. |
| Label | The label assigned to each Nexus configuration. |
| Url | The URL associated with each Nexus configuration. |
| Username | The username used for accessing each Nexus configuration. |
| Password | The password for each Nexus configuration, displayed in a masked format for security. |
| Action | Options to edit or delete each Nexus configuration. |

![](/resources/Storage/trinity-publication/settings/allnexus.png)

**Creating Nexus Configuration**

To create a nexus configuration follow these steps:

1. Within the All Nexus screen, click on click on Create nexus configuration.
   The Create New Nexus Configuration pop-up window is displayed.
   ![](/resources/Storage/trinity-publication/settings/createnexusconfig.png)
2. Enter the following details:
   - Enter the label name.
   - Enter username.
   - Enter password.
   - Enter url.
3. Click Create to create a nexus configuration.
