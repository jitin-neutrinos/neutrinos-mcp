# Expansion Panel Outlet

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/expansion-panel-outlet>

## Expansion Panel Outlet

### Overview

The** Expansion panel outlet **component is a container that provides an expandable view, where some of the content is hidden. It will be displayed when the user clicks on the **Expandable Panel **component. The **Expansion panel outlet **component can contain various component such as Expansion Header, Expansion Title, and Expansion Description.

### Usage

The** Expansion panel outlet **component can be used where the data to be displayed in an expanded view on click. By default, only the title and description will be shown and other components will be hidden. They will be displayed when the user clicks on it.

### How to use

1. Drag and drop an **Expansion panel outlet **component.
2. Fill the attributes such as style class, displaymode and multi.
3. Drag and drop other expansion panel components inside this.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **displayMode:** The display mode used for all expansion panels in the accordion. Currently, two display modes exist:
  - **default:** a gutter-like spacing is placed around any expanded panel, placing the expanded panel at a different elevation from the rest of the accordion.
  - **flat:** no spacing is placed around expanded panels, showing all panels at the same elevation.

- **Multiple Expansion: **It accepts Boolean values as true or false. And depending on the value it checks, whether the accordion should allow multiple expanded accordion items simultaneously or not.

### Example

1. Drag and drop an **Expansion panel outlet component,** and inside that drag and drop an **Expansion Panel **component.
2. Drag and drop an **Expansion Header** component inside the expansion panel.
3. Drag and drop an **Expansion Title** and **Expansion Description **component inside the **Expansion Header** component.
4. Click on the **Expansion Title **component and provide the title as **Personal Detail**. Click the **Description** component and provide the value as **enter your name**.
5. Save and run the page.
6. An** Expansion Panel** will be displayed with the title as **Personal Detail** and description as **enter your name**.
