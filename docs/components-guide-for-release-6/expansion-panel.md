# Expansion Panel

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/expansion-panel>

## Expansion Panel

### Overview

**Expansion Panel** is a container that contains components such as **Expansion header**, **Expansion title**,** Expansion description**, etc. **Expansion panel** can be used alone with all these component or it can be put inside an **Expansion panel outlet **component.

### Usage

The **Expansion panel **component can be used where the data to be displayed in an expanded view and will be shown and hidden based on the onclick() event. Only the title and description will be shown and other components will be hidden and they will be displayed when the user clicks on it.

### How to use

1. Drag and drop an **Expansion panel** component.
2. Fill the attributes such as style, class, ngFor, opened, closed, and expanded.
3. Drag and drop various Expansion components that can be placed inside this.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **ngFor: **It is used when there are multiple expanded panel components. So, in that case, ngFor is used to iterate through an array or object of the expanded panel to display them. And the object or area will be defined in the **.ts **file.
- **opened: **This attribute contains an event that should be emitted every time the Accordion Item is opened, so a method or function will be defined and it will be called. Inside the function, the actions will be defined that what should happen when the item is open.
- **closed:** This attribute contains an event that should be emitted every time the Accordion Item is closed, so a method or function will be defined and it will be called. Inside the function, the actions will be defined that what should happen when the item is closed.
- **HideToggle: **It accepts Boolean values as true or false, this attribute is used to check whether the Expansion indicator should be hidden.
- **[expanded]:** It accepts any type of values, to check whether the Accordion Item is expanded.
- **(afterCollapse):** Event emitted when the Expansion panel collapsed.
- **(afterExpand):** Event emitted when the Expansion panel expands.
- **Disabled: **This component can be disabled by using the disabled attribute. A disabled Expansion panel can't be toggled by the user, but can still be manipulated programmatically.
- **(destroyed): **Event emitted when the Expansion panel is destroyed.
- **id: **Is the unique ID for the Expansion Panel.

### Example

1. Drag and drop an **Expansion panel outlet **component, and inside that drag and drop an **Expansion panel** component.
2. Inside the **Expansion panel** component, drag and drop an **Expansion Title **component. In the attributes window of the **Expansion Title **component, enter **title **= {{title.name}}.
3. In the attributes window of the **Expansion Panel **component, enter the following values:
  - **Label** = Experiments
  - ***ngFor** = let title of titles
  - **Style** = background: Coral;
4. In the TS editor of the page, add the following code: Copy CodeCSStitles= [{name: "Experiment 1"}, {name: "Experiment 2"}];
5. Save and run the page.
