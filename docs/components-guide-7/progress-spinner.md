# Progress Spinner

<https://documentation.neutrinos.com/articles/#!components-guide-7/progress-spinner>

## Progress Spinner

### Overview

Progress spinner component is a circular indicator of progress and activity.

### Usage

A progress spinner is a graphical element that is used to show the loading of a process or an activity. The progress spinner keeps spinning until the specified activity is completed.

### How to use

1. Drag and drop the component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height: 200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Progress Spinner label: **The label given for the Progress Spinner. Example: If you give the label as ABC, then the value ABC is displayed next to the Progress Spinner.
- **Mode**: Specifies the mode of the progress circle. The value should be either determinate or indeterminate. Defaults to '**in****determinate**'.
- **strokeWidth**: Specifies the stroke width of the progress spinner. The value should be a number.
- **[value]**: Specifies the value of the progress circle. The value should be a number.
- **Color**: A drop-down list that accepts the color theme. You can choose between the following colors, or click the Edit button to input the color of your choice:
  - Primary
  - Accent
  - Warn
- **[diameter]**: Specify the diameter of the spinner.

### Example

1. Input the component field(s) with the attribute value(s):

- **strokewidth** = 100
- **mode** = determinate

1. Save it and run.
2. When the page is loaded the **strokewidth = 100** will be the size of the progress spinner component that will be displayed and **mo****de = determinate **is the mode in which the progress spinner is displayed.
