# user management

<https://documentation.neutrinos.com/articles/#!create-a-simple-mobile-app/user-management-server>

This service contains API created to save the user information to the Mongo DB database and an API to get data of the user from the database.

Open the **usermanagement **service and perform the following steps after creating the server service:

**Flow 1**

1. Open the service. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint that responds to the requests. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    create user api
    Method
    Post
    Select from the drop-down list.
    Path
    createuser
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    construct url params
    code editor
    bh.local.doc = bh.input.body
    console.log(bh.input.body)
    ![script node of the weather app](/resources/Storage/create-a-simple-mobile-app/UMS2.png)
3. Drag and drop a **MongoDB** node. Double click the node and enter the following properties:
  1. You need to add a MongoDB database connection that was mentioned before in the prerequisites. To do so,
  2. Click the map icon next to the **Database config** field in the attributes window.
  3. Enter the URL of your MongoDB database.
  4. After adding the URL, navigate back to the attributes window and add the following properties:
4. Drag and drop an **Http out** node. The **HTTP out** node is used to send responses back to requests received from an **HTTP In** node and it is also used to pass the control to the next middleware. Double click the node and enter the following properties:
    **Property**
    **Value**
    Name
    Response type
    JSON
    Status code
    Select **number** property and enter the value as **200**
    Response body
    Select **bh.local** property and enter the value as **result**
    ![user management properties](/resources/Storage/create-a-simple-mobile-app/UMS4.png)

**Flow 2**

1. Drag and drop a **HttpIn node** to create a flow. The **HTTP In** node is used to create an HTTP endpoint that responds to the requests. Double click the node and enter the following:
    **Property**
    **Value**
    **Action**
    Name
    getusers
    Method
    Get
    Select from the drop-down list.
    Path
    getusers
2. Drag and drop a** Script node**. In the **Script properties **window, add the following details:
    **Property**
    **Value**
    Name
    construct url params
    code editor
    bh.local.query={}
    ![script node of the weather app](/resources/Storage/create-a-simple-mobile-app/UMS6.png)
3. Drag and drop a **MongoDB** node. You will be using the same MongoDB configuration as that of the previous one. Double click the node and enter the following properties:

Connect the nodes to create the following server

After configuring this service, you can view the swagger documentation. To do so,

- Save the service.
- Click the **Click here for swagger link** icon and the swagger docs appear.

![Swagger docs icon](/resources/Storage/create-a-simple-mobile-app/SWAG.png)

The swagger document should look like this:
