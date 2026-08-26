# Mapping the Environment Property

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/configure-logger>

Neutrinos Studio allows you to [configure logger settings](/smart/project-concepts/log-files) for the server apps that you create using Neutrinos Studio. Using this editor, you can select the [log types](/smart/project-concepts/log-files/a/h3__1248978043) and [log levels](/smart/project-concepts/log-files/a/h3_2119234986).

To access Logger settings, click **Settings** on Neutrinos Studio and select **Logger**.

### 

### Mapping the Environment Property

### 

You use the** Map Env Property **setting to save the log level that you configure in the logger configuration file.

Once you choose the log level in this editor and save the app, this setting will be considered over the log level settings that you select in the [Log node](/smart/project-server-side-service-designer/log-node) of the Server Service Designer.

![Loglevel in the Log node](/resources/Storage/app-builder-s-user-guide/log_node_loglevel.png)

The **L****og Level** attribute in the** Log** node will only be enabled if you can choose a log priority level equal to or lesser than the one configured in the **Settings** editor. Else, **L****og Level** will be ignored.

#### Choose the Log Env Property

If you have an environment property that you have already created to store the log level, click the **Map Env Property** button, select the environment property from the drop-down list, and save the app. If you have not created an Environment property to indicate the log level:

1. navigate to the Environments editor and create the property.
2. Navigate back to Logger settings and select the log property.

See [Creating a property in the Environments editor](/articles/app-builder-s-user-guide/what-is-an-environment) for more details.

![Environment properties in Settings editor](/resources/Storage/app-builder-s-user-guide/logger_env.png)

### Log Output

You can choose where you want your log data to be displayed. By default, both **File** and **Console **are selected. The options you choose will be saved in the logger configuration file along with the log level.

You can find the log files in the **server/logs** folder of your app.
