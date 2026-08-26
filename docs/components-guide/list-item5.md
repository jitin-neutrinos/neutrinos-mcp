# List Item

<https://documentation.neutrinos.com/articles/#!components-guide/list-item5>

## List Item

OverviewList-item component contains individual data of items that will be placed inside the list-component. The data can be stored in an array or object and it will be accessed from the array by ngFor attribute.**Usage**List item is used to store the items or data of a list. The data can be a string, number, images etc.How to useDrag and drop a list-items inside a list component.Set the attribute such as style and class, ngFor and label.Example**Display a list of three items**
1. Drag and drop a list-component and set attributes such as style and class. 2. Drag and drop a list-item component inside the list-component. And for the list-item set the attribute such as style, class, *ngFor, *and* label.* 3*. *ngFor is used to iterate through the object and access the items of the objects, if the folders is an object which has attribute as name(name of folder) which is a string, this object must be defined in a .ts file and can be accessed by assigning ngFor as (let folder of folders). 4. Label attribute displays the name as list items, provide the name as (folder .name), this will access the folders object and get the name value. So if the folders object contains three values such as photos, work, and document, then the list will be generated which contains the list items as photos, work, and document. 5. Save and run. 6. A list of three items will be displayed.**Associated Attributes****Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**ngFor:** ngFor is used to iterate through the array object and get the data. The syntax of ngFor is **ngFor="let d of data"** where d is a loop variable and data is a array or object from which the data will be accessed. **Label:** In label attribute provide the name that should be displayed as a items name so the data is accessed by the object then give the value as (folder. name).
**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
