# Button Toggle

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/button-toggle>

## Button Toggle

### Overview

Button toggle component is used to toggle between on/off. When the button is clicked it will be activated and when the button is clicked again the button will be deactivated.

### Usage

A toggle is a specialized control that has the ability to be selected. It is used to activate the button on/off.

### How to use

1. Drag and drop the **Button Toggle** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height: 200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Value**: **ButtonToggleGroup** reads this value to assign its own value.
- **Buttonname**: Specifies the button name.
- **Name**: Name attribute for the underlying input element.
- **Id**: The unique ID for this button toggle.
- **Checked:** Used to check whether the button is checked.
- **Changed**: Is the event emitted when the group value changes and the event occurs is defined in the TS editor.
- **Click**: Is the event used to check whether the button is clicked or not and the event that occurs when the toggle is clicked should be defined in the TS editor.

### Example

1. Input the component field(s) with the attribute value(s):

**Class** = toggle

**buttonname** = Click to toggle.

**(click)**=clicked()

Copy CodeJavaScriptclicked(){
 alert('you clicked')
}

1. Save it and run.
2. When the page is loaded** class = toggle** attribute will assign the class name as toggle, which can be used to point to a class in a style sheet. The **buttonname = Click to toggle** attribute is the name given to the button and (click)=clicked() is the event that occurs when the toggle is clicked.
