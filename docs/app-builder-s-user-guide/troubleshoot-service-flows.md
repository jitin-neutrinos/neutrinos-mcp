# Using the Catch Node

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/troubleshoot-service-flows>

You can troubleshoot any service that you design on Client and Server Services Designer using the **Catch **and **Log** nodes in the respective designers.

### Using the Catch Node

You can debug and handle exceptions for any service flows that you have created by using the [Catch node](/smart/project-server-side-service-designer/catch-node).

You can handle exceptions for all the nodes by applying the **Catch** node to all nodes in the canvas. Or apply the **Catch** node to selected nodes in the canvas.

If a node throws an error, the catch node catches the **error** object which you can use to debug.

### Using the Log Node

You can also use the [Log node](/smart/project-server-side-service-designer/log-node) in your server flows to log errors which will get logged on the **Developer Tools -> Console **of the Browser. You can [configure the log level](/articles/app-builder-s-user-guide/configure-logger)of the flow, and Neutrinos will log the information based on the log level that you select.
