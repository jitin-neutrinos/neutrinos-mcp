# Button

<https://documentation.neutrinos.com/articles/#!components-guide-7/button>

## Button

### Overview

The **Button** component represents a clickable button, which can be used in forms, or anywhere in a document that needs simple, standard button functionality.

### Usage

Button refers to any graphical control element that provides the user a simple way to trigger an event, like searching for a query in a search engine, or to interact with dialog boxes, like confirming an action.

### How to use

1. Drag and drop the **Button **component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Buttonname**: Specifies the button name that is to be displayed on the screen.
- **Color**: It takes the color based on the angular material theme. Takes primary, accent or warn as its value.
- **Click**: This is an event that runs when the button is clicked.
- **Disabled**: Used to check whether the button is disabled or not.
- **disable ripple**: Disable the ripple animation when the button is clicked.
- **type**: Specify the type of the button. For example, Submit and Reset.
- **routerlink**: Used to navigate to the specified link.

### Example

1. Input the component field(s) with the attribute value(s):
  - buttonname = submit
  - Click = clickEvent()
2. In the Ts file write the following function:Copy CodeJavaScriptclickEvent() {
    alert("Button clicked!!!");
   }
3. Save it and run.
4. When the page is loaded the value **buttonname = submit** will be the name of the button that will be displayed on the button and** click = clickEvent()** in the event that runs when the button is pressed. On clicking the button, the alert message Button clicked!!! will be displayed.
