# Display a Dialog Window on a Page

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/display-a-dialog-window-on-a-page>

A dialog box is a secondary window that allows users to perform a command, asks users a question, or provides users with information or progress feedback. To display a dialog box in your application, you use the [Dialog nodes](/smart/project-page-services-designer-guide/dialog) on the [Page Flow Designer](/smart/project-concepts/page-designer/a/h3_520216706), create page flows, and link them to the page UI.

Let's say you have a **Privacy and Cookies Policy** button on your application which, when clicked, opens a dialog box displaying the policy information.

To display a dialog window similar to the example above, perform the following steps:

**Create Application Pages**

On the Neutrinos Studio Applications page, create the following pages:

- **Home** - this is the page on which you display the dialog window. Also referred to as the parent page.
- **Dialog -** This is the page that is to be displayed as a dialog window.

**Design Page Flows for the Home page**

This page flow is used to open a dialog window and configure the appearance and behavior of the dialog window.

1. Expand the **Home** page on the page explorer and select **Flow.**
2. Drag and drop a **Start** node to the canvas. Name the node as **OpenDialog** and create the following local variables:
    **Key**
    **Type**
    **Purpose**
    data
    any
    To send data to the dialog window
    response
    any
    To log the user response on the console.
3. Drag and drop a **Script** node, connect it to the** Start** node, and enter the following code in the editor. Copy CodeJavaScriptbh.data = {
    name: "This is a sample dialog window"
   }
4. Drag and drop the **Open Dialog** node and connect to the flow. Set the following properties. Refer to the [Open Dialog node](/smart/project-page-services-designer-guide/open-dialog-node) documentation to learn about each property and accepted values.
  - **Select a page:** dialog
  - **data:** bh.local.data
  - **result mapping: **bh.local.response
  - **Aria described by: **Allows you to accept or discard the website's privacy and cookies policy
  - **Aria label: **Privacy and cookies window
  - **Height:** 400px
  - **Width: **500px
5. Map the **afterClosed** port of the **Open Dialog** node to a** Script** node and enter the following code to log the action on the console:
    ![afterClosed port of the dialog window](/resources/Storage/how-to-articles-8/dialog%20-%20after%20closed.png)
    Copy CodeJavaScriptconsole.log("The User has accepted the policy", bh.local.response);

---

**Design the User Interface of the Home page**

![User interface of the home page](/resources/Storage/how-to-articles-8/home_page.png)

1. On the page explorer, select **UI** of the** Home** page to open the Page UI designer.
2. Drag and drop a **Button** component from the components palette list to the canvas. In the attributes window of the button, provide the following values:
  - **Button name: **Privacy and Cookies Policy
  - **Color:** Warn
  - **(click):** Click the** Pick a flow** mat chip and select the **openDialog** flow on the flow picker editor. On click of the button, the **openDialog** flow will be executed to display the dialog window on the **Home** page.
3. Save the page.

---

**Design Page Flows for the Dialog Page**

1. On the page explorer, select **Flow **of the Dialog page to open the Page Flow designer.
2. Create a flow to get any data passed by the parent page (**Home** page) to the dialog window.
  1. Drag and drop the **On Init **node and create a local variable called data.
  2. Drag and drop the **Get Dialog** **Data** node and set the dialog data mapping property to bh.local.data. This node will get the data passed by the parent page to the dialog window.
  3. Connect the **Get Dialog Data** node to the **On Init** node to create a flow.
  4. Drag and drop a **Script** node to the canvas, connect it to the flow. Enter the following data in the script editor to log the data received by the dialog window on the console. Copy CodeJavaScriptconsole.log("The data sent from the parent page is:",bh.local.data);
3. Create another page flow to close the dialog window. We will be mapping this flow to a button on the UI to close the dialog window on click of it.
  1. Drag and drop a **Start** node to the canvas. Enter the name as **close dialog **and create a local variable called data.
  2. Drag and drop a **Script** node and connect it to the flow. Enter the following code: Copy CodeJavaScriptbh.local.data = {message:'This is the data sent from the dialog window to the parent page'}
  3. Drag and drop the **Close Dialog** node and connect it to the flow. Map the data property to bh.local.data. This flow closes the dialog window and sends data back to the parent page.

---

**Design the User Interface of the Dialog Page**

![User Interface of the dialog page](/resources/Storage/how-to-articles-8/dialog_page.png)

1. On the page explorer, select **UI** of the **Dialog** page to design the user interface of the dialog window.
2. Drag and drop an **HTML5** component to the canvas. In the attributes window, select the Element Type as **H3**.
3. On the canvas, click the HTML editor within the HTML5 component and add Privacy and Cookies Policy in the code editor.
4. Drag and drop another **HTML5 **component to the canvas, select the Element Type as **P****aragraph**, click the HTML editor and enter the following text in the code editor: Copy CodeHTMLThis page explains what data and information we collect,
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
5. Drag and Drop a **Button **component to the canvas and configure the following attributes:
  1. Button Name: **Accept**
  2. Color: **Warn**
  3. (click): Select the **Pick a Flow** mat chip and select the closeDialog page flow on the editor and click **Save**.
6. Save the page.

---

**Test the App**

1. Initialize the app and preview the **Home** page.
2. Click the **Privacy and Cookies Policy** button to open the dialog window.
3. Click the **Accept** button on the dialog window to close it.
4. Inspect the dialog window on Dev tools and check the data that is logged on the Console.

![console log](/resources/Storage/how-to-articles-8/dialog_console1.png)
