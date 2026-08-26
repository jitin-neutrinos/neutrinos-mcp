# Server services for the weather app

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/create-server-services>

The [Server Service Designer (SSD)](/smart/project-concepts/server-services-designer) is used to create server flows for this app.

**Creating server services**

1. Click** Services** on the Menu list and select **Server**.
2. The **Server Services Designer** opens up. Click the plus icon to add a new server service. Enter **weatherserver** and click** Add**.
    ![create server services 1](/resources/Storage/tutorial-create-your-first-app/newsservice.png)

### Server services for the weather app

Perform the following steps after creating the server service:

1. Open the service. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint that responds to the requests. Double click the node and enter the following:
    **Property and value**
    **Action**
    Name: call weather api
    Method: Get
    Select from the drop-down list.
    Path: /weather
    ![Http in node of the weather app](/resources/Storage/tutorial-create-your-first-app/weatherhttpin.png)
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
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
    ![script node of the weather app](/resources/Storage/tutorial-create-your-first-app/scriptSSDweather.png)
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
    ![Http request weather](/resources/Storage/tutorial-create-your-first-app/WSSDttpreq.png)
4. Drag and drop an **Http out** node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next [middleware](/smart/project-concepts/middleware-sequence). Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    send response
    Response type
    JSON
    Status code
    Select bh. property and
    enter the value as result.statusCode
    Response body
    Select bh. property and
    enter the value as result.payload
    ![httpout node of the weather app](/resources/Storage/tutorial-create-your-first-app/WSSDhttpout.png)
5. Drag and drop a **Log node**. This is used to log variables that the user has given in the browser console. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    log result
    Log level
    info
    Log
    select **bh.** property and enter **result **
    ![Log node for the server flow of the weather app](/resources/Storage/tutorial-create-your-first-app/WSSDlognode.png)
6. Drag and drop an **Http out** node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next middleware. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Response type
    JSON
    Status code
    Select **number** and
    enter the value as **500**.
    Response body
    Select **as is** and
    enter the value as
    **{message: "Something went wrong!"}**
    ![Http out node 2 properties for the server flow](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/WSSDhttpout2.png)
    ![Http out node 2 properties for the server flow](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/WSSDhttpout2.png)
7. Drag and drop a **Catch node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Catch errors from
    Selected nodes
    Set the following nodes to true
    Select all the nodes
    except **Httpout(Httpout)**
    ![Catch node properties for the server flow](/resources/Storage/tutorial-create-your-first-app/WSSDcatchnode.png)
8. Connect the nodes to create the following server flow.
    ![The server services for the weather app](/resources/Storage/tutorial-create-your-first-app/WSSD.png)
