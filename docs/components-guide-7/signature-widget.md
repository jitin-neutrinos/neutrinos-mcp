# Signature Widget

<https://documentation.neutrinos.com/articles/#!components-guide-7/signature-widget>

## Signature Widget

### Overview

The Signature Widget component creates a canvas for handwritten signatures where it is dropped. It contains options to save a signature, undo a stroke, reset the canvas and cancel the operation.

### Usage

Signature Widget Component is used when there is a need for a handwritten signature. It also removes the need to scan and upload the signature.

### How to use

1. Drag and drop the** Signature Widget **component from the Advanced Category where it is needed on that page.
2. Double click on the component and give values to the attributes.
3. Save the changes.

### Associated Attributes

- **Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: The class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[(imageData)]**: It takes a property name that is defined in the Ts editor which stores the signature image data. Enter the image data in the form of an array of points.
- **[backgroundColor]**: Color of the canvas. The color format accepted is ‘RGB(255,255,255)’ (with single quotes).
- **Mode**: Specifies the mode of the Signature Widget. The value should be either **Responsive **or **Click-fullscreen**. Defaults to '**Responsive**'. Or click the map icon and enter the name of the component class property.
- **[dotSize]:** Radius of a single dot. Takes a number as its value.
- **[minWidth]:** Minimum width of a line.
- **[maxWidth]:** Maximum width of a line.
- **[throttle]**: The max rate (per millisecond) at which the next point is drawn.
- **[minDistance]:** Add the next point only if the previous one is farther than x pixels.
- **[penColor]**: Color used to draw the lines. The color format accepted is ‘RGB(255,255,255)’ (with single quotes).
- **[velocityFilterWeight]**: Weight used to modify new velocity based on the previous velocity.
- **[onBegin]**: Function that should be executed when the stroke begins. It takes function name as its value.
- **[onEnd]: **Function that should be executed when the stroke ends. It takes function name as its value.

### Example

1. Drag and drop the** Signature Widget **component to a page.
2. Double click on that component.
3. In the Ts file, create a property called **color** and set its value to **RGB(0,0,0)**’. For example: **color = 'rgb(0,0,0)'**

1. Set the value of** [backgroundColor]** to **color.**
2. Set the** [dotSize]** attribute to '**3**' and **[penColor]** to **‘****rgb(255,255,255)’**.
3. Set the value of** [mode] **to** 'click-fullscreen' **(with single quotes). Save the changes.
4. Go to the address where the app is running. Click the** pencil icon** to display the canvas.
5. The canvas is now black and anything written on it is white.
6. Draw something. Click on the save icon. (or 'X' icon to cancel and exit the canvas).
7. After the signature is saved if there is a need to edit it, click on the 'pencil' icon.
