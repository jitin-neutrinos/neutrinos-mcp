# Raised Button

<https://documentation.neutrinos.com/articles/#!components-guide-7/rised-button>

## Raised Button

### Overview

This component represents a clickable button. The button appears raised compared to a normal button component.

### Usage

Raised Button provides the user with a simple way to trigger an event, like searching for a query in a search engine, or to interact with dialog boxes, like confirming an action. It can be used to represent the importance of specific functionality that is performed on the click of this button.

### How to use

1. Drag and drop the **Raised Button** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Buttonname**: Specifies the button name that is to be displayed on the screen.
- **Color**: Takes the color based on the angular material theme.
- **Click**: This is an event that runs when the button is clicked.
- **disabled**: Used to disable the Raised button.
- **routerlink**: Used to navigate to the specified link.
- **type**: Specify the type of the Raised button.
- **disabled ripple**: Disable the ripple animation when the Raised button is clicked.

### Example

1. Input the component field(s) with the attribute value(s):

- **buttonname** = submit
- **Click **= clickEvent()

In the Ts file write the following function:

```javascript
clickEvent() {    alert("Button clicked!!!");}
```

2. Save it and run.

3. When the page is loaded the value** buttonname = submit** will be the name of the button that will be displayed on the button and **click = clickEvent() **in the event that runs when the button is pressed. On clicking the button, the alert message Button clicked!!! will be displayed.
