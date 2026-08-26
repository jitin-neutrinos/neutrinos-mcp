# Tab

<https://documentation.neutrinos.com/articles/#!components-guide/tab5>

## Tab

OverviewTabs are used to navigate between different views within the same context. Only one view is rendered at a time. Tabs should always be used inside a **Tab Group** component.**Usage**Tabs are useful for containing and navigating between contextually related but distinct contents.How to useDrag and drop the **Tab Group** component from the **Navigation** category.Drag and drop the **Tab** component(s) inside the **Tab Group** component.Set the **label** attribute of the **Tab** component(s).Drag and drop the components needed within each **Tab** component.Save the changes.ExampleCreate a page.Drag and drop the **Tab Group** component from the **Navigation** category.Drag and drop to **Tab** components inside the **Tab Group** component.Set the values of first and second Tabs' **label** property to **Image** and **Tab2** respectively.Drag and drop the **Image** component from the **Form Controls** category and set its attributes.Drag and drop to **Card** components from the **Layout** category into each of the tabs.Set height of each card to 50px. (style = height:50px;).Set the color of each card. eg. color: pink. Save the changes.Now, the tabs can be navigated.**Associated Attributes**
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
**label:** It is the name of the tab as seen in the app. Takes string as its value.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
