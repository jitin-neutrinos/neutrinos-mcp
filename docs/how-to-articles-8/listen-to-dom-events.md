# Listen to DOM Events

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/listen-to-dom-events>

You can listen to [DOM events](https://www.w3schools.com/jsref/dom_obj_event.asp) of an HTML element using the [Host Listener](/smart/project-page-services-designer-guide/host-listener-node) node.

In this example, we will listen to the wheel event on the page.

Perform the following steps:

1. Open the [flow designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page.
2. Open the **Page Variables **node in the default [On Init flow](/smart/project-page-services-designer-guide/on-init-flow), and add a page variable called scroll, and set its initial value to 0.
    ![on init flow](/resources/Storage/how-to-articles-8/on_init.png)
    ![setting the scroll page variable](/resources/Storage/how-to-articles-8/page_var1.png)
3. Drag and drop a [Host Listener](/smart/project-page-services-designer-guide/host-listener-node) node. On the attributes window of the node, enter the event name as document:wheel. The **Host Listener** node will listen to the mouse wheel event on the entire document (the entire page). If you enter the event name as wheel instead of document:wheel, the page variable - scroll gets incremented only when you scroll on any element of the page.
4. Drag and drop a **Script **node and connect it to the **Host Listener **node. On the attributes window of the node, enter the following code. This will increment the page variable scroll every time the mouse wheels: Copy CodeJavaScriptthis.page.scroll++
5. On the [UI Designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page, drag and drop a **Column**.
6. Drag and drop an **HTML 5** component inside the **Column**.
7. In the attributes window of the HTML 5 component, change the Element Type to Paragraph.
8. In the HTML Editor of the component, enter Please scroll on the mouse wheel or mousepad.
9. Drag and drop another **HTML 5** component.
10. In the attributes window of the HTML 5 component, change the Element Type to Paragraph.
11. In the HTML Editor of the component, enter Wheel Count : {{page.scroll}}. This will display the value in the page variable - scroll.
12. Initialize and run the page.
13. Every time you scroll the mouse wheel or the mouse pad on the page, the number gets incremented.
    ![scrolling on the document](/resources/Storage/how-to-articles-8/page%20scroll.png)
