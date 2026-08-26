# Radio Group

<https://documentation.neutrinos.com/articles/#!components-guide-8/radio-group>

## Radio Group

### Overview

A radio group is a group of radio buttons. It allows a user to select at most one radio button from a set. Checking one radio button that belongs to a radio group unchecks the previously checked radio button within the same group.

### Usage

Radio group component is used to contain the radio buttons.

### How to use

1. Drag and drop the component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Radio Group label: **The label given for the Radio group. Example: If you give the label as ABC, then the value ABC is displayed next to the Radio Group.
- **Style**: It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[value]**: Value for the radio group. This should equal the value of the selected radio button if there is a corresponding radio button with a matching value. If there is no such corresponding radio button, this value persists, to be applied in case a new radio button is added with a matching value.
- **[(ngmodel)]**: Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user.
- **name**: Attribute used to group buttons for a unique selection. All radio buttons inside this group will use this name.
- **selected**: The currently selected radio button component instance. If set to a new radio button, the radio group value will be updated to match the newly selected button.
- **(change)**: Event emitted when the checked state of a radio button changes. Change events are only emitted when the value changes due to user interaction with the radio button.
- **Label Position**: Defines the label to appear after or before the radio button. Defaults to '**after**'.
- **Required**: Used to check whether the Radio Group is required or not.
- **label**: The label given for the radio group .

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
