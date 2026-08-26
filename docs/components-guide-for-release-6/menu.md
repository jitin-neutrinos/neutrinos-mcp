# Menu

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/menu>

## Menu

### Overview

A **menu **component is a set of options presented to the user of a computer application to help the user find information or execute a function.

### Usage

The **menu** component is used when the user is to be provided with the ability to select from a list of options without consuming the GUI layout.

### How to use

1. Drag and drop the **Menu **component from the **Navigation **section.
2. Set the matMenu attribute to a string value.
3. Drag and drop the** Menu Item** component(s) inside the **Menu** component.
4. Set the MenuItemName of** Menu Item **component to a string value.
5. Drag and drop the **Menu Button** component to the desired position and set MenuName attribute to **menu**.
6. Set the [matMenuTriggerFor] attribute to the same value as the matMenu of the **Menu** component.
7. Save the changes.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **xPosition: **Specifies the horizontal position of the menu list. Values can be: before or after.
- **yPosition:** Specifies the vertical position of the menu list. Values can be: above or below.
- **templateRef: **Creates a template reference variable. Takes string as its value.
- **items:** DEPRECATED.
- **matMenu: **Takes string as its value. The value should be the same as [matMenuTriggerFor] attribute’s value of the Menu component.
- **Has Back Drop: **This is to specify whether the menu has a backdrop.
- **Overlap Trigger: **Specify whether the menu should overlap its trigger or not.
- **(closed):** Event emitted when the menu is closed.
- **direction: **Specifies the layout direction of the menu.
- **parentMenu: **This is used to describe the parent menu of the menu panel.

### Example

1. Drag and drop a **Menu** component.
2. Set the matMenu attribute to **menu**.
3. Drag and drop** 3 Menu Item** components inside the Menu component.
4. Set the MenuItemName attribute of the first **Menu Item **component to **item1**.
5. Set the **MenuItemName** attribute of the second Menu Item component to** item2**.
6. Set the **MenuItemName** attribute of the third** Menu Item** component to **item3**.
7. Drag and drop the **Menu Button** component to the desired position and set MenuName attribute to **Menu** and [matMenuTriggerFor] attribute to **menu**.
8. Save the changes.
9. Now, when the **Menu** button is clicked, it will reveal the list of menu items (item1, item2, item3).

### Support

- **Devices**: Android, iOS
- **Browsers**: Latest version of all modern browsers
- **Dependencies version**:
  - Angular CLI version: 6.0.0 +
  - Cordova version: 7.1.0 +
