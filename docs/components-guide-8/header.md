# Header

<https://documentation.neutrinos.com/articles/#!components-guide-8/header>

## Header

### Overview

The **Header **component typically contains one or more heading elements (h1 - h6), logo or icon, authorship information. There can be several header components in one document.

It is used when the content should be displayed with some special properties such as bigger font size, or when the text should be in bold. Various components can be inserted inside a **Header** component.

### How to use

1. Drag and drop a **Header** component.
2. Fill in the attribute such as style and class.
3. Components such as the h1-h6 component, paragraph component, etc., can be added.

### Associated Attributes

- **Header Label:** The display name for the component. This label is only used to uniquely identify the component on the canvas. It does not provide any behavioral difference on the end app.
- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The** class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

### Examples

**Example 1: To display a simple header with a description**

1. Drag and drop a **Header **component to the canvas.
2. Drag and drop a **HTML 5 **component and the following properties:
  - **style:** padding: 0;text-align: left;background: White;color: Red;font-size: 30px;
  - **Element type: **H2
  - Click the **HTML editor **and enter **Neutrinos**.
3. Drag and drop another **HTML 5 **component and select the **element type **as paragraph.
4. Double click the HTML editor and enter Neutrinos is a Low-Code powered Multiexperience development platform (MXDP) that empowers developers and customers to develop fit-for-purpose apps, based on touchpoint-specific modalities.
5. Save and run the page.

**Example 2:** **To display a header with navigation **

1. Drag and drop a** Header** component to the canvas and set the style as width: 100%; background: #EEEEEE; padding: 10px; color: #fff
2. Drag and drop a **Row** component inside the header and set the following properties:
  - **style**: padding:1rem;
  - **wrap**: Nowrap
  - **Layout**-**Direction**: space-between
  - **Perpendicular ****Direction**: Center
3. Drag and drop an **HTML 5** component inside the row and set the following properties:
  - **style**: padding: 7px 25px;
  - **Element ****type**: Div
  - Click the HTML editor and enter:Copy CodeHTML<a href="https://goneutrinos.com/" style="color:black; font-weight:bold; font-size:20px;text-decoration:none">Home</a>
4. Drag and drop another** HTML 5 **component inside the **Row **and set the following properties:
  - **style**: padding: 7px 25px;
  - **Element ****type**: Div
  - Click the HTML editor and enter: Copy CodeHTML <a href="https://goneutrinos.com/built-with-neutrinos/" style="color:black; font-weight:bold; font-size:20px; text-decoration:none">About</a>
5. Save and run the page.
