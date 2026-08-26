# Flow 1

<https://documentation.neutrinos.com/articles/#!tutorial-create-a-pwa/design-client-service-flows>

When you convert your app to PWA, the [SW-Events](/smart/project-service-designer-user-s-guide/pwa-sw-events) and [Firebase](/smart/project-service-designer-user-s-guide/pwa-firebase) nodes are installed on the Client Services Designer. You can use the **SW-Events** nodes to work with [Service Worker](/smart/project-concepts/service-worker) events, and the **Firebase **nodes to subscribe and listen to [Web Push Notifications](/smart/project-concepts/web-push-notifications) through the Service Worker.

In this section of the tutorial, you will be creating the following client service flows using the above-described nodes to:

- Subscribe to web push notifications and get weather updates of a city
- Get subscription details after subscribing to push notifications
- Unsubscribe from web push notifications

### 

| ![Information](/resources/Storage/tutorial-create-a-pwa/info.png) | Click the **How to Use** icon in the attributes window of a node to learn more about that node. |
| --- | --- |

Design the following flows:

### Flow 1

This flow is used to subscribe to web push notifications using the server public key (VAPID key) and get the subscription object on a successful subscription. It then calls the** Subscribe** flow on the Server Services Designer and passes the subscription object and the city name (to which the user has subscribed) as the body of the HTTP Request.

1. Drag and drop a **Start node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    subscribe
    Input Variables-> Key
   cityName
   Click + to add the property to the list.
    Local variables -> Key
    response
    Toggle **Output** to true. Click **+** to add the property to the list.
    Local variables -> Key
   resultToggle **Output** to true. Click **+** to add the property to the list.
2. Drag and drop **FCM Subscribe** node. This node is used to subscribe to web push notifications by entering the server public key. Double click the node and enter the following:
    ![Warning](/resources/Storage/tutorial-create-a-pwa/warning.png)
    Make sure you enter the server public key that you generated using **npm web push** in place of <your server public key>.
    **Property**
    **Value**
    **Action**
    Server Public Key
    <your server public key>
    Select **String** as property and then enter the value.
    Result Mapping
    result
    Select **bh.local** as property and then enter the value.
3. Drag and drop the **Service Variable** node. Double click the node and enter the following details to store the subscription object returned by the server in the service variable called subscription:
    **Property**
    **Value**
    **Action**
    Operation Type
    Set Service Variables
    Select from the drop-down list.
    Variables list
    Subscription
    Enter **subscription** as service variable and select **bh.local** and enter **result.**
4. Drag and drop a Script node. In the **Script properties **window, add the following details to send the subscription object and the city name as a body of the HTTP Request:
    **Property**
    **Value**
    code editor
    bh.ssdURL = `${bh.system.environment.properties.ssdURL}subscribe`;
   bh.body = {
    subscription: bh.local.result,
    cityName: bh.input.cityName
   }
5. Drag and drop the **HTTP Request** node. Double click the node and enter the following details to trigger the Subscribe flow designed on Server Services Designer:
    **Property**
    **Value**
    **Action**
    Name
    subscribe HTTP request
    Method
    POST
    URL
    ssdURL
    Select **bh.** property and enter the value.
    Return Type
    JSON
    Body
    body
    Select **bh.** property sand enter the value
    Result Mapping
    response
    Select **bh.local** property sand enter the value

---

### Flow 2

This flow is used to store the subscription object as a service variable.

1. Drag and drop **FCM OnSubscibe** node. Double click the node and enter the following:
    **Property**
    **Value**
    Name
    Result Mapping
    Select **bh.** property and enter **result**.
2. Drag and drop the **Service Variable** node. Double click the node and enter the following details to log the subscription object:
    **Property**
    **Value**
    **Action**
    Operation Type
    Set service variables
    Select from the drop-down list.
    Variables List
    Subscription
    Enter **subscription** as service variable and select **bh.** and enter **result**.

---

### Flow 3

This flow is used to handle any exceptions when calling the Subscribe flow on the Server Services Designer. If the subscription fails, the** Unsubscribe** client flow is called.

1. Drag and drop **Catch** node. Double click the node and enter the following:
    **Property**
    **Value**
    Catch from errors
    Selected nodes.
    subscribe HTTP request
    Toggle this to true.
    ![catch node properties](/resources/Storage/tutorial-create-a-pwa/catchcp.png)
2. Drag and drop a **Call Service** node. Double click the node and select the **Unsubscribe **flow. Map the key bh.local.result to the value bh.local.result. If any exception is caught by the Catch node, the Unsubscribe flow is triggered. ![call service properties](/resources/Storage/tutorial-create-a-pwa/callservicecp.png)

---

### Flow 4

This flow is used to get the subscription details from the service variable - **subscribe** and then call the unsubscribe server flow on Server Services Designer to unsubscribe from push notifications.

1. Drag and drop a **Start** node. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    unsubscribe
    Local Variables
    response
    Toggle the Output and click the plus icon.
    Local VariablesresultToggle the Output and click the plus icon.
2. Drag and drop a **Service Variable** node. Double click the node and enter the following details to fetch the details in the service variable- subscribe:
    **Property**
    **Value**
    **Action**
    Operation Type
    Get Service Variables
    Select from the drop-down list.
    Variables List
3. Drag and drop **Script **node**.** Double click the node and enter the following details to store the subscription obhect in bh.body:
    **Property**
    **Value**
    Code editor
   bh.ssdURL = `${bh.system.environment.properties.ssdURL}unsubscribe`;
   bh.body = { subscription: bh.local.subscription }
4. Drag and drop a **HTTP Request** node. Double click the node and enter the following details to call the Unsubscribe server flow:
    **Property**
    **Value**
    Method
    POST
    URL
    Select **bh.** property and enter **ssdURL**
    Return Type
    JSON
    Body
    Select **bh. **property and enter **body **as the value
    Result Mapping
    Select **bh.local **property and enter **response **as the value
5. Drag and drop an **FCM Unsubscribe** node. Double click the node and enter the following:
    **Property**
    **Value**
    Result Mapping
    Select **bh.local **property and enter **result **as the value
6. Drag and drop a **Service Variable** node. Double click the node and enter the following details to set the result of the unsubscribe operation in the service variable - suscription:
    **Property**
    **Value**
    Operation Type
    Set Service Variables
    Variables List
7. Drag and drop a **Snackbar** node. Double click the node and enter the following details to display a snack bar message to the user:
    **Property**
    **Value**
    Snackbar Message
    You have Successfully Unsubscribed
    Action Text
     Ok
    Snackar Duration
   2000

---

### Flow 5

This flow is used to log the notification on the Console. You can use this data to perform any operation of your choice.

1. Drag and drop **On Notification Click** node. Double click the node and enter the following:
    **Property**
    **Value**
    Result Mapping
    Select **bh.** property and enter **result **as the value.
2. Drag and drop a** Script **node. Double click the node and enter the following:
    **Property**
    **Value**
    code editor
    window.open(bh.result.notification.data.url);
