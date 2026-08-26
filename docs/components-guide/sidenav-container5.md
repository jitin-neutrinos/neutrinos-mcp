# Sidenav Container

<https://documentation.neutrinos.com/articles/#!components-guide/sidenav-container5>

## Sidenav Container

OverviewThe **Sidenav Container** is the container component for the **Sidenav** component. **Sidenav** component has meaning only when it is placed inside the **Sidenav Container** component. Everything that is not contained within the **Sidenav** component and contained within **Sidenav Container **component will appear as the main content that is outside the sidenav bar.**Usage**Sidenav container is used whenever a sidenav is required. Sidenav cannot exist outside sidenav container component.How to useDrag and drop the **Sidenav Container** component from the **Navigation **section.ExampleCreate a page called **page**.Drag and drop the **Sidenav Container**.Drag and drop the **Sidenav** component inside the **Sidenav Container**.Populate the **Sidenav** component with 3 buttons and provide button names.Save the changes.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class **attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style **side menu. The **Class **attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style **tab as shown below.
Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
