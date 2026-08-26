# Slider

<https://documentation.neutrinos.com/articles/#!components-guide-7/slider>

## Slider

### Overview

The **Slider** component allows for the selection of a value from a range via mouse, touch, or keyboard. By default the minimum value of the slider is 0, the maximum value is 100, and the slider moves in increments of 1. These values can be changed by setting the min, max, and step attributes respectively. The initial value is set to the minimum value unless specified.

### Usage

The slider component is used to select a range of values through mouse, touch or keyboard. Sliders reflect a range of values along a bar, from which users may select a single value. They are ideal for adjusting settings such as volume, brightness, or applying image filters.

### How to use

1. Drag and drop the **Slider **component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Slider label**: The label given for the Slider. Example: If you give the label as ABC, then the value ABC is displayed next to the Slider.
- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[(ngmodel)]**: Used for two-way data binding. The ng-model attribute is used to bind the data in your model to the view presented to the user.
- **Color**: A drop-down list that accepts the color theme. You can choose between the following colors, or click the Edit button to input the color of your choice:
  - 'primary'
  - 'accent'
  - 'warn'
- **Invert**: Used to check whether the slider is inverted. The value has to be boolean i.e. either true or false.** Example:- invert: false.**
- **max**: Specifies the maximum value that the slider can have. The value should be a number. **Example:- max: 10.**
- **min**: Specifies the minimum value that the slider can have. The value should be a number. **Example:- min: 0.**
- **step**: Specifies the values at which the slider will slide. The value should be a number. **Example:- step: 1.**
- **Show Thumb-label**: Specifies whether or not to show the thumb label. The value should be a boolean i.e. either true or false. **Example:- **thumbLabel: boolean.
- **Vertical**: Specifies whether the slider is vertical or not. The value has to be boolean i.e. either true or false. **Example:- vertical: false.**
- **disabled**: Specifies whether the component is disabled or not. The value has to be boolean i.e. either true or false. **Example:- disabled: false.**
- **value**: Specifies the value of the slider. The value should be either number or null. **Example:- value: number | null.**
- **(change)**: It is an event emitted when the slider value is changed.
- **(input)**: It is an event emitted when the slider thumb moves.
- **tickInterval**: Specify the interval for the slider which is used while dragging.

### Example

1. Input the component field(s) with the attribute value(s):

- **invert **= true
- **step** = 50
- **(changed)**= valueChange():

```javascript
valueChange(){  alert('value changed')    }
```

2. Save it and run.

3. When the page is loaded the value** invert = true** will display an inverted slider, **step=50** specifies the step increment value of the slider and the **valuechanged()** function will show the changed value. In this example, the slider takes two clicks to move to the end of the slider.
