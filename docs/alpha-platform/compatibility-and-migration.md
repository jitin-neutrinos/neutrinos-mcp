# Export Projects

<https://documentation.neutrinos.com/articles/#!alpha-platform/compatibility-and-migration>

Compatibility issues and migration of existing custom code are handled efficiently to ensure seamless execution without errors. Projects containing existing custom code will continue to function without interruption. However, any new custom code must be added through the Global Custom Code module.

### Export Projects

To export a project, follow the steps below:

1. In Workflow Studio, navigate to the desired project and open it.
2. Use the required Global Custom Codes within the relevant task page, global page, or inbox as needed, alongside any existing custom codes.
3. Publish the project to tag it along with the existing custom code and the Global Custom Code used in that specific version.
4. Once the project is published with a specific tag, click the dropdown menu next to the Publish icon at the top of the page to view the available versions of the project.
5. Click the ellipsis icon next to the desired version, then select Export Project to export the project along with all tagged custom code associated with that specific version. Previously existing custom code runs based on the project's dependencies. In contrast, global custom code is mapped into the project with its own set of dependencies, which are bundled along with it during export.

### Import Projects

To import a project, follow the steps below:

1. On the Projects page, click the Create dropdown located at the top of the page.
2. The Create dropdown allows you to either create a new project or import an existing one. Refer to the [Get Started](/articles/alpha-platform/get-started) topic for more information on creating a new project.
3. Select the ZIP file of the project you want to import. The project may include both custom code and global custom code. Note: Previously mapped custom code runs against the project’s existing dependencies, while global custom code includes its own bundled dependencies.
4. Once the project is imported into the platform, it appears in the list of available projects.
