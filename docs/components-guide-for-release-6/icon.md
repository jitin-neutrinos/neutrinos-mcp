# Icon

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/icon>

## Icon

### Overview

The icon component represents an icon in the application. Icons are most effective when they improve the visual interest and grab the user's attention. They help guide users while they're navigating a page.

### Usage

Icons are used when we need to improve the visual interest and grab the user's attention. They help guide users while they're navigating a page.

### How to use

1. Drag and drop the** Icon** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height: 200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **IconName**: Specifies a name for the icon.
- **[inline]**: If set to true, it will automatically resize the icon to match the font size of the element the icon is contained in.
- **color**: It takes the color based on the angular material theme. Takes primary, accent or warn as its value.

### Example

1. Input the component field(s) with the attribute value(s):

- **iconname** = home
- **class **= icon

1. Save it and run.
2. When the page is loaded the value **iconname = home** will be the name of the icon that will be displayed on the button and **class = icon** is the name of the class that can be used to point to a class in a style sheet.
