# Add a Custom Task

<https://documentation.neutrinos.com/articles/#!studio-guide-7/create-custom-tasks>

Custom tasks are used to execute a set of commands without having to enter them in the command line. For example, you can create a custom task to execute the commonly used tasks such as performing pod install if you are building a mobile application.

### Add a Custom Task

To add a custom task for your application:

1. On the [Studio application page](/smart/project-concepts/studio-application-page), select** Custom tas**k from the [Task drop-down list](/smart/project-concepts/studio-application-page/a/h3_1314244609).
2. On the **Custom Task Details **editor:
  1. Enter the task name. For example, **install CocoaPods**.
  2. Enter the task or the command to be executed. For example, pod install. If you want to enter multiple commands, use && to join the commands. For example, npm i && npm run start-dev.
  3. Enter an optional description of the task.
  4. Select the type of custom command. If you select **Client**, the custom task gets executed only on the client application. If you select **Server**, the command gets executed on the server of the app.
  5. Click **Create**.

### Edit a Custom Task

To edit a custom task:

1. Expand the [Task drop-down list](/smart/project-concepts/studio-application-page/a/h3_1314244609) and hover on **Custom Task**.
2. Click the **Edit** icon next to the task.
3. Make changes to the task and click **Done**.

### Run a Custom Task

To run a custom task, select the task from the [Task drop-down list](/smart/project-concepts/studio-application-page/a/h3_1314244609) and click the **Run** icon. The command gets executed in the **client **or **server** folder of the app based on the type of custom command you selected when adding the command.
