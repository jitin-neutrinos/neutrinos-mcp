# Master Data Versioning

<https://documentation.neutrinos.com/articles/#!pulse-publication/master-data-versioning>

Versioning of a Master Data File is the practice of maintaining and managing different versions of a dataset over time. Each update generates a new version of the file, following a structured versioning format such as 1.0.0, 1.0.1, and so on.

If a Master Data file is created using an API, its versioning and updates can be managed by configuring a cron to automate periodic updates. For more details on updating master data via an API, see [Updating Master Data Using a Cron](/articles/pulse-publication/add-master-data/a/h3__111809879). Similarly, if the file is created using an Excel sheet, updates can be managed by uploading a new version of the Excel file.

To update the information in master data created using excel follow the steps below:

1. Click **Master Data** from the sub-module navigation to open the Master Data lists page.
2. Navigate to the Master Data File that requires an update.
    ![master-data-version-details-page](/resources/Storage/pulse-publication/images/master-data-version-details.png)
3. Click the **Kebab** icon in the Actions column for the required file to view the list of available operations.
    ![master-data-versioning-kebab](/resources/Storage/pulse-publication/images/master-data-versioning-kebab.png)
4. Select **Upload New Version** to upload an updated Excel sheet containing the latest version of the Master Data File.
5. The pop-up window allows you to browse to select the excel file to be uploaded. Click **Next**.
    ![master-data-version-file-upload](/resources/Storage/pulse-publication/images/master-data-version-file-upload.png)
6. The headers from the Excel sheet are retrieved and mapped to the corresponding data types based on the values stored in each column. Review the data types for accuracy, then click **Next** to proceed with the upload process. Observe, that the version of the master data will be changed after the process.
    ![master-data-version-final](/resources/Storage/pulse-publication/images/master-data-version-final.png)

The GIF below illustrates the update process for the master data file:




 ![master-data-version-file-upload-gif](/resources/Storage/pulse-publication/images/master-data-version-upload-gif.gif)

To view a version, click the expansion button for the specific Master Data file. After expanding, details of all versions—including version number, status, cache status, availability date, and release notes (if available) - will be displayed.



![master-data-version-expand](/resources/Storage/pulse-publication/images/master-data-version-expand.png)

To download a specific version, click the **Kebab** icon in the Actions column after expanding the Master Data file.



![master-data-version-expand-download](/resources/Storage/pulse-publication/images/master-data-version-expand-download.png)

Alternatively, to download the latest version, click the **Kebab** icon in the Action column without expanding the file. To know more, see [Download Master File](/smart/project-neutrinos-reels/manage-data/a/h2__749525712).

[Next Topic](/articles/pulse-publication/testing)

[Previous Topic](/articles/pulse-publication/manage-data)
