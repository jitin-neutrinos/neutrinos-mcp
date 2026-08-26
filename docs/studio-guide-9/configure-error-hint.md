# Handle Errors

<https://documentation.neutrinos.com/articles/#!studio-guide-9/configure-error-hint>

## 

Here's how you can handle errors and hints in your application.

### Handle Errors

#### 

Error Handling in Components


 Neutrinos Studio allows you to handle errors when you use form control components like Input, Select, and Date Picker.


 To configure errors:



 Drag and drop the form control component to your app page.


 Double-click the component to open its attributes window.


 Click the** Errors **button to configure error messages.


 Enter a valid error condition and its associated message.


 Set the message alignment to **start** or** end**.


 Click **+Add **to add the configured error.


 Click** Save** to save the error, or click **+ Add** to configure another error.



 **Example**



 To display an error message if the user enters the current date less than today's date, drag and drop an **Input** component, click **Errors **in the attributes window and configure the error:

 ![Configuring error message](/resources/Storage/studio-guide-9/error_conf.png)




 To write the logic against which the error is to be validated, drag and drop a **Start** node and enter the error condition function name as the name of the node. For Example, **isValid**. In the **Start** node properties window, add a local property called **validityChecker** and enable the **Output **toggle button to make this an output property.


 Drag and drop a **Script** node and connect it to the** Start** node to create a flow. Add the following code to the editor:




 Copy CodeJavaScriptbh.local.validitychecker =
 new Date(this.page.selectedDate).getTime() > this.page.currentDate


 If the user enters a date bigger than the present date, the message configured in the Configure Errors window is displayed to the user.


 Configure Hints


 Hints are used to give specific information about some data, action, or page in an application. Once added, they appear like a snack bar in your application. To configure hints:



 Drag and drop an **Input**, **Select**, or **Date Picker **component to your app page.


 Double-click the component to open its attributes window.


 Click the** Hints **button to configure hints.


 Enter a valid hint condition and its associated message.


 Set the message alignment to **start** or** end**.


 Click **+ Add** to add the hint.


 **Save** to save the hint, or click **+ Add** to configure another hint.



 **Example:**


 To display a hint message saying " This is a required field" if the user does not enter any value in the Input field, drag and drop an **Input** component, and open its attributes window and perform the following:



 Add the following custom property of type Key&Value:


 **key: ** #data




 **value: ** ngModel








 Bind the custom attribute to the [(ngModel)] property:

 ![binding the attribute to ngModel](/resources/Storage/studio-guide-9/configure-error-hint-2021-08-17-2.png)







 Click the **Hints** button to open the **Configure Hints **editor and add a hint that has to display a message when the Input field is left empty:

 ![Configure Hints](/resources/Storage/studio-guide-9/conf_hint.png)









 Click** Add** in the Configure Hints editor to add the hint to the editor.




 Click **Save** to save and close the editor.




 When the Input field is left empty on the end app, a hint message is displayed like this:




 ![The Name field in the end app](/resources/Storage/studio-guide-9/name_1.png)![The hint displayed when the name is not entered](/resources/Storage/studio-guide-9/name_2.png)
