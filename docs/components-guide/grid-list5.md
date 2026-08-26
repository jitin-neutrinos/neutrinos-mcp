# Grid List

<https://documentation.neutrinos.com/articles/#!components-guide/grid-list5>

## Grid List

OverviewThis is a component that allows us to create a container of a list of particular rows and columns. The column will contain the attribute and the row will contain the data of the particular attribute. And the list will be generated. It must specify a cols attribute which sets the number of columns in the grid. The number of rows will be automatically determined based on the number of columns and the number of items.**Usage**It is a container of a list that has a user-defined layout. So the layout will be set by the user, and according to that layout, the list item will be placed inside that layout.How to useDrag and drop a **Grid List **component. Set the attributes such as **style, class, cols, gutterSize, rowHeight **how it should be displayed. According to that, the list item will be displayed on the screen.Example**Display a grid list component with a grid-tile component and under that 3 items.**
1. Drag and drop a grid list component, and fill the attribute (such as cols=4) so four columns will be there, row height will be the height of the row (such as rowHeight=100px). 2. Drag and drop a grid tile component inside a grid list. It contains attributes such as **colspan**, **rowspan**, **ngfor**, and** label**. **colspan:** Allows a single table cell to span the width of more than one cell or column. So, in this case, give **colspan=1**. **rowspan:** Allows a single table cell to span the height of more than one cell or row. Give **rowspan=1**. **Label:** This attribute contains the data of the cell that will be stored inside the row.Which will be displayed as a list item. **ngFor:** This attribute is used to iterate through the list item which is stored in the object. It will iterate through each item and display that data.Copy CodeHTMLDisplaylist.html file
<mat-grid-list cols="2" rowHeight="100px">
 <mat-grid-tile
 *ngFor="let tile of tiles" // in *ngFor attribute
 {{tile.text}} // label attribute
</mat-grid-tile>
 </mat-grid-list>Copy CodeHTMLDisplaylist.ts
tiles: Tile[] = [
{text: 'One'},
{text: 'Two'},
{text: 'Three'},
{text: 'Four'},
];
  3. So in the above example grid has two columns, and tile is an array which has four items that contain string value that basically labels.  So using **ngFor** the labels will be displayed. 4. Save and Run. 5. A table with four items will be displayed inside a grid-list.
**Associated Attributes****Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**Cols:** this property is used to specify the number of columns in the list. It accepts integer value. This section is mandatory.once we provide the column value the structure Of the list will be created, and we just give the details and that filled as a row.**gutterSize:** The gutter size can be set to any px, em, or rem value with the gutterSize property. If no units are specified, px units are assumed. By default the gutter size is 1px.**row-Height:** The height of the rows in a grid list can be set via the row-Height attribute. Row height for the list can be calculated in three ways:**Fixed height:** The height can be in px, em, or rem. If no units are specified, px units are assumed (e.g. 100px, 5em, 250).**Ratio:** This ratio is column-width:row-height, and must be passed in with a colon, not a decimal (e.g. 4:3).**Fit:** Setting row-Height to fit This mode automatically divides the available height by the number of rows. Please note the height of the grid-list or its container must be set.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
