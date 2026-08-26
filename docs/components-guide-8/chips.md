# Chips

<https://documentation.neutrinos.com/articles/#!components-guide-8/chips>

## Chips

### Overview

Chips is a component that provides small blocks of text information. **Chips **contain a sub-component called** Chip**. This sub-component can be inserted within the Chips by clicking the **Add Chip **button provided at the bottom of the Chips component. Therefore, you can call Chips as an advanced component that groups all the sub-components and displays it as a single block.

**Example**:

![Chip component on deployment](/resources/Storage/components-guide-8/chip.png)

| ![Information](/resources/Storage/components-guide-8/info.png) | This component is available from Neutrinos Studio release 7.1.0. |
| --- | --- |

### How to Use

- Drag and drop a **Chips** component to a page container.
- Add the **Chips** sub-component by clicking the **Add Chip** button. (optional)
- Double-Click the respective component and set its properties/behavior using the Attributes window.

### Associated Attributes

### Chips

**Basic Properties**

- **Chips Label: **The display name of the **Chips** component.
- style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}

- **Selectable (True/False)**: Whether the Chips component is selectable or not. When the chips component is not selectable, the selected states for all the chip inside the chips are always ignored. The default value is **true**.
- **Multiple (True/False)**: If set to **true**, the user is allowed to select multiple Chips. The default value is **true**.

**Advanced Properties of Chips component:**

- **(change): **Event emitted when the value of the selected Chips is changed.
- **[compareWith]: **A function to compare the option values with the selected values. The first argument is a value from an option. The second is a value from the selection. A boolean value should be returned.

### Chip

- style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}

- **ChipName**: The display name of the Chip.
- **Color**: The theme color palette for the component. Select the color theme from the drop-down list. It can be Primary, Accent, Warn or None. By default, it is None.
- ***ngFor**: ngFor is used to iterate through the array object and get the data. The syntax of ngFor is ngFor=let d of data where d is a loop variable and data is an array or object from which the data will be accessed.
- **Disable Ripple (True/False)**: To check whether the ripples are disabled.
- **Disabled **(True/False)****: To check whether the component is disabled or not.
- **Removable **(True/False)****: To check whether the Chip displays the remove styling and emits events.
- **Selectable **(True/False)****: Whether or not the Chip is selectable. When a Chip is not selectable, changes to its selected state are always ignored. By default a Chip is selectable, and it becomes non-selectable if its parent Chips is not selectable.
- **Selected **(True/False):** ** To check whether the Chip is selected or not.
- **[value]**: The value of the Chip.
- **(destroyed)**: Event emitted when the Chip is destroyed.
- **(removed)**: Event emitted when a Chip is to be removed.
- **(selectionchange)**: Event emitted when the Chip is selected or deselected.

**Advanced Properties of Chips component:**

- **show Icon Before Labe**l **(Boolean)**: Whether to show the icon that is before the label of the Chip or not.
- **IconBeforeLabel**: The icon that should appear before the label of the Chip. By default, the value is home.
- **IconBeforeLabelClass**: Specify the class name where the icon for the IconBeforeLabel is defined.
- **IconBeforeLabelStyle**: The style for the Icon that s displayed before the label. Default style is margin-right: 7px; margin-left: -2px ; . You can further customize the style.
- **showIconAfterLabel (Boolean)**: Whether to show the icon that is after the label of the Chip or not.
- **IconAfterLabel**: The icon that should appear after the label of the Chip. By default, the value is home.
- **IconAfterLabelClass**: Specify the class name where the icon for the IconAfterLabel is defined.
- **IconAfterLabelStyle**: The style for the Icon that displayed after the label.

### Example

Display Chips with multiple Chip and some advanced properties.

1. Drag and drop a **Chips **component to the page container. Add three Chip components inside **Chips** by clicking the **Add Chip** button.
2. Double click the Chips component and enter the following properties:
  - Chips label= Fruits list
  - style= background:orange;height:200px;
3. Now, double click the **Chip 1 **component. Enter the following properties:
  - ChipName= Grape
  - Color= primary
  - Disable ripple= true
  - Selected= selected
4. Double click the **Chip 2** component and enter the following properties:
  - ChipName= Orange
  - Color= primary
  - Disable ripple= true
  - Selected= selected
5. Double click the **Chip 3** component and enter the following properties:
  - ChipName= Watermelon
  - Color= warn
  - Selected= selected
6. Save and run the page. The Chips will be displayed like this on display:

![output rendered](/resources/Storage/components-guide-8/Chipsoutput.png)
