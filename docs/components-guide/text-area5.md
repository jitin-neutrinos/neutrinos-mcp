# Text Area

<https://documentation.neutrinos.com/articles/#!components-guide/text-area5>

## Text Area

OverviewText area component is a form control field to input user data such as numbers, alphabets, special characters, password, email, search, etc. Input can be used within the forms to capture the data from the user.**Usage**Text-area component specifies an input field where the user can enter data. Input elements are used within a form element to declare input controls that allow users to input data. An input field can vary in many ways, depending on the type attribute.How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s):  `value = input text here ` `class = input`Save it and run.When the page is loaded the **value = input text here** will be the text that will be displayed and the **class = input** is the class name that can be used to point to a class in a style sheet. **Associated Attributes**
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
**Value:** It specifies the pre-defined text that is displayed in the text area when the application is run. Example “hello” defined in this field will display hello in the text field when the application is run.**Placeholder:** Used to hold the defined text value. Example “Name” holds the value Name for the text field.**Required:** Specifies that the text field should be filled and should not hold empty values. The value should be boolean i.e. either true or false.**Color:** Takes the color based on the angular material theme.**Name:** Specifies the name for the text field.**Ngmodel:** Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user. The ng-model attribute is used for binding controls such as input and text area, in the view, into the model.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
