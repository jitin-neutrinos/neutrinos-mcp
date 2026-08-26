# SSD Server is not running in port 8081

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/ssd-server-is-not-running-in-port-8081>

This error can occur for the following reasons:

**Failure to connect to a Database**

Consider the below mentioned steps to resolve this issue.

1. Check if the database server is running.
2. Check if the connection URL is correct.
3. If the database config which is causing the issue is not being used, disable the dbconfig through its attribute window.

**Compilation Error**

1. This is most likely to arise from user-written code in the **Script** node**.**

- The written code is treated as typescript compiled down to Javascript.
- Refer to the official guide to decipher typescript errors here: [https://www.typescriptlang.org/docs/handbook/2/understanding-errors.html](https://www.typescriptlang.org/docs/handbook/2/understanding-errors.html)

2. The stack trace of the error often contains the function name from which the error was thrown. Users can use this function name to search for the node using global node search Ctrl/Cmd+P and fix it.

**Address in Use**

This issue occurs when another process, most commonly another SSD server, is already using the port in which the server is starting.

![](/resources/Storage/how-to-articles-8/how-2021-12-29.png)

To resolve this issue,

1. You can kill the other process that is using the port and then start the server app again
2. Or, change the port configured by changing the SSD_DEFAULT_PORT environment variable value. (Ex. 8082)
3. Finally, restart your machine and then start the server app.
