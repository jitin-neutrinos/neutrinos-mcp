# Slide Toggle

<https://documentation.neutrinos.com/articles/#!components-guide-7/slide-toggle>

## Slide Toggle

### Overview

Slide Toggle component is used to toggle between on/off. The toggle allows the user to change a setting between two states.

### Usage

Slide Toggle is a specialized control that has the ability to be selected. Typically a toggle is rendered similarly to a button.

### How to use

1. Drag and drop the **Slide Toggle **component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Slide Toggle label: **The label given for the Slide Toggle. Example: If you give the label as ABC, then the value ABC is displayed next to the Slide Toggle.
- **Required**: Used to check whether the slide-toggle is required or not.
- **text**: Specifies the text to be displayed for the slide-toggle when the application is run.
- **Labelposition**: Specifies whether the label should appear after or before the slide-toggle. Defaults to 'after'. Values to be specified are before and after.
- **name**: Name value will be applied to the input element if present. The value should be either string or null.
- **id**: A unique id for the slide-toggle input.
- **(change)**: The event that will be dispatched each time the slide-toggle changes its value.
- **checked**: Used to check whether the slide-toggle element is checked or not.
- **Color**: A drop-down list that accepts the color theme. You can choose between the following colors, or click the Edit button to input the color of your choice:
  - Primary
  - Accent
  - Warn
- **Disabled**: Used to disable the Slide toggle.
- **Disabled Drag Value**: Disable the drag value of the slide toggle.
- **Disabled Ripple**: Disable the ripple animation when the slide-toggle is clicked.
- **Disabled Toggle Value**: Disable the toggle value of the slide toggle.
- **(dragchange)**: Event emitted when the drag value of the slide toggle changes.
- **(togglechange)**: Event emitted when the slide toggle changes.

### Example

1. Input the component field(s) with the attribute value(s):

- **Class** = toggle
- **Text** = on/off

1. Save it and run.
2. When the page is loaded** class = toggle **will assign the class name as a toggle, which can be used to point to a class in a style sheet and the **text = on/off** is the text that is displayed next to the component.
