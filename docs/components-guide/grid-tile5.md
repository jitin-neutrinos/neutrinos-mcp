# Grid Tile

<https://documentation.neutrinos.com/articles/#!components-guide/grid-tile5>

## Grid Tile

OverviewThis is a component that allows us to create a container of the list of particular rows and columns it can be used alone as well as inside the grid-list. The column will contain the attribute and the row will contain the data of the particular attribute. And the data of the list can be iterated by a ngFor loop that can access all the data from the array and can be displayed on the screen.**Usage**The grid-tile component can be used where the list of items should be displayed. It can be used as alone or it can be put inside a grid-list component to set the layout of the list.How to useDrag and drop a grid tile component.Set the attributes such as style,class,*ngFor,[rowspan],[colspan], and label.According to this to grid list items will be displayed.Example**Display a grid tile component inside the grid-list component with three items**
1. Drag and drop a grid list component. And fill the attribute (such as cols=4) so four columns will be there, the row height will be the height of the row (such as rowHeight=100px). 2. Drag and drop a grid tile component inside a grid list. It contains attribute such as-**colspan:** Allows a single table cell to span the width of more than one cell or column. So in this case give colspan=1.**rowspan:** Allows a single table cell to span the height of more than one cell or row. Give rowspan=1. **Label:** This attribute contains the data of the cell that will be stored inside the row.Which will be displayed as a list item. **ngFor:** This attribute is used to iterate through the list item which is stored in the grid-tile object. It will iterate through each item and display that data.Copy CodeHTMLDisplaylist.html file
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
 3. So in the above example grid has two columns, and tile is a array which has four items which contains string value that are basically labels. So using ngFor the labels will be displayed. 4. Save and Run. 5. Table with four items will be displayed inside a grid-list.
**Associated Attributes**
**Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background: orange; height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**ngFor:** ngFor is used to iterate through the array object and get the data. The syntax of ngFor is *ngFor="let d of data" where d is a loop variable and data is an array or object from which the data will be accessed. **rowspan:** This attribute allows a single table cell to span the height of more than one cell or row. So in a normal row, the rowspan is always 1, so this attribute is required when there is a requirement to change the row size, like some times a row requires two times the size of the normal row, in that case, the rowspan=2.**colspan-** This attribute allows a single table cell to span the height of more than one cell or column. So in a normal column, the colspan is always 1, so this attribute is required when there is a requirement to change the column size, like some times a row requires two times the size of the normal column, in that case, the colspan=2.**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
