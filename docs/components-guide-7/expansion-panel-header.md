# Expansion Panel Header

<https://documentation.neutrinos.com/articles/#!components-guide-7/expansion-panel-header>

## Expansion Panel Header

### Overview

The **Expansion Panel Header **component shows a summary of the panel content and acts as the control for expanding and collapsing. This header may optionally contain **Expansion Panel Title and Description **components. By default, the **Expansion Panel Header **component includes a toggle icon at the end of the header to indicate the expansion state. This icon can be hidden via the hideToggle property.

### Usage

The** expansion Panel Header **component is used to show the summary of the panel content.

### How to use

1. Drag and drop the **Expansion Panel **component.
2. Inside the **Expansion Panel **component, drag and drop the **Expansion Panel Header **component.
3. Double click the **Expansion Panel Header **component to display the list of attributes that can be used with it.
4. Fill the attributes which are needed and save the page.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **collapsedheight: **This attribute specifies the height of the header while the panel is collapsed.
- **expandedheight:** This attribute specifies the height of the header while the panel is expanded.

### Example

1. Input the component field with the attribute value:

- collapsedheight = 50
- expandedheight = 50

1. Save and run the page.
2. When the page is loaded the attribute value **collapsedheight = 50**. And **expandedheight = 50** specifies the height of header when the header is collapsed and expanded.
