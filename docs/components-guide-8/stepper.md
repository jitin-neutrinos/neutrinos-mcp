# Stepper

<https://documentation.neutrinos.com/articles/#!components-guide-8/stepper>

## Stepper

### Overview

The **Stepper** component is used to divide the content into steps. A page can be divided into parts instead of getting the information at once, the information is retrieved in steps. A task can be divided into certain steps or parts and each of them will have some actions.

### Usage

So if there is a requirement of creating a login page where username and password should be given and after that submit button, this can be divided into three steps such as at first, get the username, then at second, get the password, and finally, the submit option.

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

1. In the **Page Flow Designer **of the page, add page variables in the Page Variable node of the **On Init** flow.
2. Double click the Page Variable node and enter the following properties:
  1. Operation Type: Set Page Variables
  2. Variables List: **Variable name**
     **Default value**
     firstFormGroup
     secondFormGroup
3. Drag and drop a Use Dependency node to the On Init flow. Double click the node and set the following to import the form component to the page:
4. ![](/resources/Storage/components-guide-8/title-2021-10-20.png)
5. Drag and drop a Script node to the On Init flow and add the following code: Copy CodeJavaScript{
    page.firstFormGroup = page._formBuilder.group({
    firstCtrl: ['', Validators.required]
    });
    page.secondFormGroup = page._formBuilder.group({
    secondCtrl: ['', Validators.required]
    });
    }
6. Connect the nodes and save the page.
7. Navigate to the Page UI designer.
8. Drag and drop a **Stepper** component to the page canvas.
  1. In the custom properties section, select **Attribute** and enter **#stepper** in the attribute field.
  2. ![](/resources/Storage/components-guide-8/2021-10-20_10h42_51.png)
9. Drag and drop a Step component inside the stepper component and set the following:
  1. **Label**: Step 1
  2. **[stepControl]**: page.firstFormGroup
10. Drag and drop a Form component inside Step 1. Set the following properties for the form:
  1. In the custom properties section, select Key&Value and enter** [formGroup]** in the key field and **page.firstFormGroup** in the value field.
11. Drag and drop an **HTML 5** component inside the form and enter element type as **ng-template**. In the custom properties section, select **Attribute **and enter **matStepLabel** in the attribute field.
12. Double click the HTML Editor and enter Fill out your name
13. Drag and drop an Input component and set the following properties:
  1. Label: Name
14. Drag and drop a row below the input component.
15. Drag and drop a **Raised Button** inside the row and set the properties:
  1. **Button Name**: Next
  2. In the custom properties section, select **Attribute **and enter **matStepperNext **property name field.
16. Drag and drop a Step component inside the stepper component and set the following:
  1. **Label**: Step 2
  2. **[stepControl]**: page.secondFormGroup
17. Drag and drop a Form component inside Step 2. Set the following properties for the form:
  1. In the custom properties section, select Key&Value and enter** [formGroup]** in the key field and **page.secondFormGroup **in the value field.
18. Drag and drop an **HTML 5** component inside the form and enter element type as **ng-template**. In the custom properties section, select **Attribute **and enter **matStepLabel** in the attribute field.
  1. Double click the HTML Editor and enter Fill out your address
19. Drag and drop an Input component and set the following properties:
  1. Label: Address
20. Drag and drop a row below the input component.
21. Drag and drop a **Raised Button** inside the row and set the properties:
  1. Button Name: Back
  2. In the custom properties section, select **Attribute **and enter **matStepperPrevious **property name field.
22. Drag and drop another **Raised Button** inside the row and set the properties:
  1. **Button Name**: Next
  2. In the custom properties section, select **Attribute **and enter **matStepperNext **property name field.
23. Drag and drop another Step component inside the stepper component and set the following:
  1. **Step Label**: Step 3
  2. **Label**: Done
24. Drag and drop an **HTML 5** component inside the form and enter element type as **ng-template**. In the custom properties section, select **Attribute **and enter **matStepLabel** in the attribute field.
25. Double click the HTML Editor and enter Done
26. Drag and drop another **HTML 5** component inside the form and enter element type as **paragraph**.
27. Double click the HTML Editor and enter You are now done
28. Drag and drop a row component.
29. Drag and drop a **Raised Button** inside the row and set the properties:
  1. Button Name: Back
  2. In the custom properties section, select **Attribute **and enter **matStepperPrevious **property name field.
30. Drag and drop another **Raised Button** inside the row and set the properties:
  1. **Button Name**: Reset
  2. **(click)**: stepper.reset()
31. Save and run the page.
