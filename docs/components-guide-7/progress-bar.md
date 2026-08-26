# Progress Bar

<https://documentation.neutrinos.com/articles/#!components-guide-7/progress-bar>

## Progress Bar

### Overview

Progress Bar is used for indicating progress and activity. It is used to indicate the progress of the work that has been completed.

### Usage

The progress bar is a graphical control element used to visualize the progression of an extended computer operation, such as file download, file transfer, or installation.

### How to use

1. Drag and drop the** Progress Bar** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Progress Bar Label:** The label given for the Progress Bar. Example: If you give the label as ABC, then the value ABC is displayed next to the Progress Bar.
- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height: 200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Mode**: It is used to select the mode. Must take one of the following values: determinate, indeterminate, buffer, query. Defaults to '**determinate**'.
- **Color**: A drop-down list that accepts the color theme. You can choose between the following colors, or click the Edit button to input the color of your choice:
  - Primary
  - Accent
  - Warn
- **Value**: Value of the progress bar. Defaults to zero. The input value should be a number.
- **Buffervalue**: Specifies the buffer value of the progress bar. Defaults to zero. The input value should be a number.
- **(animatedEnd)**: Event emitted when the progress bar animation ends.
- **[progressbarID]**: Specify the Unique id for the progress bar.

### Example

1. Input the component field(s) with the attribute value(s):

- **value **= 55
- **mode** = determinate
- **(animationEnd)**=animation()

```javascript
animation(){    alert('animation end')}
```

2. Save it and run.

3. When the page is loaded, A progress bar (in Determinate mode) with 55% of work completed is displayed.
