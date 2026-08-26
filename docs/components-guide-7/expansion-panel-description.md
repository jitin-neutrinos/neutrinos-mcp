# Expansion Description

<https://documentation.neutrinos.com/articles/#!components-guide-7/expansion-panel-description>

## Expansion Description

### Overview

The **Expansion Description** component is used for describing the expansion panel components. It can be used inside the **Expansion Panel Header** component or it can be used individually to display the description.

### Usage

**Expansion Description** is used to write a description of the expansion panel content. Only the description will be displayed.

### How to use

1. Drag and drop the **Expansion Description** component.
2. Inside the component, drag and drop the **E****xpansion Header** component. And inside the E**xpansion Header** component drag and drop the E**xpansion Description** component.
3. Double click the **Expansion Description** component to display the list of attributes that can be used with it.
4. Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **description: **This attribute used to give a description of the expansion panel.

### Example

1. Set the description field value to **This is a description panel**.
2. Save and run the page.
3. When the page is loaded, this is a description panel will be displayed. And when the description is clicked, the **Expansi****on Header** panel will be extended.
