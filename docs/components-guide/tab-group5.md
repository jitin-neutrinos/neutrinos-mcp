# Tab Group

<https://documentation.neutrinos.com/articles/#!components-guide/tab-group5>

## Tab Group

Overview**Tab Group** component is a container component that is used to contain one or more **Tab** components. **Tab** components should always be contained in the **Tab Group** component.**Usage****Tabgroup** component is used whenever the tab(s) are used. A tab can not exist outside of the tab group component.How to useDrag and drop the **Tab Group** component from the** Navigation** category.Drag and drop the **Tab** component(s) inside the **Tab Group** component.Set the **label** attribute of the **Tab** component(s).Drag and drop the components needed within each **Tab** component.Save the changesExampleCreate a page.Drag and drop the **Tab Group** component from the **Navigation** category.Drag and drop 3 **Tab** components inside the **Tab Group** component.Set the value of the **label** property of first, second and third Tabs as **Tab1**, **Tab2** and **Tab3** respectively.Drag and drop a **Card** component (from **Layout** category) within each tab.Set height of each card to 100px. (style = height:100px;).Set the color of each card. Eg: color: pink;Save the changes.Now, the tabs can be navigated.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
