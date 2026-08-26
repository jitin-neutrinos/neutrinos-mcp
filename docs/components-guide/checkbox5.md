# Checkbox

<https://documentation.neutrinos.com/articles/#!components-guide/checkbox5>

## Checkbox

OverviewThe checkbox is rendered by default as square boxes that are checked (ticked) when activated. They allow you to select single values for submission in a form.**Note:** Radio buttons are similar to checkboxes, but with an important distinction — radio buttons are grouped into a set in which only one radio button can be selected at a time, whereas checkboxes allow you to turn single values on and off. Where multiple controls exist, radio buttons allow one to be selected out of them all, whereas checkboxes allow multiple values to be selected.**Usage**Checkbox component allows the users to select any combination of options in a group of check boxes. A group of check boxes is used for independent choices. A group of check boxes can also be used to select from a set of one or more choices.How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s): `class = check`, Id = checkSave it and run.When the page is loaded the attribute "class = check" is the class name that can be used to point to a class in a style sheet and the "id = check" is the unique id given for the checkbox which can be used to apply styles or give reference to point to the checkbox.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px; **Checked:** Used to check whether the checkbox is checked or not.**Color:** It takes the color based on the angular material theme. Takes **primary**, **accent** or **warn** as its value.**Disabled:** Used to check whether the checkbox is disabled or not.**Id:** A unique id for the checkbox input.**Labelposition:** Specifies whether the label should appear after or before the checkbox. Defaults to **after**.**Name:** Specifies the name for the component.**Required:** Used to check whether the checkbox is required or not.**Value:** Specifies the value attribute of the native input element.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
