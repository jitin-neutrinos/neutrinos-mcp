# weather

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/weather-server>

This service is used to fetch the weather details.

Open the weather service and perform the following steps:

**Flow 1**

1. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint that responds to the requests. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    call weather api
    Method
    Get
    Select from the drop-down list.
    Path
    weather
    ![weather properties](/resources/Storage/create-a-simple-mobile-app/service-designer-user-s-guide/WeatherS1.png)
    You can generate the swagger document on the go. To do so, add the following properties in the documentation section of the **Http in** node:
    **Parameters:**
    **Name**
    **Description**
    **Type**
    **Required**
    lat
    lattitude
    quey
    true
    lon
    longitude
    query
    true
    APPID
    app id of the app
    query
    true
    units
    units for temperature
    query
    false
    ** Responses:**
    ![api docs](/resources/Storage/create-a-simple-mobile-app/apapapapapapap.png)
  - **Message**: {"coord":{"lon":139.01,"lat":35.02},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01n"}],"base":"stations","main":{"temp":285.514,"pressure":1013.75,"humidity":100,"temp_min":285.514,"temp_max":285.514,"sea_level":1023.22,"grnd_level":1013.75},"wind":{"speed":5.52,"deg":311},"clouds":{"all":0},"dt":1485792967,"sys":{"message":0.0025,"country":"JP","sunrise":1485726240,"sunset":1485763863},"id":1907296,"name":"Tawarano","cod":200}
  - Status code: 200
  - Click the plus icon and the property gets added.
2. Drag and drop a** Script node **and connect it to the previous node. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    construct url params
    code editor
    bh.url = process.env.weatherProviderURL;
   bh.qparams = {
   lat: bh.input.query.lat,
   lon: bh.input.query.lon,
   APPID: process.env.apiid,
   units: 'metric'
    }
    ![weather properties](/resources/Storage/create-a-simple-mobile-app/service-designer-user-s-guide/weatherS1script.png)
3. Drag and drop an **HTTP request** node and connect it to the **Script** node. This node makes HTTP requests to the server using the URL constructed in the previous node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Method
    Get
    URL
    Click the **Map** icon at the right. Select **bh.** and enter the value as **url.**
    Return type
    JSON
    Result Mapping
    Select **bh.** and enter the value as **result**.
    Query Parameters
    Select** bh. **and enter the value as **qparams. **Click the **+ **icon to add the parameter to the list.
    ![Http request weather](/resources/Storage/create-a-simple-mobile-app/tutorial-create-your-first-app/WSSDttpreq.png)
4. Drag and drop an **Http out** node and connect it to the previous node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next [middleware](/smart/project-concepts/middleware-sequence). Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    send response
    Response type
    JSON
    Status code
    Select **bh.** property and enter the value as **result.statusCode**.
    Response body
    Select **bh.** property and enter the value as **result.payload**.
    ![httpout node of the weather app](/resources/Storage/create-a-simple-mobile-app/tutorial-create-your-first-app/WSSDhttpout.png)

---

**Flow 2**

1. Drag and drop a **Catch node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Catch errors from
    Selected nodes
    Set the following nodes to true
    Select all the nodes
    ![Catch node properties for the server flow](/resources/Storage/create-a-simple-mobile-app/project-tutorial-create-your-first-app-using-version-7/weatherS3.png)
2. Drag and drop an **Http out** node and connect it to the **Catch** Node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next middleware. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    send response
    Response type
    JSON
    Status code
    Select **number** property and enter the value as 500.
    Response body
    Select **as is** from the drop-down list and enter the value as **{message: 'Something went wrong!'} **

![weather properties](/resources/Storage/create-a-simple-mobile-app/weatherS4.png)

Connect the nodes to create the following server flow.

After configuring this service, you can view the swagger documentation. To do so,

- Save the service.
- Click the **Click here for swagger link** icon and the swagger docs appear.

![Swagger docs icon](/resources/Storage/create-a-simple-mobile-app/SWAG.png)

The swagger document looks like this.
