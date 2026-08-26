# Expansion Description

<https://documentation.neutrinos.com/articles/#!components-guide-8/expansion-panel-description>

## Expansion Description

### Overview

The **Expansion Panel Description **component is used to display the description of the [Expansion Panel](/articles/components-guide-8/expansion-panel). This component cannot be used individually. It should be used inside the [Expansion Header](/articles/components-guide-8/expansion-panel-header) component.

### Usage

**Expansion Description** is used to write a description of the expansion panel content. Only the description will be displayed.

### How to use

1. Drag and drop an **Expansion Panel** component.
2. Inside the component, drag and drop the **E****xpansion Header** component. And inside the **E****xpansion Header** component, drag and drop the **E****xpansion Description** component.
3. Double click the **Expansion Description** component to display the list of attributes that can be used with it.
4. Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Expansion Description label: **The display name of the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided example- background:orange;height:200px;).
- **Class: **The** class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **description: **The description of the expansion panel.

### Examples

To learn how to use this component, see the examples documented in [Expansion Panel Outlet](/articles/components-guide-8/expansion-panel-outlet).
