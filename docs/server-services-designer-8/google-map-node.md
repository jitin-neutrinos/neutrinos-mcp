# How to use

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/google-map-node>

The** Google Map **node allows you to perform operations related to google maps such as directions, distance, and much more.

| ![Information](/resources/Storage/server-services-designer-8/info.png) | This node is available from Neutrinos Studio Release 7.4.0.You have to download this node from the**[Neutrinos Store](https://store.neutrinos.co/web/catalog/featured)** to use it in your APIs or services in the Server Services Designer. |
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

### Associated Attributes

1. **Name**: The name of the config.
2. **Function Name**: This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Google Config:**The name of the configuration that connects to the Google APIs.
  - If you have an existing Google configuration, choose that config from the drop-down list.
  - If you want to create a new Google configuration, select **Add new config** from the drop-down list and click the **Map** icon to add a new configuration. See [Attributes for a new Google Config](/articles/server-services-designer-8/google-map-node/a/googleconfig_map) to learn about the properties to configure.
4. **Operations**: Select the operation that you want the node to perform.
  - **Directions**: Provides the driving directions between two places. Syntax: Directions:{ origin: "String", destination: "string"}. See [Directions](https://developers.google.com/maps/documentation/directions/get-directions)to learn more about the required parameters.
  - **Distance Matrix**: Provides the travel distance between two places. Syntax: Distance Matrix:{ origins: ["string"], destinations: ["string"]}. See [Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/overview) to learn more about the required parameters.
  - **Elevation:** Provides elevation data of the location. Syntax: Elevation:{ locations: ["string"]} . See [Elevation](https://developers.google.com/maps/documentation/elevation/overview) to learn more about the required parameters.
  - **Geocoding: **Provides a human-readable address along with the geological coordinates for a given location. Syntax: Geocoding:{ address: "string"}. See [Geocoding](https://developers.google.com/maps/documentation/elevation/overview)to learn more about the required parameters.
  - **Places: **Provides a list of places based on the location. Syntax: Places:{ input: "string", inputtype: "string", fields: "string"}. See [Places](https://developers.google.com/maps/documentation/places/web-service/search) to learn more about the required parameters.
  - **Roads: **Provides the road segments for the given location. Syntax: Roads:{ points: ["string"]}. See [Roads](https://developers.google.com/maps/documentation/roads/nearest) to learn more about the required parameters.
5. **Params:** The parameters that you want to pass for this node. Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads]. Depending on the operation you select, the parameters that has to passed changes.
6. **Result Mapping:** Map the response of the API call to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result.

### Attributes for a new Google Map Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

1. **Name**: The name of the config.
2. **Google API Key:** Enter the API key of your google account.
