# Row

<https://documentation.neutrinos.com/articles/#!components-guide-8/flex-layout-row>

## Row

### Overview

The **Row** component is used to set the position or flow of the child components horizontally. Its main axis is from left to right and the cross axis is from top to bottom.

![Row - main axis](/resources/Storage/components-guide-8/project-component-docs-test/row-axis.png)

We recommend learning about [Flex Layout and its underlying concepts](/smart/project-concepts/flexbox-layout) before using this component.

To create a responsive app using rows and columns, follow our [Best Practices](/articles/best-practices/best-practices-for-using-responsive-layouts).

### How to use

1. Drag and drop the **Row **component.
2. Fill the required attributes.
3. Drag and drop other components inside the **Row **component.

### Associated Attributes

- **Row label: **The display name of the component. This label is only used to uniquely identify the component on the [canvas](/smart/project-concepts/studio-application-page/a/h3__2105229662). It does not provide any behavioral difference on the end app.
- Style: It accepts a string value and affects different properties (height, width, color etc.) of the component based on the values provided (example- background:orange;height:200px;).
- Class: Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the Style side menu. The "Class" attribute accepts space-separated class names (example- class1 class2) which are defined in the Style tab as shown below.

```css
.class1 {  border-radius:10px;  flex-basis:10%;  height:100px;}.class2 {  border-radius:10px;  flex-basis:10%;  height:100px;}
```

- **fxFlex: **Resizes the child components along the [main axis](/smart/project-concepts/flexbox-layout/a/h4_1299346612) of the layout. Negative numbers are invalid. fxFlex is the shorthand for flex-grow, flex-shrink, and flex-basis combined. The second and third parameters (flex-shrink and flex-basis) are optional. The default is 0 1 auto. You can also give a single value such as 6 in which case it is considered as flex-grow.
- **flex-grow: **Specifies how much the flexbox item will grow relative to the rest of the flexbox child components inside the same flex container, when there is enough space. it will work only when we add flex-basis value is set to auto.
- **flex-shrink:** Specifies how much the flexbox item should shrink relative to the rest of the flexbox child components in the same flex container when there isn’t enough space.
- **flex-basis:** Specifies the initial default size of the flexbox item before it is changed by the flex-grow and flex-shrink properties. Once you specify the initial size, the flex item will not grow or shrink even when we specify the grow and shrink properties.
- **fxLayoutGap: **Specifies margin gaps on child components within a flexbox container. It accepts an integer value such as 20px, 5em, etc.
- **Wrap:** Choose whether flex child components are forced onto one line or can wrap onto multiple lines.
  - Wrap (default): Flex child components will wrap onto multiple lines, from top to bottom.
  - NoWrap: all flex child components will be on one line.
- **Layout Direction: **Specifies how child components should be aligned along the main axis. Select a direction from the drop-down list:
  - none (default): Child components are packed in their default position as if no value was set.
  - start: Child components are packed to the start of the container.
  - end: Child components are packed to the end of the container.
  - center: child components are centered in the container.
  - space-between: Child components are evenly distributed; the first line is at the start of the container while the last one is at the end.
  - space-around: Child components are evenly distributed with equal space around each line.
  - space-evenly: Child components are evenly distributed with equal space around them.
- **Perpendicular Direction:** Specifies how the child components should be aligned along the [cross axis](/smart/project-concepts/flexbox-layout/a/h4_195358557). Select a direction from the drop-down list:
  - start: Child components are placed at the start of the cross axis.
  - end: Child components are placed at the end of the cross axis.
  - center: child components are placed at the center of the cross axis.
  - stretch: Child components stretch to fill the container.
  - space-between: Child components are evenly distributed vertically.
  - space-around: Child components are evenly distributed vertically with equal space around them.
  - baseline: Child components are aligned such as their baselines align. A baseline is a line where most letters sit. The child elements are aligned based on that line.
- **fxShow:** Choose whether to dynamically show the element by selecting True or False. Or, click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the field to a [page flow](/smart/project-sample-how-to-guide/design-page-flows) a using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.
- **fxHide: **Choose whether to dynamically hide the element by selecting True or False. Or, click ![flow picker icon](/resources/Storage/components-guide-8/flow_picker_icon.png) and map the field to a [page flow](/smart/project-sample-how-to-guide/design-page-flows) a using the [Flow Picker](/smart/project-sample-how-to-guide/bind-page-flows-to-components) editor.

### Examples

**Example 1:****To display a row with four buttons**

1. Drag and drop a **Row** component. Double click the column to open its attributes window.
2. Update the following attribute values:
  - Style: width:100%; height:500px;background:#FFEBEE;
  - layout direction: space-around
  - perpendicular direction: center
3. Drag and drop five Buttons inside the **Row **component.
4. Name the buttons as **Button 1**, **Button 2**, **Button 3**, **Button 4**, and** Button 5** respectively.
5. In the [Styles](/smart/project-sample-how-to-guide/apply-global-styling) editor, create a class named .btn-style with the following CSS: .btn-style {height:100px;background:#E8EAF6;border: 1px solid black; width:200px;}
6. Save and run the page.
7. When the page is loaded, the buttons appear horizontally and are evenly distributed in with equal space around them. ![Row example](/resources/Storage/components-guide-8/project-component-docs-test/row_ex_1.png)
8. Update the layout direction and perpendicular direction attributes of **Row** and see how the placement of the buttons change. For example, if you choose the layout direction to start and the perpendicular direction to end, this is how the buttons are displayed within the row. ![row example 2](/resources/Storage/components-guide-8/project-component-docs-test/row_ex_1_1.png)
9. Update the width of **Button 1, Button 2,** and **Button 5 **to 700px - width:700px; and change the **Row** property from nowrap to wrap. You will see that the width of the buttons exceeds the screen size. Therefore, they are wrapped onto multiple lines, from top to bottom as we set the Row property to wrap.![Row example 3](/resources/Storage/components-guide-8/project-component-docs-test/row_ex_3.png)
10. Change the **Row** property from wrap to nowrap. The buttons are wrapped into a single line even though their width exceeds the screen size.![Row example 4](/resources/Storage/components-guide-8/project-component-docs-test/row_ex_4.png)

#### 

**Example 2: ****To demonstrate how to work with flex layout**

1. Add the following CSS to the [Styles](/smart/project-sample-how-to-guide/apply-global-styling) editor on the Neutrinos Application page. Save the changes. .demo-content{  padding: 25px;  min-height: 150px; margin-bottom: 10px; background:#FFEBEE; height:300px; width:100%; }
2. Add the Row Label as **Row 1**.
3. Select demo-content for the class attribute drop-down list.
4. Set fxlayoutGap to 20px to add a gap of 20px between the child elements of this row.
5. Drag and drop three **Rows **inside **Row1**. Update the row labels to **Row2**, **Row3**, and **Row4** respectively.
  - Update the style attribute of each row to background:#E1BEE7;border: 1px solid;
  - Set fxflex of **Row2** to **70**.
  - Set the fxflex of **Row3** to **20 10 auto**.
  - Set the fxflex of **Row4** to **10 10 3**.
6. Save and run the app.

![Row example 5](/resources/Storage/components-guide-8/project-component-docs-test/row_ex_5.png)

Because the main axis of a row runs horizontally, you will see that **Row1** will flex up to 70% of the width of the parent row from left to right. As only flex-grow value is provided, the default values of flex-shrink and flex-basis , that is **1** and **auto**, are assumed. **Row 2** will flex up to 20% of the width of the parent row and shrink 10% if necessary. For Row3, even though the flex-grow value is provided as 10, the row will not flex up as the flex-basis value is set to **1** instead of **auto**. Therefore, by default, it takes flex-basis value and flexes up to 3%.

#### 

**Example 3: ****To hide the row at extra-small screen sizes**

1. Double-click **Row1** from the previous example.
2. Add [fxHide.xs] as the [custom property](/smart/project-component-docs-test/how-to-use-palette-components/a/h4__1320575622) of type **Key & Value **and set it to **true**.
3. Click the **Add** button to add the property.
4. Save and preview the app.

![custom property for a row component](/resources/Storage/components-guide-8/project-component-docs-test/row_cust_prop.png)

If you preview the app in an **iPad** view, you will see **Row1** and its child rows visible. But, if you preview the same app in an **iPhone** view, **Row1** and its child elements are not displayed as they are hidden from extra-small screens using the [fxHide.xs] property.

![iPAd view](/resources/Storage/components-guide-8/project-component-docs-test/row_ipad.png)

![iPhone view](/resources/Storage/components-guide-8/project-component-docs-test/row_iphone.png)
