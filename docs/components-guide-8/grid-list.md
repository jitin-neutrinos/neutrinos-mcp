# Grid List

<https://documentation.neutrinos.com/articles/#!components-guide-8/grid-list>

## Grid List

### Overview

This is a component that allows us to create a container of a list of particular rows and columns. The column will contain the attribute and the row will contain the data of the particular attribute. And the list will be generated. It must specify a **cols** attribute which sets the number of columns in the grid. The number of rows will be automatically determined based on the number of columns and the number of items.

### Usage

It is a container of a list that has a user-defined layout. So the layout will be set by the user, and according to that layout, the list item will be placed inside that layout.

### How to use

1. Drag and drop a **Grid List** component.
2. Set the attributes such as style, class, cols, gutterSize, and rowHeight to determine how it should be displayed.
3. According to that, the list item will be displayed on the screen.

### Associated Attributes

- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

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

- **Cols: **this property is used to specify the number of columns in the list. It accepts integer value. This section is mandatory. Once we provide the column value the structure of the list will be created, and we just give the details and that filled as a row.
- **gutterSize:** Gutter size is the empty space between the element's boundary and the element's content. The gutter size can be set to any **px**, **em**, or **rem** value with the gutterSize property. If no units are specified, **px** units are assumed. By default the gutter size is** 1px**.
- **row-Height: **The height of the rows in a grid list can be set via the row-Height attribute. Row height for the list can be calculated in three ways:
  - **Fixed height: **The height can be in** px, em,** or **rem**. If no units are specified, **px** units are assumed (e.g. 100px, 5em, or 250).
  - **Ratio:** This ratio is column-width:row-height, and must be passed in with a colon, not a decimal (e.g. 4:3).
  - **Fit: **Setting row-Height to fit This mode automatically divides the available height by the number of rows. Please note the height of the grid-list or its container must be set.

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
