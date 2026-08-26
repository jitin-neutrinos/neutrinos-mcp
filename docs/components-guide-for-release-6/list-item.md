# List Item

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/list-item>

## List Item

### Overview

The** List Item** component contains individual data of items that will be placed inside the **List** component. The data can be stored in an array or object and it will be accessed from the array by ngFor attribute.

### Usage

**List Item** is used to store the items or data of a list. The data can be a string, number, images, etc.

### How to use

1. Drag and drop a **List Item** component inside a **List** component.
2. Set the attribute such as style and class, ngFor and label.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

- **ngFor:** ngFor is used to iterate through the array object and get the data. The syntax of ngFor is ngFor=let d of data where d is a loop variable and data is an array or object from which the data will be accessed.
- **Label:** This attribute displays the name as list items. Provide the extension as (.name). This will access the folder's object and get the name value. If the folders object contains three values such as photos, work, and document, then the list items will be photos, work, and document.

### Example

Display a list of three items.

1. Drag and drop a **List **component and set attributes such as style and class.

2. Drag and drop a **List Item** component inside the **List **component. Set the attribute such as style, class, ngFor, and label for the** List Item** component.

3. ngFor is used to iterate through the object and access the items of the objects. If the folder is an object which has its attribute as name(name of the folder) which is a string, this object must be defined in a .ts file and can be accessed by assigning ngFor as (let folder of folders).

4. The Label attribute displays the name as list items, provide the name as (.name), this will access the folders object and get the name value. So if the folders object contains three values such as photos, work, and document, then the list will be generated which contains the list items as photos, work, and document.

5. Save and run the app.

6. A list of three items will be displayed.
