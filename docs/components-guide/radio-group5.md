# Radio Group

<https://documentation.neutrinos.com/articles/#!components-guide/radio-group5>

## Radio Group

OverviewA radio group is a group of radio buttons. It allows a user to select at most one radio button from a set. Checking one radio button that belongs to a radio group unchecks the previously checked radio button within the same group.**Usage**Radio group component is used to contain the radio buttons.How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s):  `Labelposition = after ` `Name = rdgroup`Save it and run.When the page is run the label appears after the radio button and name specifies the name given to the component. All radio buttons inside the group will use this name.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**Value:** Value for the radio group. Should equal the value of the selected radio button if there is a corresponding radio button with a matching value. If there is no such corresponding radio button, this value persists, to be applied in case a new radio button is added with a matching value.**Ngmodel:** Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user.**Name:** Attribute used to group buttons for unique selection. All radio buttons inside this group will use this name.**Change:** Event emitted when the checked state of a radio button changes. Change events are only emitted when the value changes due to user interaction with the radio button.**Selected:** The currently selected radio button. If set to a new radio button, the radio group value will be updated to match the newly selected button.**labelposition:** Defines the label to appear after or before the radio button. Defaults to 'after'.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
