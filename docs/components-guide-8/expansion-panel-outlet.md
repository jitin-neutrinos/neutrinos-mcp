# Expansion Panel Outlet

<https://documentation.neutrinos.com/articles/#!components-guide-8/expansion-panel-outlet>

## Expansion Panel Outlet

### Overview

The** Expansion panel outlet **component is a container that provides an expandable view, where some of the content is hidden. It will be displayed when the user clicks on the **Expandable Panel **component. The **Expansion panel outlet **component contains one or more [Expansion Panels](/articles/components-guide-8/expansion-panel).

### Usage

The** Expansion panel outlet **component can be used where the data to be displayed in an expanded view on click. By default, only the title and description will be shown and other components will be hidden. They will be displayed when the user clicks on it.

### How to use

1. Drag and drop an **Expansion panel outlet **component.
2. Fill in the attributes such as style class, display mode, and multi.
3. Drag and drop other expansion panel components inside it depending on your requirement.

### Associated Attributes

- **Expansion Panel Outlet label: **The display name for the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/canvas). It does not provide any behavioral difference on the end app.
- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The **class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

**[displayMode]**: The display mode used for all expansion panels in the expansion panel outlet. you can choose between two display modes:

**default** - a gutter-like spacing is placed around any expanded panel, placing the expanded panel at a different elevation from the rest.**flat** - no spacing is placed around expanded panels, showing all panels at the same elevation.**Multiple Expansion: **If set to True, allows the user to expand multiple expansion panels at a time. If set to False, allows the user to expand only one expansion panel at a time.

### Example

### 

1. Drag and drop an **Expansion Panel Outlet** component to the canvas of the [Page UI designer](/smart/project-concepts/page-designer/a/h3__1090805748).
2. Drag and drop an **Expansion Panel **component inside the **Expansion Panel Outlet**. Double click the component and set the following properties:
  - **style**: background: #BDBDBD;margin: 8px;
  - **(opened)**: panelOpenState = true
  - **(closed)**: panelOpenState = false
3. Drag and drop an **Expansion Header** component inside the **Expansion Panel**.
4. Drag and drop an **Expansion Title** inside the **Expansion Header** and set self aware panel in the title field.
5. Drag and drop an **Expansion Description** component inside the **Expansion Header,** below the **Expansion Title**. Set Currently I am {{panelOpenState ? 'open' : 'closed'}} in the description property.
6. Drag and drop an **HTML 5** component inside the **Expansion Panel,** below the **Expansion Header**. Set the **Element Type **as **Paragraph**.
7. Double click the HTML editor and enter I'm visible because I am open
8. Save and run the page.

**Page Layout**

![layout 1](/resources/Storage/components-guide-8/project-component-docs-test/exp1%20layout.png)

### Example 2

![](/resources/Storage/components-guide-8/project-component-docs-test/exp_panel2.png)

Design the following flows in the [Flow designer](/smart/project-concepts/page-designer/a/h3_520216706) of the page in which you are using the Expansion components. These flows are required to be used in the raised buttons to navigate between expansion panels:

**Flow 1: **Used to set the initial value of a variable called **step**.

1. Drag and drop a Start node. Name the node as **setStep**.
2. Add an input property called **index** and set its type as **number**.
3. Drag and drop a Script node and join it to the Start node.
4. Add the following code within it: Copy CodeJavaScriptthis.page.step = bh.input.index;

**Flow 2**: Used to increment the value of the** step** variable.

![nextStep flow](/resources/Storage/components-guide-8/directives-2021-09-21-1.png)

1. Drag and drop a Start node. Name the node as **next****Step**.
2. Drag and drop a** Script** node and join it to the **Start** node.
3. Add the following code within it: Copy CodeJavaScriptthis.page.step++;

**Flow 3: **Used to decrement the value of the** step** variable.

1. Drag and drop a Start node. Name the node as previous**Step**.
2. Drag and drop a** Script** node and join it to the **Start** node.
3. Add the following code within it: ;Copy CodeJavaScriptthis.page.step--;

Switch to the [UI designer](/smart/project-concepts/page-designer/a/h3__1090805748) of the page and perform the following steps:

1. Drag and drop an **Expansion Panel Outlet** component to the canvas and set the** style** as margin:20px;
2. Drag and drop an **Expansion Panel** component inside the** Expansion Panel Outlet**. Double click the component and set the following properties:
  - **style**: background: #E0E0E0;
  - **(opened)**: setStep(0)
  - **[expanded]**: page.step === 0
3. Drag and drop an **Expansion Header** component inside the **Expansion Panel**.
4. Drag and drop an **Expansion Title** inside the **Expansion Header** and set Personal data in the title field.
5. Drag and drop an **Expansion Description** component inside the **Expansion Header** below the **Expansion Title**. Set **Type your name **in the description property.
6. Drag and drop a **Row** inside the **Expansion Panel **component.
7. Drag and drop an **HTML 5** component inside the Row. Set the following properties:
  - **style: **margin: 25px 50px 75px;
  - **Element Type: **Label
8. Click the HTML editor and enter** Name.**
9. Drag and drop a **Input **field and set the** style **as margin: 0px 50px 75px;
10. Drag and drop a **HTML 5** component and set the **Element Type** as **div.** Double click the HTML editor and enter <hr>
11. Drag and drop a **Raised Button a**nd set the following properties:
  - **buttonName: **Next
  - **Color**: Primary
  - (**click**): Click the **Pick a Flow **button and select the **nextStep **flow in the Flow Picker editor.
12. Drag and drop another **Expansion Panel** component inside the** Expansion Panel Outlet**. Double click the component and set the following properties:
  - **style**: background: #BDBDBD;
  - **(opened)**: setStep(1)
  - **[expanded]**: page.step === 1
13. Drag and drop an **Expansion Header** component inside the **Expansion Panel**.
14. Drag and drop an **Expansion Title** inside the **Expansion Header** and set **Destination you want to travel? **in the title field.
15. Drag and drop an **Expansion Description** component inside the **Expansion Header** below the **Expansion Title**. Set** Type the country **in the description property.
16. Drag and drop a **Row** inside the **Expansion Panel **component.
17. Drag and drop an **HTML 5** component inside the Row. Set the following properties:
  - **style**: margin: 25px 50px 75px;
  - **Element Type: **Label
18. Click the HTML editor and enter** Country**
19. Drag and drop a **Input **field and set the** style **as margin: 0px 50px 75px;
20. Drag and drop a **Row **component inside the expansion panel component.
21. Drag and drop a **Raised button** inside the row and set the following properties:
  - **style**: margin: 25px 50px;
  - **button name:** Previous
  - **Color**: Warn
  - **(click):** Click the **Pick a Flow **button and select the **previous****Step **flow in the Flow Picker editor.
22. Drag and drop another **Raised button** inside the** Row** component and set the following properties:
  - **style**: margin: 25px 50px;
  - **button ****name**: End
  - **color**: Primary
  - (**click**): Click the **Pick a Flow **button and select the **nextStep **flow in the Flow Picker editor.
23. Save and run the page.

**Page Layout**
