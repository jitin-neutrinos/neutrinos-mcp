# Sidenav Container

<https://documentation.neutrinos.com/articles/#!components-guide-8/sidenav-container>

## Sidenav Container

### Overview

The **Sidenav Container **is the container component for the **Sidenav** component. **Sidenav **component has meaning only when it is placed inside the **Sidenav Container** component. Everything that is not contained within the **Sidenav **component and contained within** Sidenav Container **component will appear as the main content that is outside the **sidenav **bar.

### Usage

**Sidenav container **is used whenever a **sidenav** is required. **Sidenav **cannot exist outside **sidenav container **component.

### How to use

1. Drag and drop a **Sidenav Container** component from the Navigation section.
2. Drag and drop one or more Sidenav components within the **Sidenav Container** component.
3. Save and run the page.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Auto size: **Specify whether to automatically resize the container whenever the size of any of its drawers changes.
- **Has Back Drop: **This is to specify whether the drawer container should have a backdrop while one of the sidenavs is open. If explicitly set to true, the backdrop will be enabled for drawers in the side mode as well.
- **(backdropClick): **Event emitted when the drawer backdrop is clicked.

### Example

1. Drag and drop a **Sidenav Container **component.
2. Drag and drop a **Sidenav **component inside the **Sidenav Container**.
3. Set **Has Back Drop** = true and** (backdropclick)**= onBackdrop() and write the following in the TS editor

```javascript
onBackdrop(){  alert("Event Occured")    }
```

1. Populate the Sidenav component with 3 buttons and provide button names.
2. Save and run the page.
