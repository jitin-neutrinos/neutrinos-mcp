# Platform crashes while launching Studio

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/platform-crashes-while-launching-studio>

This error occurs on start-up of the Neutrinos Studio when the machine on which the Neutrinos Studio is running is not able to reach the npm registry to install the default plugins.

![](/resources/Storage/how-to-articles-8/how-2021-12-29-1.png)

Check the reasons mentioned below:

1. Internet connection to the machine is very slow

- Try to manually run npm install command in the .neutrinos/plugins/marketplace-components directory
- Change the reInstallTemplates setting in <OS_HOME_DIR>/.neutrinos/settings.json to true
- Restart the neutrinos studio

2. Proxy setting for the network blocks access to *.neutrinos.co or registry.npm.org domains

- Allow access to above mentioned domains by configuring the appropriate proxy settings.
- [Set up proxy config for studio](/articles/studio-guide-8/setup-proxy-on-neutrinos-studio).

3. Or, backup <OS_HOME_DIR>/.neutrinos directory, delete it and restart the Neutrinos Studio.

| ![Warning](/resources/Storage/how-to-articles-8/warning.png) | This will remove all the Store plugins installed by the user. |
| --- | --- |
