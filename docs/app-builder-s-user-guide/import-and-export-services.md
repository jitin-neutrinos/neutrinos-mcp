# Export a Service

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/import-and-export-services>

Starting with release 7.9.0 of Neutrinos Studio, you can import and export [services](/smart/project-concepts/services) between applications by using the **Import **and** Export** icons on the respective service designers. You can export the entire service, or export selected service flows.

This feature helps reduce development time and facilitates the exchange of code between developers. It also facilitates the reusability of flows from one project /app to another.

### Export a Service

To export a service:

1. On the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662), press CTRL + A to select all the flows and click the **Export** icon on the [header of the canvas](/smart/project-concepts/canvas/a/h4_1341259387).
    Or, right-click the service on the Explorer and select **Export Service**.
    ![export service from explorer](/resources/Storage/app-builder-s-user-guide/export_service.png)
2. The export editor displays a JSON. It contains the details of the flows and their configurations.
3. Click **Export to Clipboard** to copy the JSON and share it with other developers.

### Import a Service

To import a service:

1. Click the **Import** icon on the [header of the canvas](/smart/project-concepts/canvas/a/h4_1341259387).
2. Import the service to the same application, or another application.
  - If you are importing a service in the same application, the exported JSON is already auto-populated in the **Import **editor. Click the **Import **button.
  - If you are importing a service to another application, paste the JSON that you copied from the export editor, make changes if any, and click the **Import** button.

While importing a service, you can click the **Add a new Service** in the **Import editor** to create a new service and import the flows to that service. Neutrinos Studio creates a service named import_service by default.

| ![Warning](/resources/Storage/app-builder-s-user-guide/warning.png) | Copying service/service flows from Client to Server Services Designer and vice versa is not allowed. Neutrinos Studio throws an error if you attempt to do so. |
| --- | --- |
