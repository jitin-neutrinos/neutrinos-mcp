# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/agenda-node>

The **Agenda **node is a MongoDB job scheduler. It uses the MongoDB database to store jobs and persist scheduled tasks so that even if the server goes down, the tasks will run at the specified time or intervals.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.5.0.Download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with any **Start node**.

### Associated Attributes

1. **Name:** The name of the job that is to be run.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Agenda Config: **The name of the configuration to connect to a MongoDB database.
  - If you have an existing configuration, choose that configuration from the drop-down list.
  - If you want to add a new configuration, select **Add new config** from the drop-down list and click the **Map** icon. See [Attributes for a new configuration](/articles/server-services-designer-8/agenda-node/a/h3_931954325) to learn about the properties.
4. **Run Job:** A drop-down list to select when to run a job. It has the following options:
  - **Periodic:** Runs the job at periodic intervals.
    - **Interval:** The time interval at which the job is to be run. You can express the interval in seconds, minutes, hours, days, weeks, months (assumes 30 days), and years (assumes 365 days). For example- **2 days and 4 hours**.
  - **Once: **Schedules a job, to run once, at a given time.
    - **Schedule: **The time at which the job should run. For example, enter a string such as **tomorrow at 5 pm,** or enter a date **Friday, 29 May 2021 05:50:06.**
  - **Now: **Runs the job immediately.
5. **Lock lifetime:** Interval in milliseconds indicating how long the job should stay locked for. A job will automatically unlock once a returned promise resolves/rejects (or if **done** is specified in the job signature).
6. **Priority:** Specifies the priority of the job. Enter a number or set the priority as lowest, low, normal, high, or highest. Higher priority jobs will run first. The priority mapping is as follows:

![Agenda priority mapping](/resources/Storage/server-services-designer-8/agenda_priority.png)

### Attributes for a New Configuration

Use these attributes to create a new configuration.

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name:** A display name for the configuration.
- **Address:** The URL of the MongoDB database. For example - **localhost:27017/agenda-test **or** mongodb://127.0.0.1/agenda **.
- **Collection:** The MongoDB collection name that is to be used to store the job entries. The Agenda node queries this collection to look for the jobs that are to be processed. Choose String and enter the collection name or choose env and map the environment variable that contains the collection name.
- **Process Every: **The frequency at which the node should query the database looking for jobs that need to be processed. Express the value in seconds, minutes, hours, days, weeks, months (assumes 30 days), and years (assumes 365 days). For example- **2 days and 4 hours**.
- **Max Concurrency: **The maximum number of jobs that can be running at any given moment. By default, max concurrency is set to 20.
- **Lock Limit: **Specify the maximum number of jobs that can be locked at any given moment. By default, the lock limit is 0. See the [npm Agenda](https://www.npmjs.com/package/agenda#defining-job-processors) documentation to learn more.
