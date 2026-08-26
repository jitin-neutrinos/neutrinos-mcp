# Router Outlet

<https://documentation.neutrinos.com/articles/#!components-guide/router-outlet5>

## Router Outlet

OverviewPaths can be configured for every page in an app using the Routes menu in the left panel. These paths specify how a page can be reached. A page can have child paths. Router Outlet defines the position of a navigated page within a page from where it is navigated. It acts as a placeholder for the navigated page.**Usage**Router Outlet is used to render a page in the desired location within another page.How to useConfigure the paths and child paths using the **Routes** menu.Drag and drop **Router Outlet** component from the **Navigation** section inside a page’s container where the routed page should be rendered.**Example**
Create 2 pages called **home** and **child**.Define a route for the **child** page as a child path of the home component.Create a button component on the **home** page.Set the button’s **router links** to attribute to the **child** page’s path.Drag and drop the **Router Outlet** component from the **Navigation** category in the **home** page container where the routed page (**child**) should be rendered. Save the changes.Now, when the button is clicked, the **child** page will be rendered where the **Router Outlet** component was placed on the **home** page.**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
