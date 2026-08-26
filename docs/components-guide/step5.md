# Step

<https://documentation.neutrinos.com/articles/#!components-guide/step5>

## Step

OverviewStep component is used inside a stepper component and can different components such as a textbox, buttons, radio buttons, checkbox, images, etc. A page can be divided into steps using stepper and step.**Usage**Step component can be used to create a page that is divided into various steps, it can be displayed horizontally or vertically.How to useDrag and drop a stepper component.Fill the required properties.Example**Create a stepper with the login process.**
1. Drag and drop a stepper component. In matHorizontalStepper set the same value to make it horizontal. Suppose there are three steps component, labeled as getusername, getpassword, and submit. 2. Drag and drop three-step components inside the stepper component, and give the label as getUsername,getPassword and submit. 3. Click at the stepper component and set the attribute such as type=horizontal, selected=getUsername and set the index as 0 so that the getUsername step will come first. 4. Now in getUsername step, drag and drop an input text to accept username from the user; drag and drop an input component inside getPassword step to accept the password, and a button inside the submit step. Set the name of the button as Login. 5. Save the page and run. 6. A stepper will be displayed with getUsername, getPassword and submit button will be displayed.**Associated Attributes****Style:** It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class **attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1, class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**Label:** Label is the name given to a step and each step will have different labels and accepts text values.**completed:** This accepts boolean values as true or false depending on whether the step is marked as completed.**editable:** This attribute accepts boolean value as true or false to make it whether the user can return to this step once it has been marked as completed.**interacted:** This attribute is used to check whether the user has seen the expanded step content or not. it accepts boolean values and the default value is false.**optional:** This attribute accepts boolean values as true or false, which makes a given step optional.**step control: ** This attribute is used to check the validity of the step. **Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
