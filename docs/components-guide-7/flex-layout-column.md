# Column

<https://documentation.neutrinos.com/articles/#!components-guide-7/flex-layout-column>

## Column

### Overview

A **Column** component is used to set the positions or flow of the child components vertically.

**Note: **By default, some of the attributes will be set to default values. Change it according to your needs.

### Usage

**Column** is used to display the components in a row. Components placed inside the **Column **component appear vertically.

### How to use

1. Drag and drop a **Column** component.
2. Set the required attributes such as style, class, fxflex, wrap, fxlayoutgap, layout direction, fxshow and fxhide.
3. Drag and drop any other components inside the **Column** component.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **fxFlex:** This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex basis, flex-shrink, flex-grow**.
- **wrap:** This property specifies whether the flexible items should wrap or not. It has values such as nowrap, wrap, wrap-reverse, initial, and inherit.
- **fxLayoutGap: **This attribute can be used to specify margin gaps on children within a flexbox container. It accepts integer value such as 20px, 5em, etc.
- **Layout Direction: **This attribute can be used to specify how the children components of this component should be aligned horizontally. It accepts string values such as center, start, end etc.
- **Perpendicular Direction:** This can be used to specify how the child components should be aligned vertically. It accepts string values such as center, start, end, etc.
- **fxShow: **This directive allows developers to dynamically show the element. It accepts Boolean values such as true or false.
- **fxHide:** This directive allows developers to dynamically hide the element. It accepts Boolean values such as true or false.

### Example

1. Drag and drop a **Column **component.
2. Set the component attributes values:
  - **layout direction** = start
  - **perpendicular direction** = start
3. Drag and drop some other components such as Buttons and Textboxes inside the **Column ** component.
4. Save and run the page.

When the page is loaded the components button and textbox appear vertically. And the value layout direction = start and perpendicular direction = start specifies the direction in which the flex starts.
