# Design the Server Flow

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/call-a-server-flow-from-page>

| ![Information](/resources/Storage/how-to-articles-8/info.png) | This example is only applicable to Classic apps created on Neutrinos Studio. |
| --- | --- |

You call a server endpoint from the page to perform some action on the page such as fetching some information from the server or submitting some information to the server.

To call a server endpoint, perform the following steps:

1. Design the server flow using the [Call Server API](/smart/project-page-services-designer-guide/call-server-api-node) node.
2. Call the server flow from the page UI and bind it to an action (such as a click of a button).
3. When the action takes place, the API is called. It executes the server flow and performs the desired action.

Let's look at an example. Create a form with a **Submit** button on the user interface. When the user enters the details on the form and clicks the **Submit** button, the following actions should take place:

1. The** Submit** button calls the page flow.
2. The page flow calls the API in the **Call Server API **node.
3. The API, when called, executes the server flow and adds the user information to the MongoDB database.

Perform the following steps to configure this functionality in the app:

### Design the Server Flow

Design the server service flow to accept the contact information from the page and save it to the MongoDB database.

1. Create a server flow using the **HTTP In** node, **MongoDB** node, and the **HTTP out** node.
    ![createuser server flow](/resources/Storage/how-to-articles-8/createuser_server.png)
2. The [HTTP In](/smart/project-server-side-service-designer/http-in) node, create the **createuser** API to perform the** POST** operation on the MongoDB database.
    ![Createuser API endpoint](/resources/Storage/how-to-articles-8/create_httpin.png)
3. Configure the [MongoDB node](/smart/project-server-side-service-designer/mongodb-node) to insert the user record into the NoSQL Database.
    ![Inserting a mongo record](/resources/Storage/how-to-articles-8/create_mongo.png)
4. Configure the [HTTP Out node](/smart/project-server-side-service-designer/http-out-node) to send the response of the operation back to the page.
    ![http out node](/resources/Storage/how-to-articles-8/create_httpout.png)

### Design the Page Flow

1. On the [page flow designer](/smart/project-concepts/page-designer/a/h3_520216706), design the **createUser** page flow using the** Start **node and **Call Server API** node.
    ![createUser Flow in CSD](/resources/Storage/how-to-articles-8/call%20service%20page%20flow.png)
2. In the** Start** node, create a function called **createUser**, accept the **formData** object containing user information from the page, and then map the result of the operation to the **result** object.
    ![The Start node of createuser flow](/resources/Storage/how-to-articles-8/createuser_str.png)
3. In the **Call Server API **node, call the POST/createuser API server flow. Pass the formData to the body of the API and save the result of the operation in the result variable.
    ![Call server API](/resources/Storage/how-to-articles-8/call_api.png)
4. Depending on the result of the API, show a snack bar message to the user. If the status code returned by the server API is 200, show a snack bar saying **"The user profile is created"**. Else, show a snack bar message saying "An error has occurred". Drag and drop a **Switch** node and configure the following properties.
    ![Switch node](/resources/Storage/how-to-articles-8/switch_status.png)
5. Drag and drop a **Snackbar** node and connect to the first output port of the **Switch** node. Configure the properties window.
    ![Snackbar node to display a success message](/resources/Storage/how-to-articles-8/snackbar1.png)
6. Drag and drop another **Snackbar** node and connect to the second output port of the **Switch** node. Configure the properties window.
    ![Snackbar node to display an error message](/resources/Storage/how-to-articles-8/snackbar2.png)

### Design the UI of the Page

1. On the [page UI designer](/smart/project-concepts/page-designer/a/h3__1090805748), drag and drop components and design the form. The user is required to enter a few details and click the **Submit** button.
    ![Form to capture user information](/resources/Storage/how-to-articles-8/form_page.png)
2. In the attributes window of the Form, create a custom property called formData of **Key&Value** type and map it to the Angular ngForm to bind the form fields to the template variable simpleForm.
    ![form properties](/resources/Storage/how-to-articles-8/form_properties.png)
3. In the Attributes window of the **Submit **button, bind the **createUser** page flow to the click() event using the flow picker.
    ![button properties](/resources/Storage/how-to-articles-8/submit_button.png)
4. On the flow picker editor, map the input variable formData to simpleForm.value. Where simpleForm is the custom property that we created in the form.
    ![flow picker editor](/resources/Storage/how-to-articles-8/flowpicker_submit.png)

On click of the **Submit **button, the user information entered in the form is stored in an object called **formData** and sent to the server API. The server API saves the data in the MongoDB database and sends the status code back to the page indicating the status of the request. Depending on the status code received a snack bar message is displayed to the user on the UI.

![error](/resources/Storage/how-to-articles-8/form2.png)
