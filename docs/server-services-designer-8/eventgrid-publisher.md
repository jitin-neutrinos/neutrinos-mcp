# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/eventgrid-publisher>

The ** EventGrid Publisher **node is used to publish events to the Azure Event Grid.

Azure Event Grid is a fully managed event service that enables you to easily manage events across many different Azure services and applications. See [Microsoft documentation](https://azure.microsoft.com/en-in/resources/videos/introducing-azure-event-grid/) to learn more.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.5.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Select** Plugins** in the menu and navigate to the Neutrinos Store.
- Search for the node that you want to download.
- Click the **Download** icon and select **Open Neutrinos Studio** in the pop-up that appears and you will be navigated to the Neutrinos Studio.
- In the Neutrinos Studio, click **Yes** on the confirmation pop-up and the node gets installed.
- In the Nodes Palette, search for the installed node and drag and drop it to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node**.

### Associated Attributes

1. **Name:** The name of the node. This name will display on the canvas when the node is saved.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Event Grid Config: **The name of the config.
  - If you have an Event grid service that is already configured, choose that config from the drop-down list.
  - If you want to configure a new Event grid service, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for Event Grid Configuration](/articles/server-services-designer-8/eventgrid-publisher/a/h3__32461948) to learn the properties to configure.
4. **Multiple Events:** Toggle this button if you want to publish multiple events at a time.
  - **Event List:** List of events you want to publish. Create an object in the [Script](/articles/server-services-designer-8/script-node) node and pass the object name in this field. The object should contain the event information. For example:Copy CodeJavaScriptdata = [
      {
      eventType: "Azure.SDK.Samples.CustomEvent",
      subject: "azure/sdk/eventgrid/samples/sendEventSample",
      dataVersion: "1.0",
      data: {
      message: "this is a sample event 1",
      }
      },
      {
      eventType: "Azure.SDK.Samples.CustomEvent",
      subject: "azure/sdk/eventgrid/samples/sendEventSample",
      dataVersion: "1.0",
      data: {
      message: "this is a sample event 2",
      }
      }
      ]
5. **Event Type:** The registered event types for this event source.
6. **Subject:** The publisher-defined path to the event subject.
7. **Data Version:** The schema version of the data object. The publisher defines the schema version.
8. **Message:** The message to be published.
9. **Result Mapping: **Map the data retrieved to bh., bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

### Event Grid Configuration

Use these attributes to create a new connection with the Event Grid service.

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name:** A display name for the configuration.
- **Event Grid Endpoint:** The user-defined endpoint that you post your events to. Every event grid topic provides an endpoint.
- **Event Grid Access Key: **The Access key to authenticate an application publishing events to Azure Event Grid topics.
