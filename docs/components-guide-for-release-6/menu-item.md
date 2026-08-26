# Menu Item

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/menu-item>

## Menu Item

### Overview

**Menu** component provides a list of options from which you can select an option to perform a specific operation. A **Menu Item** is an individual option that can be selected. It is always contained in the **Menu** component.

### Usage

**Menu Items **are what make up a menu. Menu items are used to provide options within a menu.

### How to use

1. Drag and drop the **Menu** component from the **Navigation** section.
2. Set the matMenu attribute to a string value.
3. Drag and drop the Menu Item component(s) inside the Menu component.
4. Set the MenuItemName of **Menu Item** component to a string value.
5. Drag and drop the **Menu** Button component to the desired position and set MenuName attribute.
6. Set the [matMenuTriggerFor] attribute to the same value as the matMenu of the **Menu** component.
7. Save the changes.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **MenuItemName:** It is the name of the menu item that appears in the application. Takes string as its value. Example- **item1**.
- **Disabled:** Used to disable the menu item.

### Example

1. Drag and drop the **Menu** component.
2. Set the matMenu attribute to **menu**.
3. Drag and drop 3 **Menu Item **components inside the **Menu** component.
4. Set the MenuItemName attribute of the first Menu Item component to item1.
5. Set the MenuItemName attribute of the second Menu Item component to item2.
6. Set the MenuItemName attribute of the third Menu Item component to item3.
7. Drag and drop the **Menu** Button component to the desired position and set MenuName attribute to **Menu** and [matMenuTriggerFor] attribute to **menu**.
8. Save the changes.
9. Now, when the **Menu** button is clicked, it will reveal the list of menu items (item1, item2, item3).
