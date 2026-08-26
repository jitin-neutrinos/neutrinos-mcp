# Add a Dialog Box to your App Page

<https://documentation.neutrinos.com/articles/#!how-to-articles/add-a-dialog-box-in-an-app>

A dialog box is a secondary window that allows users to perform a command, asks users a question, or provides users with information or progress feedback. To display a dialog box in your application, you should import and use the [Angular](https://material.angular.io/components/dialog/overview) [MatDialog](https://material.angular.io/components/dialog/overview)[service](https://material.angular.io/components/dialog/overview).

Let's say you have a **Privacy and Cookies Policy** button on your application which, when clicked, opens a dialog box displaying the policy information. The dialog box allows the user to accept the policy and logs the result of the action on the Console.

To display a dialog box similar to the example above, perform the following steps:

1. On the Neutrinos Studio Applications page, create a page named **dialogbox** (or any other name of your choice). This is where you design the dialog box.
2. Switch to the TS editor of the page, add the following code:
  1. Import the Angular MatDialog, MatDialogRef, MAT_DIALOG_DATA , and Inject services into your application.Copy CodeJavaScriptimport { Component, OnInit, Inject} from '@angular/core';
     import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
  2. To access the data in your dialog component and log the user action, use the MAT_DIALOG_DATA injection token.
      Copy CodeJavaScriptimport { Component, OnInit, Inject } from '@angular/core';
     @Component({
      selector: 'bh-dialogbox',
      templateUrl: './dialogbox.template.html'
     })
     export class dialogboxComponent extends NBaseComponent implements OnInit {
      constructor(
      public dialogRef: MatDialogRef<dialogboxComponent>,
      @Inject(MAT_DIALOG_DATA) public data: any) {
      super();
      }
      ngOnInit() {
      }
     }
3. Create another page called **customers**. This is the page on which you will display the dialog box.
4. Switch to the TS editor of the page and add the following code:
  1. Import the Angular services to your page.Copy CodeJavaScriptimport {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
  2. Import dialogbox.component from the dialogboxComponent class. This class resides in the **dialogbox** page. Copy CodeJavaScriptimport {dialogboxComponent
     } from '../dialogboxComponent/dialogbox.component';
  3. Use the MatDialog service to open a dialog box. A dialog is opened by calling the open method with a component to be loaded and an optional config object. The open method will return an instance of MatDialogRef. Create a variable named data and assign the name and message key-value pairs with values. This key-value pair will be used to send the data from **customers** page to the dialog box. Similar to this key-value pair, you can send any data to the dialog box based on your requirement. Copy CodeJavaScriptconstructor(public dialog: MatDialog)
      {
      super();
      }
      ngOnInit()
      {
      }
      openDialog(): void {
      const dialogRef = this.dialog.open(dialogboxComponent, {
      width: '500px',
      data: {name: 'Privacy and Cookies Policy',
      message: 'The user has accepted the Privacy and Cookies policy'}
      });
      }
  4. The MatDialogRef provides a handle on the opened dialog. Use it within the open method to close the dialog box and to receive notifications when the dialog box has been closed. Update the above code to:Copy CodeJavaScriptconstructor(public dialog: MatDialog)
      {
      super();
      }
     ngOnInit()
      {
      }
     openDialog(): void
      {
      const dialogRef = this.dialog.open(dialogboxComponent, {
      width: '500px',
      data: {name: 'Privacy and Cookies Policy',
      message: 'The user has accepted the Privacy and Cookies policy'}
      });
      dialogRef.afterClosed().subscribe(result => {
      console.log(result);
      });
      }
      ![Information](/resources/Storage/how-to-articles/info.png)
      See [MatDialogConfig](https://material.angular.io/components/dialog/api#MatDialogConfig) to learn about the other options that Angular supports to configure your dialog box.
5. Switch to the HTML editor of the page.
6. Drag and drop a **Row **component. In the attributes window of the row, configure the following properties:
  1. Style: **height:100px;**
  2. Layout Direction: **Center**
  3. Perpendicular direction: **Center**
7. Drag and drop a **Button** component inside the **Row** component. In the attributes window of the button, provide the following values:
  - Button name: **Privacy and Cookies Policy**
  - Color: **Warn**
  - (click): **openDialog()**
8. Save the page.
9. Open the **dialogbox** page. Update the code within the constructor. Add the class name of the dialog box(dialogboxComponent) and log the result of the user operation on the console:Copy CodeJavaScriptconstructor(
    public dialogRef: MatDialogRef<dialogboxComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any) {
    super();
    console.log(data); //log data
    }
10. Switch to the HTML editor of the page to design the user interface of the dialog box.
11. Drag and drop an **HTML5** component to the canvas. In the attributes window, select the Element type as **H3**.
12. On the canvas, click the HTML editor within the HTML5 component and add {{data.name}} in the code editor.![The header HTML5 component](/resources/Storage/how-to-articles/data_name.png)
13. Drag and drop another **HTML5 **component to the canvas, select the Element Type as P**aragraph**, click the HTML editor and enter the following text in the code editor: Copy CodeHTMLThis page explains what data and information we collect,
   how and why We collect it, and how We store, use,
   disclose, and keep information about you / your interactions with us secure.
   <br>
   These interactions include: when you use our websites, when you
   register or attend any event organized by Neutrinos,
   at webinars and trade shows, sales / marketing activities,
   when you download an e-book / report / other digital assets,
   when you register and participate in our online
   community (using our forums or online training),
   you reply to a Neutrinos survey, and/or if you use
   the Neutrinos platform, any of our products and/or
   services, including any trial version
   (collectively the “Services”) in any manner.
   <br>
14. Drag and drop a **Row** component to the canvas and configure the following properties in the attributes window:
  - style: **padding-top:20px;**
  - perpendicular Direction: **Center**
15. Drag and Drop a **Button **component inside the Row and configure the following attributes:
  1. Button Name: **Accept**
  2. Color: **Warn**
  3. Add a **Key&Value** custom property where the **key** is [mat-dialog-close] and **value** is data.message.
      ![custom property](/resources/Storage/how-to-articles/data_messsage.png)
  4. Save the page.
16. Initialize the app and preview the **customers** page.
