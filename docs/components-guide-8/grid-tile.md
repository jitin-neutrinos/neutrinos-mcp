# Grid Tile

<https://documentation.neutrinos.com/articles/#!components-guide-8/grid-tile>

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

1. On the UI editor of the page, drag and drop the **Grid List** component to a page.
2. In the Grid List component, set the following properties:
  1. **cols**: 2
  2. **rowHeight**: 2:1
3. Drag and drop a Grid Tile inside the Grid List component. Set the following properties for the Grid Tile:
  1. **Grid Tile Label**: {{season}}
  2. **Style**: background-color: #CEE5D0;
  3. ***ngFor**: let season of page.gridseason; let i = index;
  4. **label**: {{season}}
4. Navigate to the **Page Flow Designer**.
5. Add the following page variable to the **Page Variables** node in the [On Init flow](/smart/project-page-services-designer-guide/on-init-flow):
  1. Page Variable: gridseason
  2. Default Value: Select **as is** and enter ['Winter', 'Spring', 'Summer', 'Autumn']
6. Save and Run the page.
