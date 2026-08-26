# Form

<https://documentation.neutrinos.com/articles/#!components-guide-8/form>

## Form

### Overview

The** Form** component is a container that contains several components such as Input, Radio button, etc. Users interact with these components and can change their value.

### Usage

A **Form **component can be used whenever there is a requirement for the data-entry tasks. It is basically a block in which another component can be inserted.

### How to use

1. Drag and drop a **Form** component.
2. Set the style and class attributes.
3. Drag and drop other components such as Input, Buttons, etc. inside the Form.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **action:** Action performed when the form is submitted.
- **method:** A method that is used to inform a browser how to send the data to the webserver. For example, post, get.
- **target:** A keyword that indicates where to display the response after submitting the form.
- **(onsubmit): **Event emitted when the form is submitted.
- **(onreset):** Event emitted when the form is reset.

### Example

Display a login page

1. Drag and drop a **Form** component.

2. Drag and drop a **Paragraph **component inside and set the **text** as **Username**.

4. Drag and drop an **Input** component.

5. Drag and drop another **Paragraph **component below the Input component and set the **text **as a **password**.

6. Drag and drop an **Input **component to enter the password.

7. Drag and drop a **Button **component below the **Input **component and name the Button as **Submit** and set the **onClick** attribute to submit.

8. Save and run the page.

A login page is created in which a user can give his username and password and he can submit.
