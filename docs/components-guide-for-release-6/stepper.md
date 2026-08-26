# Stepper

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/stepper>

## Stepper

### Overview

The **Stepper** component is used to divide the content into steps. A page can be divided into parts instead of getting the information at once, the information is retrieved in steps. A task can be divided into certain steps or parts and each of them will have some actions.

### Usage

So if there is a requirement of creating a login page where username and password should be given and after that submit button, this can be divided into three steps such as at first, get the username, then at second, get the password, and finally, the submit option. The stepper component can be used to a great effect in the above use-case.

### How to use

1. Drag and drop a **Stepper** component.
2. Double click on the component and fill the required properties in the attribute window.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **linear(True/False): **The linear attribute can be set on **mat-horizontal-stepper** and **mat-vertical-stepper **to create a linear stepper that requires the user to complete previous steps before proceeding to follow steps. It accepts a Boolean value.
- **type:** This accepts one of the two values either horizontal or vertical. If the stepper is horizontal then give the type as horizontal and vice versa.
- **matHorizontalStepper:** Used to create a horizontal stepper, which means the step will be displayed in a horizontal direction. So if the steps should be displayed in a row then just provide the value as **mat-horizontal-stepper**.
- **matVerticalStepper: **Used to create a vertical stepper, the steps will be displayed in a vertical direction. So if the steps should be displayed in a row then just provide the value as **mat-vertical-stepper**.
- **[selected]:** The first step to be selected, give the step label that should be selected by default at the first step. It will contain the label of one of the Stepper component.
- **[selectedIndex]: **Accepts a number. In this attribute, the step that should be first is given index = 0, so the value of the index will be (index=position-1).
- **(selectionChange): **This is an event emitter that will be emitted when the selected step has changed from previous to next.
- **(animationDone)**: Event emitted when the animation is done.

### Example

Create a stepper with the login process.

1. Drag and drop a **Stepper** component.
2. Drag and drop three **Step** components inside the **Stepper **component, and give the label as **getUsername**, **getPassword**, and **reset**.
3. Drag and drop a card component inside the **getUsername** step 1 to accept the username. Double click the card component and set the properties in the attributes window.
4. Drag and drop an **Input **component inside the **getPassword** step 2 to accept the password.
5. Drag and drop a **Button** component inside the **reset **step. Set the name of the button as reset. Double click on the button component and set the properties in the attribute window
  - click()=S1.reset()
6. Double click the stepper component and set the following properties
  - matHorizontalStepper=S1
  - type= horizontal
  - selected= getUsername
  - set the index as 0 so that the **getUsername** step will come first.
  - (selectionChange)= selectionChange($event). Enter the following code in the TS editor Copy CodeJavaScriptpublic selectionChange($event?: StepperSelectionEvent): void {
      console.log('stepper.selectedIndex: ' + this.selectedIndex
      + '; $event.selectedIndex: ' + $event.selectedIndex);
      if ($event.selectedIndex == 0) return;
      // First step is still selected
      this.selectedIndex = $event.selectedIndex;
     }

A stepper with getUsername, getPassword, and reset button will be displayed.
