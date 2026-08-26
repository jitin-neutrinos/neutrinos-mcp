# Work with Neutrinos Modelr

<https://documentation.neutrinos.com/articles/#!tutorial-integrate-your-app-with-apis/modeler-flow>

After you get familiar with the base app, you create a Neutrinos Modelr flow and UI Services.

- Using Neutrinos Modelr, you can link to a variety of backend systems such as Enterprise Service Bus (ESB), Cloud Services, databases, etc. See [About Neutrinos Modelr](/articles/neutrinos-modelr-guide/new-topic-2) to learn more.
- Using UI Services designer, you can create client-side services in your app. See [About Client Services](/articles/service-designer-user-s-guide/client-services) to learn more.

### Work with Neutrinos Modelr

Create a Modelr flow to call the weather API and fetch weather data. Perform the following steps:

1. Click the **Modelr** option on the Application page.
    ![The Modelr option](/resources/Storage/tutorial-integrate-your-app-with-apis/modelr_option.png)
2. The Neutrinos Modelr opens up on the browser.
    ![The Neutrinos Modelr](/resources/Storage/tutorial-integrate-your-app-with-apis/modelr1.png)
3.
4. Drag and drop a **HTTP In **node to the flow. Double click the node. In the **Edit http in node** window, add the following details.
    ![HTTP In node](/resources/Storage/tutorial-integrate-your-app-with-apis/http_in_modelr.png)
    **Property**
    **Value**
    Method
    GET
    URL
    /weather
    Name
    call weather api
    Once you click **Done**, the information gets reflected in the Information section to the right. **c****all weather api **is an API endpoint that we have created using Modelr to fetch the weather data.
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/node1.png)
5. Drag and drop a **f****unction **node to the flow. This node is used to set the URL on the msg object. Double-click the node to configure its properties. In the **Edit function node** window, add the following details.
    **Property**
    **Value**
    Name
    construct request params
    Function
    msg.url = `http://api.openweathermap.org/data/2.5/weather?q=${msg.payload.cityName}&APPID=**your_app_id**`;return msg;
   //Replace **your_app_id** with your registered API key.
    Outputs
    1
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/mod_1.png)
6. Drag and drop a **HTTP Request **node to the flow. This node sends the HTTP Request to the **openweathermap** API endpoint. The result of the call will be parsed to a JavaScript object. Double-click the node to configure its properties. In the **Edit http request node** window, add the following details.
    **Property**
    **Value**
    Method
    GET
    Return
    a parsed JSON object
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/node3.png)
7. Drag and drop a **Debug **node to the flow. This node debugs the msg object and logs it to the debug window. Double-click the node to configure its properties. In the **Edit debug node** window, add the following details.
    **Property**
    **Value**
    Object
    complete msg object
    To
    debug window
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/node5.png)
8. Drag and drop an **HTTP response **node to the flow. This node will send the data returned by the API provider to the client that calls this flow. There are no functionalities that should be entered.
9. Connect the nodes to create the following flow:
    ![The HTTP node configuration](/resources/Storage/tutorial-integrate-your-app-with-apis/node6.png)
10. Deploy the Modelr flow. Click ![](/resources/Storage/tutorial-integrate-your-app-with-apis/mod_deploy.png) on the top right corner of the screen.
