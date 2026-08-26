# List

<https://documentation.neutrinos.com/articles/#!components-guide-8/list>

## List

### Overview

The** List** component is a container component that wraps and formats a series of [List Item](/articles/components-guide-8/list-item) components. It contains **List Item** components in the form of line items.

You can create a simple list of textual items, or a more complex one, containing an array of different layout elements.

### How to use

1. Drag and drop a **List **component.
2. Set the attribute such as style and class.
3. Insert **List Item** components inside the **List** component.

### Associated Attributes

- **List label: **The display name for the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- **Style: **It accepts a string value and affects different properties (height, width, color, etc.) of the component based on the values provided as inline styling. For example-(background:orange;height:200px;).
- **Class: **It accepts space-separated class names that are defined in the Styles editor. For example, if the following CSS classes are defined in the Styles editor, then you can select them here to apply to this component. Copy CodeHTML.class1
   {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }
   .class2
   {
   border-radius:10px;
   flex-basis:10%;
   height:100px;
   }

### Examples

**Example 1: ****A simple list using multiple list item components**

1. Drag and drop a** List** component to the canvas.
2. Drag and drop four **List Item** components inside the **List **component.
3. Update the labels of each list item to Boots, Clogs, and Loafers, Sneakers respectively.
4. Save and preview the app.

**Example 2: ****A simple list using Array**

****![Simple list example](/resources/Storage/components-guide-8/project-component-docs-test/simple_list.png)**


 **

1. Drag and drop a** List** component to the canvas.
2. Drag and drop a **List Item** component inside the **List **component.
3. Switch to the [Flow Designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page and design the following [page flow](/smart/project-sample-how-to-guide/design-page-flows) by dragging and dropping the following nodes:
    ![list flow](/resources/Storage/components-guide-8/list_flow.png)
4. Open the **Page Variables **node and add the following page variable:
    ![creating the device variable](/resources/Storage/components-guide-8/devices_var.png)
5. Open the **Script **node and define the **devices** array: Copy CodeHTMLpage.devices = [
    {
    name : "Desktop",
    imgsrc: "https://png.pngtree.com/png-vector/20190214/ourlarge/pngtree-vector-laptop-icon-png-image_509609.jpg"
    },
    {
    name : "Mobile",
    imgsrc: "https://icons-for-free.com/iconfiles/png/512/phone+mobile+mobile+phone+phone+icon-1320184367369922557.png"
    }
   ]
6. Switch to the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page. Open the properties window of **List Item** and enter the following values to access the items of the array:
  - *ngFor: let device of page.devices
7. Drag and drop a **Row** inside the **List Item**.
8. Drag and drop an **HTML5 **component inside the **Row** and set the following properties:
  1. Element type: Div
  2. Open the **HTML Editor** within the HTML5 component and add {{device.name}} in it.
9. Drag and drop an **Image** component inside the **Row** and set the following properties:
  1. style: width: 20px; height:20px;
  2. alt: devices icon
  3. [src]: device.imgsrc
10. Save and run the page.

### 

**Example 3: A single list with 2 sections (folders and notes)**

![List with different sections](/resources/Storage/components-guide-8/project-component-docs-test/list_ex_2.png)

1. Drag and drop a** List** component to the canvas.
2. Drag and drop an **HTML5 **component. Select the **Element type** as **Header 3**.
3. Double-click the **HTML Editor**, and enter **Folders**.
    ![Html - header 3](/resources/Storage/components-guide-8/project-component-docs-test/html_h3.png)
4. Drag and drop a** List Item** inside the List. Configure the following properties:
  - List item label = List Item 1
  - Style = height:100px;padding-left:20px;
  - *ngFor = let folder of folders
5. Switch to the [Flow Designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page and design the following [page flow](/smart/project-sample-how-to-guide/design-page-flows) by dragging and dropping the following nodes:
    ![list flow](/resources/Storage/components-guide-8/list_flow.png)
6. Open the **Page Variables **node and add the following page variables:
    ![creating the list variables](/resources/Storage/components-guide-8/list_var.png)
7. Open the **Script **node and define the following arrays: Copy CodeHTMLpage.folders = [
    {
    name: 'Photos',
    updated: new Date('1/1/16'),
    },
    {
    name: 'Recipes',
    updated: new Date('1/17/16'),
    },
    {
    name: 'Work',
    updated: new Date('1/28/16'),
    }
   ];
   page.notes = [
    {
    name: 'Vacation Itinerary',
    updated: new Date('2/20/16'),
    },
    {
    name: 'Kitchen Remodel',
    updated: new Date('1/18/16'),
    }
   ];
8. Switch to the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page.
9. Drag and drop an** Image** component inside **List Item 1**. Configure the following attributes:
  - style = height:50px;widht:50px;
  - [src] = 'https://www.netclipart.com/pp/m/318-3186747_black-folder-icon-icons-png-grey-folder-clipart.png'
  - alt = folder icon
10. Drag and drop a **Column** below the image. Set padding:20px; in the Style attribute.
11. Inside the column, drag and drop a **HTML5** component. Select the Element type as Label. Select HTML editor and enter {{folder.name}} as the code.
12. Inside the column, drag and drop another **HTML5** component. Select the Element type as Label. Select HTML editor and enter {{folder.updated | date}} as the code.
13. At the end of this step, your list item should look like the following image. This list item will list all the folders that you defined in the** Script** node of the page flow.
    ![List Item 1](/resources/Storage/components-guide-8/project-component-docs-test/list%20item%201.png)
14. Next, add another list item to list all the notes. Drag and drop an **HTML5** component. Select the **Element type** as **Div**.
15. Double-click the HTML editor, and enter <hr><h3>Notes</h3>.
16. Drag and drop a** List Item** inside the List. Configure the following properties:
  - List item label = List Item 2
  - Style = height:50px;width:20px;
  - *ngFor = let note of notes
17. Drag and drop an** Image** component inside **List Item 2**. Configure the following attributes:
  - style = height:80px;
  - [src] = 'https://www.shareicon.net/data/128x128/2015/08/19/87755_document_512x512.png'
  - alt = Notes icon
18. Drag and drop a **Column** below the image. Set padding:20px; in the Style attribute.
19. Inside the column, drag and drop a **HTML5** component. Select the Element type as Label. Select HTML editor and enter {{note.name}} as the code.
20. Inside the column, drag and drop another **HTML5** component. Select the Element type as Label. Select HTML editor and enter {{note.updated | date}} as the code.
21. Save and run the page.
