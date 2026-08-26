# Flow 1

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/notification-flow>

Create a new service called **notification **and design the following flows in it:

### 

### Flow 1

This flow is used to send notifications for the sunscribers.

1. Drag and drop a **HttpIn node**. Double click the node and enter the following details:
    **Property**
    **Value**
    **Action**
    Method
    POST
    Select from the drop-down list.
    Path
    send
    Parameters
   **Name**: Send notification**Description**: { "notification":{ "badge":"https://media.glassdoor.com/sqll/1960709/neutrinos-squarelogo-1564113473875.png", "body":"Neutrinos Test Notification", "dir":"auto", "icon":"https://media.glassdoor.com/sqll/1960709/neutrinos-squarelogo-1564113473875.png", "image":"https://media.glassdoor.com/sqll/1960709/neutrinos-squarelogo-1564113473875.png", "silent":false, "title":"Neutrinos", "vibrate":100 } }**Type**: Body**Required**: Toggle it to trueClick Add.
2. Drag and drop a** Script node **and connect it to the previous node. In the **Script properties **window, add the following details to store the subscription object and the city name in a flow variable called** subcription**:
    **Property**
    **Value**
    code editor
    bh.notification = JSON.stringify(bh.input.body);bh.searchQuery = {};
3. Drag and drop a **Mongo DB** node and connect it to the previous node. In the properties window, add the following details to find if the subscription details already exist in the database:
    **Property**
    **Value**
    Database Config
    Collection
    Select **String **and enter **subscription**
    Operation
    find
    Query
    Select **bh.** and enter **searchQuery**
    Result Mapping
    Select** bh.** and enter **subscribers **
4. Drag and drop **Script node. ** Enter the following code:
    Copy CodeJavaScriptconst webPush = require('web-push');
   const publicVapidKey = "BJ-ZIj7rfwn-TCU0DH0_wriClaJNhQY73n57RA9DWXzARuyjrrYtZAxLadxSW-wnFBxXwdcV0QsYdKZT8k-P48c";
   const privateVapidKey = "OM_rIzY3jAXdVVReZEk5leC9bboPO93u1aKOPbDSqBA";
   webPush.setVapidDetails('mailto:example@example.com', publicVapidKey, privateVapidKey);
   bh.subscribers.forEach(obj => {
    webPush.sendNotification(obj.subscription, bh.notification).catch(error => {
    console.log(error);
    });
   });
   bh.res = {
    httpStatus: 200,
    message: 'success'
   }
5. Drag and drop an **Http out** node and connect it to the previous node. Double click the node and enter the following properties to send a response back to the client flow - **subscribe** indicating that the request made by the client is successful:
    **Property**
    **Value**
    Response type
    JSON
    Status code
    Select **number** property and enter the value as **200**
    Response body
    Select **as is** and enter its value as **{message:'success'}**

---

### Flow 2

This flow is used to store the subscription object and the city name in the **Mongo DB **database. If the subscription details already exist, the database is not updated.

1. Drag and drop a **HttpIn node**. Double click the node and enter the following details to create an HTTP Endpoint called **Subscribe**:
    **Property**
    **Value**
    **Action**
    Method
    POST
    Select from the drop-down list.
    Path
    subscribe
2. Drag and drop a** Script node **and connect it to the previous node. In the **Script properties **window, add the following details to store the subscription object and the city name in a flow variable called** subcription**:
    **Property**
    **Value**
    code editor
    bh.subscription = bh.input.body;
3. Drag and drop a **Mongo DB** node and connect it to the previous node. In the properties window, add the following details to find if the subscription details already exist in the database:
    **Property**
    **Value**
    Database Config
    Collection
    Select **String **and enter **subscription**
    Operation
    find
    Query
    Select **bh.** and enter **subscription**
    Result Mapping
    Select** bh.** and enter **subscribers **
4. Drag and drop **Switch**** node** and connect it to the previous node. In the Script node properties window, add the following details to check for the subscriber length. If the length is 0, the subscription object is saved to the database. Else, this step is skipped:
    **Property**
    **Value**
    property
    Select** bh**. and enter **subscribers.length**
    Set the following condition in the conditions list.
    **Condition**
    **Type**
    **Value**
    ==
    number
    0
    Select **stopping after the first match** from the drop-down list at the end of the attributes window.
5. Drag and drop a **Mongo DB** node and connect it to the previous node. In the properties window, add the following details to insert the subscription details and the city name in the database:
    **Property**
    **Value**
    Database Config
    Select the database configuration that you used previously.
    Collection
    Select **String **and enter **subscription**
    Operation
    insertOne
    Document
    Select **bh.** and enter** subscription**
    Result Mapping
    Select** bh.** and enter **result**
6. Drag and drop an **Http out** node and connect it to the previous node. Double click the node and enter the following properties to send a response back to the client flow - **subscribe** indicating that the request made by the client is successful:
    **Property**
    **Value**
    Response type
    JSON
    Status code
    Select **number** property and enter the value as **200**
    Response body
    Select **as is** and enter its value as **{message:'success'}**

---

### Flow 3

This flow is used to find and delete the subscription object from MongoDB.

1. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint called **Unsubscribe**. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Method
    POST
    Select from the drop-down list.
    Path
    unsubscribe
2. Drag and drop a** Script node **and connect it to the previous node. In the **Script properties **window, add the following details to get the subscription details from the client flow - **unsubscribe** and save it in a flow variable called **subscription**:
    **Property**
    **Value**
    code editor
    bh.subscription = {subscription: bh.input.body.subscription};
3. Drag and drop a MongoDB node and connect it to the previous node. In the properties window, add the following details to find the subscription object and the city name that is saved in the flow variable **subscription** and delete it from the database:
    **Property**
    **Value**
    Database Config
    Select the database configuration that you configured previously.
    Collection
    Select **String **and enter **subscription**
    Operation
    findOneAndDelete
    Filter
    Select **bh. **and enter **subscription**
    Result Mapping
    Select** bh.** and enter** result**
4. Drag and drop an **Http out** node and connect it to the previous node. Double click the node and enter the following details to send a response back to the client service flow - **unsubscribe**.
    **Property**
    **Value**
    Response type
    JSON
    Status code
    Select **number** property and enter the value as **200**
    Response body
    Select **as is** property and enter the value as **{message: 'success'} **

---

### Flow 4

This flow is used to send weather notifications. It has a scheduler node(CRON) to notify the user about the weather details of the subscribed city at every 5-minute interval.

1. Drag and drop a **Cron** node. Double click the node and set the following properties to set a scheduler to trigger the weather notifications every 5 minutes:
    **Property**
    **Value**
    Name
     notificationScheduler
    Expression
    */5 * * * *
    Scheduled
    True
2. Drag and drop a **Script node** and enter the following details. The flow variable bh.searchQuery will be used in the MongoDB node to get all the subscribers details :
    **Property**
    **Value**
    Name
    code editor
    bh.searchQuery = {};
3. Drag and drop a **Mongo DB** node and connect it to the previous node. In the properties window, add the following details to get all the subscribers who have subscribed to the weather updates:
    **Property**
    **Value**
    Database Config
    Select the database config.
    Collection
    Select **String **and enter **subscription**
    Operation
    find
    Query
    Select bh. and enter **searchQuery**
    Result Mapping
    Select bh. and enter **subscribers**
4. Drag and drop a **Script** node and enter the following code to configure web push based on the VAPID keys. The script node also calculates the initial index and the total number of subscribers which is stored in the flow variable - bh.length.
    **Property**
    **Value**
    Name
    code editor
    bh.webPush = require('web-push');const publicVapidKey = "<your_public_vapiud_key>";const privateVapidKey = "<your_private_vapiud_key>"; bh.webPush.setVapidDetails('mailto:example@example.com', publicVapidKey, privateVapidKey);bh.length = bh.subscribers.length;bh.index = 0;
5. Drag and drop a **Switch** node and set the following conditions. After entering each property, click **+** to add the condition to the conditions list. This switch node is used to break the loop if there are no subscribers or if the notifications is sent to all the subscribers.
    **Property**
    **Value**
    Name
    Property
    Select **bh.** and enter **index**
    **Condition**
    **Value**
    Otherwise
    <
    Select **bh.** and enter** length**
6. Drag and drop a **Script** node and enter the following details to get the city name of each subscriber:
    **Property**
    **Value**
    Name
    code editor
    bh.cityName =`${bh.subscribers[bh.index].cityName}`
7. Drag and drop a **Call Service **node and set the following properties to get the weather details of the city name the subscriber has subscribed to:
    **Property**
    **Value**
    Select a flow
     reqAndSendWeatherData
    Input Variables
    Key - bh.input.cityName
    Select **bh**. and enter **cityName**
    Toggle **Map **to true.
    Output Variables
    Key - bh.local.result
    Select bh. and enter weatherData
8. Drag and drop a** Script **node and enter the following code to trigger the weather update notification based on the city name and the subscriber:
    **Property**
    **Value**
    Name
    code editor
    bh.notification = { "notification":{"body":`Temp. ${bh.weatherData.payload.main.temp}°C`,"data":`${bh.weatherData.payload}`,"dir":"auto","icon":"https://media.glassdoor.com/sqll/1960709/neutrinos-squarelogo-1564113473875.png","image":"https://media.glassdoor.com/sqll/1960709/neutrinos-squarelogo-1564113473875.png","silent":false,"title":`Weather - ${bh.subscribers[bh.index].cityName}`,"vibrate":100} };bh.notification = JSON.stringify(bh.notification);console.log(bh.subscribers[bh.index]);bh.webPush.sendNotification(bh.subscribers[bh.index].subscription, bh.notification).catch(error => {console.log(error);});bh.index = bh.index+1;

Connect the nodes in this fashion:

---

### Flow 5

1. Drag and drop an HTTP In node. Double click the node and enter the following properties:
    **Property**
    **Value**
    **Action**
    Name
   getWeatherData
    Method
    Get
    Select from the drop-down list.
    Path
    getweatherdata
2. Drag and drop a Script node. Double click the node and add the following code:Copy CodeJavaScriptbh.local.ssdWeatherApiUrl = `http://localhost:8081/api/weather`;
   bh.local.qparams = {
    cityName: "Tokyo"
   }
3. Drag and drop an **HTTP Request** node. Double click the node and add the following details:
    **Property**
    **Value**
    **Action**
    Method
    Get
    Select from the drop-down list.
    Url
    Select **bh.local** and enter **ssdWeatherApiUrl**
    Return Type
   JSON
    Result Mapping
   Select **bh.** and enter **weatherData**
    Query Parameters
   Select **bh.local** and enter **qparams**
4. Drag and drop a script node. Add the following code:Copy CodeJavaScriptconsole.log(bh.weatherData.payload)

---

### Flow 6

This flow catches any exceptions that occur in the server flows.

1. Drag and drop a **Catch** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Catch error from
    All nodes
2. Drag and drop an** HTTP Out node **and connect it to the previous node. In the **properties **window, add the following details:
    **Property**
    **>Value**
    Response type
    JSON
    Status Code
    Select **number** property and enter the value as **200**
    Response Body
    Select **as is** and enter the value as {message: 'success'}
