# Toolbar

<https://documentation.neutrinos.com/articles/#!components-guide-8/toolbar>

## Toolbar

### Overview

A** Toolbar** is a container that contains headers, titles, menus or actions that perform specific functions.

### Usage

They are designed to provide easy and immediate access to users' most frequently used functions or provide relevant information about the page or application.

### How to use

1. Drag and drop the** Toolbar** component from the** Navigation **section into a page’s container where the toolbar component should be rendered.
2. Fill in the** Content** attribute with the value the toolbar should contain.
3. Save and run the page.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Color: **It takes the color based on the angular material theme. Takes "**primary**", "**accent**" or "**warn**" as its value.
- **Content:** This is displayed inside the toolbar. Its value can be plain text or valid Html tags. Example, **This is a toolbar** or Html tags like <button mat-button>I'm a button</button>.

### Example

1. Create a page.
2. Drag and drop the **Toolbar **component from the **Navigation** section.
3. Set the Content attribute to** I'm a toolbar**.
