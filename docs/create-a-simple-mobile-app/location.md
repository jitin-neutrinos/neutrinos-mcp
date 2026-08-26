# location

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/location>

The location service is used to fetch the current location using the geolocation plugin. This service has 4 flows:

Open the** location** service and perform the following steps:

**Flow 1**

1. Drag and drop a **Start node** to create a flow. The Start node is the entry point for a flow. When you create a Start node and call the flow, a system-defined object called bh is created. When you create input and local properties in the Start node, they are added to the bh object. See [Start Node](/smart/project-service-designer-user-s-guide/start-node) learn more. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    getCurrentLocation
    Local variables--> Key
    Coordinates
    Toggle **Output** to true. Click **+** to add the property to the list. See the screenshot below for a better understanding.
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    getlocation
    code editor
    const onSuccess = this.onSuccess.bind(this);const onError = this.onError.bind(this);navigator.geolocation.getCurrentPosition(onSuccess, onError);console.log('get current weather was called');
    ![location service properties](/resources/Storage/create-a-simple-mobile-app/locc2.png)

**Flow 2**

1. Drag and drop a **Start** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    onSuccess
    Accept flow object
    Toggle to true
    ![start properties](/resources/Storage/create-a-simple-mobile-app/locc3.png)
2. Drag and drop a **Services Variables** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    send response
    Operation type
    Set service variables
    Variables list
    Enter loc as service variable and select as is available and enter bh.
3. Drag and drop a **Script node**. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Script
    let bh = this.sdService.__constructDefault({});
   bh.system.pubsubService.$pub('getloc-complete');
   ![script properties](/resources/Storage/create-a-simple-mobile-app/locc5.png)

**Flow 3**

1. Drag and drop a **Start** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    onError
    Accept flow object
    Toggle it to true
   ![start properties](/resources/Storage/create-a-simple-mobile-app/locc6.png)
2. Drag and drop a **Snackbar node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Snackbar message
    Select string property and enter Could not get coordinates
    Action Text
    Select string property and enter okay
    Snackbar duration
    2000
    ![snackbar properties](/resources/Storage/create-a-simple-mobile-app/locc7.png)

---

After creating all the flows, the service will look like this:
