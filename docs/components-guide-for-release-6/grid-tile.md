# Grid Tile

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/grid-tile>

## Grid Tile

### Overview

This component allows you to create a container of the list of particular rows and columns. The column will contain the attribute and the row will contain the data of the particular attribute. The data of the list can be iterated by a ngFor loop.

### Usage

The** Grid Tile** component can be used where the list of items should be displayed. It can be used alone as well as inside the **Grid List **component.

### How to use

1. Drag and drop a ** Grid Tile** component.
2. Set the attributes such as **style,class,*ngFor**,**[rowspan]**,**[colspan****]**, and **label**.
3. According to the attributes set, the grid list items will be displayed.

### Associated Attributes

- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **ngFor:** ngFor is used to iterate through the array object and get the data. The syntax of **ngFor** is *ngFor="let d of data" where d is a loop variable and data is an array or object from which the data will be accessed.
- **rowspan: **This attribute allows a single table cell to span the height of more than one cell or row. So in a normal row, the **rowspan** is always 1, so this attribute is required when there is a requirement to change the row size, like some times a row requires two times the size of the normal row, in that case, the rowspan=2.
- **colspan:** This attribute allows a single table cell to span the height of more than one cell or column. So in a normal column, the **colspan** is always 1, so this attribute is required when there is a requirement to change the column size, like some times a row requires two times the size of the normal column, in that case, the colspan=2.

### Example

Display a **Grid Tile** component inside the **Grid List **component with three items.

1. Drag and drop a **Grid List** component and enter values for the following attributes:

- **cols** = 4
- **rowHeight **= 100px).

2. Drag and drop a **Grid Tile** component and set the following attributes:

- **colspan** = 1.
- **rowspan **= 1.
- **Label** = {{tile.text}}
- ***ngFor** = "let tile of tiles"

3. In the TS editor of the page, enter the following code:

```javascript
Displaylist.tstiles: Tile[] = [{text: 'One'},{text: 'Two'},{text: 'Three'},{text: 'Four'},];
```

4. In the above example, the grid has two columns, and tile is an array that has four items that contain string values that are basically labels. So, using **ngFor** the labels will be displayed.

5. Save and Run the page.

6. A table with four items will be displayed inside a grid list.
