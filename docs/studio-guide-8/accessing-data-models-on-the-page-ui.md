# Accessing Data Models on the Page UI

<https://documentation.neutrinos.com/articles/#!studio-guide-8/accessing-data-models-on-the-page-ui>

When you create a page on Neutrinos Studio, along with the page variable, a namespace called page.dm gets created. This namespace can be used to access the data model that you have designed on the **[Models](/articles/studio-guide-8/designing-data-models)** editor, and bind them to the page UI. See [Properties in Page Designer](/smart/project-page-services-designer-guide/properties-page-designer) to learn about the page properties in more detail.

**Example 1:**

Let us look at an example of creating a data model called **user**.

On the front-end, we will bind the data model attributes to the form elements, capture the user information, and display the information on click of the **Submit **button.

**Step 1: Create the data model**

1. Click** Models** on the side menu of the Studio Application page, and select **Add New**.
2. Create a new data model called **user**.
    ![the user data model](/resources/Storage/studio-guide-8/user_datamodel.png)
3. Create the following data model attributes:
    ![attributes of the data model](/resources/Storage/studio-guide-8/user_dm_attr.png)
4. Save the changes.

**Step 2: Bind the data Model to the Page UI**

Create or open a page. On the HTML editor of the page, drag and drop a **Card** component to the canvas.




 Click on the **card title** and enter the title as **User Details**.




 Add a** Form** component inside the **card content**.




 To align the form elements vertically, drag and drop a **Column** component inside the form. Set the fxlayoutGap to **2rem**.




 Add an** Input** component inside the column. Set the following properties:




 placeholder: **Full Name**




 [(ngModel)]: **page.dm.user.name**






 Add a **Date Picker** component below the input component. Set the following properties:




 placeholder: **Date of Birth**




 [(ngModel)]: **page.dm.user.dob**




 **Step 3: Bind the Data Model to a Page Flow**

 Open the flow designer of the page.
 Drag and drop a **Start** node to the canvas and name it **submitForm**.
 Join a **Page Variables** node to the Start node to make a flow and set the following properties:

 Operation Type: **Get Page variables**

 Variables List: select bh. and enter **userinfo** and map it to the dm.user data model. The flow property **userinfo** will save the details entered by the user on the form.


 Add a** Script** node to the flow and enter the following code in the editor. This node will create an alert message displaying the user details (that you entered in the form) on the alert window.Copy CodeJavaScriptalert(JSON.stringify(bh.userInfo))


 **Step 4: Bind the Page Flow to a Component's Attribute:**



 Drag and drop a **Button** component below the date picker and set the following properties:




 button name: **Submit**




 (click): Click the **Pick a Flow** mat chip and select the **submitForm** flow.






 Save and preview the page.



 On the end app, enter the details and click the **Submit** button. An alert window is displayed with the user details.





 ![preview of the app](/resources/Storage/studio-guide-8/user_details.png)
