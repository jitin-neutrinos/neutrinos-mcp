# Button Toggle Group

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/button-toggle-group>

## Button Toggle Group

### Overview

Button toggle group contains many buttons whose behavior is similar to radio buttons. Only one of the buttons can be selected at a time.

### Usage

Selecting any one of the unselected buttons in a button group will unselect the previously selected button and selects that button.

### How to use

1. Drag and drop the **Button Toggle Group** component from Forms Control category where it is needed on that page.
2. Double click on the component and give values to the attributes.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the **Style** tab as shown below

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[align]:** Sets the alignment of the buttons in the button group. Takes vertical or Horizontal as its value (with single quotes).
- **[disableIndex]:** Index of the button that should be disabled by default. Takes a number as its value.
- **[checkIndex]:** Index of the button that should be selected by default. Takes a number as its value.
- **(valueChange)**: Takes function( that is defined in the Ts file) name as an argument which will be called whenever the value of button group changes. Example: onValChange()
- **(indexChange)**: Takes function( that is defined in the Ts file) name as an argument which will be called whenever different button gets selected in a button group. Example: onIndexChange().
- **[toggleoptions]**: This is used to **switch** from one option to another.
- **value**: Specify the value of the button toggle group.

### Example

1. Drag and drop the **Button Toggle Group** component to a page.
2. Double click on that component.
3. In the Ts file, create a property called **buttons** and set its value as below.

```javascript
buttons = [{"value":"Bold"}, {"value":"italic"}, {"value":"strike"}];
```

1. Set the value of [toggleOptions] to **buttons**.
2. Write a function in Ts file as below: Copy CodeJavaScriptonValueChange(){
    console.log("val changed")
    }
3. Set the (valueChanged) attribute to onValueChange().
4. Set **[disableIndex]** to 0.
5. Save the changes.
6. Open the address where the app is running, and try selecting a button from the button group.
7. The console will output the value changed.
