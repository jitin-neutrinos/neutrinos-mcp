# user management

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/user-management>

This service is used to create a user and save user info to the Mongo DB database and fetch user data from the Mongo DB database after scanning the PAN Card.

Perform the following steps after creating the server service:

---

**Flow 1**

1. Open the service. Drag and drop a **Start node** to create a flow. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    createUser
    InputVariables -> Key
    formData
    Click **+** to add the property to the list.
    Local Variables -> Key
    result
    Toggle **Output** to true. Click **+** to add the property to the list.
    Local variables -> Key
    api
    Select string property and enter createuser
    ![client user properties](/resources/Storage/create-a-simple-mobile-app/uc1.png)
2. Drag and drop a** Call server API node**. In the ** properties **window, add the following details:
    **Property**
    **Value**
    Name
    call create api
    Method
    All
    Server Name
    All
    API
    POST createuser
    Return type
    JSON
    Body
    Select **bh.input** and enter **formData **
    Result Mapping
    Select **bh.local **and enter** result**
    ![Call service properties](/resources/Storage/create-a-simple-mobile-app/uc2.png)
3. Drag and drop a **Snackbar** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Snackbar message
    User added successfully
    Action text
    Okay
    Snackbar duration
    2000
    ![snackbar properties](/resources/Storage/create-a-simple-mobile-app/uc3.png)
4. Drag and drop a **Navigation** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Path to navigate
    /home/usersList
    ![navigation properties](/resources/Storage/create-a-simple-mobile-app/uc4.png)

**Flow 2**

1. Drag and drop a **Start node**. This is used to log variables that the user has given in the browser console. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    getUser
    Local variables
    Enter** usersList**, toggle the Output to True and click the + icon.
    /![start properties](/resources/Storage/create-a-simple-mobile-app/uc5.png)
2. Drag and drop a **Call Server API** node. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    call get api
    API
    GET getusers
    Return type
    JSON
    Result Mapping
    Select **bh.local** and enter** usersList**
    ![call server api properties](/resources/Storage/create-a-simple-mobile-app/uc6.png)

**Flow 3**

1. Drag and drop a **Catch node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Catch errors from
    Selected nodes
    createUser (Start)
    Toggle it to true
    getUsers (Start)
    Toggle it to true
    call create api (CallSSDApi)
    Toggle it to true
    call get api (CallSSDApi)
    Toggle it to true
    ![catch properties](/resources/Storage/create-a-simple-mobile-app/uc7.png)
2. Drag and drop a **Snackbar node** to flow. This node is used to catch errors thrown by nodes on the same service. Double click the node and enter the following properties.
    **Property**
    **Value**
    Snackbar message
    Enter Something went wrong
    Action text
    Enter Okay
    Snackbar Duration
    2000
    ![snackabr properties](/resources/Storage/create-a-simple-mobile-app/uc8.png)

---

Connect the nodes to create the following server flow.
