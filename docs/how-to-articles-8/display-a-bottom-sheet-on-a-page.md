# Add the Angular Library to the App

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/display-a-bottom-sheet-on-a-page>

**Bottom Sheet **is a component that slides up from the bottom of the screen to showcase additional content in your application. As the Bottom Sheet component is not readily available for use on Neutrinos Studio, to display a bottom sheet in your application, you should import and use the [Angular Bottom Sheet](https://material.angular.io/components/bottom-sheet/overview) component.

Let's consider an example. On click of an **Open Image** button, you want to display a few options to the user to perform some action:

To display a bottom sheet similar to the example above, perform the following steps:

### Add the Angular Library to the App

As the** Bottom Sheet **component is not available by default on Neutrinos Studio, import the bottom-sheet Angular library to the app.

1. On the top menu of your application page, select **Plugins > Manage Plugins** to open the plugins manager. This editor allows you to import, remove or update a component that you want to use in your application.
2. In the **Add Dependency** section, perform the following:
  1. Enter the following details:
    - Name: @angular/material.
    - Version: 10.2.7
    - Type of dependency: **Angular**
    - Library: @angular/material/bottom-sheet
        .This library is used to open Material Design panels to the bottom of the screen.
  2. Click the **+** icon next to Library to add the library to the dependency list.
      ![bottom sheet dependency](/resources/Storage/how-to-articles-8/add_dep1.png)
  3. Expand the library and enter the module name as MatBottomSheetModule. Click the **+** icon to add the module to the list.
  4. ![bottom sheet dependency](/resources/Storage/how-to-articles-8/add_dep2.png)
3. Click **Add Dependency** to add the dependency to the app.

### Design the Application

Add the following pages to your application:

- **customers: **This is the page on which you display the bottom sheet.
- **bottomsheet:** This is the bottom sheet.
- **share: **This is another bottom sheet that takes your email or phone number to share the image on the respective platform.

#### Design the flows in the Share page

You will be designing the following flows:

Perform the following steps:

**Flow 1**

1. Open the flow designer of the **share** page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. Delete the **Script node** and replace the **Page Variables** node with the [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node in the flow.
3. In the **Use Dependency **node, import the following modules to the page and assign them to [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h3_545829551). Mark as** Injectable** so that these modules are injected into the page component. This node is used to import a custom dependency on a page.
  - MatBottomSheet - To open the bottom sheet component.
  - MatBottomSheetRef - A reference to the currently-opened bottom sheet. This module is used to close the bottom sheet and subscribe to events.
  - MAT_BOTTOM_SHEET_DATA - To access the injected data from the customer's page and inject it in your bottom sheet component.
  - ![import bottomsheet modules](/resources/Storage/how-to-articles-8/2021-07-13_15h33_04.png)
4. Add another **Use Dependency** node to the flow and import the Inject service to your page.
    ![Importing angular core dependency](/resources/Storage/how-to-articles-8/use_dep_3.png)
5. Add a script node to the flow and enter the following code in the script editor: Copy CodeJavaScriptthis.page.selected = this.page.data.media;
   this.page.address = null
   console.log("data", this.page.selected)

**Flow 2**

Create a flow to share the image on Gmail or Whatsapp.

1. Drag and drop a **Start** node.
  1. Enter the name as **share**.
  2. Add an input variable named image of type any.
      ![Start node](/resources/Storage/how-to-articles-8/share_input.png)
2. Drag and drop a **Script** node and enter the following in the script editor. This node allows you to share the image on the platform that you select.Copy CodeJavaScriptif (this.page.selected) {
    if (this.page.data.shareType == 'gmail')
    {
    let url = `https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=${this.page.address}&su=Image+Address&body='+${this.page.selected}+'&ui=2&tf=1&pli=1`;
    window.open(url, 'sharer', '_blank');
    } else if (this.page.data.shareType == 'whatsapp') {
    let url = `https://api.whatsapp.com/send?phone=${this.page.address}&text=${this.page.selected}`
    window.open(url, 'sharer', '_blank');
    }
   }
   this.page.bottomSheetRef.dismiss();

#### Design the UI of the share page

1. Open the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the **share** page.
2. Drag and drop the **HTML5** component. In the attributes window, select the **Element type** as **H3**.
3. On the canvas, click the HTML editor within the HTML5 component and add the following text in the code editor:
    Copy CodeHTML{{page.data.shareType == 'gmail' ? 'Enter Your Gmail Address' : 'Enter Your WhatsApp Number'}}
4. Drag and drop a **Row **component below the HTML 5 componentand set the following attributes:
  - fxLayoutGap : **1rem**
  - Layout Direction:** Center**
  - Perpendicular Direction: **Center**
5. Drag and drop an **Input **component within the row. Set the following attributes:
  1. Form field appearance : **Legacy**
  2. [(ngModel)] :** page.address**
  3. Name : **Address**
6. Drag and drop a Raised Button component next to the **Input **component. Set the following attributes:
  1. Name: **Send**
  2. (click) : Select the **Flow Picker** icon and select the** share** flow. Assign page.selected to the input variable image.
      ![](/resources/Storage/how-to-articles-8/flowpicker_share.png)

---

#### Design the flows on the bottomsheet page

You will be designing the following flows:

Perform the following steps:

**Flow 1**

1. Open the flow designer of the **bottomsheet** page. You will see a default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow) on the canvas.
2. Delete the **Script node** and replace the **Page Variables** node with the [Use Dependency](/smart/project-page-services-designer-guide/use-dependency-node) node in the flow.
3. In the **Use Dependency **node, import the following modules to the page and assign them to [page variables](/smart/project-page-services-designer-guide/properties-page-designer/a/h3_545829551). Mark as** Injectable** so that these modules are injected into the page component.
  - MatBottomSheet - To open the bottom sheet component.
  - MatBottomSheetRef - A reference to the currently-opened bottom sheet. This module is used to close the bottom sheet and subscribe to events.
  - MAT_BOTTOM_SHEET_DATA - To access the injected data from the customer's page and inject it in your bottom sheet component.
      ![import bottomsheet modules](/resources/Storage/how-to-articles-8/2021-07-13_15h33_04.png)
4. Add another **Use Dependency** node to the flow and import the Inject service to your page.
    ![Importing angular core dependency](/resources/Storage/how-to-articles-8/use_dep_3.png)

**Flow 2**

Create a flow to open links on the bottom sheet.

1. Drag and drop a **Start** node.
  1. Enter the name as **openlink**.
  2. Add an input variable named shareType.
2. Add a **Script** node to the flow and enter the following in the script editor. This module creates a reference to the currently-opened bottom sheet.Copy CodeJavaScriptthis.page.bottomSheetRef.dismiss({message: "done"});
3. Add a **Use Dependency **node to the flow and add the **share** page as a dependency to this page. Set the following properties:
  1. Library: **./share.component**
  2. Module: **shareComponent**
  3. Injectable: **true**
      ![](/resources/Storage/how-to-articles-8/share_component.png)
4. Add a **Script** node to the flow and enter the following code in the script editor:
    Copy CodeHTMLbh.local.bottomSheetRef = this.page.bottomSheet.open(shareComponent,{
    data: {media: this.page.data.imgsrc,
    shareType: bh.input.shareType}
   });
   bh.local.bottomSheetRef.afterDismissed().subscribe(result => {
    console.log(result);
   });

#### Design the UI of the bottomsheet page

1. Open the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the **bottomsheet** page.
2. Drag and drop a **List** component to the canvas.
3. Add two** List Item** components inside the list and name them **List item 1 **and **List item 2 **respectively.
4. On **List Item 1**, set the following properties:
  1. Add the following CSS to the class property: Copy CodeCSSbackground-color:whitesmoke;
     cursor: pointer;
  2. Add a custom property of type Key & Value.
    1. Enter the key as (click) and value as **openlink** and click the **Add** button.
    2. After adding the property, click the **Flow Picker** icon next to the (click) property.
    3. Select **pick a flow **to open the flow picker editor.
    4. Select the **openlink** flow and enter 'gmail' as the shareType.
        ![share type as gmail](/resources/Storage/how-to-articles-8/flowpicker_mail.png)
5. On **List Item 2**, set the following properties:
  1. Add the following CSS to the class property: Copy CodeCSS.item:hover{
      background-color:whitesmoke;
      cursor: pointer;
     }
  2. Add a custom property of type Key & Value.
    1. Enter the key as (click) and value as **openlink** and click the **Add** button.
    2. After adding the property, click the **Flow Picker** icon next to the (click) property.
    3. Select **pick a flow **to open the flow picker editor.
    4. Select the **openlink** flow and enter 'whatsapp'  as the shareType
6. Drag and drop a **Column** component inside **List Item 1**. In the attributes window, name the column as **Column 1** and add a custom property mat-line of attribute type.
7. Drag and drop another Column component inside **Column 1** and name that** Column 2**. Add a custom property mat-line of attribute type.
8. Drag and drop a** HTML 5** component inside **Column 2**. Select the **Element Type** as **Span** and enter **Gmail** in the HTML editor.
9. Drag and drop another **HTML 5 **component inside Column 2. Select the **Element Type** as **Span** and enter **Share using** **Gmail** in the HTML editor.
10. Drag and drop an **Image** component inside list item 1, below Column 1. Set the following properties:
  1. [src]: **page.data.imgsrc**
  2. style: **width: 2rem; height: 2rem;**
11. Drag and drop a **Column** component inside **List Item 2**. In the attributes window, name the column as **Column 3** and add a custom property mat-line of attribute type.
12. Drag and drop another **Column** component inside **Column 3** and name that** Column 4**. Add a custom property mat-line of attribute type.
13. Drag and drop a** HTML 5** component inside **Column 4**. Select the **Element Type** as **Span** and enter **Whatsapp** in the HTML editor.
14. Drag and drop another **HTML 5 **component inside Column 4. Select the **Element Type** as **Span** and enter **Share using ****Whatsapp** in the HTML editor.
15. Drag and drop an **Image** component inside list item 2, below Column 3. Set the following properties:
  1. [src]: **page.data.imgsrc**
  2. style: **width: 2rem; height: 2rem;**

#### 

---

#### Design the flows in the Customer Page

You will be designing the following flows on this page:

1. Open the flow designer of the **customers** page.
2. Replace the **Page Variables** node in the [on init flow](/smart/project-page-services-designer-guide/on-init-flow) with the **Use Dependency** node. Import the Angular module MatBottomSheet and inject it to the page.
    ![importing dependencies](/resources/Storage/how-to-articles-8/customer_flow.png)
3. In the **Script **node, log the page data. Copy CodeJavaScriptconsole.log(this.page)
4. Create another flow. Drag and drop a** Start** node and set the following parameters:
  - Name: **openBottomSheet**
  - Local variable: **bottomSheetRef **
5. Drag and drop a **Use Dependency **node and import bottomsheet.component from the bottomsheetComponent class. This is the class of the **bottomsheet** page.
    ![import the component](/resources/Storage/how-to-articles-8/use_dep3.png)
6. Drag and drop a **Script** node to the flow. Use the MatBottomSheet service and call the open method to open the bottom sheet. This method will return an instance of MatBottomSheetRef. Enter the following code in the script editor:Copy CodeJavaScriptbh.local.bottomSheetRef = this.page.bottomSheet.open(bottomsheetComponent,{
    data: {imgsrc:'https://images.freeimages.com/images/thumbs/62b/axle-the-parrot-1373433.jpg' },
   });
   bh.local.bottomSheetRef.afterDismissed().subscribe(result => {
    console.log(result);
   });

The variable named data contains the imgsrc . It is used to send the image URL from **customers** page to the bottom sheet. Similar to this key-value pair, you can send any data to the bottom sheet based on your requirement.

#### Design the UI of the Customers page

1. Open the UI designer of the Customers page.
2. Drag and drop a **HTML5 **component. Set the **Element type** to **Paragraph**. Click the HTML editor inside the HTML5 component and enter the following text in the code box:
    Copy CodeHTMLYou have received an image.
3. Drag and drop a **Raised ****Button** component to the canvas and configure the following attributes:
  - Button name: **Open Image**
  - Color: **Warn**
  - (click): Click the flow picker icon. Select the **openBottomSheet **flow in the editor and click** Save.**
4. Save both the pages.
5. Initialize the app and preview the **customers** page.
