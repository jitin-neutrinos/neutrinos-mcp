# Create Server Services

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/create-server-services>

The [Server Service Designer (SSD)](/smart/project-concepts/server-services-designer) is used to create server flows for this app.

Perform the following steps:

1. Click** Services** on the Menu list and select **Server**.
2. The **Server Services Designer** opens up. Click the plus icon and add a new server service. Enter **weatherserver** and click** Add**.
    ![create server service](/resources/Storage/psd-tutorial-publication/create_ssd.png)
3. Open the service.

Design the following server flows:

![server flows of weather app](/resources/Storage/psd-tutorial-publication/weather_server_flows.png)

**Flow 1**- This flow is used to create an HTTP endpoint called weather to call the weather API and construct the URL parameters to make the HTTP request to the server.

1. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint to call the weather API. Double click the node and enter the following:
    **
    Property
    **
    **Value
    **
    Name
    call weather api
    Method
    Get
    Path
    /weather
    ![Http in node of the weather app](/resources/Storage/psd-tutorial-publication/weatherhttpin.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details to construct the URL parameters:
    **Property**
    **Value**
    Name
    construct url params
    code editor
    bh.url = process.env.weatherProviderURL;
    bh.qparams = {
    q: bh.input.query.cityName,
    APPID: process.env.apiId,
    units: 'metric'
    }
    ![script node of the weather app](/resources/Storage/psd-tutorial-publication/scriptSSDweather.png)
3. Drag and drop an **HTTP request** node. This node makes HTTP requests to the server using the URL constructed in the previous node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Method
    Get
    URL
    select **bh.** and enter the value as **url.**
    Return type
    JSON
    Result Mapping
    Select **bh.** and enter the value as **result**.
    Query Parameters
    Select** bh. **and enter the value as **qparams.**
    ![Http request weather](/resources/Storage/psd-tutorial-publication/WSSDttpreq.png)
4. Drag and drop an **Http out** node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next [middleware](/smart/project-concepts/middleware-sequence). Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    send response
    Response type
    JSON
    Status code
    Select** bh. **property and
    enter the value as **result.statusCode**
    Response body
    Select** bh.** property and
    enter the value as **result.payload**
    ![httpout node of the weather app](/resources/Storage/psd-tutorial-publication/WSSDhttpout.png)
5. Drag and drop a **Log node**. This is used to log variables that the user has given in the browser console. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    log result
    Log level
    info
    Log
    select **bh.** property and enter **result **
    ![Log node for the server flow of the weather app](/resources/Storage/psd-tutorial-publication/WSSDlognode.png)

Join the nodes like this:

![call weather api flow](/resources/Storage/psd-tutorial-publication/call_weather%20API.png)

---

**Flow 2**- This flow is used to catch any exceptions in the server service.

1. Drag and drop a **Catch node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
2. Drag and drop an **HTTP Out** node, join the node to the **Catch** node, and set the following properties:
    ![HTTP Out node](/resources/Storage/psd-tutorial-publication/server_htttp_out.png)
