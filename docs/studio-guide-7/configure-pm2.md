# Configure PM2

<https://documentation.neutrinos.com/articles/#!studio-guide-7/configure-pm2>

A [process manager](/smart/project-concepts/process-manager) helps in keeping your application alive so that users can access them without downtime. On Neutrinoss Studio, you can configure any process manager for your application. The most popular process managers include:

- Forever
- PM2
- StrongLoop Process Manager (Strong-PM)
- SystemD

Presently, Neutrinos Studio provides an editor to configure the PM2 [process manager](/smart/project-concepts/process-manager) and manage the settings for the server app that you create.

If you run your applications with PM2:

- It will automatically restart your application if it crashes.
- It will keep a log of your unhandled exceptions
- With one command, it can ensure that it restarts the applications that it manages when the server reboots.
- It will run multiple processes with multiple cores of CPU to achieve a Load Balancer like effect.
- It provides information, including restart number, CPU usage, memory usage, process id, etc.
- It allows auto-restart under specific conditions, such as ‘up-time, ‘memory usage’, etc.
- It provides a simple deployment method, and support multiple server deployments

### Configure PM2

To configure PM2 for your server application, click **Settings** on the editor pane of Neutrinos Studio, and select **PM2**. All the configurations are mentioned below which is divided into two sections:

- General settings - where you can perform some general process manager settings.
- Advanced settings - where you can perform configurations related to your server instances.

#### General Settings

To configure the General settings:

- Select the checkbox of the **fields** that you want to configure under the general settings.
- Fill in the **value** for the fields.

The general settings that you can configure are:

- **name**: The name of the application. This is the name of the app displayed on the PM2 dashboard.
- **script**: The script to run the app. For example, ./api or /app.js
- **cwd**: The directory from which the application should be launched. For example, /var or /www
- **interpreter**: Interprets the absolute path of node.js. For example, /usr/bin/python .
- **interpreter_args**: The options to pass to the interpreter. This can be any arguments you pass to the node.js interpreter.
- **node_args**: Any arguments that we pass to the node.js application. For example, –harmony.

#### Advanced settings

To configure Advanced settings:

- Tick the checkbox of the **fields** that you want to configure under the advanced settings.
- Fill in the** value** for the fields.

The advanced settings that you can configure are:

- **instances**: The number of application instances that should be launched.
- **exec_mode**: The mode to start the execution of the application. It can be **cluster** or **fork**.
  - Node.js is single-thread. That means only 1 core of your CPU can execute the node application. That is the default fork mode.
  - The cluster mode allows the application to be scaled across all CPUs available, without any code modifications. This greatly increases the performance and reliability of your applications, depending on the number of CPUs available.
- **watch(true/false)**: Set to True or False to enable the watch to restart your application when a file is modified in the current directory or in its subdirectories.
- **ignore_watch**: If the watch is enabled, specify the folders to ignore from watching.
- **max_memory_restart**: Specify the maximum memory. For example, **150M**. If this value exceeds, the application will be restarted.
- **env**: Specify the environment variables for the application. For example,** NODE_ENV**, **development**, **ID**, etc.
- **env_**: Specify the object that restarts the application.
- **Instance_var: I**n a clustered environment, by default NODE_APP_INSTANCE is the variable mapped to get the instance id. To rename the default variable name, instance_var is used. For example, instance_var : "INSTANCE_ID". Instead of using process.env.NODE_APP_INSTANCE you can use process.env.INSTANCE_ID.

All the configured settings are stored in the **PM2 ecosystem.config.js **file as a single app configuration in the server folder of your app.

### Start PM2

| ![Information](/resources/Storage/studio-guide-7/info.png) | A server application should be compiled before you start PM2. |
| --- | --- |

You can start PM2 by navigating to the server folder of your app and executing the following command:

```markdown
pm2 start ecosystem.config.js
```

### Monitor and manage apps on PM2

After you start PM2, you can:

- Monitor the app and view the realtime dashboard on the terminal Copy CodeMarkdown$ pm2 monit
- List all running apps Copy CodeMarkdownpm2 [list|ls|l|status]
- Restart the apps Copy CodeMarkdown//To restart an application
   $ pm2 restart api
   //To restart all applications
   $ pm2 restart all
   //To restart multiple apps at once
   $ m2 restart app1 app3 app4
- Stop apps Copy CodeMarkdown//To stop a specified application
   $ pm2 stop api
   $ pm2 stop [process_id]
   //To stop them all
   $ pm2 stop all
   //To stop multiple apps at once:
   $ pm2 stop app1 app3 app4
- Delete apps Copy CodeMarkdown//To stop and delete an app
   $ pm2 delete api
   //To delete all apps
   $ pm2 delete all
