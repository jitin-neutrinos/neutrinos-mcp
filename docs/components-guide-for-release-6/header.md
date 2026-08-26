# Header

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/header>

## Header

### Overview

The **Header** component typically contains one or more heading elements (h1 - h6), logo or icon, authorship information. There can be several eader components in one document.

### Usage

A **Header** component is used when the content should be displayed with some special properties such as bigger font size, or when the text should be in bold. Various components can be inserted inside a **Header** component.

### How to use

1. Drag and drop a **Header** component.
2. Fill the attribute such as style and class.
3. Components such as the h1-h6 component, paragraph component, etc., can be added.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

### Example

Display a **Header** component with the title a subtitle in and a paragraph component

1. Drag and drop a **Header** component, and provide the style and class attribute.
2. Now drag and drop an HTML 5 component. Select the element type as Header 3. In the HTML editor of Header 3, enter Agra. This sets the title to Agra.
3. Now drag and drop an HTML 5 component and set the **element type** as **paragraph **inside the Header component, and provide some text as content that will be displayed below the subtitle.
4. Save and Run the page.
5. A block with title Agra in h3 and a paragraph will be displayed.
