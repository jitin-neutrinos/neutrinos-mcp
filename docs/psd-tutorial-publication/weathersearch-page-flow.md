# Perform the following steps:

<https://documentation.neutrinos.com/articles/#!psd-tutorial-publication/weathersearch-page-flow>

You will be designing the following flows for this page:

![Page flows in the Weather search page](/resources/Storage/psd-tutorial-publication/weather%20search_flows.png)

#### Perform the following steps:

#### Flow 1 - This flow is used to define the page variables.

1. Open the flow designer of the **weathersearch **page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. In the Page Variable node of the On Init flow, set the following properties:
  1. **Operation Type** - Set page variables
  2. **Variables list**:
      **Page Variable**
      **Default Value**
      **Action**
      searchString
      Click **+** to add the variable to the list.
      logArray
      Select **as is** and enter **[]**
      Click **+** to add the variable to the list.

**Flow 2 - **This flow is created to update the log information.




 Drag and drop a **Start node** and set the following properties:


 **Name **- updateLog


 Input Variables - Add **logobject **in the input variable and click **Add**.




 Drag and drop a **Script node** and add the following code:

 Copy CodeJavaScriptpage.logArray.push(bh.input.logobject);






 **Flow 3 - **This flow is created to process and log the weather data.



 Drag and drop a **Start node** to the flow. Enter the name of the node as** processWeather**. Double click the node and enter **cityName** as an **input variable**.

 ![Start node properties](/resources/Storage/psd-tutorial-publication/ws_pros.png)




 Drag and drop a **Script **node to the flow to show the weather card based on a condition. In the **Script properties **window, add the following code: Copy CodeMarkdownthis.page.showCard = (typeof this.page.weatherdata === 'object' && Object.keys(this.page.weatherdata).length > 2);


 Drag and drop a **Switch **node to the flow. This node allows the flow to take different paths based on the conditions that you define. Double-click the node to open its Attributes window.


 Enter the property type as **page.** and the variable as **showCard**.


 Set the following conditions. After entering each property, click **+ Add** to add the condition to the conditions list.


 **is false
 **
 **
 otherwise**




 Stop after the first match

 ![The switch condition to show weather card](/resources/Storage/psd-tutorial-publication/showcard_switch.png)





 Drag and drop a **Script **node to the flow. Add the following code:
 Copy CodeMarkdownlocalStorage.lastCity = bh.input.cityName;
bh.input.successlog = {type: 'info', message: 'Successfully Retrieved the Weather Data for city: ' + bh.input.cityName}


 Drag and drop a **Call Service** node to the flow. In the properties window, add the following details:


 **Name: **success log


 **Select a page flow**: updateLog


 Input Variables:




 **Key**





 **Value**






 bh.input.logobject




 bh.input.successlog









 Drag and drop a **Catch** node. Select **Catch error from selected flows **and toggle the **call server flow (HttpRequest)** flow to true.

 Drag and drop a **Script** node to the flow and enter the following code:Copy CodeMarkdownbh.input.errorlog = { type: 'error', message: `Weather Data Not Found${bh.input.cityName ? ` For the City: ${bh.input.cityName}` : ''}!` }
 Drag and drop a **Call Service** node to the flow. In the properties window, add the following details:


 **Name**: Error log


 **Select a page flow**: updateLog



 **Input Variables:**




 **Key**





 **Value**






 bh.input.logobject




 bh.input.errorlog












 Connect the node like this:

 ![process weather flow](/resources/Storage/psd-tutorial-publication/process_wea1.png)


 Flow 4 - This flow is created to fetch the weather of the city that is entered on the **Weathersearch** page.



 Drag and drop the **Start **node, double click the node to open its Attributes window. Add the following details:




 **Type**





 **Variable


 **


 **Value**






 Input Variable




 cityName










 Local Variable




 ssdWeatherApiUrl













 Drag and drop a **Switch **node to the flow. This node allows a flow to take different paths based on the conditions that you define. Double-click the node to open its Attributes window.

 Enter the name as **cityNameNullCheck**.

 In the **Property** field, select **bh.input** and enter **cityName**.


 Set the following conditions. After entering each property, click **+** to add the condition to the conditions list.




 **Condition**





 **Type


 **




 is of type




 Undefined






 is null










 is empty










 is of type




 string






 Stop the search after the first match.

 ![switch node proeprties](/resources/Storage/psd-tutorial-publication/ws_switch.png)





 Drag and drop a **Snackbar** node to the flow. This node is used to display a snack-bar message if the city name is undefined, null or is empty. In the **Snackbar**** properties **window, add the following details:

 ![properties of the snackbar](/resources/Storage/psd-tutorial-publication/ws_snackbar.png)



 Drag and drop a **Script **node to the flow to construct the API URL. This is the API endpoint that will be defined in the Server Service designer. In the **Script properties **window, add the following details:
 Copy CodeMarkdownbh.local.ssdWeatherApiUrl = `${bh.system.environment.properties.ssdURL}weather`;
bh.local.qparams = {
 cityName: bh.input.cityName
}


 Drag and drop an **HTTP Request** node to the flow. This node makes the HTTP request to server flow using the URL constructed in the previous node. In the **HTTP Request properties **window, add the following details:

 ![properties of the HTTP Request node](/resources/Storage/psd-tutorial-publication/ws_http.png)



 Drag and drop a **log node** to the flow. This node is used to log the result of the **HTTP Request** node. Double click the node. In the Log field, enter the type as **bh.local** and enter the variable name as **ssdWeatherApiUrl**.



 Drag and drop a **Call Service node** to the flow. This node is used to call the **Process Weather Flow** that will be created next. Double click the node and enter the following properties.




 **Name**: callProcessWeather




 **Select a Page flow**: Select **processWeather** flow in the list




 **Input Variables**: In the value field, select **bh.input** and enter the key as **bh.input.****cityName, **and toggle the** Map** field to true.

 ![call service node properties](/resources/Storage/psd-tutorial-publication/ws_cs.png)





 Connect the nodes like this:


 ![get weather flow](/resources/Storage/psd-tutorial-publication/get_wea_flow.png)
