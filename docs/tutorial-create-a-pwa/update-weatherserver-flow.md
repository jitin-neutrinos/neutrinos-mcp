# Update weatherserver flow

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/update-weatherserver-flow>

![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-16.png)

**Flow 1**

1. Replace the **Script **and **HTTP Request** node with a **Call service** node. Set the following properties:
  1. **Select a flow**: reqandSendWeatherData
  2. **Input Variables**:
  3. Key
     Value
     Action
     bh.input.cityName
     Select **bh.input** and enter **query.cityName**
  4. **Output Variables**:
  5. Key
     ValueAction
     bh.local.result
     Select** bh.** and enter **result**
2. Remove the **Log **node from the flow.

Connect the nodes like this:

![](/resources/Storage/tutorial-create-a-pwa/tutorial-build-a-pwa-2021-09-16-1.png)

---

**Flow 2** - This flow is created to request the weather data.

1. Drag and drop a **Start node** and set the following properties:
  1. **Name **- reqAndSendWeatherData
  2. **Input Variables** - Add **cityName **in the input variable and click **Add**.
  3. **Local Variables** - Add **result **and toggle the output. Click **Add **icon.
2. Drag and drop a Script node. In this node, the logic to pass parameters is written.
3. Copy CodeJavaScriptbh.url = process.env.weatherProviderURL;
   bh.qparams = {
    q: bh.input.cityName,
    APPID: process.env.apiId,
    units: 'metric'
   }
4. Drag and drop an **HTTP request** node. This node makes HTTP requests to the server using the URL constructed in the previous node. Double click the node and enter the following properties: **Property****Value**Name reqWeatherDataMethod
   Get
   URLselect **bh.** and enter the value as **url.** Return typeJSONResult MappingSelect **bh.local** and enter the value as **result**.Query ParametersSelect** bh. **and enter the value as **qparams.**
   ![Http request weather](/resources/Storage/tutorial-create-a-pwa/project-psd-tutorial/WSSDttpreq.png)
5. Drag and drop a **Log node**. This is used to log variables that the user has given in the browser console. Double click the node and enter the following properties:**Property****Value**Namelog resultLog levelinfoLogselect **bh.** property and enter **result **![Log node for the server flow of the weather app](/resources/Storage/tutorial-create-a-pwa/project-psd-tutorial/WSSDlognode.png)

Connect the nodes like this:
