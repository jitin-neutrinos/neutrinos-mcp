# List

<https://documentation.neutrinos.com/articles/#!components-guide-7/list>

## List

### Overview

A list component contains **List Item** components in the form of line items.

### Usage

List component contains a number of** List Item** components, there is no requirement to set the number of columns. It is an unordered list, and the list items will come one below the other.

### How to use

1. Drag and drop a **List **component.
2. Set the attribute such as style and class.
3. Insert **List Item** components inside the **List** component.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style **side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {

border-radius:10px;

flex-basis:10%;

height:100px;

}

.class2 {

border-radius:10px;

flex-basis:10%;

height:100px;

}
```

### Example

Display a list of three items:

1. Drag and drop a **List** component and set the attribute such as style and class.
2. Drag and drop a List Item component inside the **List** component, set the attributes for **L****ist Item** such as style, class, ngFor, and label.
3. ngFor is used to iterate through the object and access the items of the objects, if folders is an object which has an attribute as name (name of the folder) as a string type, with three items in the folder object, set the field in ngFor as let folder of folders.
4. The **Label** attribute displays the name as list items. Provide the extension as (**.name**). This will access the folder's object and get the name value. If the folder object contains three values such as photos, work, and document, then the list items will be photos, work, and documents.
5. Save and run the app. A list of three items will be displayed.
