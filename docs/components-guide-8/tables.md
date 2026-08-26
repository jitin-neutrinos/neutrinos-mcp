# Table

<https://documentation.neutrinos.com/articles/#!components-guide-8/tables>

## Table

### Overview

The Table component provides a styled data table that can be used to display rows of data. The Table component focused on a single responsibility to efficiently render rows of data in a performant and accessible way.

The simplest way to provide data to the table is by passing a data array to the table's dataSource input. The table will take the array and render a row for each object in the data array. The data source is meant to serve a place to encapsulate any sorting, filtering, pagination, and data retrieval logic specific to the application. A data source is simply a base class that has two functions: connect and disconnect. The connect function will be called by the table to receive a stream that emits the data array that should be rendered. The table will call the disconnect when the table is destroyed.

### How to use:

1. Drag and drop a Table component into the page container.
2. Optionally add columns, drop columns, paginator, and filter components.
3. Double click the Table component to display the list of attributes that can be used with it.
4. Double click the column, drop a column, paginator, and filter components added within the table, and set its attributes.
5. Fill the attributes.
6. Save and run the page.

### Associated Attributes

**Basic Properties**: These properties remain the same for all Table components.

- **Table label: **Specify the display name of the table.
- **style**: Accepts a string value that affects different properties of the Card such as height, width, and color, based on the values provided. For example: background:orange:height:200px.

- **class**: Used to point to a class in a style sheet. Each class contains one or more style statements defined in the Style editor. The Class field accepts space-separated class names such as class1 class2, where each class is defined in the Style editor as shown below:

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **[datasource]**: Specify the data that needs to be rendered inside the table.
- **rowclick**: Action performed when particular table row is clicked.
- **show header**: Set this property to true to show the table header.

**Column**:

- **Header Label**: Specify the display name of the column.
- **Mapping**: Specify the data to be displayed in the column. For example: {{table.position}}
- **Sort:** Allows you to sort column data. Choose between True or False.
- **headerClass**: The class used to define the header of the table column.
- **columnClass**: The class used to define the column of the table.

**Droppable Column:**

- **Sort Key**: Key to sort/arrange the data. For example- ascending.
- **Sort**: Allows you to sort column data. Choose between True or False.
- **columnid**: Unique ID for the component.
- **Header Label**: Specify the display name of the Droppable Column.
- **headerClass**: The class used to define the header of the droppable column.
- **columnClass**: The class used to define the column of the table.

**Paginator:**

- **[length]**: Specify the length of the total number of items that are being paginated.
- **[page Size]**: Specify the number of items to display on a page.
- **[pageSizeOptions]**: Specify the set of provided page size options to display to the user. The page size options include 5, 10, 25, and 100.
- **(page)**: The event is emitted when the paginator changes the page size.

**Filter**:

- **(tableFilterFunction)**: The function used to perform the table filter.
- **placeholder**: Specify the name of the filter to be displayed on the screen.
- **Layout Direction**: The position to display the filter.
- **fxFlex**: Size of the filter component.

### Example

1. Open the Page UI Designer.
2. Drag and drop a **Table **component to the canvas.
3. Double click the table component and click the **Add Flows** icon.
4. The properties of the table component get auto-updated. Additionally, set the **style **of the table as width:70%; border: 1px solid black;
5. In the flow designer, the **setDataSource** is auto-generated.
6. Add a **Filter **to the table on the **UI Designer**. Double click the table filter component and click the **Add Flows** icon.
7. In the flow designer, the **onFilter **is auto-generated.
8. Add 4 columns to the parent table component.
9. Double click column 1 of the table on the UI Designer and set the following properties:
  1. Header Label: POSITION
  2. Sort: True
  3. Mapping: {{table.position}}
10. Double click column 2 of the table on the UI Designer and set the following properties:
  1. Header Label: Name
  2. Sort: True
  3. Mapping: {{table.name}}
11. Double click column 3 of the table on the UI Designer and set the following properties:
  1. Header Label: WEIGHT
  2. Sort: True
  3. Mapping: {{table.weight}}
12. Double click column 4 of the table on the UI Designer and set the following properties:
  1. Header Label: SYMBOL
  2. Sort: True
  3. Mapping: {{table.symbol}}
13. Add a **Paginator **to the table on the **UI Designer**.
14. Navigate to the flow designer, update the On Init flow.
15. Drag and drop a **Call Service** node to the on init flow and set the following properties:
  1. **Select a page flow**: setDataSource_1
16. Create an **After View Init** flow, drag and drop an **After View Init **node and name it** After View Init**.
17. Drag and drop a View Picker node and set the following properties:
18. Drag and drop a Page Variables node and set the following properties:
19. Save and run the page.
