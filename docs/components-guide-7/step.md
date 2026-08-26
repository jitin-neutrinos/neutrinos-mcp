# Step

<https://documentation.neutrinos.com/articles/#!components-guide-7/step>

## Step

### Overview

The **Step** component is used inside a** Stepper** component to divide content into logical steps within a page. The **Step** component can contain other components such as a Textbox, Button, Radio button, Checkbox, Images, etc.

### Usage

The **Step **component can be used to create a page that is divided into various steps, it can be displayed horizontally or vertically.

### How to use

1. Drag and drop a **S****tepper** component.
2. Fill the required properties.
3. Drag and drop a **Step** component.
4. Fill the required properties.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Label: **Label is the name given to a step and each step will have different labels and accepts text values.
- **completed: **Accepts Boolean values as true or false depending on whether the step is marked as completed.
- **editable:** Accepts Boolean value as true or false to make it whether the user can return to this step once it has been marked as completed.
- **interacted: **Used to check whether the user has seen the expanded step content or not. it accepts boolean values and the default value is false.
- **optional: **Accepts Boolean values as true or false, which makes a given step optional.
- **[stepControl]: **Checks the validity of the step.
- **State: **Specifies the state of the step.
- **Has Error:** Checks whether the step has an error.
- **errorMessage:** Used to specify the message that has to be displayed when the step has an error.

### Example

Create a stepper with the login process.

1. Drag and drop a **Stepper** component. Set the **matHorizontalStepper** attribute value to **matHorizontalStepper **to make it horizontal.

2. To create 3 steps, drag and drop three **Step** components inside the **Stepper **component, and give the label as **getUsername**, **getPassword**, and **submit**.

3. Click the **Stepper** component and set the following attributes:

- type = horizontal
- selected = getUsername
- set the index as 0 so that the **getUsername** step will come first.

4. In the **getUsername** step, drag and drop an **Input **component to accept username from the user.

5. Drag and drop an **Input **component inside the **getPassword** step to accept the password.

6. Drag and drop a **Button** component inside the **submit** step. Set the name of the button as Login.

5. Save and run the page.

6. A stepper with getUsername, getPassword and submit button will be displayed.
