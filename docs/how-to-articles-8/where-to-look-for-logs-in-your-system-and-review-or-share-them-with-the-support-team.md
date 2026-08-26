# Where to look for logs in your system and review or share them with the support team

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/where-to-look-for-logs-in-your-system-and-review-or-share-them-with-the-support-team>

Neutrinos Studio logs can be found in <OS_HOME_DIR>/.neutrinos/logs/log.txt.

Users can also control the maximum log level that can be logged to this file by changing the log.file property in the <OS_HOME_DIR>/.neutrinos/settings.json file. By default this is set to "error"

Each log inside this `log.txt` consists of the following information:

1. Timestamp: The time when the error is logged.
2. process from which the log was written

- ”AD” - the UI process.
- "CORE" - The backend process with which the "AD" communicates.

3. data - miscellaneous data related to the functionality from which it was logged such as component, editor, node etc.

4. error - If the error is logged, the error stack trace with the message is logged.

Users can share this log.txt with the platform support team by writing to [support@neutrinos.co](mailto:support@neutrinos.co) for further help.
