# Footer

<https://documentation.neutrinos.com/articles/#!components-guide-7/footer>

## Footer

### Overview

A **Footer** component typically contains authorship information, copyright information, contact information, sitemap, back to top links, related documents. There can be several footer components in one document.

### Usage

A **Footer **component is used when the content should be displayed at the bottom of the page. It can contain multiple components inside it. In the footer, the data can be anything such as contact information, copyright, etc.

### How to use

1. Drag and drop a **Footer** component.
2. Fill attributes such as style and class.
3. Inside that, some components can be inserted for the content such as the **HTML 5 - Paragraph** component.
4. The **Footer** will be displayed with a paragraph at the bottom.

### Associated Attributes

**Footer Label: The display**

**Style: **It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).

**Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the **Style** tab as shown below.

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

Display a block with a title, a paragraph, and a footer.

1. Drag and drop a **Header** component, and provide the **style** and **class** attributes.
2. Drag and drop an **HTML 5** component inside the **Header** component, and set its **E****lement type** to Header 3. Set the Header value as **Agra** in the HTML editor.
3. Drag and drop an **HTML 5** component below the **Header 3** component, and set its **E****lement type** to paragraph. Provide some text as the content that will be displayed below the header.
4. Drag and drop a **Footer** component below the paragraph.
5. Drag and drop an **HTML 5** component inside the **Footer **component and set its **E****lement type** to paragraph. Inside the **Footer** component, give the content as (published by a blogger).
6. Save and Run the app
7. A block with a title, a paragraph with some content in the footer at the bottom will be displayed.
