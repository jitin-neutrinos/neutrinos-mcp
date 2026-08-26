# weather

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/weather>

The weather service is used to display the weather of the current geolocation.

Open the weather service and perform the following steps:

**Flow 1**

1. Open the service. Drag and drop a **Start node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    getWeather
    InputVariables -> Key
    lat
    Click **+** to add the property to the list.
    InputVariables-> Key
    lon
    Click + to add the property to the list.
    Local Variables -> Key
    currentWeather
    Toggle **Output** to true. Click **+** to add the property to the list.
    Local variables -> Key
    ssdWeatherApiUrl
    Click **+** to add the property to the list.
    ![start properties](/resources/Storage/create-a-simple-mobile-app/w1.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    coordinates check
    code editor
    if (bh.input.lat && bh.input.lon) {
   bh.local.pos = 1;
   } else {bh.local.pos = 0; }
    ![script properties](/resources/Storage/create-a-simple-mobile-app/w2.png)
3. Drag and drop a **Switch **node to the flow. This node allows a flow to take different paths based on the conditions that you define. Double-click the node to open its Attributes window. Add the following details:
    **Property**
    **Value**
    Name
    Property -> **bh.local**
    pos
    Set the following conditions. After entering each property, click **+ Add** to add the condition to the conditions list.
    **Condition**
    **Type**
    **Value**
    ==
    number
    0
    ==
    number
    1
    Select **stopping after the first match** from the drop-down list at the end of the attributes window.
    ![weather 3](/resources/Storage/create-a-simple-mobile-app/w3.png)
4. Drag and drop a **Snackbar** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Snackbar Message
    Location not found
    Action text
    Okay
    Snackbar Duration
    2000
    ![weather 4](/resources/Storage/create-a-simple-mobile-app/w4.png)
5. Drag and drop a **Script** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    contruct api url
    Script
    bh.local.ssdWeatherApiUrl = `${bh.system.environment.properties.ssdURL}weather`;
   bh.local.qparams = {
   lat: bh.input.lat,
   lon: bh.input.lon
   }
    ![script properties](/resources/Storage/create-a-simple-mobile-app/w5.png)
6. Drag and drop a **Call Server API node**. Double click the node and enter the following properties:
    **Property**
    **Value**
    Method
    All
    Server Name
    All
    API
    GET weather
    Return type
    JSON
    Result Mapping
    Select **bh.local** and enter **currentWeather**
    Query Parameters
    Select the Map icon, select **bh.local** and enter** qparams**
    ![call server api properties](/resources/Storage/create-a-simple-mobile-app/w6.png)

---

**Flow 2**

1. Drag and drop a **Catch** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Catch error from
    Selected nodes
    Toggle exception handling for the following nodes:
2. Drag and drop a **snackbar node** to flow. Double click the node and enter the following properties.
