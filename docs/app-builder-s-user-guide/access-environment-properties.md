# Access Environments-properties

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/access-environment-properties>

All the environment properties that you have defined on the Environments editor can be accessed on the page. If you want to add other environment properties, add them in the editor and save the editor.

To access the properties on pages, perform the following steps:

1. Open the page where you want to access the environment property that you have created.
2. Access the value of the env property using this.sys.getVal('<env_property>'). For example, to log the name of the app, navigate to the TS editor of the page and log the property like this:
