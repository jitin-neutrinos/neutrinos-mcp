# Router Outlet

<https://documentation.neutrinos.com/articles/#!components-guide-8/router-outlet>

## Router Outlet

### Overview

Paths can be configured for every page in an app using the **Routes** menu in the left panel. These paths specify how a page can be reached. A page can have child paths. The **Router Outlet** component defines the position of a navigated page within the page from where it is navigated. It acts as a placeholder for the navigated page.

### Usage

Router Outlet is used to render a page in the desired location within another page.

### How to use

1. Configure paths and child paths using the** Routes** menu.
2. Drag and drop the **Router Outlet **component from the **Navigation** section inside a page’s container where the routed page should be rendered.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **(activate):** Event emitted when the router outlet is activated.
- **(deactivate):** Event emitted when the router outlet is deactivated.

### Example

1. Create 2 pages called **home** and **ch****ild**.
2. Define a route for the child page as a child path of the **home** page.
3. Create a **Button** component on the home page.
4. Set the button’s router links to attribute to the child page’s path.
5. Drag and drop the **Router Outlet **component from the **Navigation **category in the home page container where the routed page (child) should be rendered. Save the changes.
6. Now, when the button is clicked, the child page will be rendered where the **Router Outlet **component was placed on the home page.
