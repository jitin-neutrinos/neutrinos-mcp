# Create Client Services

<https://documentation.neutrinos.com/articles/#!tutorial-create-your-first-app/create-client-services>

In this section, you will be creating a Client Service in the [Client Services Designer](/smart/project-concepts/client-services-designer) to call the Server flow that you will create in the next step. The Server flow will get the data from the weather API provider and sends it back to the Client Service flow.

Perform the following steps:

1. On the left pane, click **Services** in the menu options and select **Client**.
    ![create client service for weather 1](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/create%20client%20services.png)
2. The Client Services Designer opens up. Click the ![](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/add.png) icon to add a new Client Service. Enter **weatherservice** in the popup window and click **Add**.
    ![client services for weather app 2](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/clientservice.png)
3. The new service gets added. Drag and drop a **Start **node to the flow. The Start node is the entry point for a flow. When you create a Start node and call the flow, a system-defined object called bh is created. When you create input and local properties in the Start node, they are added to the bh object. See [Start Node](/smart/project-service-designer-user-s-guide/start-node) learn more.
    Double click the node to open its Attributes window. Add the following details:
    **Property and Value**
    **Action**
    Name: get weather
    **Input Variables****Key:** cityName
    Click **+** to add the property to the list.
    **Local Variables****Key:** currentWeather
    Toggle Output to true. Click + to add the property to the list.
    **Local variables****Key:** ssdWeatherApiUrl
    Click **+** to add the property to the list.
    The currentWeather property is used to capture the result returned by the Server flow. It is set as an output property and can be accessed outside the flow.
    ![The HTTP node configuration](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/WcsdStart.png)
4. Drag and drop a **Switch **node to the flow. This node allows a flow to take different paths based on the conditions that you define. Double-click the node to open its Attributes window. Add the following details:
    **Property**
    **Value**
    Name
    cityNameNullCheck
    Property -> **bh.input**
    cityName
    Set the following conditions. After entering each property, click **+ Add** to add the condition to the conditions list.
    **Condition**
    **Value**
    is of type
    undefined
    is null
    is empty
    is of type
    string
    Select **stopping after first match** from the drop-down list at the end of the attributes window.
     ![The switch node configuration](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/switch.png)
5. Drag and drop a **Snackbar** node to the flow. This node is used to display snack-bar notifications. Snackbars provide brief messages about app processes on the screen. In the **Snackbar**** properties **window, add the following details:
    **Property
    **
    **Value**
    Name
    snackbar
    Snackbar messageInvalid city name
    Action text
    okay
    SnackBar Duration
    2000
    ![The log node configuration](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsdsnachbar1.png)
6. Drag and drop a **Script **node to the flow to construct the API URL. This is the API endpoint that we defined using the Server Service designer. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    construct api url
    Code Editor
    bh.local.ssdWeatherApiUrl = `${bh.system.environment.properties.ssdURL}weather`;
   bh.local.qparams = { cityName: bh.input.cityName}
7. Drag and drop a **HTTP Request** node to the flow. This node makes the HTTP request to server flow using the URL constructed in the previous node. In the **HTTP Request properties **window, add the following details:
    **Property**
    **Value**
    Name
    call server flow
    Method
    Get
    URL
    Select the bh.local property, and enter ssdWeatherApiUrl as the value.
    Return Type
    JSON
    Body
    bh.input.
    Result Mapping
    Select the bh.local property and enter currentWeather as the value.
    Query Parameters
    Select the bh.local propertyand enter qparams as the value.
    ![The HTTP node configuration](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsdhttpreq.png)
8. Drag and drop a **log node** to the flow. This node is used to log the **ssdWeatherApiUrl** called previously. Double click the node and enter the following properties.
    **Property**
    **Value**
    Name
    log ssdWeatherApiUrl
    Log
    Select bh.local property,enter ssdWeatherApiUrl as the value
   ![log property](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsdlog1.png)
9. Drag and drop a **Snackbar** node to flow. Snackbars provide brief messages about app processes on the screen. Double click the node and enter the following properties. **Property****Value**Name Error snackbarSnackbar message Something went wrong! Action textokaySnackbar duration 3000
   ![Snackbar 2 of the client service flow](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsdsnackbar2.png)
10. Drag and drop a **Catch node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Catch errors from
    Selected nodes
    Set the following nodes to true
    Select all the nodesexcept **E****rror Snackbar(Snackbar) **
    ![The error node for the CSD](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsderrornode.png)
11. Connect the nodes to create the following service flow:

![UI services flow](/resources/Storage/tutorial-create-your-first-app/project-tutorial-weather-app/Wcsdflow.png)
