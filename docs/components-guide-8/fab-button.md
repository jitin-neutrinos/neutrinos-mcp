# Fab Button

<https://documentation.neutrinos.com/articles/#!components-guide-8/fab-button>

## Fab Button

### Overview

**FABs (Floating Action Buttons**) are standard material design components. They are shaped as a circle that represents a promoted action. When pressed, it may contain more related actions. FABs, as its name suggests, are floating over the content in a fixed position.

### Usage

The **fab button** can be used to contain more related actions.

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

- **fabicon**: Specifies the text or image to be shown on the button.
- **Color**: Takes the color based on the angular material theme.
- **Click**: This is an event that checks when the button is clicked.
- **disabled**: Used to disable the fab button.
- **disabled ripple**: Disable the ripple animation when the **fab button** is clicked.
- **type**: Specify the type of the fab button.
- **routerlink**: Used to navigate to the specified link.

### Example

1. In the **Page Flow Designer **of the page, create a **Clickbutton **flow. This flow displays a snackbar onclick of the button.
2. Drag and drop a **Start **node.
3. Drag and drop a **Snackbar node** and set the following properties:
  1. **Snackbar Message**: Clicked Successfully
  2. **Action Text**: Okay
4. Connect the nodes.
5. Navigate to the UI editor of the page, drag and drop the **Fab** **Button **component to a page.
6. Double click the Fab Button component and set the following properties:
  1. **fabicon**: Home
  2. **(click)**: Click **![](/resources/Storage/components-guide-8/flow_picker_icon.png)** to open the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor. Select the Clickbutton flow. Save the settings.
7. Save and run the page.
8. When the page is loaded, a button is displayed. On clicking the button, the alert message **Clicked Successfully!!! **will be displayed.
