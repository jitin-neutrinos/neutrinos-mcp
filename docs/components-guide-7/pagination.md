# Example

<https://documentation.neutrinos.com/articles/#!components-guide-7/pagination>

You use the Paginator component to provide navigation for paged information. It allows consecutive page numbering to indicate the proper order of the pages. Each paginator component displays:

- The number of items per page
- The total number of items being paged

### Example

![pagination](/resources/Storage/components-guide-7/pagination_33.png)

### How to use

1. In your application, click **Plugins** in the top left side of the screen and click **Manage Plugins**.
2. The Plugins Manager opens up. Navigate to the **App Plugins** tab. Click **Go to Store** and download **Pagination** from Neutrinos Store.
3. Once installed, the component should show up at the bottom of the palette list. Drag and drop the component to the page container.

1. In the TypeScript editor of the page where you dropped the **Pagination** component, add the following code:Copy CodeJavaScript// Import the MatPainator in the Pagination component and assign it to a public property
   import { MatTableDataSource, MatPaginator } from '@angular/material';

1. Save the page and run your application.

### Associated Attributes

- **Style**:  It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class**: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **Pagination label**: The display name for the pagination component.
- **[hidePageSize]**: Whether to hide the UI size of the page selection from the user.
- **[length]**: The length of the total number of items that are being paginated. By default, it is set to 0.
- **[pageIndex]**: The page index of the displayed list of items. By default, it is set to 0.
- **[pageSize]**: Number of items to display on a page. By default, it set to 50.
- **[pageSizeOptions]**: The set of provided page size options to display to the user.
- **[showFirstLastButton]**: Whether to show the UI of the first or last buttons to the user.
- **(page)**: Event emitted when the page size or page index of the paginator is changed. This is used to update any associated data view.
- **Disabled**: To check whether the component is disabled or not.
