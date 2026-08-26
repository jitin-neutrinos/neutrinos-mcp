# Startup Script

<https://documentation.neutrinos.com/articles/#!project-plugins-builder-guide/startup-script>

If you have a node-specific logic that is to be executed every time an application starts, you specify that in the Startup Script. This is an optional step while adding a node and is applicable only when building Server nodes.

The purpose of the Startup Script is to do some operation automatically when the server node is installed so that you don't have to do it manually every time. For example, the script might change some settings every time the node is loaded, or create a new connection every time the application starts so that the same connection can be reused multiple times.

To add a Startup Script, click the ****+**** icon next to the server node. For example:

Open the script. You will see the following methods (which are the same as that in the code generation file). Use them to write the logic that is to be executed at the start of the application.

- [generateImports()](/articles/project-plugins-builder-guide/code-generation/a/h4_1584156788)
- [generateSnippet()](/articles/project-plugins-builder-guide/code-generation/a/h4__1084950754)

```javascript
let BaseComponent = require('@jatahworx/bhive-toolkits').BaseComponent;module.exports = class newNodeStartup extends BaseComponent   {    generateImports()     {        /*Eg to import a util...=> rootPaths.pathToUtilsRoot + '/(gen package name)/nodeName/utilname'     return [{                      library: rootPaths.pathToUtilsRoot + '/neutrinos-sftp/59897528-50aa-e203-83db-4bd6c97d35af/sftp',       modules:[           "sftpUtil" // (class name from node utils)       ]     }]; */        return [];    }    generateSnippet()     {      /*Eg for node logic                                                           (confignode nodeName)      return `let configObj = this.sdService.getConfigObj('306d616b-3471-2452-0320-bdc8c7eae343', '${this.configId}')      let listUtil = new sftpUtil();      await listUtil.listUtilSftp(configObj,${this.remotePath},${this.pattern});      `;*/      return ``;    }};
```

**Example:**

This is the logic provided in the start script of the [ODBC](/smart/project-server-side-service-designer/odbc-node)node. It creates an ODBC connection when the application starts so that the same connection can be reused each time the node is executed. Therefore, saving application resources.

```javascript
let BaseComponent = require('@jatahworx/bhive-toolkits').BaseComponent;module.exports = class odbcConfigStartup extends BaseComponent {    generateImports() {        /*Eg to import a util...=> rootPaths.pathToUtilsRoot + '/(gen package name)/nodeName/utilname'     return [{                      library: rootPaths.pathToUtilsRoot + '/neutrinos-sftp/59897528-50aa-e203-83db-4bd6c97d35af/sftp',       modules:[           "sftpUtil" // (class name from node utils)       ]     }]; */        return [            {                library: './utils/neutrinos-odbc/bceb0727-1aba-fec0-e7a6-44b28b0c2938/odbcConnections',                modules: [                    "odbcConnections"                ]            }        ];    }    generateSnippet() {        /*Eg for node logic                                                             (confignode nodeName)        return `let configObj = this.sdService.getConfigObj('306d616b-3471-2452-0320-bdc8c7eae343', '${this.configId}')        let listUtil = new sftpUtil();        await listUtil.listUtilSftp(configObj,${this.remotePath},${this.pattern});        `;*/        return `            let odbcConnection = odbcConnections.getInstance();            const dbConfig = configNodes.default["2fc6ea74-bab5-d069-3746-22cf1f749fa3"];            if (dbConfig) {                const dbConfigsList = Object.keys(dbConfig);                for (let i = 0; i < dbConfigsList.length; i++) {                                let dbOption = dbConfig[dbConfigsList[i]];                                               await odbcConnection.newConnection(dbOption, dbConfigsList[i]);                }            }           `;    }};
```
