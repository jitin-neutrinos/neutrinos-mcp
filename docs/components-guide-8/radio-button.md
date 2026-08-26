# Radio Button

<https://documentation.neutrinos.com/articles/#!components-guide-8/radio-button>

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

- **Radio Button Label**: Is the label given for the radio button. Example: If you give the label as **ABC, then t**he value **ABC** is displayed next to the **Radio Button**.
- **value**: It is the value given for the radio button.
- **Required**: Used to check whether the radio button is required or not.
- **label**: The label for the radio button.
- **i****d**: Is the unique ID for the radio button.
- **name**: Attribute used to group buttons for a unique selection.
- **checked**: Used to set the radio button to checked or not. It can be either True or False or you can click the map icon and enter the component class property name.
- **(change)**: Event emitted when the radio button selection is changed.
- **Label position**: Specifies whether the labels should appear after or before the radio-buttons. Defaults to 'after'. You can select a value from the drop-down or click the map icon and enter the component class property name.
- **Disabled**: Specify whether to disable the radio button. It can be either True or False or you can click the map icon and enter the component class property name.
- **Disabled Ripple**: Disable the ripple animation when the radio button is clicked. It can be either True or False or you can click the map icon and enter the component class property name.
- **color**: ThemePaletteColor for the radio button. It takes values like primary, accent, and warn.

### Example

1. On the UI editor of the page, drag and drop the **HTML 5** component. Set the **Element Type** as Paragraph.
2. In the HTML editor, enter Pick your favorite season: {{page.favoriteSeason}}
3. Drag and drop a **Radio Group** component. Set the following properties:
  1. **[(ngModel)]**: page.favoriteSeason
4. Drag and drop a** Radio Button** inside the Radio Group component. Set the following properties:
  1. [value]: season
  2. label: {{season}}
  3. id: radio{{i}}
  4. In the Custom Properties section, add a Key value attribute:
    1. ***ngFor**: let season of page.seasons; let i = index;
5. Navigate to the Page Flow designer of the page.
6. Add the following page variable to the **Page Variables** node in the [On Init flow](/smart/project-page-services-designer-guide/on-init-flow):
  1. **Page Variables**
     **Default Value**
     **Action**
     favoriteSeason
     Select **bh**.
     Click the + icon
     seasons
     Select **as is** and enter ['Winter', 'Spring', 'Summer', 'Autumn']
     Click the + icon
7. Save and Run the page.
8. When the page is loaded, the radio buttons with values of the seasons will be displayed. On selection of the radio button the name of the season is displayed as your favorite season.

![](/resources/Storage/components-guide-8/title-2021-09-30.png)
