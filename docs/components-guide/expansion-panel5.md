# Expansion Panel

<https://documentation.neutrinos.com/articles/#!components-guide/expansion-panel5>

## Expansion Panel

OverviewExpansion panel is a container that contains some of the components such as expansion header, expansion title, expansion description, etc. Expansion panel can be used alone with all these component or it can be put inside an expansion panel outlet component.**Usage**The expansion panel component can be used where the data to be displayed in an expanded view and will be shown and hidden onclick event. Only the title and description will be shown and other components will be hidden and they will be displayed when the user clicks on it.How to useDrag and drop an expansion panel component.Fill the attributes such as style, class, ngFor, opened, closed, hidetoggle and expanded.Now a container is there various expansion components can be placed inside this.ExampleDrag and drop an expansion panel outlet component, and inside that drag and drop an expansion panel component.Drag and drop an expansion header component inside the expansion panel.Drag and drop an expansion title and expansion description component inside the expansion header component.Click on the title and provide the title= Personal Detail and click on the description component and provide the description attribute as enter your name.Save and run.An expansion panel will be displayed with the title as Personal Detail and description as enter your name. Many other components can be inserted inside it and it can be implemented more.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**ngFor:** ngFor is used when there are multiple expanded panel components. So, in that case, ngFor is used to iterate through an array or object of the expanded panel to display them. And the object or area will be defined in the .ts file. **opened:** This attribute contains an event that should be emitted every time the Accordion Item is opened, so a method or function will be defined and it will be called. Inside the function, the actions will be defined that what should happen when the item is open.**closed:** This attribute contains an event that should be emitted every time the Accordion Item is closed, so a method or function will be defined and it will be called. Inside the function, the actions will be defined that what should happen when the item is closed.**hideToggle:** It accepts boolean values as true or false, this attribute is used to check whether the expansion indicator should be hidden.**expanded:** It accepts any type of values, to check whether the Accordion Item is expanded.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
