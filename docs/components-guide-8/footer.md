# Footer

<https://documentation.neutrinos.com/articles/#!components-guide-8/footer>

## Footer

### Overview

A **Footer** component typically contains authorship information, copyright information, contact information, sitemap, back to top links, related documents. There can be several footer components in one document.

It is used when the content should be displayed at the bottom of the page. It can contain multiple components inside it. In the footer, the data can be anything such as contact information, copyright, etc.

### How to use

1. Drag and drop a **Footer** component.
2. Fill attributes such as style and class.
3. Inside that, some components can be inserted for the content such as the **HTML 5 - Paragraph** component.
4. The **Footer** will be displayed with a paragraph at the bottom.

### Associated Attributes

- **Footer Label:** The display name of the component. This label is only used to uniquely identify the component on the canvas. It does not provide any behavioral difference on the end app.
- **Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- **Class: **The **class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

```css
.class1 {border-radius:10px;
flex-basis:10%;
height:100px;
}
.class2 {
border-radius:10px;
flex-basis:10%;
height:100px;
}
```

### Example

**To display a static footer with a link **

1. Drag and drop a** Footer** component to the canvas.
2. Drag and drop a **Row **component inside the footer.
  1. Set the style as background-color: grey;color: white; text-align: center; font-size:20px;
  2. set the **l****ayout-direction **as **Space-Evenly.**
3. Drag and drop an** HTML5 **component inside the **Row** component.
4. Double-click the **HTML5** to open its attributes window and set the following properties:
  - **style**: width: 100%;
  - **Element ****Type:** Label
5. Double click the HTML editor and enter &copy 2021 Neutrinos | All Rights Reserved
6. Drag and drop another **HTML 5 **component inside the row and set the following properties:
  - **style**: width: 100%;
  - **Element Type**: Label
  - Double click the **HTML editor** and enter the following code: Copy CodeHTML<a href="https://goneutrinos.com/privacy-cookies-policy/">
      Privacy and Cookies Policy </a>
7. Save and preview the page.

**Page Layout**

![page layout of the footer](/resources/Storage/components-guide-8/project-component-docs-test/footer_pg_layout.png)
