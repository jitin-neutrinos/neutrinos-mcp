# Expansion Panel Header

<https://documentation.neutrinos.com/articles/#!components-guide/expansion-panel-header>

## Expansion Panel Header

OverviewThe expansion-panel-header shows a summary of the panel content and acts as the control for expanding and collapsing. This header may optionally contain panel-title and panel-description. By default, the expansion-panel header includes a toggle icon at the end of the header to indicate the expansion state. This icon can be hidden via the hideToggle property.**Usage**Expansion-header is used to show the summary of the panel content.How to useDrag and drop the expansion panel component.Inside the expansion panel component, drag and drop the expansion header component.Double click the expansion header component to display the list of attributes that can be used with it.Fill the attributes which are needed and save the page. ExampleInput the component field with the attribute value: collapsedheight = 50 expandedheight = 50Save it and run.When the page is loaded the attribute value "collapsedheight = 50". And "expandedheight = 50" specifies the height of header when the header is collapsed and expanded.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1, class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**collapsedheight:** This attribute specifies the height of the header while the panel is collapsed. **expandedheight:** This attribute specifies the height of the header while the panel is expanded.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
