# Mini Fab Button

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/mini-fab-button>

## Mini Fab Button

### Overview

**Mini FABs (Floating Action Buttons) **are standard material design components. They are shaped like a circle and represents a promoted action. When pressed, it may contain more related actions. Mini FABs, as its name suggests, are floating over the content in a fixed position.

### Usage

The mini fab button component can be used to contain more related actions.

### How to use

1. Drag and drop the** Mini Fab Button** component.
2. Double click the component to display the list of attributes that can be used with it.
3. Fill the attributes which are needed and save the page.

### Associated Attributes

- **Style**: It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (Example: background: orange; height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (Example: class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **fabicon**: Specifies the text seen on the button.
- **Color**: Takes the color based on the angular material theme.
- **Click**: The event that runs when the button is clicked.
- **disabled**: Used to disable the fab button.
- **disabled ripple**: Disable the ripple animation when the Mini fab button is clicked.
- **type**: Specify the type of the Mini fab button.
- **routerlink**: Used to navigate to the specified link.

### Example

1. Input the component field(s) with the attribute value(s):
2. **fabicon** = decorate
3. **Click** = clickEvent()
4. In the Ts file write the following function. Copy CodeJavaScriptclickEvent() {
    alert("Button clicked!!!");
   }
5. Save it and run.
6. When the page is loaded the value **fabicon = decorate** will be the name of the button that will be displayed on the button and **click = clickEvent()** is the event that runs when the button is pressed. On clicking the button, the alert message Button clicked!!! will be displayed.
