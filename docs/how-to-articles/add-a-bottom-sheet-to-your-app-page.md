# Add a Bottom Sheet to your App Page

<https://documentation.neutrinos.com/articles/#!how-to-articles/add-a-bottom-sheet-to-your-app-page>

The

Bottom Sheet

is a component that slides up from the bottom of the screen to showcase additional content in your application. To display a bottom sheet in your application, you should import and use the

Angular Bottom Sheet

component.

Let's consider an example where you have received an image file. With on click of a button, the image should be displayed on a bottom sheet.

To display a bottom sheet similar to the example above, perform the following steps:

1. Make sure the MatBottomSheetModule module is added in your application's /app/src/app/config/import-module.ts file.
    ![import_module.ts](/resources/Storage/how-to-articles/import_modules.png)
2. Open your app and create the following pages:
  - **customers: **This is the page on which you display the bottom sheet.
  - **bottomsheet:** This is the bottom sheet.
3. Open the **bottomsheet **page. Switch to the TS editor of the page and add the following code:
  1. Import the Angular MatBottomSheet, MatBottomSheetRef, MAT_BOTTOM_SHEET_DATA , and Inject services into your application.
      Copy CodeJavaScriptimport {Inject } from '@angular/core'
     import {MatBottomSheet, MatBottomSheetRef, MAT_BOTTOM_SHEET_DATA} from '@angular/material/bottom-sheet';
  2. To access the injected data from the **customers** page and inject it in your bottom sheet component, use the MAT_BOTTOM_SHEET_DATA  injection token.
      Copy CodeJavaScriptexport class bottomsheetComponent extends NBaseComponent implements OnInit {
      constructor(
      public bottomSheetRef: MatBottomSheetRef<bottomsheetComponent>,
      @Inject(MAT_BOTTOM_SHEET_DATA) public data: any) {
      super();
      }
4. Open the **customers** page. Switch to the TS editor of the page and add the following code:
  1. Import the Angular service MatBottomSheet to your page.
      Copy CodeJavaScriptimport {MatBottomSheet} from '@angular/material/bottom-sheet';
  2. Import bottomsheet.component from the bottomsheetComponent class. This is the class of the **bottomsheet** page.
      Copy CodeJavaScriptimport {bottomsheetComponent
     } from '../bottomsheetComponent/bottomsheet.component'
  3. Use the MatBottomSheet service and call the open method to open the bottom sheet. This method will return an instance of MatBottomSheetRef.
      Copy CodeJavaScriptconstructor(public bottomSheet: MatBottomSheet) {
      super();
      }
  4. Create a variable named data and assign the imgsrc key-value pair. This key-value pair will be used to send the data from **customers** page to the bottom sheet. Similar to this key-value pair, you can send any data to the bottom sheet based on your requirement.
      Copy CodeJavaScriptopenBottomSheet(): void {
     const bottomSheetRef = this.bottomSheet.open(bottomsheetComponent,{
      data: {imgsrc:'https://img-authors.flaticon.com/google.jpg' },
     });
     }
  5. The MatBottomSheetRef is a reference to the currently-opened bottom sheet and can be used to close it or to subscribe to events. Note that only one bottom sheet can be open at a time.
      Copy CodeJavaScriptbottomSheetRef.afterDismissed().subscribe(result => {
      console.log(result);
      });
5. Switch to the HTML editor of the page.
6. Drag and drop a **HTML5 **component. Set the **Element type** to **Paragraph**. Click the HTML editor inside the HTML5 component and enter the following text in the code box:
    Copy CodeHTMLYou have received an image.
7. Drag and drop a **Raised ****Button** component to the canvas and configure the following attributes:
  - Button name: **Open Image**
  - Color: **Warn**
  - (click): **openBottomSheet()**
8. Save the page.
9. Open the **bottomsheet** page. Add the following code in the TS editor to open the link of the image on click of it.Copy CodeJavaScriptopenlink()
   {
    window.location.href = this.data.imgsrc;
   }
10. Switch to the HTML editor of the page to design the user interface of the bottom sheet.
11. Drag and drop an **HTML5** component to the canvas. In the attributes window, select the Element type as **Paragraph**.
12. On the canvas, click the HTML editor within the HTML5 component and add the following text in the code editor:
    Copy CodeHTMLClick the image to view its source URL.
13. Drag and drop an **Image **component and set the following attributes:
    ![custom attribute](/resources/Storage/how-to-articles/custom_attr_bs.png)
  - style: cursor:pointer
  - [src]: data.imgsrc
  - Add a custom attribute of **Key&Value** pair and click the** Add** button. This will call the openlink() method on click of the image.
    - property name: (click)
    - property value: openlink()
14. Drag and drop another **HTML5 **component to the canvas, select the Element Type as P**aragraph**, click the HTML editor and enter the following text in the code editor:
    Copy CodeHTMLClick anywhere outside the Bottom Sheet to close it.
15. Save both the pages.
16. Initialize the app and preview the **customers** page.
