# Button Toggle Group

<https://documentation.neutrinos.com/articles/#!components-guide-7/button-toggle>

## Button Toggle Group

### Overview

The button toggle group contains many buttons whose behavior is similar to radio buttons. Only one of the buttons can be selected at a time.

### Usage

Selecting any one of the unselected buttons in a button group will unselect the previously selected button and selects that button.

### How to use

1. Drag and drop the **Button Toggle Group** component from the **Layouts **category where it is needed on that page.
2. Double click on the component and give values to the attributes.

### Associated Attributes

- **Button Toggle Group Label:** The label given for the Button Toggle Group. Example: If you give the label as ABC, then the value ABC is displayed next to the Button Toggle Group.
- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the **Style** tab as shown below

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[name]: **Name for the underlying input element.
- **[value]**: Specify the value of the button toggle group.
- **Disabled: **Used to disable the multiple button toggle group.
- **Multiple: **Specify whether the multiple button toggles can be selected.
- **Vertical: **Specify whether the toggle group is vertical.
- **(change): **Event emitted when the button selection is changed.
- **Button Toggle Appearance: **The appearance style of the button. It can be standard or legacy.
- **[(ngmodel)]: **Used for two-way data binding. The ngmodel attribute is used to bind the data in your model to the view presented to the user.

**Button Toggle**

- **Button Toggle name**: The label given for the Button Toggle. Example: If you give the label as ABC, then the value ABC is displayed next to the Button Toggle.
- **[name]: **Attribute used to group buttons for a unique selection.
- **[id]:** The unique ID for this button toggle.
- **Checked: **Used to check whether the button is checked.
- **[value]: **ButtonToggleGroup reads this value to assign its own value when the toggle with the particular value is selected.
- **Disable Ripple: **Disable the ripple animation when the button is clicked**. **
- **Disabled: **Used to disable the button toggle.
- **(change): **Event emitted when the group value changes.
- ***ngFor: **ngFor is used to iterate through the array object and get the data. The syntax of ngFor is property value is let d of data where d is a loop variable and data is an array or object from which the data will be accessed.

**Advanced Properties**:

- **Show Icon Before Label: **Set to **True **if you want to show an icon before the toggle button name.
- **IconBeforeLabel: **The icon that is to be displayed
- **IconBeforeLabelClass: **The class associated with the icon.
- **IconBeforeLabelStyle: **The CSS styling of the icon.
- **Show Icon After Label: **Set to **True** if you want to show an icon after the toggle button name.
- **IconAfterLabel: **The icon that is to be displayed.
- **IconAfterLabelClass: **The class associated with the icon.
- **IconAfterLabelStyle: **The CSS styling of the icon.

### Example

1. Drag and drop the **Button Toggle Group** component to a page.
2. In the Ts file, create a property called **buttons** and set its value as below.

```javascript
buttons = [{"value":"Bold"}, {"value":"italic"}, {"value":"strike"}];defaultValue = this.buttons[0].value
```

1. Set the value of *ngFor in the button toggle component to let button of buttons.
2. Write a function in Ts file as below: Copy CodeJavaScriptonValueChange(event) {
    console.log("val changed", event)
   }
3. Set the value of **[value]** attribute to button.value in the **button toggle** component.
4. Set the value of **(change)** attribute to onValueChange() in the **button toggle group** component.
5. Set the value of **[value]** attribute to defaultValue in the **button toggle group** component.
6. Save the changes.
7. Open the address where the app is running, and try selecting a button from the button group.
8. The console will output the value changed.
