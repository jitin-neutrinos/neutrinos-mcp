# Expansion Panel Title

<https://documentation.neutrinos.com/articles/#!components-guide-8/expansion-panel-title>

## Expansion Panel Title

### Overview

The **Expansion Panel Title **component is used to display the title of the [Expansion Panel](/articles/components-guide-8/expansion-panel). This component cannot be used individually. It should be used inside the [Expansion Header](/articles/components-guide-8/expansion-panel-header) component.

### Usage

The **Expansion Title** component is used to display the title for the **Expansion Panel **content. Only the title will be displayed, and the other components (if any) will be displayed after clicking the title.

### How to use

1. Drag and drop the **Expansion Panel **component.
2. Inside the **Expansion Panel **component, drag and drop the **Expansion Header** component. And inside the **Expansion Header** component drag and drop the **Expansion Title** component.
3. Double click the **Expansion Title** component to display the list of attributes that can be used with it.
4. Fill in the attributes which are needed and save the page.

### Associated Attributes

- **Expansion Title label: **The display name of the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The **class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **title: **The title of the expansion panel.

### Examples

To learn how to use this component, see the examples documented in [Expansion Panel Outlet](/articles/components-guide-8/expansion-panel-outlet).
