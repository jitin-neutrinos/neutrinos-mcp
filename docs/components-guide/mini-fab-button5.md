# Mini Fab Button

<https://documentation.neutrinos.com/articles/#!components-guide/mini-fab-button5>

## Mini Fab Button

OverviewMini FABs (Floating Action Buttons) are standard material design components. They are shaped as a circle and represents a promoted action. When pressed, it may contain more related actions. Mini FABs, as its name suggests, are floating over the content in a fixed position.**Usage**The mini fab button component can be used to contain more related actions.How to useDrag and drop the component. Double click the component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field(s) with the attribute value(s): `fabicon = decorate ``Click = clickEvent() ` In the **Ts** file write the following function.Copy CodeJavaScriptclickEvent() {

 alert("Button clicked!!!");
}  2. Save it and run.  3. When the page is loaded the value **fabicon = decorate** will be the name of the button that will be displayed on the button and **click = clickEvent()** is the event that runs when the button is pressed. On clicking the button, the alert message **Button clicked!!!** will be displayed.
**Associated Attributes****Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
} **fabicon:** Specifies the text seen on the button.**Color:** Takes the color based on the angular material theme.**Click:** Is an event that runs when the button is clicked.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
