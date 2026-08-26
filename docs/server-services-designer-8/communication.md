# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/communication>

**Communication** nodes are used to add voice-calling functionalities into your app. That is, they add voice calling capabilities to the services built on Neutrinos Studio. The communication nodes package consists of these three nodes:

- [Tele Call node](/articles/server-services-designer-8/tele-call-node)
- [Get Call Recording](/articles/server-services-designer-8/get-call-recording-node)
- [Get Instance](/articles/server-services-designer-8/get-instance-node)

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node package internally uses the Nexmo npm package. See the [Nexmo documentation](https://www.npmjs.com/package/nexmo) to learn more. |
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

### Attributes for a New Nexmo Config

These are the attributes required to add a new configuration and connect the Nexmo APIs:

- **Name**: Name of the config.
- **API Key**: The API Key to be used to connect to Nexmo and access the voice APIs.
- **API Secret**: The API secret associated with the API key to connect to Nexmo and access the voice API?
- **Application ID**: The Application ID to be used when creating JSON WEB Tokens (JWTs).
- **Upload Private Key File**: The Private Key file to be used for authenticating with the Nexmo APIs before creating JWTs. To generate the Private Key, use the Nexmo CLI. See the [Nexmo documentation](https://developer.nexmo.com/concepts/guides/authentication#using-the-nexmo-cli-to-generate-jwts) to learn more.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | To get the API Key, API Secret, and the Application ID, you should create a developer account on Nexmo (Vonage). See [https://dashboard.nexmo.com/sign-up](https://dashboard.nexmo.com/sign-up) . |
| --- | --- |
