# Mapping the Log Level to an Environment Property

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-logger>

When you use the [Log](/smart/project-server-side-service-designer/log-node) node, different levels of logs are logged throughout your server application.

Based on the application environment, you would want to limit or include certain logs according to their level. For example, you would not want to log **debug **logs in a production environment and want to log the logs above that level. So, you would set the log level to I**nfo** or **W****arn**. However, in a development environment, you would want to log all the logs in your application. Therefore, you would set the log level to **Silly**.

Such settings can be configured in the **Settings > Logger** editor by selecting the [log types](/smart/project-concepts/log-files/a/h3__1248978043) and [log levels](/smart/project-concepts/log-files/a/h3_2119234986). To access Logger settings, click **Settings** on Neutrinos Studio and select **Logger**.

![logger editor](/resources/Storage/studio-guide-9/logger_2.png)

Using this editor, you can decide the log level for each type of output channel (file or console).

Here is a helper diagram to visualize log levels:

- If the log level is set to **Error** in the Logger editor, the server app will only log that level logs.
- If the log level is set to **Verbose**, the server app will log **error**, **warn**, **info**, and **verbose** level logs. It does not log anything below that level, that is, **debug** and **silly** logs.
- If the log level is set to **silly**, the server app will log all the logs.

Once you choose the log level in this editor and save the settings, only the logs with the configured level and below will be logged. All log nodes with higher log levels are ignored.

You can override the log level of each log by selecting the log level in the **Log level** field of the **Log** node.

![Loglevel in the Log node](/resources/Storage/studio-guide-9/log_node_loglevel.png)

### Mapping the Log Level to an Environment Property

If you have an environment property that you have already created to store the log level, click the **Map Env Property** button, select the environment property from the drop-down list, and save the app. If you have not created an Environment property to indicate the log level:

1. navigate to the Environments editor and create the property.
2. Navigate back to Logger settings and select the log property.

See [Creating a property in the Environments editor](/articles/studio-guide-9/what-is-an-environment) for more details.

![Environment properties in Settings editor](/resources/Storage/studio-guide-9/logger_env.png)

### Log Output

You can choose where you want your log data to be displayed. By default, both **File** and **Console **are selected. The options you choose will be saved in the logger configuration file along with the log level.

You can find the log files in the **server/logs** folder of your app.
