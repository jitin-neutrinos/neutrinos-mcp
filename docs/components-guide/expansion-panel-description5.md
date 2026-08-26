# Expansion Panel Description

<https://documentation.neutrinos.com/articles/#!components-guide/expansion-panel-description5>

## Expansion Panel Description

OverviewThe **Expansion Panel Description** component is used for describing the expansion panel components. It can be used inside the **Expansion Panel Header** component or it can be used individually to display the description.**Usage****Expansion Panel Description** is used to write a description for the expansion panel content. Only the description will be displayed.How to useDrag and drop the **Expansion Panel **component.Inside the expansion panel component, drag and drop the expansion header component. And inside the expansion-header component drag and drop the expansion-description component.Double click the** **Expansion Panel Description** **component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page.ExampleInput the component field with the attribute value: description = This is a description panelSave it and run.When the page is loaded the attribute value **description = This is a description panel** will be displayed. And when the description is clicked, the expansion-header panel will be extended.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background:orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg class1, class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**description:** This attribute used to give a description for the expansion panel. **Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
