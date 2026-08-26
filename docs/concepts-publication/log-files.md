# Types of Logs

<https://documentation.neutrinos.com/articles/#!concepts-publication/log-files>

Log files are useful in debugging and auditing applications and their flows.

### Types of Logs

Neutrinos Studio supports the following types of logs:

- **Error:** Records critical errors that are encountered by the server app.
- **Warn:** Records potential warnings. Warn logs should be used when a server app still has the chance to heal itself or the issue can wait a day or two to be fixed.
- **Info:** Records information about the execution of functions and event handlers and state of the flow variables.
- **Verbose: **Records more information than the usual logging mode. Verbose means using more words than necessary. Verbose logging options are usually enabled specifically for troubleshooting because they create large log files and can slow down performance.
- **Debug: **Records database operations, system processes, and errors that occur when executing a server flow or running unit tests.
- **Silly:** Record everything which includes function calls, actions, variables, and all extra information.

### Log Levels

Log levels are ordered based on their severity. In Neutrinos Studio, the following log levels are assigned to different logs:

```markdown
Error: 0,
Warn: 1,
Info: 2,
Verbose: 3,
Debug: 4,
Silly: 5
```

If you choose the log level - **E****rror Log**, only the error log will be selected. If you choose a higher priority, for example-** I****nfo Log**, then **E****rror**, **W****arn**, and** I****nfo** log types are selected. If you choose **S****illy log**, all the log types are selected.

By default, the **Debug** log is selected when you create an app. This includes logging error logs, info logs, warn logs, and verbose logs for the server app.
