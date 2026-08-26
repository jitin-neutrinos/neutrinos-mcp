# Expansion Title

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/expansion-panel-title>

## Expansion Title

### Overview

This component is used to display the title for the **Expansion Panel** component. It can be used inside the **Expansion Header** component or it can be used individually to display the title.

### Usage

The **Expansion Title** component is used to display the title for the **Expansion Panel **content. Only the title will be displayed, and the other components will be displayed after clicking the title.

### How to use

1. Drag and drop the **Expansion Panel **component.
2. Inside the **Expansion Panel **component, drag and drop the **Expansion Header** component. And inside the **Expansion Header** component drag and drop the **Expansion Title** component.
3. Double click the **Expansion Title** component to display the list of attributes that can be used with it.
4. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **title: **Specifies the title that is to be displayed when the page is loaded.

### Example

1. Drag and drop the **Expansion Title **component and set the title attribute to **title** = {{title.text}}.
2. Create a Custom key-value pair property. Set: **key**= *ngFor**Value**= let title of titles
3. In the TS editor, add the following code: Copy CodeJavaScripttitles= [{text: "Expansion Title"}, {text: "Exp Title"}];
4. Save and run the page.
5. When the page is loaded, both the titles will be displayed.
