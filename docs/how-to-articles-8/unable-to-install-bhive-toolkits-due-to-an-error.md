# Unable to install Bhive-Toolkits due to an error

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/unable-to-install-bhive-toolkits-due-to-an-error>

This error occurs on start-up of the Neutrinos Studio when the machine on which the Neutrinos Studio is running when trying to install default plugins. Follow the steps mentioned below to resolve this issue.

**Slow Internet connection**

1. Try to manually run npm install command in the .neutrinos/plugins/marketplace-components directory and Restart the neutrinos studio.
2. Change the reInstallTemplates setting in <OS_HOME_DIR>/.neutrinos/settings.json to true and restart the neutrinos studio.
3. Or, backup <OS_HOME_DIR>/.neutrinos directory, delete it and restart the Neutrinos Studio.

| ![Warning](/resources/Storage/how-to-articles-8/warning.png) | This will remove all the Store plugins installed by the user and has to be re-installed. |
| --- | --- |
