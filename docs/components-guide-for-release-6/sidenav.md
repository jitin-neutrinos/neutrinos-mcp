# Sidenav

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/sidenav>

## Sidenav

### Overview

The **Sidenav** components are designed to add side content to a fullscreen app. **Sidenav** typically contains links to different pages in the app or links for different sections on that page. Sidenav is a fixed layout whose slide-in and slide-out activity can be bound to an action (ex. Button press, checkbox, etc.). The **Sidenav** component has meaning only when it is placed inside the **Sidenav Container **component.

### Usage

The **Sidenav** component is useful when the user needs to have immediate access to the most used pages/components of an app.

### How to use

1. Drag and drop a **Sidenav Container** component. Drag and drop a** Sidenav** component from the **Navigation **section and drop it inside the **Sidenav Container **component.
2. Populate the **Sidenav** component with the content that is required.
3. Save and run the page.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **mode: **Sidenav can render in one of three different ways based on the mode property.
  - **over - **Sidenav floats over the primary content, which is covered by a backdrop
  - **push -** Sidenav pushes the primary content out of its way, also covering it with a backdrop
  - **side - **Sidenav appears side-by-side with the main content, shrinking the main content's width to make space for the sidenav.
- **opened:** It decides whether the sidenav is opened. It can be true or false.
- **position:** Position can be either start or end which places the side content on the left or right side. Default is** start**.
- **fxLayout: **Specifies the flex-direction and whether the contents should be wrapped or not. Example, fxLayout=column wrap.
- **(opened):** Takes function name as the value. This function is defined in the Ts file and is executed when the sidenav is opened.
- **(closed): **Takes function name as the value. This function is defined in the Ts file and is executed when the sidenav is closed.
- **(toggle):** Takes function name as the value. This function is defined in the Ts file and is executed when the sidenav is toggled.
- **Autofocus: **Specify whether the drawer should focus the first focusable element automatically when opened.
- **Disable close:** Specify whether the drawer can be closed with the escape key or by clicking on the backdrop.
- **(onPositionChanged): **Event emitted when the drawer's position changes. The event is defined in the TS editor.
- **(openedChange):** Event emitted when the drawer open state is changed.
- **fixedBottomGap:** The gap between the bottom of the sidenav and the bottom of the viewport when the sidenav is in fixed mode.
- **Fixed InViewPort: **Whether the sidenav is fixed in the viewport.
- **FixedTopGap: **The gap between the top of the sidenav and the top of the viewport when the sidenav is in fixed mode.

### Example

1. Drag and drop the **Sidenav Container** component to the page.
2. Drag and drop the **Sidenav** component inside the **Sidenav Container.**
3. Drag and drop an **HTML5** component.
4. Write an anchor tag inside that HTML component with the **hre****f** attribute set to [http://www.neutrinos.co](http://www.neutrinos.co) and target attribute to **blank**.

<a href="http://www.neutrinos.co">neutrinos</a>

1. Set **(toggle)**=eventOccured() in the attribute window and write the following code in the TS editor:

```javascript
eventOccured(){  alert("Event Occured")    }
```

1. Save and run the page. Clicking the button will open the neutrinos website.
