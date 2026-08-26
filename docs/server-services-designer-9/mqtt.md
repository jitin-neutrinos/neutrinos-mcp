# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/mqtt>

MQTT (Message Queuing Telemetry Transport) is a message protocol for restricted networks (low bandwidth) and IoT devices with extremely high latency.

See [What is MQTT](https://www.opc-router.com/what-is-mqtt/) to learn more.

It comprises 2 nodes:

- [MQTT Publish](/articles/server-services-designer-9/mqtt-publish)
- [MQTT Subscribe](/articles/server-services-designer-9/mqtt-subscribe)

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available from Neutrinos Studio Release 7.5.0.   You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs. |
| --- | --- |

### How to use

- Open the **Server Services** editor window.
- Open an existing service from the service list or click the** plus icon **to add a new Server Service.
- Download the Plugin from Neutrinos Store. See [Download from Store](/articles/studio-guide-7/import-plugin).
- In the Nodes Palette, search for the installed node and drag and drop the node to the canvas.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node **or **HTTP In node.**

### MQTT Configuration

Use these attributes to create a new connection with an MQTT broker.

Note that for every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name:** A display name for the MQTT configuration.
- **URL:** The endpoint of the MQTT broker you want to connect to. The URL can be on the following protocols:
  - mqtt
  - mqtts
  - tcp
  - tls
  - ws
  - wss
- **clientId: **The client identifier that uniquely identifies the MQTT client that connects to an MQTT broker.
- **username: **The username to connect to the MQTT broker.
- **password: **The password to connect to the MQTT broker.
- **clean:** If set to **True**, erases [QoS](https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/) 1 and 2 messages. If set to **F****alse**, receives [QoS](https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/) 1 and 2 messages while offline.
- **level store: **The file path to store incoming and outgoing packets.
- **protocol ID:** The protocol ID you want to use. For example, MQTT or TCP.
- **protocol version:** The version of the protocol you want to use. For example, version 4.
- **keepalive:** Keeps the connection alive for the specified seconds. Set to 0 to disable this feature.
- **queue QoS zero: **Enable this field to Queue outgoing [QoS](https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/) zero messages if the connection is broken. By default, this field is disabled.
- **reconnect period:** Specify the interval between two connection periods (in milliseconds). Disable auto-reconnect by setting the value to 0.
- **connection timeout: **The time to wait before the connection acknowledgment is received.
