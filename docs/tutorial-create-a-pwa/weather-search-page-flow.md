# Flow 1 - This flow is used to define the page variables.

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/weather-search-page-flow>

Delete the existing flows on the weather search page and create the following flows:

![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-15.png)

#### Flow 1 - This flow is used to define the page variables.

![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-15-3.png)

1. Open the flow designer of the **weathersearch **page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. In the Page Variable node of the On Init flow, set the following properties:
  1. **Operation Type** - Set page variables
  2. **Variables list**:
      **Page Variable**
      **Default Value**
      **Action**
      logArray
      Select **as is** and enter **[]**
      Click **+** to add the variable to the list.
3. Drag and drop another **Service Variable** node to the flow, set the following properties:
  1. **Name**: get subscribe csd var
  2. **Operation Type**: Get page variables
  3. **Select a Client Service**: notification
  4. **Variables list**: **Service Variable**
     **Service Variable**
     **Action**
     Select **bh.** and enter **subscribe**
     subscription
     Click **+** to add the variable to the list.
4. Drag and drop a **Switch **node to the flow and set the following conditions:
5. ![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-15-1.png)
6. Drag and drop a [Open Dialog](/smart/project-page-services-designer-guide/open-dialog-node) node to the flow and set the following properties:
  1. **Name**: open subscribe dialog
  2. **Select a page**: subscribe
7. Drag and drop another **Switch **node and set the following properties:
8. ![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-15-2.png)
9. Drag and drop a **Call Service** node to the flow, set the following properties:
  1. **Name**: call fcm subscribe
  2. **Client Service Flow**: Toggle to true
  3. **Select the Client Flow**: subscribe
  4. **Input Variables**: **Key**
     **Value**
     **Action**
     bh.input.cityName
     Select **bh**. and enter **result**
     Toggle the map field
  5. **Output Variables**:**Key**
     **Value****Action**bh.local.result
     bh.local.response

---

#### Flow 2 - This flow is created to fetch the weather of the city that is entered on the Weathersearch page.

![Get weather flow updated](/resources/Storage/tutorial-create-a-pwa/get_weather_updated.png)

1. Drag and drop the **Start **node, double click the node to open its Attributes window. Add the following details:
    **Type**
    **Variable
   **
    **Value**
    Input Variable
    cityName
2. Drag and drop a **Switch **node to the flow. This node allows a flow to take different paths based on the conditions that you define. Double-click the node to open its Attributes window.
  1. Enter the name as **cityNameNullCheck**.
  2. In the **Property** field, select **bh.input** and enter **cityName**.
  3. Set the following conditions. After entering each property, click **+** to add the condition to the conditions list.
      **Condition**
      **Type
     **
      is of type
      Undefined
      is null
      is empty
      is of type
      string
  4. Stop the search after the first match.![switch node proeprties](/resources/Storage/tutorial-create-a-pwa/project-psd-tutorial/ws_switch.png)
3. Drag and drop a **Snackbar** node to the flow. This node is used to display a snack-bar message if the city name is undefined, null or is empty. In the **Snackbar**** properties **window, add the following details: ![properties of the snackbar](/resources/Storage/tutorial-create-a-pwa/project-psd-tutorial/ws_snackbar.png)
4. Drag and drop a **Script **node to the flow to construct the API URL. This is the API endpoint that will be defined in the Server Service designer. In the **Script properties **window, add the following details:
5. Copy CodeJavaScriptbh.local.ssdWeatherApiUrl = `${bh.system.environment.properties.ssdURL}weather`;
   bh.local.qparams = {
    cityName: bh.input.cityName
   }
   page.weatherdata = {};
6. Drag and drop an **HTTP Request** node to the flow. This node makes the HTTP request to server flow using the URL constructed in the previous node. In the **HTTP Request properties **window, add the following details: ![properties of the HTTP Request node](/resources/Storage/tutorial-create-a-pwa/project-psd-tutorial/ws_http.png)
7. Drag and drop a **Catch node** and select the **call server flow (HttpRequest) **flow.
    ![selecting the Call server flow](/resources/Storage/tutorial-create-a-pwa/call_server_flow.png)
8. Drag and drop a **Script** node, enter the name of the node as **set showcard **and enter the following code in the script editor:
    Copy CodeMarkdownthis.page.showCard = (typeof this.page.weatherdata === 'object'
    && Object.keys(this.page.weatherdata).length > 2);
9. Drag and drop a **Switch** node and set the following conditions:
    ![Switch node properties](/resources/Storage/tutorial-create-a-pwa/card_swirch.png)
10. Drag and drop a** Storage node** and set the following properties:
    ![properties of the Storage node](/resources/Storage/tutorial-create-a-pwa/storage_prop.png)
11. Drag and drop a **Call Service** node, select the **updateLog** page flow and set the following input variable:
    **Key**
    **Value**
    bh.input.logobject
    { type: 'info', message: 'Successfully Retrieved the Weather Data for city: ' + bh.input.cityName, }
12. Drag and drop another **Call Service** node, select the** updateLog** page flow, and set the following input variable:
    **Key**
    **Value**
    bh.input.logobject
    {type: 'error',message: `Weather Data Not Found${bh.input.cityName ? ` For the City: ${bh.input.cityName}` : ''}!`,}

**Flow 2 - **This flow is created to update the log information.

Drag and drop a **Start node** and set the following properties:**Name **- updateLogInput Variables - Add **logobject **in the input variable and click **Add**.Drag and drop a **Script node** and add the following code:Copy CodeJavaScriptpage.logArray.push(bh.input.logobject);
