# Button

<https://documentation.neutrinos.com/articles/#!components-guide-8/button>

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

1. In the **Page Flow Designer **of the page, create a **Clickbutton **flow. This flow displays a snackbar onclick of the button.
2. Drag and drop a **Start **node.
3. Drag and drop a **Snackbar node** and set the following properties:
  1. **Snackbar Message**: Clicked Succesfully
  2. **Action Text**: Okay
4. Connect the nodes.
5. Navigate to the UI editor of the page, drag and drop the **Button **component to a page.
6. Double click the Button component and set the following properties:
  1. **Color**: Accent
  2. **(click)**: Click **![](/resources/Storage/components-guide-8/flow_picker_icon.png)** to open the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. Select the Clickbutton flow. Save the settings.
7. Save and run the page.
8. When the page is loaded, a button is displayed. On clicking the button, the alert message **Clicked Successfully!!! **will be displayed.
