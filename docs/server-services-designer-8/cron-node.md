# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/cron-node>

The **Cron** node is used to schedule a time-based job. That is, it can schedule a job to run periodically at fixed times, dates, or intervals. The intervals for the job is defined by the **Cron Expression**.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.4.0.    You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node. **

### Attributes Associated

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name: ** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field.
3. **Expression**: Enter the Cron expression. A Cron expression is a string that describes individual details of the schedule. The string contains the following fields, separated by white space:
    ![cron fields](/resources/Storage/server-services-designer-8/cron_fields.png)
    These fields can have the following values:
    **Field**
    **Value**
    Second
    0-59
    Minute
    0-59
    Hour
    0-23
    Day of month
    1-31
    Month
    1-12 (or names)
    Day of week
    0-7 (or names, 0 or 7 are Sunday)
    For example:
    ![Information](/resources/Storage/server-services-designer-8/info.png)
     Indicating the **Seconds **field in the expression is optional.
  - If you enter *** * * * * ***, the job runs every second.
  - If you enter *** ****1,2,4,5 * * * ***, the job runs every 1,2,4, and 5 minutes.
  - If you enter *** * * * January, September Sunday**, the job runs every Sunday of January and September.
  - If you enter ***/5 * * * * ***, the job runs every 5 seconds.
4. **Scheduled (Boolean)**: Set this field to true if the created task is scheduled to be run.
5. **Timezone**: Specify the timezone to run the job. This will modify the actual time relative to your timezone.
