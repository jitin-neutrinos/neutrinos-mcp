# Footer

<https://documentation.neutrinos.com/articles/#!components-guide/footer5>

## Footer

OverviewA footer component typically contains authorship information, copyright information, contact information, sitemap, back to top links, related documents. There can be several footer components in one document.**Usage**A footer component is used when the content should be displayed at the bottom of the page. It can contain multiple components inside it. In the footer, the data can be anything such as contact information, copyright, etc.How to useDrag and drop a **Footer** component.Fill attributes such as style and class.Inside that, some components can be inserted for the content such as paragraph component, etc.The footer will be displayed at the bottom.Example**Display a block with a title a subtitle, a paragraph component, and a footer.** 1. Drag and drop a **Header** component, and provide the **style** and **class** attribute. 2. Now drag and drop an H**3** component inside the header for a title and provide the text such as Agra. So the title will be set as Agra. 3. After setting the title, drag and drop an H5 component inside the header below h3 component to set a subtitle because subtitle should be smaller than the title, and provide the subtitle as Taj Mahal. 4. Now drag and drop a paragraph component inside the header component below the h5 component, and provide some text as content that will be displayed below the subtitle. 5. Drag and drop a footer component below the header component. 6 Drag and drop a paragraph component inside the footer component, give the content as (published by a blogger). 7. Save and Run the studio. 8. A block with title Taj in h3, a subtitle with Agra in h5 and a paragraph with some content in header component and a footer at the bottom will be displayed.**Associated Attributes****Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class:** **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below.Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}

**Support**

- **Devices:** Android, iOS
- **Browsers:** Latest version of all modern browsers
- **Dependencies version:**
