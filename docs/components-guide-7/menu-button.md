# Menu Button

<https://documentation.neutrinos.com/articles/#!components-guide-7/menu-button>

## Menu Button

### Overview

A **Menu Button** is always associated with a **Menu** component that contains a list of **Menu Items**. When a **Menu Button** is clicked, the associated menu will be shown.

### Usage

The **Menu Button** component is used to provide an interface for the user to trigger a menu list. The menu appears where the **Menu Button ** exists.

### How to use

After creating a Menu,

1. Drag and drop the **Menu Button** component to the desired position and set the MenuName attribute.
2. Set the [matMenuTriggerFor] attribute to the same value as the matMenu attribute of the **Menu** component.
3. Save the changes.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **MenuName:** It is the name of the menu button that appears in the application. Takes string as its value. (Example, **Menu**).
- **Color:** It takes the color based on the angular material theme. Takes primary, accent or warn as its value.
- **[matMenuTriggerFor]: **It should have the same value as the matMenu attribute of the associated **Menu** component. Takes string as its value.

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
