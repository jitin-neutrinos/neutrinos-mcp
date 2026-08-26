# Create a Flow in Client Services Designer

<https://documentation.neutrinos.com/articles/#!tutorial-integrate-your-app-with-apis/ui-services>

The Client Services Designer is used to create client-side services for your application. In this app, you will be creating a Client Service to call the Modeler flow that you created in the previous step. The Modelr will get the data from the weather API provider and sends it back to the Client Service flow.

Perform the following steps:

1. Navigate back to Neutrinos Studio. Click **Services** in the menu options and select **UI ****Services**.
    ![The Modelr option](/resources/Storage/tutorial-integrate-your-app-with-apis/service1.png)
2. The Client Services Designer opens up. Click the ![](/resources/Storage/tutorial-integrate-your-app-with-apis/add.png) icon to add a Client Service. Enter **weatherservice** in the popup window and click **Add**.
    ![Create a UI service](/resources/Storage/tutorial-integrate-your-app-with-apis/service2.png)
3. The new service gets added. Drag and drop a **Start **node to the flow. The Start node is the entry point for a flow. When you create a Start node and call the flow, a system-defined object called bh is created. When you create input and local properties in the Start node, they are added to the bh object. See [Start Node](/smart/project-service-designer-user-s-guide/start-node) to learn more.
    Double click the node to open its Attributes window. Add the following details:
    **Property**
    **Value**
    **Action**
    Name
    get weather modelr
    Function NamegetWeatherModelr
    Input Properties -> Key
    cityName
    Click **+** to add the property to the list.
    Local Properties -> Key
    currentWeather
    Toggle **Output** to true. Click **+** to add the property to the list.
    Local properties -> Key
    modelrApiUrl
    Click **+** to add the property to the list.
    The currentWeather property is used to capture the result returned by the Modeler flow. It is set as an output property and can be accessed outside the flow.
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/start.png)
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
    ![The switch node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/switch.png)
5. Drag and drop a **Log **node to the flow. This node is used to [log the bh object](/smart/project-service-designer-user-s-guide/service-designer-variables) to reveal message flow issues and application problems (if any). In the **L****og properties **window, add the following details:
    **Property**
    **Value**
    Name
    log bh
    Logbh.
    ![The log node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/log_node.png)
6. Drag and drop a **Script **node to the flow to construct the API URL. This is the API endpoint that we defined using Neutrinos Modeler. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    construct api url
    Code Editor
    bh.local.modelrApiUrl = `http://localhost:24483/api/weather?cityName=${bh.input.cityName}`;
    ![The Script node](/resources/Storage/tutorial-integrate-your-app-with-apis/script_node.png)
7. Drag and drop a **HTTP Request** node to the flow. This node makes HTTP request to Neutrinos Modeler using the URL constructed in the previous node. In the **HTTP Request properties **window, add the following details:
    **Property**
    **Value**
    Name
    call modelr flow
    Method
    Get
    URLSelect the **bh.local** property, and enter **modelrApiUrl** as the value. Return TypeJSONBodybh.input.Result Mappingbh.local.currentWeather
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/http_request.png)
8. Drag and drop a log node to the flow. This node is used to log the modelrApiUrl called previously. Double click the node and enter the following properties. **Property****Value**Name log modelrApiLogSelect **bh.local** property, enter **modelrApiUrl** as the value
   ![log property](/resources/Storage/tutorial-integrate-your-app-with-apis/lognewss.png)
9. Connect the nodes to create the following service flow:

![UI services flow](/resources/Storage/tutorial-integrate-your-app-with-apis/servicesflow.png)
