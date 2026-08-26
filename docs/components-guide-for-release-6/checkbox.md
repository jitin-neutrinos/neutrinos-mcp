# Checkbox

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/checkbox>

## Checkbox

### Overview

The checkbox is rendered by default as square boxes that are checked (ticked) when activated. They allow you to select single values for submission in a form.

| ![Information](/resources/Storage/components-guide-for-release-6/info.png) | Radio buttons are similar to checkboxes, but with an important distinction — radio buttons are grouped into a set in which only one radio button can be selected at a time, whereas checkboxes allow you to turn single values on and off. Where multiple controls exist, radio buttons allow one to be selected out of them all, whereas checkboxes allow multiple values to be selected. |
| --- | --- |

### Usage

The **Checkbox** component allows the users to select any combination of options in a group of checkboxes. A group of checkboxes is used for independent choices. A group of checkboxes can also be used to select from a set of one or more choices.

### How to use

1. Drag and drop the component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;
```

- **Checked**: Used to check whether the checkbox is checked or not.
- **Color**: It takes the color based on the angular material theme. Takes primary, accent or warn as its value.
- **Disabled**: Used to check whether the checkbox is disabled or not.
- **Id**: A unique id for the checkbox input.
- **Labelposition**: Specifies whether the label should appear after or before the checkbox. Defaults to after.
- **Name**: Specifies the name for the component.
- **Required**: Used to check whether the checkbox is required or not.
- **Value**: Specifies the value attribute of the native input element.
- **[(ngmodel)]**: Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user. The ng-model attribute is used for binding controls such as input and text area, in the view, into the model.

- **label**: The label given for the checkbox.
- **(change)**: Event emitted when the checkbox selection is changed.
- **disable Ripple**: Disable the ripple animation when the checkbox is clicked.
- **Indeterminate**: Specify whether the checkbox is indeterminate or not.

### Example

1. Input the component field(s) with the attribute value(s):

- class = check
- Id = check
- Checked= true

1. Save and run the page.
2. When the page is loaded, the attribute **class = check** is the class name that can be used to point to a class in a style sheet and the **id = check** is the unique id given for the checkbox which can be used to apply styles or give reference to point to the checkbox and **checked=true** indicated that the property is checked.
