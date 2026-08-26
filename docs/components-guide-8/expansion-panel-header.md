# Expansion Panel Header

<https://documentation.neutrinos.com/articles/#!components-guide-8/expansion-panel-header>

## Expansion Panel Header

### Overview

The **Expansion Panel Header **component is used within the [Expansion Panel](/articles/components-guide-8/expansion-panel) component to display a header. This component cannot be used individually.

To display the header, you use the [Expansion Panel Title](/articles/components-guide-8/expansion-panel-title) and [Expansion Panel Description](/articles/components-guide-8/expansion-panel-description) components.

When a page is loaded, by default, only the **Expansion Panel Title** and **Expansion Panel Description **are displayed. The other components (if added) are displayed when the user clicks on the component.

### Usage

The** Expansion Panel Header **component is used to show the summary of the panel content.

### How to use

1. Drag and drop the **Expansion Panel **component.
2. Inside the **Expansion Panel **component, drag and drop the **Expansion Panel Header **component.
3. Double click the **Expansion Panel Header **component to display the list of attributes that can be used with it.
4. Fill in the attributes which are needed and save the page.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The** class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **collapsedheight: **Thhe height of the header while the panel is collapsed.
- **expandedheight:** The height of the header while the panel is expanded.

### Examples

To learn how to use this component, see the examples documented in [Expansion Panel Outlet](/articles/components-guide-8/expansion-panel-outlet).
