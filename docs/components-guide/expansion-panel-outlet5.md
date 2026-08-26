# Expansion Panel Outlet

<https://documentation.neutrinos.com/articles/#!components-guide/expansion-panel-outlet5>

## Expansion Panel Outlet

OverviewExpansion panel outlet component is a container which provides the expandable view, where some of the content will be hidden and it will be displayed when the user clicks on the expandable panel component, it can contain various component such as expansion header, expansion title, and expansion description, etc.**Usage**Expansion panel outlet component can be used where the data to be displayed in a expanded view, and will be shown and hidden onclick event. Only the title and description will be shown and other components will be hidden and they will displayed when the user clicks on it.How to useDrag and drop an expansion panel outlet component.Fill the attribute such as style class, displaymode and multi.Drag and drop other expansion panel components inside this.ExampleDrag and drop an expansion panel outlet component, and inside that drag and drop an expansion panel component.Drag and drop an expansion header component inside the expansion panel.Drag and drop an expansion title and expansion description component inside the expansion header component.Click on the title and provide the title= Personal Detail and click on the description component and provide the description attribute as enter your name.Save and run.An expansion panel will be displayed with the title as Personal Detail and description as enter your name. Many other component can be inserted inside it and it can be implemented more.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**displayMode:** The display mode used for all expansion panels in the accordion. Currently, two display modes exist: 1: default: a gutter-like spacing is placed around any expanded panel, placing the expanded panel at a different elevation from the rest of the accordion. 2: flat: no spacing is placed around expanded panels, showing all panels at the same elevation.**Multi-** It accepts boolean values as true or false. And depending on the value it checks, whether the accordion should allow multiple expanded accordion items simultaneously or not.
**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
