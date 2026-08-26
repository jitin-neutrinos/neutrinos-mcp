# Sidenav

<https://documentation.neutrinos.com/articles/#!components-guide-8/sidenav>

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

1. In the styles editor of the app, add the following CSS:
2. Copy CodeCSS.example-container {
    width: 500px;
    height: 300px;
    border: 1px solid rgba(0, 0, 0, 0.5);
   }
   .example-sidenav-content {
    display: flex;
    height: 100%;
    align-items: center;
    justify-content: center;
   }
   .example-sidenav {
    padding: 20px;
   }
3. In the **Page Flow Designer **of the page, update the **On Init** flow.
4. Add the following page variable to the Page Variables node in the On Init flow:
5. ![](/resources/Storage/components-guide-8/title-2021-10-27.png)
6. Navigate to the Page UI designer.
7. Drag and drop a Sidenav Container component to the page. Set the following properties:
  1. **Class**: example-container
8. Drag and drop a Sidenav component and set the following properties:
  1. **Class**: example-sidenav
  2. **Sidenav Mode**: Side
  3. In the custom properties section, select Attribute and enter **#drawer** in the attribute field.
9. Drag and drop a HTML 5 component and set the element type to **Paragraph**.
10. Double click the HTML editor and enter Auto-resizing sidenav
11. Drag and drop another HTML 5 component and set the following properties:
  1. **Element type**: Paragraph
  2. In the custom properties, select Key&Value and enter** *ngIf **in the key field and **page.showFiller **in the value field.
12. Double click the HTML editor and enter Lorem, ipsum dolor sit amet consectetur.
13. Drag and drop a **Button **inside the sidenav component and set the following attributes:
  1. **buttonName**: Toggle extra text
  2. **color**: Primary
  3. **(click)**: page.showFiller = !page.showFiller
14. Drag and drop a HTML 5 component inside the sidenav container component and set the class as example-sidenav-content
15. Drag and drop a Button inside the HTML 5 component and set these properties:
  1. **buttonName**: Toggle sidenav
  2. **(click)**: drawer.toggle()
16. Save and run the page.
