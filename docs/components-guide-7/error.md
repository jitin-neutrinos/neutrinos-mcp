# Error

<https://documentation.neutrinos.com/articles/#!components-guide-7/error>

ErrorOverviewThe Error component allows you to configure custom error messages to be displayed on the screen when the error conditions are met.How to useDrag and drop an Error component to the page container.Double click the component to display the list of attributes that can be used with it.Fill the required attributes.Save and run the page.Associated Attributes**Error Label:** The Display name of the error.**style**: Accepts a string value that affects different properties of the Card such as height, width, and color, based on the values provided. For example: background:orange:height:200px.**class:** Used to point to a class in a style sheet. Each class contains one or more style statements defined in the Style editor. The Class field accepts space-separated class names such as class1, class2, where each class is defined in the Style editor as shown below:Copy CodeCSS.class1 {
border-radius:10px;
flex-basis:10%;
height:100px;
}
.class2 {
border-radius:10px;
flex-basis:10%;
height:100px;
}**Error Message:** Enter the information to be displayed on the screen when the error is generated.**Error Condition**: Specify the condition which defines an error.**Input hint align:** Alignment to input the hint messages. That is, start or end.ExampleDrag and drop a **column** component and **row** component inside the column.Drag and drop **text area** component and **error** component inside the row.Double click the text area component and set the following attributes **[(ngModel)]**=usernameIn the custom properties, select the **attribute** tab and enter #user and select **key&value** tab and enter ngModel
Double click the error component and set the following attributes**error message**=text required **error condition**=username.length < 1
**Input hint align**= startSave and run the page.On page rendering, the error message will popup on the screen if the error condition turns out to be true.
