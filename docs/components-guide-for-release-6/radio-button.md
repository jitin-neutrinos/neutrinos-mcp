# Radio Button

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/radio-button>

## Radio Button

### Overview

A **R****adio Button** is a button that can be either checked or unchecked. A user can tap the button to check or uncheck it. It can also be checked using the checked property. Use an element with a radio-group attribute to group a set of radio buttons. When radio buttons are inside a radio group, exactly one radio button in the group can be checked at any time. If a radio button is not placed in a group, they will all have the ability to be checked at the same time.

### Usage

**Radio buttons** are typically rendered as small circles, which are filled or highlighted when selected. It can be either checked or unchecked.

### How to use

1. Drag and drop the **Radio Button** component to the page.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (example: background: orange; height: 200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Value**: It is the value given for the radio button.
- **Required**: Used to check whether the radio button is required or not.
- **Label**: Is the label given for the radio button. Example: If you give the label as **ABC, then t**he value **ABC** is displayed next to the **Radio Button**.
- **Id**: Is the unique ID for the radio button.
- **Name**: Attribute used to group buttons for a unique selection.
- **Checked**: Used to check whether the radio button is checked or not.
- **Label position**: Specifies whether the labels should appear after or before the radio-buttons. Defaults to 'after'.
- **(change)**: Event emitted when the radio button selection is changed.
- **Disabled**: Disable the radio button.
- **Disabled Ripple**: Disable the ripple animation when the radio button is clicked.
- **color**: ThemePaletteColor for the radio button. It takes values like primary, accent and warns.

### Example

1. Input the component field(s) with the attribute value(s):

- **Checked** = oncheck()
- **Value** = option1

2. In the Ts file write the following function:

```javascript
oncheck() {    alert("checkbox checked");}
```

3. Save it and run.

4. When the page is loaded the attribute checked = oncheck() is the event that runs when the radio button is checked. On checking the radio button the alert message checkbox checked will be displayed. The value attribute displays the value option1 for the radio button.
